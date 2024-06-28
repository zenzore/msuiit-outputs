/*
 * Square Class
 * Author: Zach David B. Maregmen
 * 
 * A Rhomus has the same structures as the parallelogram but with different sides and bases.
 * I just extended it from the parallelogram class.
 * 
 */


public class Trapezoid extends Parallelogram {
    double secondBase;
    double secondSide;

    // I just added two variables.
    Trapezoid(double side, double base, double height, double secondBase, double secondSide) {
        super(side, base, height);
        this.secondBase = secondBase;
        this.secondSide = secondSide;
    }


    /*
     * The perimeter is 
     * the sum of all sides and bases.
     */
    @Override
    public double getPerimeter() {
        return this.side + this.secondSide + this.base + this.secondBase;
    }

    /*
     * Formula of the area is the sum of two bases dived by 2 multiplied by the height.
     */
    @Override
    public double getArea() {
        return ((this.base + this.secondBase) / 2) * this.height;
    }

    public String toString() {
        return String.format(
            "Circle [<width=%f>, <height=%f>, <firstDiagonal=%f>, <firstDiagonal=%f>, <area=%f>, <perimeter=%f>]", 
            this.base, 
            this.height,
            this.side,
            this.secondSide,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }
}
