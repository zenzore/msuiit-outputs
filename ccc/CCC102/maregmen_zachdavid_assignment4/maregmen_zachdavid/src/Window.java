import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

public class Window extends JFrame implements ActionListener {
    private final JComboBox<String> firstComboBox;
    private final JComboBox<String> secondComboBox;
    private final JButton generateButton = new JButton("GENERATE");
    private final JTextField textField = new JTextField(20);
    private String firstItem, secondItem = "NONE";
    Window() {
        this.setTitle("Number Systems Converter.");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setLayout(new FlowLayout());

        String[] selections = {"NONE", "BINARY", "OCTAL", "DECIMAL", "HEXADECIMAL"};

        JPanel firstComboBoxPanel = new JPanel();
        JPanel secondComboBoxPanel = new JPanel();
        firstComboBoxPanel.add(new JLabel("Converted from: "));
        secondComboBoxPanel.add(new JLabel("Converted to: "));

        this.firstComboBox = new JComboBox<>(selections);
        this.firstComboBox.addActionListener(this);
        this.secondComboBox = new JComboBox<>(selections);
        this.secondComboBox.addActionListener(this);
        this.generateButton.addActionListener(this);
        firstComboBoxPanel.add(firstComboBox);
        secondComboBoxPanel.add(secondComboBox);

        this.add(firstComboBoxPanel);
        this.add(secondComboBoxPanel);
        this.add(textField);
        this.add(generateButton);
        this.pack();
        this.setLocationRelativeTo(null);
        this.setVisible(true);
    }

    public void errorMessage(String message) {
        JOptionPane.showMessageDialog(this, message);
    }

    public void convertSuccessPane(String message) {
        JOptionPane.showMessageDialog(this, "Converted Successfully!\n\n= " + message);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == firstComboBox) {
            firstItem = (String) this.firstComboBox.getSelectedItem();
            System.out.println(firstItem);
        }
        if (e.getSource() == secondComboBox) {
            secondItem = (String) this.secondComboBox.getSelectedItem();
            System.out.println(secondItem);
        }

        // the generate button will have the longest action statement
        outer: // labeled value
        if (e.getSource() == generateButton) {
            // it will check if y
            if (Objects.equals(firstItem, "NONE") || Objects.equals(secondItem, "NONE")) {
                errorMessage("Error, you didn't select a converter");
                break outer;
            }
            if (Objects.equals(firstItem, secondItem)) {
                errorMessage("Error, you can't convert your value to the same type of value.");
                break outer;
            }
            if (textField.getText().length() == 0) {
                errorMessage("Error, you did not provide the value that you want to convert");
                break outer;
            }

            // after this checks above, it can finally check if the provided query and text can be converter
            // without any errors.
            if (Objects.equals(firstItem, "BINARY")) {

                if (!NumberMethods.checkIfBinary(textField.getText())) {
                    errorMessage("Error, the number is not a binary number.");
                    break outer;
                }

                String decimal = NumberMethods.binaryToDecimal(textField.getText());

                if (Objects.equals(secondItem, "DECIMAL")) {
                    convertSuccessPane(decimal);
                }
                if (Objects.equals(secondItem, "OCTAL")) {
                    convertSuccessPane(NumberMethods.decimalToOctal(decimal));
                }
                if (Objects.equals(secondItem, "HEXADECIMAL")) {
                    convertSuccessPane(NumberMethods.decimalToHexadecimal(decimal));
                }
            }

            if (Objects.equals(firstItem, "OCTAL")) {

                if (!NumberMethods.checkIfOctal(textField.getText())) {
                    errorMessage("Error, the number is not a octal number.");
                    break outer;
                }

                String decimal = NumberMethods.octalToDecimal(textField.getText());

                if (Objects.equals(secondItem, "DECIMAL")) {
                    convertSuccessPane(decimal);
                }
                if (Objects.equals(secondItem, "BINARY")) {
                    convertSuccessPane(NumberMethods.decimalToBinary(decimal));
                }
                if (Objects.equals(secondItem, "HEXADECIMAL")) {
                    convertSuccessPane(NumberMethods.decimalToHexadecimal(decimal));
                }
            }

            if (Objects.equals(firstItem, "DECIMAL")) {

                if (!NumberMethods.checkIfDecimal(textField.getText())) {
                    errorMessage("Error, the number is not a decimal number.");
                    break outer;
                }

                String decimal = textField.getText();

                if (Objects.equals(secondItem, "BINARY")) {
                    convertSuccessPane(NumberMethods.decimalToBinary(decimal));
                }
                if (Objects.equals(secondItem, "OCTAL")) {
                    convertSuccessPane(NumberMethods.decimalToOctal(decimal));
                }
                if (Objects.equals(secondItem, "HEXADECIMAL")) {
                    convertSuccessPane(NumberMethods.decimalToHexadecimal(decimal));
                }
            }

            if (Objects.equals(firstItem, "HEXADECIMAL")) {

                if (!NumberMethods.checkIfHexaDecimal(textField.getText())) {
                    errorMessage("Error, the number is not a hexadecimal number.");
                    break outer;
                }

                String decimal = NumberMethods.hexadecimalToDecimal(textField.getText());

                if (Objects.equals(secondItem, "BINARY")) {
                    convertSuccessPane(NumberMethods.decimalToBinary(decimal));
                }
                if (Objects.equals(secondItem, "DECIMAL")) {
                    convertSuccessPane(decimal);
                }
                if (Objects.equals(secondItem, "OCTAL")) {
                    convertSuccessPane(NumberMethods.decimalToOctal(decimal));
                }
            }
        }

    }
}
