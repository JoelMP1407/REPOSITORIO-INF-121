public class Circulo extends Figura {
    private double radio;

    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
    }

    public Circulo(double radio, String color) {
        this.radio = radio;
        setColor(color);
    }

    @Override
    public double getPerimetro() {
        return 2 * Math.PI * getRadio();
    }

    @Override
    public double getArea() {
        return Math.PI * (getRadio() * getRadio());
    }

    @Override
    public String toString() {
        return "Circulo [Radio=" + radio + ", Color:" + getColor() + ", Perimetro=" + getPerimetro() + ", Area=" + getArea() + "]";
    }
}