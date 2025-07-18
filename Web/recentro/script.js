
function criaOrg(id) {
    const menuOrgs = document.querySelector('.col4-orgs');

    var div1 = document.createElement('div');
    div1.className = "org tirar"; div1.id = String(id); 
    div1.addEventListener("click", () => {escolheOrg(div1.id);})
    menuOrgs.appendChild(div1);

    var lin = document.createElement('div');
    lin.className = "ini-lin";
    div1.appendChild(lin);

    var col3 = document.createElement('div');
    col3.className = "ini-col3";

    var img = document.createElement('img');
    img.src = "pchd-img.png"; img.className = "org-img";
    col3.appendChild(img);

    var col4 = document.createElement('div');
    col4.className = "ini-col4 org-desc";

    var onom = document.createElement('p');
    onom.style = "justify-self: left;";
    var oend = document.createElement('p');
    oend.style = "justify-self: left;";
    col4.appendChild(onom);
    col4.appendChild(oend);

    lin.appendChild(col3);
    lin.appendChild(col4);

    let teste

    //parte da requisição
    fetch(`http://localhost:8000/org/` + String(id), {
        method: 'GET'
    })
    .then(res => res.json())
    .then(dados => {
        onom.textContent = dados.nom
        oend.textContent = dados.end
    })
    .catch(err => alert(err.toString()));
}

function carregarOrgs() {
    const menuOrgs = document.querySelector('.col4-orgs');
    //menuOrgs.innerHTML = ""; // Limpa o conteúdo atual

    //pegar ids
    let qtdid
    fetch(`http://localhost:8000/orgids`, {
        method: 'GET'
    })
    .then(res => res.json())
    .then(dado => {
        qtdid = parseInt(dado.res)

        //colocar as orgs no menu
        for (let i=1; i < qtdid+1; i++) {
            criaOrg(i);
        }

        var x = document.createElement('section')
        x.className = "orgs-x"
        menuOrgs.appendChild(x);
    })
}


let dadosCache = {};
dadosCache.ctt = []
dadosCache.cmax = 0
dadosCache.cid = 0
dadosCache.catual = 0

function escolheOrg(id) {
    localStorage.setItem("orgid", id)
    const iNome = document.getElementById('iNome')
    const iEnd = document.getElementById('iEnd')
    const iReg = document.getElementById('iReg')
    const iImg = document.querySelector('.info-img')
    const iCtt = document.querySelector('.ctt1')
    iNome.textContent = "------"
    iEnd.textContent = "------"
    iReg.textContent = "------"
    iImg.src = ""
    iCtt.textContent = "------"
    iImg.src = "pchd-img.png"

    //lógica para buscar dados no bd e trocar
    fetch(`http://localhost:8000/org/` + String(id), {
        method: 'GET'
    })
    .then(res => res.json())
    .then(dados => {
        iNome.textContent = dados.nom;
        iEnd.textContent = dados.end;
        iReg.textContent = dados.reg

        return fetch('http://localhost:8000/orgctt/' + String(id), {
        method: 'GET'
        })
    })
    .then(res => res.json())
    .then(dados => {
        if (dados.ctts[0]) {
            iCtt.textContent = dados.ctts[0]

            for (let i of dados.ctts){
                dadosCache.ctt.push(i)
                dadosCache.cmax++
            }
            dadosCache.cid = id
            dadosCache.catual = 0
            dadosCache.cmax -= 1
        }
    }) 
}

function trocaCtt(){
    const iCtt = document.querySelector('.ctt1')

    if (dadosCache.catual == dadosCache.cmax) {
        dadosCache.catual = 0
        iCtt.textContent = dadosCache.ctt[dadosCache.catual]
    } else {
        dadosCache.catual++
        iCtt.textContent = dadosCache.ctt[dadosCache.catual]
    }
}

function delOrg() {
    id = localStorage.getItem("orgid")

    fetch(`http://localhost:8000/orgdel/` + String(id), {
        method: "DELETE"
    })

    const iNome = document.getElementById('iNome')
    const iEnd = document.getElementById('iEnd')
    const iReg = document.getElementById('iReg')
    const iCtt = document.querySelector('.ctt1')

    iNome.textContent = "------"
    iEnd.textContent = "------"
    iReg.textContent = "------"
    iCtt.textContent = "------"
    carregarOrgs()
}

function addOrg() {
    const form = document.querySelector('.adi-form');

    if (form) {
        form.addEventListener('submit', function (e) {
        e.preventDefault();

        const fnom = form.nom.value.trim();
        const freg = form.reg.value;
        const fend = form.end.value.trim();
        const fctt1 = form.ctt1.value.trim();
        const fctt2 = form.ctt2.value.trim();
        const fctt3 = form.ctt3.value.trim();

        fetch("http://localhost:8000/orgadd", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                nom: fnom,  reg: freg, end: fend, ctts: [fctt1, fctt2, fctt3]
            })
        })

        limpaForm()
        alert("Adicionado!")
    })}
}

function setOrg() {
    const form = document.querySelector('.edi-form');
    id = localStorage.getItem("orgid")

    if (form) {
        form.addEventListener('submit', function (e) {
        e.preventDefault();

        const fnom = form.nom.value.trim();
        const freg = form.reg.value;
        const fend = form.end.value;
        const fctt1 = form.ctt1.value.trim();
        const fctt2 = form.ctt2.value.trim();
        const fctt3 = form.ctt3.value.trim();

        fetch(`http://localhost:8000/orgset/` + String(id), {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                nom: fnom,  reg: freg, end: fend, ctts: [fctt1, fctt2, fctt3]
            })
        })

        limpaForm()
        alert("Editado!")
    })}
}

function carregaForm(){
    const form = document.querySelector('.edi-form');

    if (form){
    let fnom = document.getElementById("nom")
    let fend = document.getElementById("end")
    let freg = document.getElementById("reg")
    let id = localStorage.getItem("orgid")

    fetch(`http://localhost:8000/org/` + String(id), {
        method: 'GET'
    })
    .then(res => res.json())
    .then(dados => {
        fnom.value = dados.nom;
        fend.value = dados.end;
        freg.value = dados.reg;
    })
    .catch(err => alert(err.toString()));
    }
}
document.addEventListener('DOMContentLoaded', carregaForm)

function limpaForm(){
    let fnom = document.getElementById("nom").value
    let fend = document.getElementById("end").value
    let fctt1 = document.getElementById("ctt1").value
    let fctt2 = document.getElementById("ctt2").value
    let fctt3 = document.getElementById("ctt3").value

    fnom = ""
    fend = ""
    fctt1 = ""
    fctt2 = ""
    fctt3 = ""
}

/* Exemplo de uso da rota
fetch("http://localhost:8000/clientes")
      .then(res => res.json())
      .then(dados => {
        const lista = document.getElementById("lista-clientes");

        dados.forEach(cliente => {
          const li = document.createElement("li");
          li.textContent = `ID: ${cliente.id} - Nome: ${cliente.nome}`;
          lista.appendChild(li);
        });
      })
      .catch(err => {
        console.error("Erro ao buscar clientes:", err);
      });
*/