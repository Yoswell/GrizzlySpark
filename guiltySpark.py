#!/usr/bin/python3

from pwn import log as o
from termcolor import colored
import argparse
import base64
import os
from time import sleep
import getpass
import fnmatch
import click
from tabulate import tabulate

from convert import (
    hex_to_text, long_bytes, imprimir_valor_hexadecimal, binary_to_hex, revert_strings, hex_to_text,
    hex_to_text, text_to_hex, decimal_to_text, decimal_to_hex, binary_to_text, url_encode
)

from decode import (
    brute_force_xor, trithemius_decode, bacon_decode, cesar_decode, brainfuck_interpreter, 
    luhn_find_card, vigenere_decrypt, rsa_decode_3_values, decode_base, 
    decode_morse, rot13, url_decode, ascii_caesar_shift, xor_files, atbash_cipher, crack_hash_md5
)

from exploit import (
    fetch_and_search, scan_icmp, analyze_macros, generate_reverse_shell_examples, generate_wordlist
)

def print_modes():
    from tabulate import tabulate

    print(r"""
 __         __
/  \.-'''-./  \  | Author: Vishok
\    -   -    /  |---------------
 |   o   o   |   | Version: 1.0
 \  .-'''-.  /   |---------------
  '-\__Y__/-'    | A versatile text and cipher decoding/encoding tool designed to assist in Capture The Flag (CTF)
     '---'    
""")

    data = [
        (f"{colored('C1', 'red')}", "Convert Hexadecimal to Text", "-m -i", "Hexadecimal", "Text"),
        (f"{colored('C2', 'red')}", "Convert Text to Hexadecimal", "-m -i", "Text", "Hexadecimal"),
        (f"{colored('C3', 'red')}", "Convert Decimal to Text", "-m -i", "Decimal", "Text"),
        (f"{colored('C4', 'red')}", "Convert Binary to Text", "-m -i", "Binary", "Text"),
        (f"{colored('C5', 'red')}", "Convert Binary to Hexadecimal", "-m -i", "Binary", "Hexadecimal"),
        (f"{colored('C6', 'red')}", "Convert Decimal to Hexadecimal", "-m -i", "Decimal", "Hexadecimal"),
        (f"{colored('C7', 'red')}", "URL Encode", "-m -i", "Text", "URL-encoded String"),
        (f"{colored('C8', 'red')}", "Revert Strings", "-m -i", "Text", "Reversed String"),
        (f"{colored('C9', 'red')}", "Convert Long Bytes to Text", "-m -i", "Long Bytes", "Text"),
        (f"{colored('C10', 'red')}", "Convert Hexadecimal (0x?? format) to Decimal", "-m -i", "Hexadecimal (0x format)", "Decimal"),
        
        ("", " ", " ", " "),

        (f"{colored('D1', 'yellow')}", "Bases Decode (base64, base58, base62, base85)", "-m -i", "Base64 Encoded String", "Decoded Text"),
        (f"{colored('D2', 'yellow')}", "Morse Code Decode", "-m -i", "Morse Code", "Text"),
        (f"{colored('D3', 'yellow')}", "ROT13 Decode", "-m -i", "ROT13 Encoded Text", "Decoded Text"),
        (f"{colored('D4', 'yellow')}", "Atbash Cipher Decode", "-m -i", "Atbash Encoded Text", "Decoded Text"),
        (f"{colored('D5', 'yellow')}", "Base64 File Decode", "-m -f -r", "Base64 File", "Decoded File"),
        (f"{colored('D6', 'yellow')}", "URL Decode", "-m -i", "URL Encoded String", "Decoded String"),
        (f"{colored('D7', 'yellow')}", "RSA Decode with Parameters (e, n, c, p, q)", "-m -f", "RSA Parameters", "Decrypted Text"),
        (f"{colored('D8', 'yellow')}", "Vigenère Cipher Decode", "-m -i -k", "Encrypted Text, Key", "Decrypted Text"),
        (f"{colored('D10', 'yellow')}", "MD5 Hash Cracking", "-m -i", "MD5 Hash", "Cracked Text"),
        (f"{colored('D13', 'yellow')}", "Brainfuck Language Decode", "-m -i", "Brainfuck Code", "Decoded Text"),
        (f"{colored('D14', 'yellow')}", "Caesar Cipher Decode", "-m -i", "Caesar Encrypted Text", "Decrypted Text"),
        (f"{colored('D15', 'yellow')}", "Bacon Cipher Decode", "-m -i", "Bacon Cipher Encrypted Text", "Decrypted Text"),
        (f"{colored('D16', 'yellow')}", "Trithemius Cipher Decode", "-m -i", "Trithemius Encrypted Text", "Decrypted Text"),
        (f"{colored('D17', 'yellow')}", "XOR Brute Force (One Chain, HEX Format)", "-m -i", "XOR Encrypted Text", "Decrypted Text"),
        (f"{colored('D18', 'yellow')}", "Caesar ASCII Decode", "-m -f", "Caesar Encrypted ASCII", "Decrypted ASCII"),
        (f"{colored('D19', 'yellow')}", "XOR Two Files Decode", "-m -x -y -z", "Two Files", "Decrypted File"),

        ("", " ", " ", " "),

        (f"{colored('E1', 'blue')}", "Web Scraping", "-m -i -j", "URL, Text Pattern", "Extracted Data"),
        (f"{colored('E2', 'blue')}", "Check Active IP", "-m -i", "IP Address", "Active Status"),
        (f"{colored('E3', 'blue')}", "Extract Macros", "-m -x", "DOCM File Path", "Extracted Macros"),
        (f"{colored('E4', 'blue')}", "Generate Reverse Shell", "-m -i -j", "IP, Port", "Reverse Shells"),
        (f"{colored('E5', 'blue')}", "Generate dictionary", "-m -i", "Text Pattern", "Dictionary File"),
    ]

    # Table headers
    headers = [colored("Code", 'cyan'), colored("Description", 'cyan'), colored("Parameters", 'cyan'), colored("Input", 'cyan'), colored("Output", 'cyan')]

    print(f'\n{tabulate(data, headers=headers, tablefmt="list", numalign="center")}')


