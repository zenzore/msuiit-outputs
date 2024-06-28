package maregmen_zachdavid_assignment1.com;

/*
 * Zach David B. Maregmen | BSCS 1
 * 
 * 
 * This is a Line Class which contains two point objects
 * and can determine the slope of two points by its given 
 * coordinates.
 */


public class Line {
    private Point point1;
    private Point point2;

    Line(Point p1, Point p2) {
        this.point1 = p1;
        this.point2 = p2;
    }

    // GETTERS 

    public Point getFirstPoint() {
        return this.point1;
    }
    
    public Point getSecondPoint() {
        return this.point2;
    }

    // SETTERS 

    public void setFirstPoint(Point p1) {
        this.point1 = p1;
    }
    
    public void setSecondPoint(Point p2) {
        this.point2 = p2;
    }

    // METHOD 

    public double slope() {

        /*
         * Formula: y2 - y1 / x2 - x1
         */

        return (this.point2.getY() - this.point1.getY()) / (this.point2.getX() - this.point1.getX());
    }
    
}

