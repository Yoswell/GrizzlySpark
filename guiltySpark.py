#!/usr/bin/python3

from pwn import log as o
from termcolor import colored
import argparse
import base64
import os
from time import sleep


from convert import (
    hex_to_text, long_bytes, imprimir_valor_hexadecimal, binary_to_hex, revert_strings, hex_to_text,
    hex_to_text, text_to_hex, decimal_to_text, decimal_to_hex, binary_to_text, url_encode
)

from decode import (
    brute_force_xor, trithemius_decode, bacon_decode, cesar_decode, brainfuck_interpreter, 
    luhn_find_card, xor_chain_sin_key, vigenere_decrypt, rsa_decode_3_values, base64_to_text, 
    decode_morse, rot13, url_decode, ascii_caesar_shift, xor_files, atbash_cipher
)

from exploit import fetch_and_search, scan_icmp

def print_modes():
    print("""
                    ▄▄                    ▄▄                                                            
  ▄▄█▀▀▀█▄█          ██                  ▀███                ▄█▀▀▀█▄█                         ▀███       
▄██▀     ▀█                                ██               ▄██    ▀█                           ██       
██▀       ▀▀███▄███▀███  █▀▀▀███ █▀▀▀███   ██ ▀██▀   ▀██▀   ▀███▄   ▀████████▄ ▄█▀██▄ ▀███▄███  ██  ▄██▀ 
█▓           ██▀ ▀▀  ██  ▀  ███  ▀  ███    ▓█   ██   ▄█       ▀█████▄ ██   ▀████   ██   ██▀ ▀▀  ██ ▄█    
█▓▄    ▀████ █▓      ▓█    ██▓     ██▓     ▓█    ██ ▄▓            ▀██ ▓█    ██ ▄███▓█   █▓      ▓█▄██    
▀▓█▄     ██  █▓      ▓█   ▓██     ▓██      ▓█     ██▓       ██     ██ ▓█    ▓██▓   ▓█   █▓      ▓█ ▀██▄  
▓▓▓    ▀▓█▓▓ ▓▓      ▓▓   ▓█▓     ▓█▓      ▓▓     █▓▓       ▓     ▀█▓ ▓█▓   ▓▓ ▓▓▓▓▒▓   ▓▓      ▓▓▓▓▓    
▀▒▓▓     ▓▓  ▓▒      ▓▓  ▓▓▓   ▓ ▓▓▓   ▓   ▒▓     ▒▓▒       ▓▓     ▓▓ ▓█   ▓▓▓▓▓   ▒▓   ▓▒      ▒▓ ▀▓▓▓  
  ▒▒▒ ▒ ▒▒ ▒ ▒▒▒   ▒ ▒ ▒ ▒ ▒▓▒▓▒ ▒ ▒▓▒▓▒ ▒ ▒ ▒     ▓        ▒▓▒ ▒ ▒▓  ▒▓▒ ▒ ▒ ▒▓▒ ▒ ▓▒▒ ▒▒▒   ▒ ▒ ▒  ▒ ▒""")
    #---------------------------------------------------------------------------------#
    print(f"\n{colored('[+]', 'red')} Convert")
    print(f"\t{colored('[+]', 'yellow')} C1  - Hexadecimal to text                               options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C2  - Text to hexadecimal                               options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C3  - Decimal to text                                   options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C4  - Binary to text                                    options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C5  - Binary to hexadecimal                             options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C6  - Decimal to hexadecimal                            options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C7  - URL encode                                        options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C8  - Revert strings (aloh -> hola)                     options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C9  - Long_bytes to text                                options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} C10 - Convert hexadecimal (0x?? format) to decimal      options(-m -i)")
    #---------------------------------------------------------------------------------#
    print(f"{colored('[+]', 'red')} Decode")
    print(f"\t{colored('[+]', 'yellow')} D1  - Base64                                            options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D2  - Morse decode                                      options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D3  - ROT13 decode                                      options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D4  - Atbash decode                                     options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D5  - Base64 file decode                                options(-m -f -r)")
    print(f"\t{colored('[+]', 'yellow')} D6  - URL decode                                        options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D7  - RSA decode with (e:? n:? c:? p:? q:?)             options(-m -f)")
    print(f"\t{colored('[+]', 'yellow')} D8  - Vigenere decode                                   options(-m -i -k)")
    print(f"\t{colored('[+]', 'yellow')} D9  - Xor (Two chains) without (key) (HEX format)       options(-m -i -j)")
    print(f"\t{colored('[+]', 'yellow')} D13 - BrainFuck lenguage (format -> >+++++++++[<+)      options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D14 - Caesar decode                                     options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D15 - Bacon decode (format -> abbb abaaa abbaa)         options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D16 - Trithemius decode                                 options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D17 - XOR (One chain) brute force (HEXformat)           options(-m -i)")
    print(f"\t{colored('[+]', 'yellow')} D18 - Caesar ascii decode                               options(-m -f)")
    print(f"\t{colored('[+]', 'yellow')} D19 - Xor (Two Files) decode                            options(-m -x -y -z)")
    #-------------------------------------=-------------------------------------------#
    print(f"{colored('[+]', 'red')} Exploits")
    print(f"\t{colored('[+]', 'yellow')} E1  - Web Scrapping (url, text pattern)                 options(-m -i -j)")
    print(f"\t{colored('[+]', 'yellow')} E2  - Check active ip                                   options(-m -i)\n")
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
    parser = argparse.ArgumentParser(description="", add_help=False)
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
            print(f"[{colored('*', 'red')}] >> None")
        else:
            print(f"[{colored('*', 'blue')}] >> {a}")

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

    modes_map = {
        "C1": hex_to_text,
        "C2": text_to_hex,
        "C3": decimal_to_text,
        "C4": binary_to_text,
        "C5": binary_to_hex,
        "C6": decimal_to_hex,
        "C7": url_encode,
        "C8": revert_strings,
        "C9": long_bytes,
        "C10": imprimir_valor_hexadecimal,

        "E1": fetch_and_search,
        "E2": scan_icmp
    }

    if mode:
        try:
            mode_func = modes_map.get(mode.upper())
            if mode == "E1":
                result = mode_func(opc, opc_2)
                printear()
                printt(result)
            else:
                if mode_func:
                    result = mode_func(opc)
                    printear()
                    printt(result)
                else:
                    pass
        except:
            pass
    
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

    if mode == "D4" or mode == "d4":
        new_text = atbash_cipher(opc)
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

def printear():
    print("")
    bar_progress = o.progress("Uploading")
    for i in range(344):
        sleep(0.001)
        bar_progress.status(f"{colored(i, 'cyan')}")

if __name__ == "__main__":
    main()
