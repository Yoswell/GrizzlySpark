from termcolor import colored
import base64
import subprocess as sub
import os
from urllib.parse import quote, unquote
import fnmatch
import getpass
from Crypto.Util.number import long_to_bytes

# Convertir numeros binarios a numeros en hexadecimal
def binary_to_hex(text: str) -> str:
    try:
        integer_representation = int(text, 2)
        hexadecimal_string = hex(integer_representation)[2:]
        return hexadecimal_string
    except Exception as e: pass

# Convertir formato hexadecimal con 0x a numeros hexadecimales
def imprimir_valor_hexadecimal(text: str) -> str:
    try:
        valor_decimal = int(text, 16)
        return valor_decimal
    except Exception as e: pass

# Decodificador de long bytes
def long_bytes(text: str) -> str:
    try:
        text = int(text)
        plaintext = long_to_bytes(text).decode('utf-8')
        return plaintext
    except Exception as e: pass

# Invertir una cadena
def revert_strings(n):
    try:
        return n[::-1]
    except Exception as e: pass

# Convertir numeros hexadecimales a texto plano
def hex_to_text(text: str) -> str:
    try:
        hex_to_text = bytes.fromhex(text).decode('utf-8', 'ignore')
        return hex_to_text
    except ValueError: pass

# Convertir texto plano a numeros en hexadecimal
def text_to_hex(text: str) -> str:
    try:
        bytes_object = text.encode("utf-8")
        hex_representation = bytes_object.hex()
        return hex_representation
    except Exception as e: pass

# Convertir numeros decimales a texto plano
def decimal_to_text(number: str) -> str:
    try:
        text = ''.join(chr(int(num)) for num in number.split(','))
        return text
    except Exception as e: pass

# Convertir numeros decimales a hexadecimal
def decimal_to_hex(number: str) -> str:
    try:
        hexadecimal_string = hex(number)[2:]
        return hexadecimal_string
    except Exception as e: pass

# Convertir numeros binarios a texto plano
def binary_to_text(binary_str, encoding='ascii'):
    try:
        bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        chars = [chr(int(byte, 2)) for byte in bytes_list]
        text = ''.join(chars)
        decoded_text = text.encode('latin1').decode(encoding)
        return decoded_text
    except Exception as e: pass

# Decodificar el url-encode en las urls
def url_encode(text: str) -> str:
    try:
        return quote(text)
    except Exception as e: pass
