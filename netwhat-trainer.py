
import time
import os
import sys
import string
from en_questions import EnQuestions
from fr_questions import FrQuestions

# normal text = \033[0;37;40m

def sprint(string, speed = 1):
    for c in string + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed / 100)

def cowsay(string):

    line_nb = len(string) + 4
    print("")
    print("-" * line_nb)
    sprint("\033[1;32;40m{}\033[0;37;40m".format(string))
    print("-" * line_nb)
    print('''\033[1;32;40m
                \\   ^__^
                 \\  (♥♥)\\_______
                    (__)\\       )\\
                        ||----w |        
                        ||     ||
        \033[0;37;40m''')

def logo():
    color_green = "\033[1;32;40m"
    color_originale = "\033[0;37;40m"
    color_yellow = "\033[1;33;40m"
    color_red = "\033[1;31;40m"
    sprint("""
{}   __    __  __       __          ________                      __                               
  |  \  |  \|  \  _  |  \        |        \                    |  \ {}https://github.com/salmiabdlali{}
  | $$\ | $$| $$ / \ | $$         \$$$$$$$$  ______    ______   \$$ _______    ______    ______         \ | /    
  | $$$\| $$| $$/  $\| $$  ______   | $$    /      \  |      \ |  \|       \  /      \  /      \        - * -    
  | $$$$\ $$| $$  $$$\ $$ |      \  | $$   |  $$$$$$\  \$$$$$$\| $$| $$$$$$$\|  $$$$$$\|  $$$$$$\\        /|\     
  | $$\$$ $$| $$ $$\$$\$$  \$$$$$$  | $$   | $$   \$$ /      $$| $$| $$  | $$| $$    $$| $$   \$$       /\|/\    
  | $$ \$$$$| $$$$  \$$$$           | $$   | $$      |  $$$$$$$| $$| $$  | $$| $$$$$$$$| $$            /  |  \   
  | $$  \$$$| $$$    \$$$           | $$   | $$       \$$    $$| $$| $$  | $$ \$$     \| $$           /\/\|/\/\  
   \$$   \$$ \$$      \$$            \$$    \$$        \$$$$$$$ \$$ \$$   \$$  \$$$$$$$ \$$          /  {}13{}|{}37  {}\{}  

""".format(color_green, color_yellow,color_green, color_red,color_green, color_red, color_green, color_originale),0.05)

def  language():
    print("\033[1;32;40m[1]\033[0;37;40m : English")
    print("\033[1;32;40m[2]\033[0;37;40m : Français")
    language = '0'
    while (language != '1' or language != '2'):
        language = input("Choose your language: ")
        if language == '1':
            cowsay("[√] : You Choose English")
            return language
        elif language == '2':
            cowsay("[√] : Vous Choisissez Français")
            return language
        else:
            print("\033[0;37;41mInvalid Choice !!!\033[0;37;40m")


def main():
    os.system("clear")
    logo()
    sprint(("Welcome to NetWhat Trainer, show us what you've learned :)").upper())

    lang = language()
    if (lang == '1'):
        sprint("The training will start now...", 5)
    elif (lang == '2'):
        sprint("La Préparation Commencera Maintenant...", 3)

    time.sleep(3)
    os.system("clear")
    logo()
    if (lang == '1'):
        print("\033[1;32;40m[√]\033[0;37;40m ==> Good Answer")
        print("\033[0;37;41m[X]\033[0;37;40m ==> Wrong Answer")
    elif (lang == '2'):
        print("\033[1;32;40m[√]\033[0;37;40m ==> Bonne Réponse")
        print("\033[0;37;41m[X]\033[0;37;40m ==> Mauvaise Réponse")


    if lang == '1':
        EnQuestions()
    elif lang == '2':
        FrQuestions()
    if (lang == '1'):
        repeat = input("Do You Want To Repeat Training ? y/n : ").upper()
    elif (lang == '2'):
        repeat = input("Voulez-Vous Répéter La Préparation ? y/n : ").upper()
    
    if (repeat == 'Y' and repeat == 'YES'):
        main()


if __name__ == '__main__':
    main()












