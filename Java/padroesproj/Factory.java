package aplicjava;

//Apenas uma classe cuida da instanciação de novos objetos sem o solicitante necessariamente entender o que ocorre

interface Registro{
    public String getDados();
}

class Func implements Registro{
    String nome;
    String cargo;

    public Func(String nome, String cargo) {
        this.nome = nome; this.cargo = cargo;
    }

    public String getDados(){
        return "Func\nNome: " + this.nome + "\nCargo: " + this.cargo;
    }
}

class Cliente implements Registro{
    String nome;
    String ctt;

    public Cliente(String nome, String ctt) {
        this.nome = nome; this.ctt = ctt;
    }

    public String getDados(){
        return "Cliente\nNome: " + this.nome + "\nContato: " + this.ctt;
    }
}

public class Factory{
    public Registro getRegistro(String tipo, String nome, String ctt, String cargo){
        Registro r = null;

        if (tipo.equals("cliente")) r = new Cliente(nome, ctt);
        else if (tipo.equals("func")) r = new Func(nome, cargo);

        return r;
    }
}

class fctMain {
    public static void main(String[] args) {
        Factory f = new Factory();
        Registro r = null;

        r = f.getRegistro("cliente", "Julio", "juliaodoaa@hotmail.com", null);
        System.out.println(r.getDados());

        System.out.println("");
        r = f.getRegistro("func", "Marcelo", null, "Repositor");
        System.out.println(r.getDados());
    }
}

