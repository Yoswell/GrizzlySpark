<div align="center">
  <img src="https://github.com/user-attachments/assets/91880a9f-f659-42e2-a926-6f9ebdc5ce44" alt="image" width="200px" />
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
  <img src="https://img.shields.io/badge/Go-%3E%3D%201.0-blue.svg" />
</div>

<div align="center">
    <a href="#features">Features</a> • 
    <a href="#installation">Installation</a> • 
    <a href="#contributing">Contributing</a> • 
    <a href="#authors">Authors</a> 
</div>

<div align="center">
    <h1>GrizzlySpark | CTF tools | All in one</h1>
</div>

### Description
**GrizzlySpark** is a powerful Python tool designed to assist CTF (Capture The Flag) participants in solving IT security challenges. The tool provides various functionalities for data analysis, conversion, and manipulation, allowing users to focus on solving complex security problems efficiently. Whether you're decoding, analyzing traffic, or working with different formats, GrizzlySpark simplifies your tasks.

### Features
GrizzlySpark includes a variety of essential features for CTF challenges:
1. **Data Conversion**: Convert between different formats (Base64, Hex, etc.)<br>
2. **Decoding/Encoding**: Decode or encode data using (e.g., Base64, ROT13, XOR).<br>
3. **File Analysis**: Analyze suspicious files for CTF purposes.<br>
4. **Automation**: Automate tasks to save time and reduce errors during challenges.

### Ilustrative code:
```cs
[+] Convert modes
+---------------------------------------------------------------------------------------------------------------------------------------+
|   Code   Description                                           Options       More details                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+
    C1     Convert Hexadecimal to Text                           -m -i         Input: Hexadecimal, Output: Text
    C2     Convert Text to Hexadecimal                           -m -i         Input: Text, Output: Hexadecimal
    C3     Convert Decimal to Text                               -m -i         Input: Decimal, Output: Text
    C4     Convert Binary to Text                                -m -i         Input: Binary, Output: Text
    C5     Convert Binary to Hexadecimal                         -m -i         Input: Binary, Output: Hexadecimal
    C6     Convert Decimal to Hexadecimal                        -m -i         Input: Decimal, Output: Hexadecimal
    C7     URL Encode                                            -m -i         Input: Text, Output: URL-encoded String
    C8     Revert Strings (e.g., 'aloh' -> 'hola')               -m -i         Input: Text, Output: Reversed String
    C9     Convert Long Bytes to Text                            -m -i         Input: Long Bytes, Output: Text
    C10    Convert Hexadecimal (0x?? format) to Decimal          -m -i         Input: Hexadecimal (0x format), Output: Decimal

[+] Decode modes
+---------------------------------------------------------------------------------------------------------------------------------------+
|   Code   Description                                           Options       More details                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+
    D1     Bases Decode (base64, base58, base62, base85)         -m -i         Input: Base64 Encoded String, Output: Decoded Text
    D2     Morse Code Decode                                     -m -i         Input: Morse Code, Output: Text
    D3     ROT13 Decode                                          -m -i         Input: ROT13 Encoded Text, Output: Decoded Text
    D4     Atbash Cipher Decode                                  -m -i         Input: Atbash Encoded Text, Output: Decoded Text
    D5     Base64 File Decode                                    -m -f -r      Input: Base64 File, Output: Decoded File
    D6     URL Decode                                            -m -i         Input: URL Encoded String, Output: Decoded String
    D7     RSA Decode with Parameters (e, n, c, p, q)            -m -f         Input: RSA Parameters, Output: Decrypted Text
    D8     Vigenère Cipher Decode                                -m -i -k      Input: Encrypted Text, Key, Output: Decrypted Text
    D10    MD5 Hash Cracking                                     -m -i         Input: MD5 Hash, Output: Cracked Text
    D13    Brainfuck Language Decode                             -m -i         Input: Brainfuck Code, Output: Decoded Text
    D14    Caesar Cipher Decode                                  -m -i         Input: Caesar Encrypted Text, Output: Decrypted Text
    D15    Bacon Cipher Decode                                   -m -i         Input: Bacon Cipher Encrypted Text, Output: Decrypted Text
    D16    Trithemius Cipher Decode                              -m -i         Input: Trithemius Encrypted Text, Output: Decrypted Text
    D17    XOR Brute Force (One Chain, HEX Format)               -m -i         Input: XOR Encrypted Text, Output: Decrypted Text
    D18    Caesar ASCII Decode                                   -m -f         Input: Caesar Encrypted ASCII, Output: Decrypted ASCII
    D19    XOR Two Files Decode                                  -m -x -y -z   Input: Two Files, Output: Decrypted File

[+] Exploits modes
+---------------------------------------------------------------------------------------------------------------------------------------+
|   Code   Description                                           Options       More details                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+
    E1     Web Scraping (Extract Data from URL, Text Patterns)   -m -i -j      Input: URL, Text Pattern, Output: Extracted Data
    E2     Check Active IP (Check if IP is Active)               -m -i         Input: IP Address, Output: Active Status
    E3     Extract Macros from DOCM Files                        -m -x         Input: DOCM File Path, Output: Extracted Macros
    E4     Generate Reverse Shell (IP, Port)                     -m -i -j      Input: IP, Port, Output: Reverse Shell Command
```

### Installation
To install GrizzlySpark, clone the repository and install the necessary dependencies:

1. Clone the repository:
    ```bash
    Vishok@user > git clone https://github.com/username/grizzlyspark.git
    Vishok@user > cd grizzlyspark
    ```

2. Install the required dependencies:
    ```bash
    Vishok@user > pip install -r requirements.txt
    Vishok@user > pip install -r requirements.txt //In warning case
    ```

### Contributing
We welcome contributions from the community. To contribute to GrizzlySpark:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

Please make sure to follow the Code of Conduct and provide clear explanations for your changes.

### Authors
Developed by [Yoswel Badilla](https://www.linkedin.com/in/yoswel-badilla-cyberjr/), also known as **Vishok**.
