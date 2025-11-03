import PyQt5.QtWidgets as qt
import PyQt5.QtCore as qtc
import os
from functools import partial #por algum motivo a função é executada na hora sem isso???
import ast #txt

#COMO USAR O TXT COMO BANCO

'''
tamanho:
label.setMinimumWidth(200)   # largura mínima
label.setMaximumHeight(50)   # altura máxima
label.setFixedSize(200, 40)  # tamanho fixo
'''

def limpar_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()

class Lista:
    def __init__(self):
        self.l = []

class Adicionar(qt.QWidget):
    def __init__(self, lista, main):
        super().__init__()
        self.lista = lista
        self.main = main
        self.setStyleSheet("""
                           *{
                            background-color: #414141;
                           color: white
                           }
                           
                           *::selection{
                            text-decoration: none;
                            background-color: #414141
                           }
                           """)

        self.setWindowTitle("Adicionar registro")
        self.resize(400, 300)

        layout = qt.QVBoxLayout()
        layout.setSpacing(10)

        layout2 = qt.QHBoxLayout()

        self.input_tipo = qt.QComboBox()
        self.input_tipo.addItems(["Receita", "Despesa"])
        self.input_tipo.setMinimumHeight(40)
        self.input_tipo.setMaximumWidth(100)
        self.input_tipo.setStyleSheet("font-size: 20px")
        layout2.addWidget(self.input_tipo)

        self.input_val = qt.QDoubleSpinBox()
        self.input_val.setRange(0.0, 100.0)
        self.input_val.setDecimals(2)
        self.input_val.setMinimumHeight(40)
        self.input_val.setAlignment(qtc.Qt.AlignCenter)
        self.input_val.setStyleSheet("font-size: 24px")
        layout2.addWidget(self.input_val)

        layout.addLayout(layout2)

        self.input_desc = qt.QLineEdit()
        self.input_desc.setMinimumHeight(100)
        self.input_desc.setPlaceholderText("Descrição: Exemplo de texto")
        self.input_desc.setStyleSheet("font-size: 15px; padding-top: -75px")
        layout.addWidget(self.input_desc)

        layout3 = qt.QHBoxLayout()

        btn = qt.QPushButton("Cancelar")
        btn.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95); border: none")
        btn.clicked.connect(partial(self.fechar))
        layout3.addWidget(btn)

        btn2 = qt.QPushButton("Salvar")
        btn2.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95); border: none")
        btn2.clicked.connect(partial(self.add))
        layout3.addWidget(btn2)

        layout.addLayout(layout3)

        self.setLayout(layout)

    def add(self):
        if len(self.lista.l) != 0:
            leng = len(self.lista.l)
            ult = (self.lista.l[leng-1])
            maiorid = ult["id"]
        else:
            maiorid = 1

        #pegar os inputs e passar pra var
        if self.input_tipo.currentText() == "Receita":
            tipo = "r"
        else:
            tipo = "d"

        val = float(self.input_val.text().replace(",", "."))

        dicti = {"tipo": tipo, "val": val, "desc": self.input_desc.text(), "id" : maiorid+1}
        self.lista.l.append(dicti)
        self.main.atualizar()
        self.close()
    
    def closeEvent(self, event):
        self.main.show()
        super().closeEvent(event)

    def fechar(self):
        self.close()

class Editar(qt.QWidget):
    def __init__(self, lista, id, main):
        super().__init__()
        id = int(id)
        self.main = main
        self.setStyleSheet("border: none; background-color: #414141; color: white")

        for i in lista.l:
            if i["id"] == id:
                mov = i

        if mov:
            layout1 = qt.QVBoxLayout()
            
            self.setWindowTitle("Editar registro")
            self.resize(300, 220)

            if mov["tipo"] == "r":
                tipo = "Receita"
            else:
                tipo = "Despesa"

            layout3 = qt.QHBoxLayout()

            label2 = qt.QLabel(tipo)
            label2.setStyleSheet("font-size: 18px; font-weight: 500; padding-top: 35px")
            label2.setAlignment(qtc.Qt.AlignCenter)
            layout3.addWidget(label2)

            label3 = qt.QLabel("R$"+"{:.2f}".format(mov["val"]))
            label3.setStyleSheet("font-size: 25px; font-weight: 500; padding-top: 20px")
            label3.setAlignment(qtc.Qt.AlignCenter)
            layout3.addWidget(label3)

            layout1.addLayout(layout3)

            label4 = qt.QLabel("Descrição: "+mov["desc"])
            label4.setStyleSheet("font-size: 13px")
            label4.setAlignment(qtc.Qt.AlignCenter)
            layout1.addWidget(label4)

            #botoões
            layout2 = qt.QHBoxLayout()

            btn1 = qt.QPushButton("Fechar")
            btn1.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95);")
            layout2.addWidget(btn1)

            btn2 = qt.QPushButton("Remover")
            btn2.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95);")
            layout2.addWidget(btn2)

            layout1.addLayout(layout2)
            self.btn1 = btn1; self.btn1.clicked.connect(partial(self.fechar))
            self.btn2 = btn2; self.btn2.clicked.connect(partial(self.remover, id))

            self.setLayout(layout1)

        self.lista = lista

    def remover(self, id):
        self.rem(id)
        self.main.atualizar()
        self.close()

    def rem(self, id):
        for i in self.lista.l:
            if i["id"] == id:
                self.lista.l.remove(i)

    def fechar(self):
        self.close()

    def closeEvent(self, event):
        self.main.show()
        super().closeEvent(event)

