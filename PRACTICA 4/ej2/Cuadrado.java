public class Cuadrado extends Figura implements Coloreado {
    private double lado;

    public double getLado() {
        return lado;
    }

    public void setLado(double lado) {
        this.lado = lado;
    }

    public Cuadrado(double lado, String color) {
        this.lado = lado;
        setColor(color);
    }

    @Override
    public double getPerimetro() {
        return getLado() * 4;
    }

    @Override
    public double getArea() {
        return getLado() * getLado();
    }   

    @Override
    public String comoColorear() {
        return ("Colorear los 4 lados");
    }
    
    @Override
    public String toString() {
        return "Cuadrado [Lado=" + lado + ", Color:" + getColor() + ", Perimetro=" + getPerimetro() + ", Area=" + getArea() + "]";
    }
}