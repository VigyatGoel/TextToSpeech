import os

if __name__ == '__main__':

    print("Hello, Welcome to Text-to-Speech engine created by Vigyat Goel ")

    print("If you are using mac then well and good, but if you are using windows then bye bye.")

    while True:

        x = input("Enter what you want me to speak or press q to exit : ")

        if x == "q":

            print("Bye bye friend.")
            os.system("say 'Bye bye friend'")
            break

        command = f"say {x}"
        os.system(command)