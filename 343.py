#!/usr/bin/python3

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
from convert import hex_to_text
from convert import long_bytes
from convert import imprimir_valor_hexadecimal
from convert import binary_to_hex

from decode import brute_force_xor
from decode import trithemius_decode
from decode import bacon_decode
from decode import cesar_decode
from decode import brainfuck_interpreter
from decode import luhn_find_card
from decode import md5_decode
from decode import xor_chain_sin_key
from decode import vigenere_decrypt
from decode import rsa_decode_3_values
from decode import base64_to_text
from decode import sustitution
from decode import decode_morse
from decode import rot13
from decode import url_decode
from decode import ascii_caesar_shift
from decode import xor_files

from exploit import fetch_and_search

ascii_art = [
    "",
    "      .---.        .-----------",
    "     /     \\  __  /    ------",
    "    / /     \\(  )/    -----",
    "   //////   ' \\/ `   ---",
    "  //// / // :    : ---",
    " // /   /  /`    '--",
    "//          //..\\\\",
    "       ====UU====UU====",
    "           '//||\\\\'",
    "              ''",
]

for line in ascii_art:
    print(colored(line, 'blue'))

def print_modes():
    #---------------------------------------------------------------------------------#
    print(f"\n{colored('[+]', 'red')} Convert")
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
    #-------------------------------------=-------------------------------------------#
    print(f"""Usage: To continue for see more information about this program...\n\n(...{colored('[*]', 'blue')}
    {colored('[!]', 'green')} guiltySpark.py -m<MODE>               <For select mode>
    {colored('[!]', 'green')} guiltySpark.py -s<M>                  <For see modes>
    {colored('[!]', 'green')} guiltySpark.py -i<INPUT1>             <For insert input>
    {colored('[!]', 'green')} guiltySpark.py -f<PATH FILE>          <For insert path file>
    {colored('[!]', 'green')} guiltySpark.py -x<PATH FILE 1>        <For insert path file 1>
    {colored('[!]', 'green')} guiltySpark.py -y<PATH FILE 2>        <For insert path file 2>
    {colored('[!]', 'green')} guiltySpark.py -z<NAME FILE OUTPUT>   <For insert output name file>
    {colored('[!]', 'green')} guiltySpark.py -k<KEY>                <For insert key>
    {colored('[!]', 'green')} guiltySpark.py -j<INPUT2>             <For insert input>
    {colored('[!]', 'green')} guiltySpark.py -r<REPETITIONS>        <For insert repetition number>\n(...{colored('[*]', 'blue')}\n""")
    print("guiltySpark.py: finish")
    #---------------------------------------------------------------------------------#

