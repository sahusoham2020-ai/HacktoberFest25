import javax.swing.*;
import javax.swing.border.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.*;
import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;
import java.util.Base64;

public class FileEncryptionTool extends JFrame {
    private JTextField filePathField;
    private JPasswordField passwordField;
    private JTextArea logArea;
    private JButton selectFileBtn, encryptBtn, decryptBtn, clearBtn;
    private File selectedFile;
    
    public FileEncryptionTool() {
        setTitle("File Encryption Tool - AES-256");
        setSize(700, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        
        initComponents();
        setVisible(true);
    }
    
    private void initComponents() {
        // Main panel with padding
        JPanel mainPanel = new JPanel(new BorderLayout(10, 10));
        mainPanel.setBorder(new EmptyBorder(15, 15, 15, 15));
        
        // Top panel for file selection
        JPanel topPanel = new JPanel(new BorderLayout(10, 10));
        topPanel.setBorder(BorderFactory.createTitledBorder("File Selection"));
        
        filePathField = new JTextField();
        filePathField.setEditable(false);
        filePathField.setFont(new Font("Arial", Font.PLAIN, 12));
        
        selectFileBtn = new JButton("Select File");
        selectFileBtn.setFocusPainted(false);
        selectFileBtn.addActionListener(e -> selectFile());
        
        topPanel.add(filePathField, BorderLayout.CENTER);
        topPanel.add(selectFileBtn, BorderLayout.EAST);
        
        // Middle panel for password and actions
        JPanel middlePanel = new JPanel(new GridBagLayout());
        middlePanel.setBorder(BorderFactory.createTitledBorder("Encryption/Decryption"));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        
        // Password label and field
        JLabel passwordLabel = new JLabel("Password:");
        passwordField = new JPasswordField(20);
        passwordField.setFont(new Font("Arial", Font.PLAIN, 12));
        
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.weightx = 0;
        middlePanel.add(passwordLabel, gbc);
        
        gbc.gridx = 1;
        gbc.weightx = 1;
        middlePanel.add(passwordField, gbc);
        
        // Buttons panel
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        
        encryptBtn = new JButton("🔒 Encrypt");
        encryptBtn.setFocusPainted(false);
        encryptBtn.setBackground(new Color(76, 175, 80));
        encryptBtn.setForeground(Color.WHITE);
        encryptBtn.addActionListener(e -> encryptFile());
        
        decryptBtn = new JButton("🔓 Decrypt");
        decryptBtn.setFocusPainted(false);
        decryptBtn.setBackground(new Color(33, 150, 243));
        decryptBtn.setForeground(Color.WHITE);
        decryptBtn.addActionListener(e -> decryptFile());
        
        clearBtn = new JButton("Clear Log");
        clearBtn.setFocusPainted(false);
        clearBtn.addActionListener(e -> logArea.setText(""));
        
        buttonPanel.add(encryptBtn);
        buttonPanel.add(decryptBtn);
        buttonPanel.add(clearBtn);
        
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        middlePanel.add(buttonPanel, gbc);
        
        // Bottom panel for log
        JPanel bottomPanel = new JPanel(new BorderLayout());
        bottomPanel.setBorder(BorderFactory.createTitledBorder("Activity Log"));
        
        logArea = new JTextArea(10, 50);
        logArea.setEditable(false);
        logArea.setFont(new Font("Monospaced", Font.PLAIN, 11));
        JScrollPane scrollPane = new JScrollPane(logArea);
        
        bottomPanel.add(scrollPane, BorderLayout.CENTER);
        
        // Add panels to main panel
        mainPanel.add(topPanel, BorderLayout.NORTH);
        mainPanel.add(middlePanel, BorderLayout.CENTER);
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);
        
        add(mainPanel);
    }
    
