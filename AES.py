from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, lpossword, file_path):
        
        self.plainlpossword = lpossword
        self.lpossword = hashlib.sha256(lpossword.encode('utf-8')).digest()
        self.file_path = file_path

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, lpossword, lpossword_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(lpossword, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def gen(self):
        with open(self.file_path, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.lpossword)
        with open(self.file_path, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")

            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, lpossword, file_path):\n")
            f.write("\t\tself.lpossword = hashlib.sha256(lpossword.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_path = file_path\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, lpossword):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(lpossword, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decryptorHashlib(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_path, self.lpossword)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class bruteForceit:\n")
            f.write("\tdef __init__(self, bytes_values):\n")
            f.write("\t\tself.bytes_values = bytes_values\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.bytes_values)\n")
            f.write("\t\t\t\tdecrypted_code = test.decryptorHashlib()\n")
            f.write("\t\t\t\texecbyteval = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn execbyteval \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"bytes_values = {enc}\n")
            f.write(f"bruting = bruteForceit(bytes_values)\n")
            f.write(f"execbyteval = bruting.start()\n")
            f.write("exec(execbyteval)\n")      
