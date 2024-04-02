import os
import platform


def text_to_speech():
    print("Hello, Welcome to Text-to-Speech engine created by Vigyat Goel ")

    if platform.system() == 'Windows':
        print("Sorry, this program does not support Windows.")
        return
    elif platform.system() != 'Darwin':  # macOS
        print("Sorry, this program only supports macOS.")
        return

    while True:
        x = input("Enter what you want me to speak or press q to exit : ")

        if x == "q":
            print("Bye bye friend.")
            os.system("say 'Bye bye friend'")
            break

        try:
            command = f"say {x}"
            os.system(command)
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    text_to_speech()


if __name__ == '__main__':
    main()
