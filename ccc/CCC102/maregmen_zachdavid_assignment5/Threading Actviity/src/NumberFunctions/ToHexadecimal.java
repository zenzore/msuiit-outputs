/**
 * @author Zach David B. Maregmen
 *
 * This class is a runnable class which will append the converted hexadecimal value to a text area provided.
 */


package NumberFunctions;

import javax.swing.*;

public class ToHexadecimal implements Runnable {
    private int minNumber;
    private int maxNumber;
    private JTextArea area;

    public ToHexadecimal(String minNumber, String maxNumber, JTextArea area) {
        this.minNumber = Integer.parseInt(minNumber);
        this.maxNumber = Integer.parseInt(maxNumber);
        this.area = area;
    }

    @Override
    public void run() {
        for (int i = minNumber; i <= maxNumber; i++) {
            String hexNumber = NumberSystems.decimalToHexadecimal(String.valueOf(i));
            area.append(hexNumber + "\n");
        }
    }
}