@click.command()
@click.option("-m", "--mode", help="Mode of operation (e.g., D10)", required=False, type=str)
@click.option("-i", "--opc", help="Input data", required=False, type=str)
@click.option("-s", "--show", help="Show mode -sS o -ss", required=False, type=str)
@click.option("-f", "--path", help="Path to a file", required=False, type=str)
@click.option("-x", "--path1", help="Another file path", required=False, type=str)
@click.option("-y", "--path2", help="Yet another file path", required=False, type=str)
@click.option("-z", "--path3", help="Path for output file", required=False, type=str)
@click.option("-r", "--repeat", help="Repeat the operation", required=False, type=int)
@click.option("-k", "--key", help="Key for decryption", required=False, type=str)
@click.option("-j", "--input_two", help="Second input data", required=False, type=str)

def main(mode, opc, show, path, path1, path2, path3, repeat, key, input_two):
    opc = opc
    show_mode = show
    file_path = path
    file_path_1 = path1
    file_path_2 = path2
    name_output_file = path3
    repetitions = repeat
    key_val = key
    opc_2 = input_two
    mode = mode

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
            print(f"\n[{colored('*', 'red')}] >> None")
        else:
            print(f"{a}")

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

        "D1": decode_base,
        "D2": decode_morse,
        "D3": rot13,
        "D4": atbash_cipher,
        "D6": url_decode,
        "D10": crack_hash_md5,
        "D13": brainfuck_interpreter,
        "D15": bacon_decode,
        "D16": trithemius_decode,

        "E1": fetch_and_search,
        "E2": scan_icmp,
        "E3": analyze_macros,
        "E4": generate_reverse_shell_examples,
        "E5": generate_wordlist,
    }

    if show_mode == "S" or show_mode == "s":
        print_modes()

    if mode:
        try:
            mode_func = modes_map.get(mode.upper())

            if mode == "D1":
                result = decode_base(opc)
                printear()
                for key, value in result:
                    print(f"{colored(key + ':', 'cyan')} {value}")

            elif mode == "D10":
                result = crack_hash_md5(opc)
                printear()
                printt(result)

            elif mode == "E1":
                result = mode_func(opc, opc_2)
                printear()
                for x in result:
                    printt(x)
            
            elif mode == "E3":
                result = mode_func(file_path_1)
                printear()
                printt(result)

            elif mode == "E4":
                result = generate_reverse_shell_examples(opc, opc_2)
                printear()
                printt(result)

            elif mode_func:
                result = mode_func(opc)
                printear()
                printt(result)
        except:
            pass
    
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

    if mode == "D7" or mode == "d7":
        new_text = rsa_decode_3_values(file_path)
        printear()
        printt(new_text)
    
    if mode == "D8" or mode == "d8":
        new_text = vigenere_decrypt(opc, key)
        printear()
        printt(new_text)

    if mode == "D14" or mode == "d14":
        printear()
        for x in range(40):
            a = cesar_decode(opc, x)
            printt(a)

    if mode == "D17" or mode == "d17":
        printear()
        try:
            ciphertext = bytes.fromhex(opc)
            possible_texts = brute_force_xor(ciphertext)

            for key, text in possible_texts[:10]:
                if possible_texts == None or possible_texts == "":
                    printt(possible_texts)
                else:
                    printt(text)
        except Exception as e: pass
    
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
    print("")

if __name__ == "__main__":
    main()
