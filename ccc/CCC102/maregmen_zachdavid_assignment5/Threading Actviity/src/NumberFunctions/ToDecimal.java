/**
 * @author Zach David B. Maregmen
 *
 * This class is a runnable class which will append the converted decimal value to a text area provided.
 */

package NumberFunctions;

import javax.swing.*;

public class ToDecimal implements Runnable {
    private final int minNumber;
    private final int maxNumber;
    private JTextArea area;

    public ToDecimal(String minNumber, String maxNumber, JTextArea area) {
        this.minNumber = Integer.parseInt(minNumber);
        this.maxNumber = Integer.parseInt(maxNumber);
        this.area = area;
    }

    @Override
    public void run() {
        for (int i = minNumber; i <= maxNumber; i++) {
            area.append(i + "\n");
        }
    }
}
