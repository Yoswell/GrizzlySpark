# GrizzlySpark / CTF tool resolved
![382589821-2065ecf5-0e9b-4263-a10a-546a6bbd6e23](https://github.com/user-attachments/assets/032b5557-5c00-4337-86c6-a08372383c03)


## Documentation
<p>A powerful tool written in Python designed to help CTF (Capture The Flag) participants in solving IT security challenges. This tool provides several useful functionalities that facilitate data analysis and manipulation, allowing users to focus on solving challenges. <a href="https://discord.com/api/guilds/1296164292424368148/widget.json">Join to discord</a>
</p>

## Installation

Install all external dependencies

```bash
git clone https://github.com/Yoswell/GrizzlySpark.git

pip3 install -r requirements.txt

![Warning]
pip3 install -r requirements.txt --break-system-packages
```

## Features
This project includes several conversion and decoding functionalities. Below is the menu of available options:

```python
from termcolor import colored

print(f"\t{colored('[+]', 'yellow')} C1  - Hexadecimal to text                               options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C2  - Text to hexadecimal                               options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C3  - Decimal to text                                   options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C4  - Binary to text                                    options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C5  - Binary to hex                                     options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C6  - Decimal to hexadecimal                            options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C7  - URL encode                                        options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C8  - Revert strings (aloh -> hola)                     options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C9  - Long_bytes to text                                options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} C10 - Convert hexadecimal (0x?? format) to decimal      options(-m -i)")
#---------------------------------------------------------------------------------#
print(f"{colored('[+]', 'red')} Decode")
print(f"\t{colored('[+]', 'yellow')} D1  - Base64 cypher                                     options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D2  - Morse cypher                                      options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D3  - ROT13 cypher                                      options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D4  - Sustitution cypher file decode                    options(-m -f)")
print(f"\t{colored('[+]', 'yellow')} D5  - Base64 cypher file decode                         options(-m -f -r)")
print(f"\t{colored('[+]', 'yellow')} D6  - URL decode                                        options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D7  - RSA decode with (e:? n:? c:? p:? q:?)             options(-m -f)")
print(f"\t{colored('[+]', 'yellow')} D8  - Vigenere decode                                   options(-m -i -k)")
print(f"\t{colored('[+]', 'yellow')} D9  - Xor (Two chains) without (key) (HEX format)       options(-m -i -j)")
print(f"\t{colored('[+]', 'yellow')} D10 - FuckJs lenguage  (format -> +(+!+[]+(!+)          options(-m -f)")
print(f"\t{colored('[+]', 'yellow')} D11 - MD5 decode                                        options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D12 - Luhn find card (5612****123:234)                  options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D13 - BrainFuck lenguage (format -> >+++++++++[<+)      options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D14 - Caesar decode                                     options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D15 - Bacon decode (format -> abbb abaaa abbaa)         options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D16 - Trithemius decode                                 options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D17 - XOR (One chain) brute force (HEXformat)           options(-m -i)")
print(f"\t{colored('[+]', 'yellow')} D18 - Caesar ascii decode                               options(-m -f)")
print(f"\t{colored('[+]', 'yellow')} D19 - Xor (Two Files) decode                            options(-m -x -y -z)")
#-------------------------------------=-------------------------------------------#
print(f"{colored('[+]', 'red')} Exploits")
print(f"\t{colored('[+]', 'yellow')} E1  - Web Scrapping (url, text pattern)                 options(-i -j)\n")
```

## Uses examples
Below I show you some ways to use Guilty-Spark
![image](https://github.com/user-attachments/assets/edbc2849-421f-4edb-a416-0d741d9444fc)

## Authors
Developed by <a href="https://www.linkedin.com/in/yoswel-badilla-cyberjr/">Vishok</a>
