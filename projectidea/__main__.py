import sys
import random
from colorama import init, Fore
from .ideaslist import *

init()

def main():

    arg = sys.argv[1:]

    args = [x.lower() for x in arg]

    if len(args) == 0:
        print("\nHi, if you stuck you can type", Fore.GREEN + "'projectidea help'" + Fore.RESET + ".\n")
    elif len(args) == 1:
        if args[0] == "help":
            print("\nYou can select four types of difficulty level", Fore.MAGENTA + "(easy, medium, hard, impossible)", Fore.RESET + "and algroithm will give you a project idea. Example code:", Fore.MAGENTA + "'projectidea medium'" + Fore.RESET + ".\n")
        elif args[0] == "easy":
            print("\nYou",  Fore.CYAN + "can", Fore.RESET + easy[random.randint(0, easy_number)]+"\n")
        elif args[0] == "medium":
            print("\nYou",  Fore.CYAN + "can", Fore.RESET + medium[random.randint(0, medium_number)]+"\n")
        elif args[0] == "hard":
            print("\nYou",  Fore.CYAN + "can", Fore.RESET + hard[random.randint(0, hard_number)]+"\n")
        elif args[0] == "impossible":
            print("\nYou",  Fore.CYAN + "can", Fore.RESET + impossible[random.randint(0, impossible_number)]+"\n")
        else:
            print("\nCommand not found :(  If you stuck you can type", Fore.GREEN + "'projectidea help'"+ Fore.RESET + ".\n")
        
    if len(args) >= 2:
        print("\nCommand not found :(  If you stuck you can type", Fore.GREEN + "'projectidea help'"+ Fore.RESET + ".\n")



if __name__ == '__main__':
    main()