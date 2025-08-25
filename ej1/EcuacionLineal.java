import java.util.Scanner;
public class EcuacionLineal {
    private double a,b,c,d,e,f;
    public EcuacionLineal(double a, double b, double c, double d, double e, double f){
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.e = e;
        this.f = f;
    }
    double tieneSolucion(){
        if((a*d)-(b*c) != 0){
            return 1;
        }else{
            return 0;
        }
    }
    double getX(){
        if(tieneSolucion() == 1){
            return ((e*d)-(b*f))/((a*d)-(b*c));
        }else{
            return 0;
        }
    }
    double getY(){
        if(tieneSolucion() == 1){
            return ((a*f)-(e*c))/((a*d)-(b*c));
        }else{
            return 0;
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Ingrese los valores de a, b, c, d, e y f:");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double d = sc.nextDouble();
        double e = sc.nextDouble();
        double f = sc.nextDouble();
        EcuacionLineal ecuacion = new EcuacionLineal(a,b,c,d,e,f);
        if(ecuacion.tieneSolucion() == 1){
            System.out.println("La ecuacion tiene solucion");
            System.out.println("X: " + ecuacion.getX());
            System.out.println("Y: " + ecuacion.getY());
        }else{
            System.out.println("La ecuacion no tiene solucion");
        }
    }
}
