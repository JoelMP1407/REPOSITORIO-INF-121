import java.util.Random;
import java.util.Scanner;
public class JuegoAdivinaPar extends JuegoAdivinaNumero{   
    public JuegoAdivinaPar(int numDeVidas, int numeroAAdivinar) {
        super(numDeVidas, numeroAAdivinar);
    }    
    @Override
    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10) {
            if (numero % 2 == 0) {
                return true;
            } else {
                System.out.println("Error: el numero ingresado es impar. Solo se permiten numeros pares entre 0 y 10.");
                return false;
            }
        } else {
            System.out.println("Error: el numero está fuera del rango permitido (0 a 10).");
            return false;
        }
    }   
    @Override
    public void juega() {
    super.reiniciarPartida();
    Random random = new Random();
    Scanner sc = new Scanner(System.in);
    numeroAAdivinar = 2*random.nextInt(6);
        while (true) {
            System.out.println("Adivina un numero entre el 0 y el 10:");
            int intento = sc.nextInt();
            if (!validaNumero(intento)) {
                System.out.println("Numero invalido. Debe estar entre 0 y 10. Intenta de nuevo.");
                continue;
            }if (intento == numeroAAdivinar) {
                System.out.println("!!ACERTASTE!!");
                return;
            }else{
                boolean tieneVidas = quitaVida();
                if(tieneVidas){
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