from termcolor import colored
import base64
import subprocess as sub
import os
from urllib.parse import quote, unquote
import fnmatch
import getpass

# Función para obtener el usuario actual
def get_current_user():
    return getpass.getuser()

# Función para localizar archivos
def locate_file(directory, filename):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, filename):
            matches.append(os.path.join(root, filename))
    return matches

# Decodificador XOR entre el contenido de dos archivos
def xor_files(file1_path, file2_path, output_file_path):
    try:
        current_user = get_current_user()
        search_root = f'/home/{current_user}/'
        file_to_find1 = file1_path
        file_to_find2 = file2_path
        found_files1 = locate_file(search_root, file_to_find1)
        found_files2 = locate_file(search_root, file_to_find2)

        if found_files1 and found_files2:
            with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
                file1_data = file1.read()
                file2_data = file2.read()

            if len(file1_data) != len(file2_data):
                return None

            xor_result = bytearray(a ^ b for a, b in zip(file1_data, file2_data))

            current_user = get_current_user()
            search_root = f'/home/{current_user}/'
            with open(f'{search_root}a.pdf', 'wb') as output_file:
                output_file.write(xor_result)

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Decodificador caesar en formato ASCII
def ascii_caesar_shift(message, distance):
    encrypted = ""
    for char in message:
        a = ord(char)
        value = ord(char) + distance
        if value <= 33:
            value -= 33
        encrypted += chr(value % 128)
    return encrypted

# Decodificador XOR
def xor_decrypt(ciphertext, key):
    return ''.join(chr(c ^ key) for c in ciphertext)

# Fuerza bruta XOR
def brute_force_xor(text: str) -> str:
    possible_texts = []
    for key in range(256):
        decrypted_text = xor_decrypt(text, key)
        possible_texts.append((key, decrypted_text))
    return possible_texts

# Decodificación Trithemius
def trithemius_decode(text: str) -> str:
    try:
        plaintext = []
        shift = 0

        for char in text:
            if char.isalpha():
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')

                decoded_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(decoded_char)
                shift += 1
            else:
                plaintext.append(char)

        return ''.join(plaintext)
    except Exception as e: pass

# Decodificación Bacon
def bacon_decode(text: str) -> str:
    try:
        bacon_dict_1 = {
            'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
            'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
            'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
            'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
            'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
            'BBAAB': 'Z'
        }

        bacon_dict_2 = {
            'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
            'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'K',
            'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P',
            'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'U',
            'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'
        }

        bacon_dict_3 = {
            'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
            'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'J', 'ABAAB': 'K',
            'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P',
            'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'V',
            'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'
        }

        bacon_dict_4 = {
            'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
            'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'K',
            'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P',
            'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'V',
            'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'
        }

        bacon_dict_5 = {
            'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
            'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'J', 'ABAAB': 'K',
            'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P',
            'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'U',
            'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'
        }

        def bacon_decode_1(text):
            ciphertext = text.replace(' ', '').upper()
            if len(ciphertext) % 5 != 0:
                raise ValueError("...")

            groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
            plaintext = ''.join([bacon_dict_1.get(group, '?') for group in groups])

            return plaintext

        def bacon_decode_2(text):
            ciphertext = text.replace(' ', '').upper()
            if len(ciphertext) % 5 != 0:
                raise ValueError("...")

            groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
            plaintext = ''.join([bacon_dict_2.get(group, '?') for group in groups])

            return plaintext

        def bacon_decode_3(text):
            ciphertext = text.replace(' ', '').upper()
            if len(ciphertext) % 5 != 0:
                raise ValueError("...")

            groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
            plaintext = ''.join([bacon_dict_3.get(group, '?') for group in groups])

            return plaintext
        
        def bacon_decode_4(text):
            ciphertext = text.replace(' ', '').upper()
            if len(ciphertext) % 5 != 0:
                raise ValueError("...")

            groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
            plaintext = ''.join([bacon_dict_4.get(group, '?') for group in groups])

            return plaintext
        
        def bacon_decode_5(text):
            ciphertext = text.replace(' ', '').upper()
            if len(ciphertext) % 5 != 0:
                raise ValueError("...")

            groups = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
            plaintext = ''.join([bacon_dict_5.get(group, '?') for group in groups])

            return plaintext

        decoded_text = []
        decoded_text.append(bacon_decode_1(ciphertext).lower())
        decoded_text.append(bacon_decode_2(ciphertext).lower())
        decoded_text.append(bacon_decode_3(ciphertext).lower())
        decoded_text.append(bacon_decode_4(ciphertext).lower())
        decoded_text.append(bacon_decode_5(ciphertext).lower())
        
        return decoded_text
    except Exception as e: pass

