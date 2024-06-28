import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;
import NumberFunctions.*;

public class Window extends JFrame implements ActionListener {
    private final String[] selections = {"BINARY", "OCTA DECIMAL", "DECIMAL", "HEXADECIMAL"};
    private final JComboBox<String> comboBoxSelection;
    private final JButton generateButton = new JButton("GENERATE");
    private final JTextField minTextField = new JTextField(20);
    private final JTextField maxTextField = new JTextField(20);
    private final JTextArea firstTextArea = new JTextArea(20, 6);
    private final JTextArea secondTextArea = new JTextArea(20, 6);
    private final JTextArea thirdTextArea = new JTextArea(20, 6);
    private final JLabel firstConversion;
    private final JLabel secondConversion;
    private final JLabel thirdConversion;

    private String comboBoxItem;

    Window() {
        setDefaultLookAndFeelDecorated(true);
        this.setTitle("Number Systems");

        // Components of first panel
        this.comboBoxSelection = new JComboBox<String>(new String[]{"NONE", "BINARY", "OCTA DECIMAL", "DECIMAL", "HEXADECIMAL"});


        // PANEL
        JPanel mainPanel = new JPanel();
        JPanel outputPanel = new JPanel();

        // Set Panel Title
        mainPanel.setBorder(BorderFactory.createTitledBorder("INPUT"));
        outputPanel.setBorder(BorderFactory.createTitledBorder("OUTPUT"));

        // Set Panel Layout
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        outputPanel.setLayout(new BoxLayout(outputPanel, BoxLayout.Y_AXIS));

        // Set Panel Alignment
        JLabel selectionLabel = new JLabel("Conversion Type:"); selectionLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        JLabel minNumberLabel = new JLabel("Minimum Conversion:"); minNumberLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        JLabel maxNumberLabel = new JLabel("Maximum Conversion:"); maxNumberLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        generateButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        mainPanel.add(selectionLabel);
        mainPanel.add(comboBoxSelection);
        mainPanel.add(minNumberLabel);
        mainPanel.add(minTextField);
        mainPanel.add(maxNumberLabel);
        mainPanel.add(maxTextField);
        mainPanel.add(generateButton);

        // Set Panel Alignment in the second panel (Output Panel)

        firstConversion = new JLabel("Conversion.."); firstConversion.setAlignmentX(Component.CENTER_ALIGNMENT);
        secondConversion = new JLabel("Conversion.."); secondConversion.setAlignmentX(Component.CENTER_ALIGNMENT);
        thirdConversion = new JLabel("Conversion.."); thirdConversion.setAlignmentX(Component.CENTER_ALIGNMENT);
        firstTextArea.setEditable(false);
        secondTextArea.setEditable(false);
        thirdTextArea.setEditable(false);
        JScrollPane firstConversionPane = new JScrollPane(firstTextArea);
        JScrollPane secondConversionPane = new JScrollPane(secondTextArea);
        JScrollPane thirdConversionPane = new JScrollPane(thirdTextArea);
        outputPanel.add(firstConversion);
        outputPanel.add(firstConversionPane);
        outputPanel.add(secondConversion);
        outputPanel.add(secondConversionPane);
        outputPanel.add(thirdConversion);
        outputPanel.add(thirdConversionPane);



        this.comboBoxSelection.addActionListener(this);
        this.generateButton.addActionListener(this);

        this.setLayout(new FlowLayout());
        // set the panel size
        mainPanel.setPreferredSize(new Dimension(200, 300));
        outputPanel.setPreferredSize(new Dimension(200, 300));
        // pack all the components
        this.add(mainPanel);
        this.add(outputPanel);
        this.pack();
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);
        this.setVisible(true);
    }

    public void dialogBox(String message) {
        JOptionPane.showMessageDialog(this, message);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == comboBoxSelection) this.comboBoxItem = (String) this.comboBoxSelection.getSelectedItem();
        outer:
        if (e.getSource() == generateButton) {
            if (Objects.equals(this.comboBoxItem, "NONE")) {
                dialogBox("Error, you did not select any number type.");
                break outer;
            }

            if (minTextField.getText().length() == 0 || maxTextField.getText().length() == 0) {
                dialogBox("Error, you did not provide any or both minimum and maximum values.");
                break outer;
            }

            String minNumber = minTextField.getText();
            String maxNumber = maxTextField.getText();

            if (!NumberSystems.checkNumber(minNumber, this.comboBoxItem) || !NumberSystems.checkNumber(maxNumber, this.comboBoxItem)) {
                dialogBox("yawa dili mani mga " + this.comboBoxItem.toLowerCase());
                break outer;
            }

            if (!NumberSystems.checkNumber(minNumber, comboBoxItem) || !NumberSystems.checkNumber(maxNumber, comboBoxItem)) {

                dialogBox("Error, one or both of the numbers you have provided is not a " + this.comboBoxItem.toLowerCase() + ".");
                break outer;
            }


            switch (comboBoxItem) {
                case "BINARY" -> {
                    minNumber = NumberSystems.binaryToDecimal(minNumber);
                    maxNumber = NumberSystems.binaryToDecimal(maxNumber);
                    break;
                }
                case "OCTA DECIMAL" -> {
                    minNumber = NumberSystems.octalToDecimal(minNumber);
                    maxNumber = NumberSystems.octalToDecimal(maxNumber);
                    break;
                }
                case "HEXADECIMAL" -> {
                    minNumber = NumberSystems.hexadecimalToDecimal(minNumber);
                    maxNumber = NumberSystems.hexadecimalToDecimal(maxNumber);
                    break;
                }
            }

            if (Integer.parseInt(maxNumber) < Integer.parseInt(minNumber)) {
                dialogBox("Error, Maximum Conversion number is greater than Minimum Conversion Number");
                break outer;
            }

            ArrayList<String> conversions = new ArrayList<String>(Arrays.asList(selections));
            conversions.remove(comboBoxItem);
            firstConversion.setText(conversions.get(0));
            secondConversion.setText(conversions.get(1));
            thirdConversion.setText(conversions.get(2));

            // Store the TextArea components in an array
            JTextArea[] textAreas = new JTextArea[]{firstTextArea, secondTextArea, thirdTextArea};
            Thread[] threads = new Thread[3];

            // this section is to remove all the existing data from the previous conversion if there is any
            for (JTextArea area : textAreas) {
                area.setText(null);
            }

            // set the areas to their local threads.
            for (int i = 0; i<3; i++) {
                switch (conversions.get(i)) {
                    case "BINARY" -> {
                        threads[i] = new Thread(new ToBinary(minNumber, maxNumber, textAreas[i]));
                        break;
                    }
                    case "OCTA DECIMAL" -> {
                        threads[i] = new Thread(new ToOctal(minNumber, maxNumber, textAreas[i]));
                        break;
                    }
                    case "DECIMAL" -> {
                        threads[i] = new Thread(new ToDecimal(minNumber, maxNumber, textAreas[i]));
                        break;
                    }
                    case "HEXADECIMAL" -> {
                        threads[i] = new Thread(new ToHexadecimal(minNumber, maxNumber, textAreas[i]));
                        break;
                    }
                }
            }
            // Run the threads
            for (Thread thread : threads) {
                thread.start();
            }
        }
    }

}
