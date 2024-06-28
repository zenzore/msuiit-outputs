/*
 * Parallelogram Class
 * Author: Zach David B. Maregmen
 * 
 * This class has its own attributes hence I did not extend any other class.
 * 
 * A parallelogram has a side, a base, and a height.
 */

public class Parallelogram extends Shape {
    double height;
    double base;
    double side;

    Parallelogram(double side, double base, double height) {
        this.base = base;
        this.height = height;
        this.side = side;
    }

    public double getPerimeter() {
        return 2 * (base + height);
    }

    public double getArea() {
        return base * height;
    }

    public String toString() {
        return String.format(
            "Circle [<base=%f>, <side=%f>, <height=%f>, <area=%f>, <perimeter=%f>]", 
            this.base, 
            this.side,
            this.height,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }

}
