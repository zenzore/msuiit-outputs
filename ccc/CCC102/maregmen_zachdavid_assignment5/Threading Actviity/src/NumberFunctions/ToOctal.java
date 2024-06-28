/**
 * @author Zach David B. Maregmen
 *
 * This class is a runnable class which will append the converted octa-decimal value to a text area provided.
 */

package NumberFunctions;

import javax.swing.*;

public class ToOctal implements Runnable {
    private int minNumber;
    private int maxNumber;
    private JTextArea area;

    public ToOctal(String minNumber, String maxNumber, JTextArea area) {
        this.minNumber = Integer.parseInt(minNumber);
        this.maxNumber = Integer.parseInt(maxNumber);
        this.area = area;
    }

    @Override
    public void run() {
        for (int i = minNumber; i <= maxNumber; i++) {
            String octalNumber = NumberSystems.decimalToOctal(String.valueOf(i));
            area.append(octalNumber + "\n");
        }
    }
}
