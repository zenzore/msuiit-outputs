/**
 * @author Zach David B. Maregmen
 *
 * These are the number methods class that has conversion and checker methods.
 */


public class NumberMethods {

    /*
        We need to check first if the input is a convertable number.
     */
    public static boolean checkIfBinary (String a) {
        for (int i = 0; i < a.length(); i++) {
            char ch = a.charAt(i);
            if (ch != '0' && ch != '1') {
                return false;
            }
        }
        return true;
    }

    public static boolean checkIfOctal(String a) {
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            if (c < '0' || c > '7') {
                return false;
            }
        }
        return true;
    }

    public static boolean checkIfDecimal(String a) {
        if (a == null || a.isEmpty()) {
            return false;
        }
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            if (!Character.isDigit(c) && c != '.') {
                return false;
            }
        }
        return true;
    }

    public static boolean checkIfHexaDecimal(String a) {
        if (a == null || a.isEmpty()) {
            return false;
        }
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            if (!Character.isDigit(c) && !(c >= 'a' && c <= 'f') && !(c >= 'A' && c <= 'F')) {
                return false;
            }
        }
        return true;
    }


    /*
        These are converters that will convert anything number to any number.

        I've focused everything at the decimal number because it is easy to convert it to any other number
     */
    public static String binaryToDecimal(String binary) {
        int decimal = 0;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                decimal += Math.pow(2, binary.length() - 1 - i);
            }
        }
        return Integer.toString(decimal);
    }

    public static String decimalToBinary(String decimal) {
        StringBuilder binary = new StringBuilder();
        int dcml = Integer.parseInt(decimal);
        while (dcml != 0) {
            int remainder = dcml % 2;
            binary.insert(0, remainder);
            dcml /= 2;
        }
        return binary.toString();
    }

    public static String decimalToOctal(String decimal) {
        int decimalInt = Integer.parseInt(decimal);
        StringBuilder octal = new StringBuilder();
        while (decimalInt != 0) {
            int remainder = decimalInt % 8;
            octal.insert(0, remainder);
            decimalInt /= 8;
        }
        return octal.toString();
    }

    public static String octalToDecimal(String octal) {
        int decimal = 0;
        for (int i = 0; i < octal.length(); i++) {
            int digit = Character.getNumericValue(octal.charAt(i));
            decimal += digit * Math.pow(8, octal.length() - 1 - i);
        }
        return Integer.toString(decimal);
    }

    public static String decimalToHexadecimal(String decimal) {
        StringBuilder hexadecimal = new StringBuilder();
        int dcml = Integer.parseInt(decimal);
        while (dcml != 0) {
            int remainder = dcml % 16;
            if (remainder < 10) {
                hexadecimal.insert(0, remainder);
            } else {
                hexadecimal.insert(0, (char) ('A' + remainder - 10));
            }
            dcml /= 16;
        }
        return hexadecimal.toString();
    }

    public static String hexadecimalToDecimal(String hex) {
        String digits = "0123456789ABCDEF";
        int decimal = 0;
        for (int i = 0; i < hex.length(); i++) {
            char ch = hex.charAt(i);
            int digit = digits.indexOf(ch);
            decimal = 16 * decimal + digit;
        }
        return Integer.toString(decimal);
    }
}
