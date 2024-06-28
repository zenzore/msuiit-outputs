/*
 * Circle Class 
 * Author: Zach David B. Maregmen
 * 
 * This class has its own attributes hence I did not extend any other class.
 */

public class Circle extends Shape {
    private int radius;
    public static final double PI = 3.14; 
    // I made this attribute a static since it is a universal constant

    /*
     * The area formula of a circle is the square of pi * radius
     */
    public double getArea() {
        return (this.radius * this.radius) * Circle.PI;
    }

    /*
     * The perimeter formula of a circle is twice the product of radius and PI
     */
    public double getPerimeter() {
        return (2 * this.radius) * Circle.PI;
    }

    public String toString() {
        return String.format(
            "Circle [<radius=%f>, <area=%f>, <perimeter=%f>]", 
            this.radius, 
            this.getArea(), 
            this.getPerimeter()
            ); 
    }

}