def main():
    parser = argparse.ArgumentParser(description="", add_help=False, 
    usage=f"""To continue for see more information about this program...\n\n(...{colored('[*]', 'blue')}
    {colored('[!]', 'green')} guiltySpark.py -m<MODE>               <For select mode>
    {colored('[!]', 'green')} guiltySpark.py -s<M>                  <For see modes>
    {colored('[!]', 'green')} guiltySpark.py -i<INPUT1>             <For insert input>
    {colored('[!]', 'green')} guiltySpark.py -f<PATH FILE>          <For insert path file>
    {colored('[!]', 'green')} guiltySpark.py -x<PATH FILE 1>        <For insert path file 1>
    {colored('[!]', 'green')} guiltySpark.py -y<PATH FILE 2>        <For insert path file 2>
    {colored('[!]', 'green')} guiltySpark.py -z<NAME FILE OUTPUT>   <For insert output name file>
    {colored('[!]', 'green')} guiltySpark.py -k<KEY>                <For insert key>
    {colored('[!]', 'green')} guiltySpark.py -j<INPUT2>             <For insert input>
    {colored('[!]', 'green')} guiltySpark.py -u<URL>                <For insert url>
    {colored('[!]', 'green')} guiltySpark.py -r<REPETITIONS>        <For insert repetition number>\n(...{colored('[*]', 'blue')}\n""")
    parser.add_argument("-m", dest="mode", required=False)
    parser.add_argument("-i", dest="input", required=False)
    parser.add_argument("-s", dest="show", required=False)
    parser.add_argument("-f", dest="path", required=False)
    parser.add_argument("-x", dest="path1", required=False)
    parser.add_argument("-y", dest="path2", required=False)
    parser.add_argument("-z", dest="path3", required=False)
    parser.add_argument("-r", dest="repeat", required=False)
    parser.add_argument("-k", dest="key", required=False)
    parser.add_argument("-j", dest="input_two", required=False)
    
    args = parser.parse_args()

    mode = args.mode
    opc = args.input
    show = args.show
    file_path = args.path
    file_path_1 = args.path1
    file_path_2 = args.path2
    name_output_file = args.path3
    repetitions = args.repeat
    key = args.key
    opc_2 = args.input_two

    def locate_file(directory, filename):
        matches = []
        for root, dirnames, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, filename):
                matches.append(os.path.join(root, filename))
        return matches

    def get_current_user():
        return getpass.getuser()
    
    def printt(a):
        if a == None or a == "":
            print(f"[{colored('*', 'red')}] >> {colored('None', 'white')}")
        else:
            print(f"[{colored('*', 'blue')}] >> {colored(a, 'white')}")

    content_file = ""
    if file_path != None:
        current_user = get_current_user()
        search_root = f'/home/{current_user}/'
        file_to_find = file_path
        found_files = locate_file(search_root, file_to_find)

        if found_files:
            for file in found_files:
                file_path = file

        with open(file_path, 'r') as file:
            content_file = file.read()

    if show == "M" or show == "m":
        print_modes()
    
    if mode == "C1" or mode == "c1":
        new_text = hex_to_text(opc)
        printear()
        printt(new_text)
    
    if mode == "C2" or mode == "c2":
        new_text = convert.text_to_hex(opc)
        printear()
        printt(new_text)

    if mode == "C3" or mode == "c3":
        new_text = convert.decimal_to_text(opc)
        printear()
        printt(new_text)
    
    if mode == "C4" or mode == "c4":
        new_text = convert.binary_to_text(opc)
        printear()
        printt(new_text)
    
    if mode == "C5" or mode == "c5":
        new_text = binary_to_hex(opc)
        printear()
        printt(new_text)
    
    if mode == "C6" or mode == "c6":
        new_text = convert.decimal_to_hex(int(opc))
        printear()
        printt(new_text)

    if mode == "C7" or mode == "c7":
        new_text = convert.url_encode(opc)
        printear()
        printt(new_text)
    
    if mode == "C8" or mode == "c8":
        new_text = convert.revert_strings(opc)
        printear()
        printt(new_text)
    
    if mode == "C9" or mode == "c9":
        new_text = long_bytes(opc)
        printear()
        printt(new_text)
    
    if mode == "C10" or mode == "c10":
        new_text = imprimir_valor_hexadecimal(opc)
        printear()
        printt(new_text)
    
    if mode == "D1" or mode == "d1":
        new_text = base64_to_text(opc)
        printear()
        if isinstance(new_text, dict):
            for key, value in new_text.items():
                print(f"[{colored('*', 'blue')}] >> {colored(value, 'white')}")
        else:
            printt(new_text)
    
    if mode == "D2" or mode == "d2": 
        new_text = decode_morse(opc)
        printear()
        printt(new_text)
    
    if mode == "D3" or mode == "d3":
        new_text = rot13(opc)
        printear()
        printt(new_text)
    
    if mode == "D4" or mode == "d4": #oooooooooooooooooooooooooooooooooooooooo Is file
        new_text = sustitution(content_file)
        printear()
        printt(new_text)
    
    if mode == "D5" or mode == "d5": #oooooooooooooooooooooooooooooooooooooooo Is file
        import subprocess

        def decode_text(base64_command):
            try:
                result = sub.run(base64_command, shell=True, check=True, capture_output=True, text=True)
                decoded_output = result.stdout.strip()
                return decoded_output
            except subprocess.CalledProcessError as e: pass

        initial_command = f"echo '{content_file}' | base64 -d"
        current_command = initial_command
        new_text = ""
        max_iterations = int(repetitions)

        try:
            for _ in range(max_iterations):
                decoded_text = decode_text(current_command)
                if decoded_text:
                    new_text = decoded_text
                    current_command = f"echo '{new_text}' | base64 -d"
                else:
                    break
        except Exception as e: print(f"\n[{colored('-', 'red')}] >> Error: {e}")

        printear()
        printt(new_text)
    
    if mode == "D6" or mode == "d6":
        new_text = url_decode(opc)
        printear()
        printt(new_text)

    if mode == "D7" or mode == "d7":
        new_text = rsa_decode_3_values(file_path)
        printear()
        printt(new_text)
    
    if mode == "D8" or mode == "d8":
        new_text = vigenere_decrypt(opc, key)
        printear()
        printt(new_text)
    
    if mode == "D9" or mode == "d9":
        new_text = xor_chain_sin_key(opc, opc_2)
        printear()
        printt(new_text)
        
    if mode == "D10" or mode == "d10":
        import importlib.util
        
        try:
            fuckJs_path = '/home/parrot/Desktop/aprendiendoPython/fuckJs.py'
            spec = importlib.util.spec_from_file_location("fuckJs", fuckJs_path)
            fuckJs = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(fuckJs)
            js = ""
            with open(file_path, 'r') as file:
                js = file.read()

            new_text = fuckJs.fight(js).code

            printear()
            if new_text == None or new_text == "":
                print(f"[{colored('*', 'blue')}] >> {colored('None', 'magenta')}")
            else:
                print(f"[{colored('*', 'blue')}] >> {colored({new_text}, 'magenta')}")
        except Exception as e: pass

    if mode == "D11" or mode == "d11":
        new_text = md5_decode(opc)
        printear()
        printt(new_text)

    if mode == "D12" or mode == "d12":
        n = opc.split(':')
        new_text = luhn_find_card(n)
        printear()
        printt(new_text)
    
    if mode == "D13" or mode == "d13":
        new_text = brainfuck_interpreter(opc)
        printear()
        printt(new_text)

    if mode == "D14" or mode == "d14":
        printear()
        for x in range(40):
            a = cesar_decode(opc, x)
            printt(a)

    if mode == "D15" or mode == "d15":
        a = bacon_decode(opc)
        printear()
        for x in a:
            printt(x)

    if mode == "D16" or mode == "d16":
        new_text = trithemius_decode(opc)
        printear()
        printt(new_text)

    if mode == "D17" or mode == "d17":
        printear()
        try:
            ciphertext = bytes.fromhex(opc)
            possible_texts = brute_force_xor(ciphertext)

            for key, text in possible_texts[:10]:
                if possible_texts == None or possible_texts == "":
                    print(f"[{colored('*', 'blue')}] >> {colored('None', 'magenta')}")
                else:
                    print(f"[{colored('*', 'blue')}] >> {colored(text, 'magenta')}")
        except Exception as e: print(f"[{colored('-', 'red')}] >> Error: {e}")
    
    if mode == "D18" or mode == "d18":
        printear()
        try:
            for x in range(-30, 30):
                text = ascii_caesar_shift(content_file, x)
                new_text = ''.join(text.splitlines())
                printt(new_text)

                import re

                pattern = r'([A-Za-z]+(?:\s+[A-Za-z]+){0,9})\s*\{.*?\}'
                matchs = re.search(pattern, new_text)
                if matchs:
                    print(f"[{colored('*', 'blue')}] >> {colored(new_text, 'cyan')}")
                    
        except Exception as e: print(f"[{colored('-', 'red')}] >> Error: {e}")

    if mode == "D19" or mode == "d19":
        xor_files(file_path_1, file_path_2, name_output_file)
        printear()
        printt("Generate file output with success")

    if mode == "E1" or mode == "e1":
        new_text = fetch_and_search(opc, opc_2)
        printear()
        printt(new_text)

def printear():
    print("")
    bar_progress = o.progress("Uploading")
    for i in range(344):
        sleep(0.0001)
        bar_progress.status(f"{colored(i, 'cyan')}")

class convert:
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
        def eliminar_no_imprimibles(cadena):
            patron = re.compile(r'[\x00-\x1F\x7F-\xFF]')
            cadena_limpia = patron.sub('', cadena)
            return cadena_limpia

        try:
            bytes_object = bytes.fromhex(strings)
            text = bytes_object.decode("utf-8", errors='ignore')
            new_text = eliminar_no_imprimibles(text)
            return new_text

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

if __name__ == "__main__":
    main()
