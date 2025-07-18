from fastapi import FastAPI
import pyodbc
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Conexão com autenticação do Windows
con = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=bd_recentro;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5500"]
    allow_methods=["*"],
    allow_headers=["*"],
)

class org(BaseModel):
    nom: str
    end: str
    reg: str
    ctts: list[str]

@app.get("/orgids")
def contador():
    cursor = con.cursor()
    cursor.execute("SELECT count(org_id) FROM Org")
    resultados = cursor.fetchall()
    return {"res": resultados[0][0]}

@app.get("/org/{id}")
def listar(id: int):
    cursor = con.cursor()
    cursor.execute("SELECT org_nome, org_end, org_reg FROM Org where org_id = ?", (id,))
    resultados = cursor.fetchall()
    return {"nom": resultados[0][0], "end": resultados[0][1], "reg": resultados[0][2]}

@app.get("/orgctt/{id}")
def listarctt(id: int):
    cursor = con.cursor()
    cursor.execute("SELECT org_ctt FROM org_contato where org_id = ?", (id,))
    resultados = cursor.fetchall()

    if resultados:
        return {"ctts": [{r[0]} for r in resultados]}
    
    return

@app.delete("/orgdel/{id}")
def deletar(id: int):
    cursor = con.cursor()
    cursor.execute("DELETE FROM Org WHERE org_id = ?", (id,))
    con.commit()
    return

@app.put("/orgset/{id}")
def editar(Org: org, id: int):
    cursor = con.cursor()
    cursor.execute("UPDATE Org SET org_nome = ?, org_reg = ?, org_end = ? WHERE org_id = ?", (Org.nom, Org.reg, Org.end, id,))
    cursor.execute("DELETE FROM org_contato WHERE org_id = ?", (id,))

    for c in Org.ctts:  
        cursor.execute("INSERT INTO org_contato VALUES (?, ?)", (id, c,))

    con.commit()
    return

@app.post("/orgadd")
def adicionar(Org: org):
    cursor = con.cursor()
    cursor.execute("SELECT MAX(org_id) FROM Org")
    res = cursor.fetchall()
    id = res[0][0]+1

    cursor.execute("INSERT INTO Org(org_id, org_nome, org_reg, org_end) VALUES (?, ?, ?, ?)", (id, Org.nom, Org.reg, Org.end,))
    for c in Org.ctts:
        cursor.execute("INSERT INTO org_contato VALUES (?, ?)", (id, c,))

    con.commit()
    return