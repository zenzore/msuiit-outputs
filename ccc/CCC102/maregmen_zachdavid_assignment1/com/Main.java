package maregmen_zachdavid_assignment1.com;

/*
 * Zach David B. Maregmen | BSCS 1
 * 
 * This is the Main class, there are examples how Point, Line, and RationalNumber 
 * classes can be used.
 * 
 * 
 *  Coded in Visual Studio Code
 */

public class Main {
    public static void main(String[] args) {
        Point p1 = new Point(10, 20);
        System.out.println("P1 X:" + p1.getX());
        System.out.println("P1 Y:" + p1.getY());
        
        Point p2 = new Point(30, 40);
        System.out.println("P2 X:" + p2.getX());
        System.out.println("P2 Y:" + p2.getY());

        System.out.println("Distance from p2 to p1 is: " + p1.distance(p2) + "\n\n");
        
        Line l = new Line(p1, p2);

        System.out.println("Slope is: " + l.slope() + "\n\n");

        RationalNumber n1 = new RationalNumber(5, 10);
        RationalNumber n2 = new RationalNumber(6, 9);
        RationalNumber simpleFormOfN1 = n1.toSimplestForm();

        double doubleOfN1 = n1.toDouble();
        System.out.println("Double form of "); n1.toString(); 
        System.out.println("Rational number n2 in string form: "); n2.toString();
        System.out.println("Simplest form of n1: "); simpleFormOfN1.toString();
        System.out.println("Comparison of n1 and n2: " + n1.compareTo(n2));
        
        RationalNumber sum = n1.add(n2);
        RationalNumber difference = n1.subtract(n2);
        RationalNumber quotient = n1.divides(n2);
        RationalNumber product = n1.multiply(n2);
        

        System.out.println("Sum of n1 + n2 : "); sum.toString();
        System.out.println("Difference of n1 - n2 : "); difference.toString();
        System.out.println("Quotient of n1 / n2 : "); quotient.toString();
        System.out.println("Product of n1 * n2 : "); product.toString();

        n1.setDenominator(0);
        boolean valid = RationalNumber.isValid(n1);
        System.out.println("Is n1 valid? " + valid);
        RationalNumber reciprocalOfN1 = n1.reciprocal();
        System.out.println("Reciprocal of n1 = "); reciprocalOfN1.toString();

    }
}
