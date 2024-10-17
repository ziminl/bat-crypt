import random
import string
import os
from pathlib import Path

def obfuscate_file():
    S = 5
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    file = input("bat path: ")
    out_hex = ["FF", "FE", "26", "63", "6C", "73", "0D", "0A"]

    try:
        with open(file, 'rb') as f:
            content = f.read()
        out_hex.extend(['{:02X}'.format(b) for b in content])
        
        with open(f'{ran}.bat', 'wb') as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))
        
        if Path(f'{ran}.bat').is_file():
            print('success')
        else:
            print('error')
    except Exception as e:
        print(f'error: {e}')

if __name__ == "__main__":
    obfuscate_file()
