# File Encryption Tool 🔒

A secure, user-friendly Java application for encrypting and decrypting files using AES-256 encryption algorithm.


## Features

- **AES-256 Encryption** - Military-grade encryption standard
- **Intuitive GUI** - Simple and clean interface built with Java Swing
- **Password Protected** - Secure your files with custom passwords
- **Activity Logging** - Real-time operation tracking with timestamps
- **Universal File Support** - Encrypt any file type (documents, images, videos, etc.)
- **CBC Mode with Random IV** - Enhanced security with Cipher Block Chaining
- **Non-Destructive** - Original files remain untouched during encryption

## Sample Ui

```
┌─────────────────────────────────────┐
│  File Encryption Tool - AES-256     │
├─────────────────────────────────────┤
│  File Selection                     │
│  [Selected File Path]  [Select]     │
├─────────────────────────────────────┤
│  Encryption/Decryption              │
│  Password: [**********]             │
│  [🔒 Encrypt] [🔓 Decrypt] [Clear]  │
├─────────────────────────────────────┤
│  Activity Log                       │
│  [Timestamped operations...]        │
└─────────────────────────────────────┘
```

## Prerequisites

- Java Development Kit (JDK) 8 or higher
- Java Runtime Environment (JRE) to run the application

## Installation

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/yourusername/file-encryption-tool.git
   cd file-encryption-tool
   ```

2. **Compile the program**
   ```bash
   javac FileEncryptionTool.java
   ```

3. **Run the application**
   ```bash
   java FileEncryptionTool
   ```

## Usage

### Encrypting a File

1. Launch the application
2. Click **"Select File"** and choose the file you want to encrypt
3. Enter a strong password in the password field
4. Click **"🔒 Encrypt"**
5. The encrypted file will be saved with `.encrypted` extension

**Example:**
```
Original: document.pdf
Encrypted: document.pdf.encrypted
```

### Decrypting a File

1. Click **"Select File"** and choose the `.encrypted` file
2. Enter the **same password** used during encryption
3. Click **"🔓 Decrypt"**
4. The decrypted file will be saved with `.decrypted` extension

**Example:**
```
Encrypted: document.pdf.encrypted
Decrypted: document.pdf.decrypted
```

### Important Notes

⚠️ **Password Safety**
- Your password is **NOT stored** anywhere
- If you forget your password, the file **cannot be recovered**
- Use strong passwords with mixed characters, numbers, and symbols

✅ **File Safety**
- Original files are **never deleted** by the tool
- You can safely delete the original file manually after verifying encryption
- Always test decryption before deleting originals

## How It Works

### Encryption Process

1. **Key Derivation**: Password is hashed using SHA-256 to create a 256-bit encryption key
2. **IV Generation**: A random 16-byte Initialization Vector (IV) is generated
3. **Encryption**: File data is encrypted using AES-256 in CBC mode with PKCS5 padding
4. **Storage**: IV is prepended to encrypted data and saved to output file

### Decryption Process

1. **IV Extraction**: First 16 bytes are extracted as the IV
2. **Key Derivation**: Same password is hashed to regenerate the key
3. **Decryption**: Remaining bytes are decrypted using AES-256 in CBC mode
4. **Restoration**: Original file content is restored

### Security Details

- **Algorithm**: AES (Advanced Encryption Standard)
- **Key Size**: 256 bits
- **Mode**: CBC (Cipher Block Chaining)
- **Padding**: PKCS5
- **Key Derivation**: SHA-256 hash function
- **IV**: 128-bit random initialization vector

## File Structure

```
file-encryption-tool/
│
├── FileEncryptionTool.java    # Main application file
├── README.md                   # This file
└── LICENSE                     # License information
```

## Technical Specifications

| Component | Details |
|-----------|---------|
| Language | Java |
| GUI Framework | Swing |
| Encryption | AES-256-CBC |
| Hash Function | SHA-256 |
| Key Size | 256 bits |
| Block Size | 128 bits |
| IV Size | 128 bits |

## Troubleshooting

### "Decryption failed" error
- **Cause**: Wrong password or corrupted encrypted file
- **Solution**: Verify you're using the correct password and the file hasn't been modified

### File won't open after decryption
- **Cause**: Decryption was interrupted or file was corrupted
- **Solution**: Try decrypting again with the correct password

### Application won't start
- **Cause**: Java not installed or wrong version
- **Solution**: Install JDK 8 or higher and verify with `java -version`

## Security Recommendations

1. **Use Strong Passwords**
   - Minimum 12 characters
   - Mix uppercase, lowercase, numbers, and symbols
   - Avoid common words or patterns

2. **Backup Important Files**
   - Keep encrypted backups in multiple locations
   - Store passwords securely (use a password manager)

3. **Verify Encryption**
   - Always test decryption before deleting originals
   - Check file sizes match after decryption

4. **Secure Deletion**
   - Use secure deletion tools for sensitive originals
   - Empty recycle bin after deleting

## Limitations

- Password recovery is **impossible** - keep passwords safe
- Large files (>2GB) may require more memory
- Does not compress files before encryption
- Single file processing only (no batch mode)

## Future Enhancements

- [ ] Batch file encryption/decryption
- [ ] Password strength indicator
- [ ] File compression before encryption
- [ ] Secure file deletion option
- [ ] Drag-and-drop file selection
- [ ] Multiple encryption algorithm support
- [ ] Key file generation option
- [ ] Progress bar for large files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Disclaimer

This tool is provided for educational and legitimate security purposes only. Users are responsible for:
- Complying with local laws and regulations
- Maintaining their own password security
- Backing up important files
- Understanding encryption cannot be reversed without the correct password

## Author

Created with ☕ by GB14

## Acknowledgments

- Java Cryptography Architecture (JCA)
- AES encryption standard (FIPS-197)
- Java Swing GUI framework

## Contact

- GitHub: [@yourusername](https://github.com/gandharrdotexe)
- Email: your.email@example.com

---

**⚠️ Remember: With great encryption comes great responsibility. Never lose your passwords!**