#Decodificador de cifrado caesar
def cesar_decode(texto, desplazamiento):
    try:
        resultado = ""
        for i in range(len(texto)):
            char = texto[i]
            if char.isalpha():
                if char.isupper():
                    resultado += chr((ord(char) - desplazamiento - 65) % 26 + 65)
                else:
                    resultado += chr((ord(char) - desplazamiento - 97) % 26 + 97)
            else:
                resultado += char
        
        return resultado
    except Exception as e: pass

# Decodificador de cifrado brainfuck
def brainfuck_interpreter(text: str) -> str:
    try:
        code = ''.join(filter(lambda x: x in ['>', '<', '+', '-', '.', ',', '[', ']'], text))
        tape = [0] * 30000
        code_pointer = 0
        tape_pointer = 0
        output = []
        loop_stack = []

        while code_pointer < len(code):
            command = code[code_pointer]

            if command == '>':
                tape_pointer += 1
            elif command == '<':
                tape_pointer -= 1
            elif command == '+':
                tape[tape_pointer] = (tape[tape_pointer] + 1) % 256
            elif command == '-':
                tape[tape_pointer] = (tape[tape_pointer] - 1) % 256
            elif command == '.':
                output.append(chr(tape[tape_pointer]))
            elif command == ',':
                pass
            elif command == '[':
                if tape[tape_pointer] == 0:
                    open_brackets = 1
                    while open_brackets != 0:
                        code_pointer += 1
                        if code[code_pointer] == '[':
                            open_brackets += 1
                        elif code[code_pointer] == ']':
                            open_brackets -= 1
                else:
                    loop_stack.append(code_pointer)

            elif command == ']':
                if tape[tape_pointer] != 0:
                    code_pointer = loop_stack[-1]
                else:
                    loop_stack.pop()
            code_pointer += 1
        return ''.join(output)
    except Exception as e: pass

def luhn_find_card(n):
    import luhn
    try:
        cadena_1 = int(n[0].replace(".", '0'))
        cadena_2 = int(n[0].replace(".", '9'))
        multiplo = int(n[1])

        for i in range(cadena_1, cadena_2, 10000):
            if i % multiplo == 0 and luhn.verify(str(i)):
                return i
    except Exception as e: pass

# Decodificador XOR entre cadenas de texto sin usar una clave (brute force)
def xor_chain_sin_key(input_1, input_2):
    def xor_bytes(data1, data2):
        try:
            length = min(len(data1), len(data2))
            return bytes([data1[i] ^ data2[i] for i in range(length)])
        except Exception as e: pass

    try:
        input1_bytes = bytes.fromhex(input_1)
        input2_bytes = bytes.fromhex(input_2)

        result_bytes = xor_bytes(input1_bytes, input2_bytes)
        result_str = result_bytes.decode('utf-8')
        return result_str
    except Exception as e: pass

