/*
 * Triangle Class
 * Author: Zach David B. Maregmen
 * 
 * Triangle is just half the paralellogram in terms of area
 * and the perimeter is the sum of the base and it's two sides.
 */

public class Triangle extends Parallelogram{
    double secondSide;

    Triangle(double side, double secondSide, double base, double height) {
        super( side, base, height);
        this.secondSide = secondSide;
    }

    // the area is the half of the area of the parallelogram.
    @Override
    public double getArea() {
        return super.getArea() / 2;
    }

    
    @Override
    public double getPerimeter() {
        return this.side + this.secondSide + this.base;
    }

    public String toString() {
        return String.format(
            "Triangle [<base=%f>, <height=%f>, <side=%f>, <secondSide=%f>, <area=%f>, <perimeter=%f>]", 
            this.base, 
            this.height, 
            this.side,
            this.secondSide,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }
}
