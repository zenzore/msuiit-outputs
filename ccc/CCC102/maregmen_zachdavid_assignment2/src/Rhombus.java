/*
 * Rectangle Class
 * Author: Zach David B. Maregmen
 * 
 * Since the class requires a width and a height, I extended it from Rectangle as the super class
 * 
 * I added two new variables, the first and second diagonal.
 */

public class Rhombus extends Rectangle{
    double firstDiagonal, secondDiagonal;
    Rhombus(double firstDiagonal, double secondDiagonal) {
        super(Math.exp(firstDiagonal/2), Math.exp(secondDiagonal/2));
        this.firstDiagonal = firstDiagonal;
        this.secondDiagonal = secondDiagonal;
    }

    /*
     * The area of the rhombus is the product of first and second diagonal, all devided by 2.
     */
    @Override
    public double getArea() {
        return (this.firstDiagonal * this.secondDiagonal) / 2;
    }


    /*
    * I did not override the perimeter from the super class 
    * because both shapes have the same formula of getting the perimeter
    */

    public String toString() {
        return String.format(
            "Circle [<width=%f>, <height=%f>, <firstDiagonal=%f>, <firstDiagonal=%f>, <area=%f>, <perimeter=%f>]", 
            this.width, 
            this.height,
            this.firstDiagonal,
            this.secondDiagonal,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }
}
