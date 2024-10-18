from pwn import log as o
from termcolor import colored
import argparse
import base64
import subprocess as sub
import re
import os
from time import sleep
from urllib.parse import quote, unquote
from time import sleep
import fnmatch
import getpass
from Crypto.Util.number import long_to_bytes

def binary_to_hex(opc):
    try:
        integer_representation = int(opc, 2)
        hexadecimal_string = hex(integer_representation)[2:]
        return hexadecimal_string
    except Exception as e: pass

def imprimir_valor_hexadecimal(opc):
    try:
        valor_decimal = int(opc, 16)
        return valor_decimal
    except Exception as e: pass

def long_bytes(opc):
    try:
        opc = int(opc)
        plaintext = long_to_bytes(opc).decode('utf-8')
        return plaintext
    except Exception as e: pass
    
def revert_strings(n):
    try:
        c = len(n) - 1
        string = ""
        for x in range(c + 1):
            string += n[c]
            c -= 1
        return string
    except Exception as e: pass
    
def hex_to_text(strings):
    try:
        hex_value = hex(int(strings))[2:]
        hex_to_text = bytes.fromhex(hex_value).decode('utf-8', 'ignore')
        return hex_to_text
    except Exception as e: pass

def text_to_hex(text):
    try:
        bytes_object = text.encode("utf-8")
        hex_representation = bytes_object.hex()
        return hex_representation
    except Exception as e: pass

def decimal_to_text(decimal_numbers):
    try:
        text = ''.join(chr(int(num)) for num in decimal_numbers.split(','))
        return text
    except Exception as e: pass

def decimal_to_hex(decimal_number):
    try:
        hexadecimal_string = hex(decimal_number)[2:]
        return hexadecimal_string
    except Exception as e: pass

def binary_to_text(binary_str, encoding='ascii'):
    try:
        bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        chars = [chr(int(byte, 2)) for byte in bytes_list]
        text = ''.join(chars)
        decoded_text = text.encode('latin1').decode(encoding)
        return decoded_text
    except Exception as e: pass

def url_encode(text):
    try:
        return quote(text)
    except Exception as e: pass