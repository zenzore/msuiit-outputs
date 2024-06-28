package maregmen_zachdavid_assignment1.com;

/*
 * Zach David B. Maregmen | BSCS 1
 * 
 * 
 * This is the RationalNumber class where you can define
 * it as a fraction. There are many methods of this class
 * in which you can convert it to a string, decimal, or 
 * you can compare it to other rational number classes.
 * 
 * This class also does operations such as addition, subtraction,
 * multiplication, division, getting the reciprocal and as well as 
 * to determine if it is valid or not.
 */

public class RationalNumber {
    private int numerator;
    private int denominator;

    RationalNumber(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    // GETTERS 

    public int getNumerator() {
        return this.numerator;
    }

    public int getDenominator() {
        return this.denominator;
    }

    // SETTERS 

    public void setNumerator(int numerator) {
        this.numerator = numerator;
    }

    public void setDenominator(int denominator) {
        this.denominator = denominator;
    }

    // PRIVATE FRACTION COMPUTATION FUNCTIONS 

    

    private static int gcf(int x, int y) {

        /*
         * GCF(Greatest Common Factor) FUNCTION
         * 
         * the logic is hard yet simple, it will recurse the given parameters until
         * one of it returns a remainder of 0 when divided by the bigger number.
         */

        if (x == 0) {
            return y;
        }
        return gcf(y % x, x);
    }

    

    private static int lcm(int x, int y) {

        /*
         * LCM(Least Common Multiple) FUNCTION
         * 
         * it's just basic grade 2 fraction method.
         */

        return (x * y) / gcf(x, y);
    }
    

    // METHODS

    public double toDouble() {
        return (double) this.numerator / this.denominator;
    }

    public void toString() {
        System.out.println(this.numerator + "/" + this.denominator); 
    }

    public RationalNumber toSimplestForm() {
        int factor = RationalNumber.gcf(this.denominator, this.numerator);
        return new RationalNumber(this.numerator / factor, this.denominator / factor);
    }

    public int compareTo(RationalNumber rat) {
        if (this.toDouble() > rat.toDouble()) return 1;
        if (this.toDouble() < rat.toDouble()) return -1;
        return 0;
    }

    public RationalNumber add(RationalNumber rat) {
        // get lcm of the denominators.
        
        int newDenominator = RationalNumber.lcm(this.denominator, rat.denominator);
        
        // add the two numerators in terms of fractional computation [(lcm / denominator) * numerator]

        return new RationalNumber(
            ((newDenominator / this.denominator) * this.numerator) + ((newDenominator / rat.getDenominator()) * rat.getNumerator()), // new numerator
            newDenominator // new denominator which is the lcm.
        );
    }

    public RationalNumber subtract(RationalNumber rat) {
        // get lcm of the denominators.
        
        int newDenominator = RationalNumber.lcm(this.denominator, rat.denominator);
        
        // add the two numerators in terms of fractional computation [(lcm / denominator) * numerator]

        return new RationalNumber(
            ((newDenominator / this.denominator) * this.numerator) - ((newDenominator / rat.getDenominator()) * rat.getNumerator()), // new numerator
            newDenominator // new denominator which is the lcm.
        );
    }

    public RationalNumber multiply(RationalNumber rat) { 
        return new RationalNumber(this.numerator * rat.getNumerator(), this.denominator * rat.getDenominator());
    }

    public RationalNumber divides(RationalNumber rat) {
        // division is basically the product of the first fraction and the reciprocal of the second function.
        RationalNumber reciprocalOfTheArgument = rat.reciprocal();
        return this.multiply(reciprocalOfTheArgument);
    }

    static boolean isValid(RationalNumber rat) {
        if (rat.getNumerator() == 0 || rat.getDenominator() == 0) return false;
        return true;
    }

    public RationalNumber reciprocal() {
        return new RationalNumber( this.denominator, this.numerator);
    }

}
