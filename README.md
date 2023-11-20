
<h1 align="center">
  <br>
  <a href="https://github.com/OssamaN7/OsXploiter"><img src="https://raw.githubusercontent.com/OssamaN7/OsXploiter/main/logo/Os.png" alt="osxploiter" width="400"></a>
  <br>
  osXploiter V0.1
  <br>
</h1>
<h4 align="center">Python-based Reverse Shell Payload Generator crafted for targeting Windows operating systems. </h4>



<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#warning">EmailME</a> •
  <a href="#warning">Warning</a> •
  <a href="#license">License</a>
</p>

[![Watch the video](https://img.youtube.com/vi/T-D1KVIuvjA/maxresdefault.jpg)](https://youtu.be/T-D1KVIuvjA)

## Key Features

* TCP-based reverse shell communication mechanism.
  - Rapid and highly stable with no timeout or session closure issues[Metasploit Handler].
* Dual-layer code encryption.
  - 1step : Utilizing Base64 encryption and string obfuscation for concealing LHOST and LPORT values.
  - 2step : Implementing AES encryption with self-key brute-forcing techniques to evade antivirus detection.
* The payload designed also for injection into Rubber Ducky USB devices, enabling self-execution without detection.
* Secure transmission of encrypted bytes between the client and payload sides.
* Created as a backdoor for Windows Servers [for educational purposes].
* Successfully tested and proven to bypass AVAST, Microsoft Defender, Avira, Kaspersky, and 12 other security measures.


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python]((https://www.python.org/)), some requirement :

```bash
$ sudo pip install colarama
$ sudo pip install pycryptodome
$ sudo pip install hashlib
$ git clone [repo]
$cd [repo]
$python Crypter.py
Enjoy ! :D
```



> **Note**
> Tested on Python 3.11.6 [KALI_LINUX/WIN10]



## EmailME

As a student, I would greatly appreciate your feedback and suggestions. If you have any ideas to enhance my script, please share them with me at: [oussamaeuler@gmail.com].
. I'd really appreciate it!

## Warning 
> This script is created for educational purposes, intended to share my ideas and engage in discussions with you. I want to clarify that I am not liable for any misuse or exploitation of this script.


## About Me 

Visit : elmouddene.com

## License

AIT-EL MOUDDENE OSSAMA | 2023 




