package aplicjava;

//A rotina ou processos feitos para tal objeto são escondidos dele

import java.util.*;

class Prof{
    String nome; Integer id;

    public Prof(String nome, Integer id) {this.nome = nome; this.id = id;}

    public String getNome(){return this.nome;}
}

class Sala{
    String bloco; Integer id; String status = "vago";

    public Sala(){};

    public Sala(String bloco, Integer id){this.bloco = bloco; this.id = id;}

    public void setStatus(String stat){this.status = stat;}

    public String getStatus(){return this.status;}
}

class buscaSala{
    private List<Sala> salas = new ArrayList<>(Arrays.asList(new Sala("D", 15), new Sala("A", 12)));

    public Sala buscaVaga(){
        Sala sala = new Sala();

        for (Sala s: salas) if (s.getStatus().equals("vago")){
            sala = s;
            break;
        }

        return sala;
    }
}

class Reserva{
    private Prof prof = null; private Sala sala = null;

    public Reserva(Prof prof, Sala sala){this.prof = prof; this.sala = sala;}

    public String getDados(){
        return "Dados Reserva\nProf: "+prof.getNome()+"\nNº sala reservada: "+Integer.toString(sala.id);
    }
}

//reserva facade
public class Facade{
    private Prof prof = null; private Sala sala = null; private Reserva reserva = null;

    public void fazerReserva(String nomprof){
        prof = new Prof(nomprof, 1);

        sala = new buscaSala().buscaVaga();

        reserva = new Reserva(prof, sala);

        sala.setStatus("ocupada");

        System.out.println(reserva.getDados());
    }
}

class FacadeMain{
    public static void main(String[] args) {
        new Facade().fazerReserva("Carlos Eduardo");
    }

}
