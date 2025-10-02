public abstract class Figura {
    private  String color;

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    
    public abstract double getPerimetro();
    
    public abstract double getArea();

    @Override
    public String toString() {
        return "Figura[color=" + color + "]";
    }
}