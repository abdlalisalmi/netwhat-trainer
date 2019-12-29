
import time
import os
import sys
import string
from en_questions import EnQuestions

# normal text = \033[0;37;40m

def sprint(string, speed = 1):
    for c in string + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed / 100)


def logo():
  logo = """\033[1;32;40m
                 _|  _|_|_|    _|_|_|    _|_|_|_|_|  
               _|_|        _|        _|          _|  
                 _|    _|_|      _|_|          _|    
                 _|        _|        _|      _|      
                 _|  _|_|_|    _|_|_|      _|        

      for other scripts : https://github.com/salmiabdlali
\033[0;37;40m"""
  print(logo)


def  language():
    print("""
\033[1;32;40m[1]\033[0;37;40m : English
\033[1;32;40m[2]\033[0;37;40m : Français (Not available yet)
        """)
    language = 0
    while (language != 1 ):#or language != 2):
        language = int(input("Choose your language: "))
        if language == 1:
            print("[√] : English")
            return language
        elif language == 2:
            print("Sorry French Not Available Yet")
            #return language
        else:
            print("\033[0;37;41mInvalid Choice !!!\033[0;37;40m")
            #return 0


def main():
    os.system("clear")
    logo()
    sprint(("Welcome to NetWhat Trainer, show us what you've learned :)").upper())
    lang = language()
    sprint("The training will start now...", 5)
    time.sleep(3)
    os.system("clear")
    logo()
    print("""
\033[1;32;40m[√]\033[0;37;40m ==> Good Answer :)
\033[0;37;41m[X]\033[0;37;40m ==> Wrong Answer :(
""")

    if lang == 1:
      EnQuestions()



if __name__ == '__main__':
    main()












