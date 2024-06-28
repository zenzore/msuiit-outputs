

package maregmen_zachdavid_assignment1.com;

// this will be used for getting the square root of numbers
import java.lang.Math;

/*
 * Zach David B. Maregmen | BSCS 1
 * 
 * 
 * This is a point class where you can determine the distance
 * and the quadrant of the point given by its coordinates.
 */

public class Point {
    private double x;
    private double y;
    
    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Setters

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    // GETTERS 

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    // METHODS 


    public double distance(Point p) {

        /*
         * Formula = square root of [(x2 - x1)^2 + (y2 - y1)^2]
         */

        return Math.sqrt(
            (p.getX() - this.x) * (p.getX() - this.x)
            + 
            (p.getY() - this.y) * (p.getY() - this.getY())
        );
    }

    public int getQuadrant() {
        if (this.x > 0 && this.y > 0) return 1;
        if (this.x < 0 && this.y > 0) return 2;
        if (this.x < 0 && this.y < 0) return 3;
        if (this.x > 0 && this.y < 0) return 4;

        return 0; // this will return 0 if the point resides at the origin.
    }
}
