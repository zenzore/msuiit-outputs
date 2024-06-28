/*
 * Rectangle Class
 * Author: Zach David B. Maregmen
 * 
 * This class has its own attributes hence I did not extend any other class.
 * 
 * It only has a width and a height.
 */

public class Rectangle extends Shape {
    double width;
    double height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }


    /*
     * Perimeter is just twice the sum of the width and height
     */
    public double getPerimeter() {
        return (this.width + this.height) * 2;
    }

    /*
     * Are is just the product of the width and height
     */
    public double getArea() {
        return this.width * this.height;
    }

    public String toString() {
        return String.format(
            "Circle [<base=%f>, <height=%f>, <area=%f>, <perimeter=%f>]", 
            this.width,
            this.height,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }
}
