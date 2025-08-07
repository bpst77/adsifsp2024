package aplicjava;
import java.util.ArrayList;
import java.util.List;

interface Subject {
    public void addObserver(Observer o);

    public void removeObserver(Observer o);

    public void notifyObservers(Valores v);
}

public interface Observer {
    public void updateValor(Valores v);
}

class Valores {
    List<Double> valores = new ArrayList<>();
    
    public Valores() {
        this.valores.add(10.00);
        this.valores.add(20.00);
    }

    public void limpar(){
        this.valores.clear();
    }

    public Double getValor(Integer n){ return valores.get(n); }
}

//aaaaaaaaaaaaaaaaaaaa

class CentralSubject implements Subject{
    private ArrayList<Observer> observers = new ArrayList<Observer> ();

    @Override
    public void addObserver(Observer o) { observers.add(o); }
    public void removeObserver(Observer o) { observers.remove(o); }
    public void notifyObservers(Valores v){
        for (Observer o : observers) o.updateValor(v);
    }

    public ArrayList<Observer> getObservers() { return observers; }
}

class Assinante implements Observer {
    private String nome; private int tipoPlano; private Double precoPlano;
    
    public Assinante(String nome, int tipoPlano, Valores v) { this.nome = nome; this.tipoPlano = tipoPlano; this.precoPlano = v.getValor(tipoPlano); }

    public String getValor() { return nome+", o preço do seu plano é: R$"+Double.toString(this.precoPlano); }

    @Override
    public void updateValor(Valores v) { 
        this.precoPlano = v.getValor(this.tipoPlano);
     }
}

class obsMain {
    public static void main(String[] args) {
        Valores v = new Valores();

        CentralSubject cs = new CentralSubject();

        Assinante a = new Assinante("Carlos", 1, v);
        Assinante b = new Assinante("Craudia", 2, v);

        System.out.println("Antes");
        a.getValor();
        b.getValor();

        v.limpar();

        v.valores.add(30.00);
        v.valores.add(40.00);

        cs.notifyObservers(v);

        System.out.println("Depois");
        a.getValor();
        b.getValor();
    }
}