    private void selectFile() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        
        int result = fileChooser.showOpenDialog(this);
        if (result == JFileChooser.APPROVE_OPTION) {
            selectedFile = fileChooser.getSelectedFile();
            filePathField.setText(selectedFile.getAbsolutePath());
            log("Selected file: " + selectedFile.getName());
        }
    }
    
    private void encryptFile() {
        if (!validateInputs()) return;
        
        try {
            String password = new String(passwordField.getPassword());
            byte[] fileData = Files.readAllBytes(selectedFile.toPath());
            
            log("Starting encryption...");
            byte[] encryptedData = encrypt(fileData, password);
            
            String outputPath = selectedFile.getAbsolutePath() + ".encrypted";
            Files.write(Paths.get(outputPath), encryptedData);
            
            log("✓ File encrypted successfully!");
            log("Output: " + outputPath);
            log("Original size: " + fileData.length + " bytes");
            log("Encrypted size: " + encryptedData.length + " bytes");
            
            JOptionPane.showMessageDialog(this, 
                "File encrypted successfully!\nSaved as: " + outputPath,
                "Success", JOptionPane.INFORMATION_MESSAGE);
                
        } catch (Exception ex) {
            log("✗ Encryption failed: " + ex.getMessage());
            JOptionPane.showMessageDialog(this, 
                "Encryption failed: " + ex.getMessage(),
                "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    private void decryptFile() {
        if (!validateInputs()) return;
        
        try {
            String password = new String(passwordField.getPassword());
            byte[] encryptedData = Files.readAllBytes(selectedFile.toPath());
            
            log("Starting decryption...");
            byte[] decryptedData = decrypt(encryptedData, password);
            
            String outputPath = selectedFile.getAbsolutePath().replace(".encrypted", ".decrypted");
            if (outputPath.equals(selectedFile.getAbsolutePath())) {
                outputPath = selectedFile.getAbsolutePath() + ".decrypted";
            }
            
            Files.write(Paths.get(outputPath), decryptedData);
            
            log("✓ File decrypted successfully!");
            log("Output: " + outputPath);
            log("Decrypted size: " + decryptedData.length + " bytes");
            
            JOptionPane.showMessageDialog(this, 
                "File decrypted successfully!\nSaved as: " + outputPath,
                "Success", JOptionPane.INFORMATION_MESSAGE);
                
        } catch (Exception ex) {
            log("✗ Decryption failed: " + ex.getMessage());
            JOptionPane.showMessageDialog(this, 
                "Decryption failed. Wrong password or corrupted file.",
                "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    private boolean validateInputs() {
        if (selectedFile == null) {
            JOptionPane.showMessageDialog(this, 
                "Please select a file first.", "Warning", JOptionPane.WARNING_MESSAGE);
            return false;
        }
        
        if (passwordField.getPassword().length == 0) {
            JOptionPane.showMessageDialog(this, 
                "Please enter a password.", "Warning", JOptionPane.WARNING_MESSAGE);
            return false;
        }
        
        return true;
    }
    
    private byte[] encrypt(byte[] data, String password) throws Exception {
        SecretKeySpec key = generateKey(password);
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        
        byte[] iv = new byte[16];
        SecureRandom random = new SecureRandom();
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        
        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
        byte[] encrypted = cipher.doFinal(data);
        
        byte[] result = new byte[iv.length + encrypted.length];
        System.arraycopy(iv, 0, result, 0, iv.length);
        System.arraycopy(encrypted, 0, result, iv.length, encrypted.length);
        
        return result;
    }
    
    private byte[] decrypt(byte[] data, String password) throws Exception {
        SecretKeySpec key = generateKey(password);
        
        byte[] iv = new byte[16];
        System.arraycopy(data, 0, iv, 0, iv.length);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        
        byte[] encrypted = new byte[data.length - 16];
        System.arraycopy(data, 16, encrypted, 0, encrypted.length);
        
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
        
        return cipher.doFinal(encrypted);
    }
    
    private SecretKeySpec generateKey(String password) throws Exception {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(password.getBytes("UTF-8"));
        return new SecretKeySpec(hash, "AES");
    }
    
    private void log(String message) {
        logArea.append("[" + new java.text.SimpleDateFormat("HH:mm:ss").format(new java.util.Date()) + "] " + message + "\n");
        logArea.setCaretPosition(logArea.getDocument().getLength());
    }
    
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        SwingUtilities.invokeLater(() -> new FileEncryptionTool());
    }
}