class Principal(qt.QWidget):
    def __init__(self, lista, dados):
        super().__init__()
        self.lista = lista
        self.dados = dados

        self.setWindowTitle("Controlsaldo")
        self.resize(450, 320)
        self.setStyleSheet("background-color: #414141; color: white")

        layout1 = qt.QVBoxLayout()

        #parte de cima
        layout2 = qt.QHBoxLayout()
        layout3 = qt.QHBoxLayout()
        layout3.setContentsMargins(0, 0, 0, 0)
        layout3.setSpacing(0)

        label1 = qt.QLabel("Controlador de Gastos")
        label1.setStyleSheet("font-size: 12px; font-weight: bold; text-align: center; padding-top: 10px;")
        label1.setAlignment(qtc.Qt.AlignCenter)
        layout2.addWidget(label1)

        sald = qt.QLabel("Saldo: ")
        sald.setStyleSheet("font-size: 30px;")
        sald.setFixedSize(105, 40)
        self.sal = qt.QLabel("R$ 0")

        layout3.addWidget(sald)
        layout3.addWidget(self.sal)
        layout3.setAlignment(qtc.Qt.AlignCenter)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        histscr = qt.QScrollArea()
        histscr.setStyleSheet("""
        QScrollBar:vertical {
        border: none;
        background: rgb(95, 95, 95);
        width: 12px;
        margin: 0px 0px 0px 0px;
        }
        * {
                              border: none}
                              
        QScrollBar::handle:vertical {
            background: #f0f0f0;
            max-height: 4px;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }
        """)
        histscr.setWidgetResizable(True)  # importante p/ ocupar espaço disponível
        histscr.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarAlwaysOff)
        histcont = qt.QWidget()
        self.hist = qt.QVBoxLayout(histcont)

        #item = qt.QHBoxLayout()
        for i in lista.l:
            #rec = "aplicpy/controlsaldo/up.png"
            #desp = "aplicpy/controlsaldo/down.png"
                
            lay = qt.QHBoxLayout()

            lbl1 = qt.QLabel("R$" + " {:.2f}".format(i["val"]))
            if i["tipo"] == "r":
                lbl1.setStyleSheet("background-image: url('aplicpy/controlsaldo/up.png'); background-repeat: no-repeat; font-size: 20px;")
            else:
                lbl1.setStyleSheet("background-image: url('aplicpy/controlsaldo/down.png'); background-repeat: no-repeat; font-size: 20px;")
            lbl1.setAlignment(qtc.Qt.AlignCenter)
            lbl1.setFixedSize(100, 60)

            lbl2 = qt.QLabel("")
            lbl2.setStyleSheet("font-size: 10px;")
            lbl2.setFixedSize(130, 40)

            if len(i["desc"]) > 20:
                lbl2.setText(i["desc"][0:20]+"...")
            else:
                lbl2.setText(i["desc"])

            btn = qt.QPushButton("Ver")
            btn.setStyleSheet("background-color: rgb(95, 95, 95)")
            btn.clicked.connect(partial(self.abrirEdi, i["id"]))
            btn.setFixedSize(90, 40)

            lay.addWidget(lbl1); lay.addWidget(lbl2); lay.addWidget(btn)
            
            self.hist.addLayout(lay)

        if len(self.lista.l) == 0:
            self.adicionarVoid()

        histscr.setWidget(histcont)
        layout1.addWidget(histscr)

        layout4 = qt.QHBoxLayout() #botões

        botao = qt.QPushButton("Adicionar")
        botao.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95); border: none")
        botao.clicked.connect(partial(self.abrirAdi))
        layout4.addWidget(botao)

        botao2 = qt.QPushButton("Remover todos")
        botao2.setStyleSheet("font-size: 18px; font-weight: 800; padding: 10px; background-color: rgb(95, 95, 95); border: none")
        botao2.clicked.connect(partial(self.removerTudo))
        layout4.addWidget(botao2)

        layout1.addLayout(layout4)

        self.setLayout(layout1)
        self.calcsaldo()

    def adicionarVoid(self):
        lblvoid = qt.QLabel("Parece vazio por enquanto...\ntente adicionar algo")
        lblvoid.setStyleSheet("font-size: 20px")
        lblvoid.setAlignment(qtc.Qt.AlignCenter)
        self.hist.addWidget(lblvoid)

    def calcsaldo(self):
        saldofin = 0.0
        for i in self.lista.l:
            if i["tipo"] == "r":
                saldofin += i["val"]
            else:
                saldofin -= i["val"]
        
        self.sal.setText("R$"+"{:.2f}".format(saldofin))

        if saldofin > 0:
            self.sal.setStyleSheet("color: rgb(178, 255, 155); font-size: 30px")

        else:
            self.sal.setStyleSheet("color: rgb(201, 38, 38); font-size: 30px")

    def clear_layout(self):
        while self.hist.count():
            item = self.hist.takeAt(0)

            l= item.layout()
            if l is not None:
                limpar_layout(l)
                l.deleteLater()

    def fill_layout(self):
        if len(self.lista.l) == 0:
            self.adicionarVoid()
            return

        for i in self.lista.l:
            #rec = "aplicpy/controlsaldo/up.png"
            #desp = "aplicpy/controlsaldo/down.png"
                
            lay = qt.QHBoxLayout()

            lbl1 = qt.QLabel("R$" + " {:.2f}".format(i["val"]))
            if i["tipo"] == "r":
                lbl1.setStyleSheet("background-image: url('aplicpy/controlsaldo/up.png'); background-repeat: no-repeat; font-size: 20px;")
            else:
                lbl1.setStyleSheet("background-image: url('aplicpy/controlsaldo/down.png'); background-repeat: no-repeat; font-size: 20px;")
            lbl1.setAlignment(qtc.Qt.AlignCenter)
            lbl1.setFixedSize(130, 60)

            lbl2 = qt.QLabel("")
            lbl2.setStyleSheet("font-size: 10px;")
            lbl2.setFixedSize(100, 40)

            if len(i["desc"]) > 13:
                lbl2.setText(i["desc"][0:13]+"...")
            else:
                lbl2.setText(i["desc"])

            btn = qt.QPushButton("Editar")
            btn.setStyleSheet("background-color: rgb(95, 95, 95)")
            btn.clicked.connect(partial(self.abrirEdi, i["id"]))
            btn.setFixedSize(90, 40)

            lay.addWidget(lbl1); lay.addWidget(lbl2); lay.addWidget(btn)
            
            self.hist.addLayout(lay)

    def removerTudo(self):
        if len(self.lista.l) == 0:
            aviso = qt.QMessageBox.question(
            self,
            "Erro",
            "Não há nenhum registro",
            qt.QMessageBox.Ok
            )
            return

        resposta = qt.QMessageBox.question(
            self,
            "Confirmar ação",
            "Deseja realmente excluir tudo?",
            qt.QMessageBox.Yes | qt.QMessageBox.No,
            qt.QMessageBox.No
        )

        if resposta == qt.QMessageBox.Yes:
            self.lista.l.clear()
            self.atualizar()

    def atualizar(self):
        self.clear_layout()
        self.fill_layout()
        self.calcsaldo()

    def abrirEdi(self, id):
        e = Editar(self.lista, id, self)
        e.show()
        self.hide()

    def abrirAdi(self):
        a = Adicionar(self.lista, self)
        a.show()
        self.hide()

    def closeEvent(self, event):
        with open(self.dados, "w") as f:
            f.write(str(self.lista.l))

        super().closeEvent(event)

def Iniciar():
    lista = Lista()
    lista.l = []
    app = qt.QApplication([])

    dir = os.path.dirname(os.path.abspath(__file__))
    dados = os.path.join(dir, "dados.txt")
    
    with open(dados, "r") as f:
        lista.l = ast.literal_eval(f.read())

    janela1 = Principal(lista, dados)
    janela1.show()

    app.exec_()

Iniciar()