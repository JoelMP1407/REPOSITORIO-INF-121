public class Juego {
    public int numDeVidas;
    public int record;
    public Juego(int numDeVidas) {
        this.numDeVidas = numDeVidas;
        this.record = 0;
    }
    
    public void reiniciarPartida(){
        numDeVidas=3;
    }
    public void actualizarRecord(int nuevoRecord){
        if (nuevoRecord>record){
            record = nuevoRecord;
        }
    }
    public boolean quitaVida(){
        if (numDeVidas>0){
            numDeVidas--;
        }return numDeVidas>0;
    }
}
