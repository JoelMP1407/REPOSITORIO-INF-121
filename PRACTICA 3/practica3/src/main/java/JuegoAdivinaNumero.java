import java.util.Random;
import java.util.Scanner;
public class JuegoAdivinaNumero extends Juego{
    public int numeroAAdivinar;
    public JuegoAdivinaNumero(int numDeVidas, int numeroAAdivinar){
        super(numDeVidas);
        this.numeroAAdivinar = numeroAAdivinar;
    }   
    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }    
    public void juega() {
    super.reiniciarPartida();
    Random random = new Random();
    Scanner sc = new Scanner(System.in);
    numeroAAdivinar = random.nextInt(11);
    while (true) {
        System.out.println("Adivina un numero entre el 0 y el 10:");
        int intento = sc.nextInt();        
        if (!validaNumero(intento)) {
            System.out.println("Numero invalido. Debe estar entre 0 y 10. Intenta de nuevo.");
            continue;
        }
        if (intento == numeroAAdivinar) {
            System.out.println("!!ACERTASTE!!");
            return;
        } else {
            boolean tieneVidas = quitaVida();
            if (tieneVidas) {
                if (intento < numeroAAdivinar) {
                    System.out.println("El numero a adivinar es mayor.");
                } else {
                    System.out.println("El numero a adivinar es menor.");
                }
                System.out.println("Intenta de nuevo.");
            } else {
                System.out.println("Fallaste. Ya no te quedan vidas.");
                System.out.println("El numero correcto era: " + numeroAAdivinar);
                return;
            }
        }
        System.out.println("Vidas restantes: " + numDeVidas);
        System.out.println("-----------------------------");
    }
    }
}    