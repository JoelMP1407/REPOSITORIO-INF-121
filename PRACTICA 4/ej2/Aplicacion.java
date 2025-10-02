import java.util.Random;
import java.util.Scanner;
public class Aplicacion {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[5];
        Random random = new Random();
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < figuras.length; i++) {
            int tipo = random.nextInt(2) + 1;
            if (tipo == 1) {
                System.out.println("Se ha generado un cuadrado.");
                double lado = 1 + (random.nextDouble() * 9);
                System.out.println("Introduzca el color del cuadrado:"); String color=sc.nextLine();
                figuras[i] = new Cuadrado(lado, color);
            }else{
                System.out.println("Se ha generado un circulo.");
                double radio = 1 + (random.nextDouble() * 9);
                System.out.println("Introduzca el color del circulo:"); String color=sc.nextLine();
                figuras[i] = new Circulo(radio, color);
            }
        }
        System.out.println("Figuras generadas:");
        for (int i = 0; i < figuras.length; i++) {
            System.out.println(figuras[i].toString());
            if (figuras[i] instanceof Coloreado coloreado) {
                System.out.println(coloreado.comoColorear());
            }
        }
    }
}
