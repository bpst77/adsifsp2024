package aplicjava;

//No Singleton basicamente, você limite o uso de um processo ou a instanciação de uma classe até somente 1

//classe admin
public class Singleton {
    private String status;
    private static Singleton instance = null;

    private Singleton() {status = "";}

    public static Singleton getInstance(){
        if (instance == null) {instance = new Singleton(); return instance;}
        else {System.out.println("Conta já acessada, espere"); return null;}
    }

    public void setStatus(String stat){this.status = stat;}

    public String getStatus(){return this.status;}
}

class obsMain {
    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();

        if (s1 != null) {System.out.println("Conta acessada");};
        if (s2 != null) {System.out.println("Conta acessada");};
    }

}
