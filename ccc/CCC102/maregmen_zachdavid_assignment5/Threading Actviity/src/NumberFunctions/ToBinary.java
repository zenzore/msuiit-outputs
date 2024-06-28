/**
 * @author Zach David B. Maregmen
 *
 * This class is a runnable class which will append the converted binary value to a text area provided.
 */

package NumberFunctions;

import javax.swing.*;

public class ToBinary implements Runnable {
    private int minNumber;
    private int maxNumber;
    private JTextArea area;

    public ToBinary(String minNumber, String maxNumber, JTextArea area) {
        this.minNumber = Integer.parseInt(minNumber);
        this.maxNumber = Integer.parseInt(maxNumber);
        this.area = area;
    }

    @Override
    public void run() {
        for (int i = minNumber; i <= maxNumber; i++) {
            String binaryNumber = NumberSystems.decimalToBinary(String.valueOf(i));
            area.append(binaryNumber + "\n");
        }
    }
}
