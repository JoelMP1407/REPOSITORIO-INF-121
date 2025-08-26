package com.mycompany.inf121;
import java.util.Scanner;
public class Estadisticas {
    private double d1,d2,d3,d4,d5,d6,d7,d8,d9,d10;
    public Estadisticas(double d1, double d2, double d3, double d4, double d5, double d6, double d7, double d8, double d9, double d10){
        this.d1 = d1;
        this.d2 = d2;
        this.d3 = d3;
        this.d4 = d4;
        this.d5 = d5;
        this.d6 = d6;
        this.d7 = d7;
        this.d8 = d8;
        this.d9 = d9;
        this.d10 = d10;
    }
    double promedio(){
        return (d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)/10;
    }
    double desviacion(){
        double Sum = (Math.pow((d1-promedio()), 2))+(Math.pow((d2-promedio()), 2))+(Math.pow((d3-promedio()), 2))+(Math.pow((d4-promedio()), 2))+(Math.pow((d5-promedio()), 2))+(Math.pow((d6-promedio()), 2))+(Math.pow((d7-promedio()), 2))+(Math.pow((d8-promedio()), 2))+(Math.pow((d9-promedio()), 2))+(Math.pow((d10-promedio()), 2));
        return Math.sqrt(Sum/9);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Ingrese los 10 valores para hallar su promedio y desviacion:");
        double d1 = sc.nextDouble();
        double d2 = sc.nextDouble();
        double d3 = sc.nextDouble();
        double d4 = sc.nextDouble();
        double d5 = sc.nextDouble();
        double d6 = sc.nextDouble();
        double d7 = sc.nextDouble();
        double d8 = sc.nextDouble();
        double d9 = sc.nextDouble();
        double d10 = sc.nextDouble();
        Estadisticas datos = new Estadisticas(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10);
        System.out.println("El promedio es:" + datos.promedio());
        System.out.println("La desviacion es:" + datos.desviacion());
    }
}