# Decodificador de cifrado vigenere 
def vigenere_decrypt(text: str, key: str) -> str:
    try:
        key = (key * (len(text) // len(key) + 1))[:len(text)]
        result = []
        for i in range(len(text)):
            if text[i].isupper():
                shift = ord(key[i].upper()) - ord('A') 
                result.append(chr((ord(text[i]) - ord('A') - shift + 26) % 26 + ord('A')))
            elif text[i].islower():
                shift = ord(key[i].lower()) - ord('a')
                result.append(chr((ord(text[i]) - ord('a') - shift + 26) % 26 + ord('a')))
            else:
                result.append(text[i])
        return ''.join(result)
    except Exception as e: pass

# Decodificador de cifrado RSA usando e, n, c, p, q
def rsa_decode_3_values(path: str) -> str:
    from sympy import mod_inverse
    
    line = []
    with open(path, 'r') as file:
        for l in file:
            l = l.strip()
            if l:
                line.append(l)

    data_1 = []
    if ":" in line[0]:
        data_1 = line[0].split(':')
    elif "=" in line[0]:
        data_1 = line[0].split('=')
    if int(data_1[1]) != 1:
        try:
            data_2 = []
            data_3 = []
            data_4 = []
            data_5 = []

            if ":" in line[1]:
                data_2 = line[1].split(':')
            elif "=" in line[1]:
                data_2 = line[1].split('=')

            if ":" in line[2]:
                data_3 = line[2].split(':')
            elif "=" in line[2]:
                data_3 = line[2].split('=')

            if ":" in line[3]:
                data_4 = line[3].split(':')
            elif "=" in line[3]:
                data_4 = line[3].split('=')
            
            if ":" in line[4]:
                data_5 = line[4].split(':')
            elif "=" in line[4]:
                data_5 = line[4].split('=')

            e = int(data_1[1].strip())
            n = int(data_2[1].strip())
            c = int(data_3[1].strip())
            p = int(data_4[1].strip())
            q = int(data_5[1].strip())

            other_n = (p - 1)*(q - 1)
            d = mod_inverse(e, other_n)
            m = pow(c, d, n)

            return m
        except Exception as e: pass

    if int(data_1[1]) == 1:
        try:
            data_2 = []
            data_3 = []

            if ":" in line[1]:
                data_2 = line[1].split(':')
            elif "=" in line[1]:
                data_2 = line[1].split('=')
            if ":" in line[2]:
                data_3 = line[2].split(':')
            elif "=" in line[2]:
                data_3 = line[2].split('=')

            e = int(data_1[1])
            c = int(data_2[1])
            n = int(data_3[1])
            m = c % n

            return m
        except Exception as e: pass

# Decodificador de base64 a texto plano
def base64_to_text(text: str) -> str:
    try:
        missing_padding = len(text) % 4
        if missing_padding != 0:
            text += '=' * (4 - missing_padding)
        decoded = base64.b64decode(text.encode())
        return decoded.decode()
    except Exception as e: pass

# Decodificador de codigo morse
def decode_morse(morse_code: str) -> str:
    try:
        morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
        }
        
        inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}
        
        # Dividimos el mensaje de morse en palabras (separadas por 3 espacios '   ')
        morse_words = morse_code.strip().split('   ')
        decoded_message = []

        for word in morse_words:
            letters = word.split(' ')
            decoded_word = ''.join(inverse_morse_code_dict.get(letter, ' ') for letter in letters)
            decoded_message.append(decoded_word)
        
        return ' '.join(decoded_message)
    
    except Exception as e:
        pass

def rot13(text: str) -> str:
    try:
        result = ''
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += char
        return result
    except Exception as e: pass
    
def url_decode(encoded_text):
    try:
        return unquote(encoded_text)
    except Exception as e: pass

# Función para decodificar usando Atbash Cipher
def atbash_cipher(text: str) -> str:
    try:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        atbash_dict = {char: alphabet[::-1][i] for i, char in enumerate(alphabet)}
        atbash_dict.update({char.upper(): alphabet[::-1][i].upper() for i, char in enumerate(alphabet)})
        return ''.join([atbash_dict.get(char, char) for char in text])
    except Exception as e:
        print(f"[!] Error al decodificar con Atbash: {e}")
        return ""
