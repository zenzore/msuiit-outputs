/*
 * Semi Circle Class
 * Author: Zach David B. Maregmen
 * 
 * Since the class requires a radius, I added the Circle as a super class
 * 
 * It only requires a radius and I overrided the rest of the functions.
 * 
 * all of the resulting numbers of functions from the Circle class 
 * (area and perimeter) is just twice the semi circle's values
 * 
 * I multiplied all of the formulas by 1/2
 */



public class SemiCircle extends Circle {
    @Override
    public double getArea() {
        return super.getArea() / 2;
    }

    @Override
    public double getPerimeter() {
        return super.getPerimeter() / 2;
    }
}
