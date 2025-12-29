"""
Core module for Aetherion Password Manager.
"""
import random;
import os
import sys;
from dotenv import load_dotenv

choices = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*',
           '(',')','-','=','+','[',']','{','}','|',';',':','"','.','<','>','/','?','~','`'}
def main():
    """Main Deity"""
    seed = os.getenv("SEED")
    BirdUp = False
    # Randomized Seed thats different everytime.
    while BirdUp == False:
        random.seed(random.randint(0,int(sys.maxsize/random.randint(1,5))) * int(seed))
        print("What length would you like your password to be? It is recommended to be at least 12 characters long.")
        length = int(input("Length:\t"))
        randomPassword = ''.join(random.choices(tuple(choices),k=length))
        print(randomPassword)

        retaining = input("Would you like to retain this password? Type Yes to retain, or press Enter to discard:\t").lower()
        if retaining == "yes" or retaining == "y":
            with open("retained_passwords.txt","a") as f:
                f.write(randomPassword + "\n")
                print("Password retained in password.txt")
        else:
            song = print("You have discarded the password.")
            del randomPassword
            del length
            input("Ok? Press Enter to continue.")
            del song
        askContinueProgram = input("Would you like to generate another password? Type Yes to continue, or press enter to exit.\t").lower()
        if askContinueProgram == "no" or askContinueProgram == "n":
            BirdUp = True
            print("Exiting Aetherion Password Manager.")
        pass


if __name__ == "__main__":
    print(f"Starting Generator module of Aetherion.")