package com.mycompany.inf121;
import java.util.Scanner;
public class EcuacionCuadratica {
    private double a, b, c;
    public EcuacionCuadratica(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    double getDiscriminante(){
        return (b*b)-(4*a*c);
    }
    double tieneRaices(){
        if(getDiscriminante() > 0){
            return 2;
        }else if(getDiscriminante() == 0){
            return 1;
        }else{
            return 0;
        }
    }
    double getRaiz1(){
        if(tieneRaices() >= 1){
            return (-b + Math.sqrt(getDiscriminante()))/(2*a);
        }else{
            return 0;
        }
    }
    double getRaiz2(){
        if(tieneRaices() == 2){
            return (-b - Math.sqrt(getDiscriminante()))/(2*a);
        }else{
            return 0;
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Ingrese los valores de a, b y c:");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a,b,c);
        if(ecuacion.tieneRaices() == 2){
            System.out.println("La ecuacion tiene dos soluciones");
            System.out.println("Raiz 1: " + ecuacion.getRaiz1());
            System.out.println("Raiz 2: " + ecuacion.getRaiz2());
        }else if(ecuacion.tieneRaices() == 1){
            System.out.println("La ecuacion tiene una solucion");
            System.out.println("Raiz: " + ecuacion.getRaiz1());
        }else{
            System.out.println("La ecuacion no tiene solucion");
        }
    }
}
