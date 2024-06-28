/*
 * Square Class
 * Author: Zach David B. Maregmen
 * 
 * A Square is just a rectangle but all of the sides are equal.
 */

public class Square extends Rectangle {

    // I Initiated the class with the width and the height as both same values.
    Square(double width) {
        super(width, width);
    }

    public String toString() {
        return String.format(
            "Circle [<side=%f>, <area=%f>, <perimeter=%f>]", 
            this.width,
            this.getArea(), 
            this.getPerimeter()
            ); 
    }
    
}
