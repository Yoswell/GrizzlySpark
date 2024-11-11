# GrizzlySpark / CTF tool resolved
![382589821-2065ecf5-0e9b-4263-a10a-546a6bbd6e23](https://github.com/user-attachments/assets/032b5557-5c00-4337-86c6-a08372383c03)


## Documentation
<p>A powerful tool written in Python designed to help CTF (Capture The Flag) participants in solving IT security challenges. This tool provides several useful functionalities that facilitate data analysis and manipulation, allowing users to focus on solving challenges. <a href="https://discord.com/api/guilds/1296164292424368148/widget.json">Join to discord</a>
</p>

## Installation

Install all external dependencies

```bash
git clone https://github.com/Yoswell/Guilty-Spark.git

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

```python
~ ❯ python3 guiltySpark -mc2 -i'sp4rk{Th15_15_4_f4k3_fl4g}' 

    [◒] Uploading: 343
    [*] >> 737034726b7b546831355f31355f345f66346b335f666c34677d

~ ❯ python3 guiltySpark -mc1 -i'737034726b7b546831355f31355f345f66346b335f666c34677d'

    [▝] Uploading: 343
    [*] >> sp4rk{Th15_15_4_f4k3_fl4g}

~ ❯ python3 guiltySpark -md14 -i'vs4un{Wk15_15_4_i4n3_io4j}'      
    
    [-] Uploading: 343
    [*] >> vs4un{Wk15_15_4_i4n3_io4j}
    [*] >> ur4tm{Vj15_15_4_h4m3_hn4i}
    [*] >> tq4sl{Ui15_15_4_g4l3_gm4h}
    [*] >> sp4rk{Th15_15_4_f4k3_fl4g} >> Correct flag
    [*] >> ro4qj{Sg15_15_4_e4j3_ek4f}
    [*] >> qn4pi{Rf15_15_4_d4i3_dj4e}
    [*] >> pm4oh{Qe15_15_4_c4h3_ci4d}
    [*] >> ol4ng{Pd15_15_4_b4g3_bh4c}
    [*] >> nk4mf{Oc15_15_4_a4f3_ag4b}
    [*] >> mj4le{Nb15_15_4_z4e3_zf4a}
    [*] >> li4kd{Ma15_15_4_y4d3_ye4z}
    [*] >> kh4jc{Lz15_15_4_x4c3_xd4y}
    [*] >> jg4ib{Ky15_15_4_w4b3_wc4x}
    [*] >> if4ha{Jx15_15_4_v4a3_vb4w}
    [*] >> he4gz{Iw15_15_4_u4z3_ua4v}
    [*] >> gd4fy{Hv15_15_4_t4y3_tz4u}
    [*] >> fc4ex{Gu15_15_4_s4x3_sy4t}
    [*] >> eb4dw{Ft15_15_4_r4w3_rx4s}
    [*] >> da4cv{Es15_15_4_q4v3_qw4r}
    [*] >> cz4bu{Dr15_15_4_p4u3_pv4q}
    [*] >> by4at{Cq15_15_4_o4t3_ou4p}
    [*] >> ax4zs{Bp15_15_4_n4s3_nt4o}
    [*] >> zw4yr{Ao15_15_4_m4r3_ms4n}
    [*] >> yv4xq{Zn15_15_4_l4q3_lr4m}
    [*] >> xu4wp{Ym15_15_4_k4p3_kq4l}
    [*] >> wt4vo{Xl15_15_4_j4o3_jp4k}
    [*] >> vs4un{Wk15_15_4_i4n3_io4j}
    [*] >> ur4tm{Vj15_15_4_h4m3_hn4i}
    [*] >> tq4sl{Ui15_15_4_g4l3_gm4h}
    [*] >> sp4rk{Th15_15_4_f4k3_fl4g} >> Correct flag
    [*] >> ro4qj{Sg15_15_4_e4j3_ek4f}
    [*] >> qn4pi{Rf15_15_4_d4i3_dj4e}
    [*] >> pm4oh{Qe15_15_4_c4h3_ci4d}
    [*] >> ol4ng{Pd15_15_4_b4g3_bh4c}
    [*] >> nk4mf{Oc15_15_4_a4f3_ag4b}
    [*] >> mj4le{Nb15_15_4_z4e3_zf4a}
    [*] >> li4kd{Ma15_15_4_y4d3_ye4z}
    [*] >> kh4jc{Lz15_15_4_x4c3_xd4y}
    [*] >> jg4ib{Ky15_15_4_w4b3_wc4x}
    [*] >> if4ha{Jx15_15_4_v4a3_vb4w}
```

## Authors
Developed by <a href="https://www.linkedin.com/in/yoswel-badilla-cyberjr/">Vishok</a>
