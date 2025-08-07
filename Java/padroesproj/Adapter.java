package aplicjava;

class Serviço{
    public void imprime(newComp componente){
        System.out.println(componente.getDados());
    }
}

class newComp{
    String nome; String idade; String salario;

    public newComp(String nome, String idade, String salario){this.nome = nome; this.idade = idade; this.salario = salario;}

    public String getDados(){
        return "Dados:\nNome: "+this.nome+"\nIdade: "+this.idade+"\nSalario: "+this.salario;
    }
}

class oldComp{
    String nome; Integer idade; Double salario;

    public oldComp(String nome, Integer idade, Double salario){this.nome = nome; this.idade = idade; this.salario = salario;}
}

//adaptador de outros tipos pra String
public class Adapter extends newComp {
    private oldComp Comp;
    
    public Adapter(oldComp Comp){
        super(Comp.nome, Integer.toString(Comp.idade), Double.toString(Comp.salario));
        this.Comp = Comp;
    }

    public String getDados(){
        return "Dados:\nNome: "+this.Comp.nome+"\nIdade: "+this.Comp.idade+"\nSalario :"+this.Comp.salario;
    }
}

class adpMain{
    public static void main(String[] args) {
        Serviço s = new Serviço();

        System.err.println("");
        System.err.println("Novo(com strings)");
        newComp novo = new newComp("Marcelo", "11", "5000.00");
        s.imprime(novo);

        System.err.println("");
        System.err.println("Velho(com dados numéricos)");
        oldComp velho = new oldComp("Casca", 13, 2500.00);
        Adapter adaptado = new Adapter(velho);
        s.imprime(adaptado);
    }
}
