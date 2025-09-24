public class Aplicacion {
    public static void main(String[] args){
        JuegoAdivinaNumero juegoNormal = new JuegoAdivinaNumero(3, 0);
        System.out.println("=== Juego Adivina Numero ===");
        juegoNormal.juega();
        
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3, 0);
        System.out.println("=== Juego Adivina Numero Par ===");
        juegoPar.juega();
        
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3, 0);
        System.out.println("=== Juego Adivina Numero Impar ===");
        juegoImpar.juega();
    }
}
