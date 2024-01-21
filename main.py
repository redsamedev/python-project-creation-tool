import time
import os

def GUIAPP():
    name = input("Name Of the Project: ")
    directory = input("Directory Location: ")
    print("\ncreating the project...\n\n")
    try:
        os.system(f'mkdir {directory}\{name}')
        os.system(f'type nul > {directory}\{name}\main.py')
        with open('templates.datas\simple_gui_code', "r") as gui_code, open(f'{directory}\{name}\main.py', "w") as python_file:
            code = gui_code.read()
            python_file.write(code)
        print('\n\nthe project was succesfuly created!\n\n\n')
    except FileNotFoundError or FileExistsError:
        print("\n\nFile not Found or does not exist\n\nError Code:0F0NF\n\n")

def Console_APP():
    name = input("Name Of the Project: ")
    directory = input("Directory Location: ")
    print("\ncreating the project...\n\n")
    try:
        os.system(f'mkdir {directory}\{name}')
        os.system(f'type nul > {directory}\{name}\main.py')
        with open('templates.datas\simple_console_code', "r") as console_code, open(f'{directory}\{name}\main.py', "w") as python_file:
            code = console_code.read()
            python_file.write(code)
        print('\n\nthe project was succesfuly created!\n\n\n')
    except FileNotFoundError or FileExistsError:
        print("\n\nFile not Found or does not exist\n\nError Code:0F0NF\n\n")

def Web_APP():
    name = input("Name Of the Project: ")
    directory = input("Directory Location: ")
    print("\ncreating the project...\n\n")
    try:
        os.system(f'mkdir {directory}\{name}')
        os.system(f'type nul > {directory}\{name}\main.py')
        with open('templates.datas\simple_flask_code', "r") as console_code, open(f'{directory}\{name}\main.py', "w") as python_file:
            code = console_code.read()
            python_file.write(code)
        print('\n\nthe project was succesfuly created!\n\n\n')
    except FileNotFoundError or FileExistsError:
        print("\n\nFile not Found or does not exist\n\nError Code:0F0NF\n\n")


def main():
    print("\n\nWelcome to Pypt Console APP\n\n")
    print('you can see the tutorial with "tuto" command\n\n')
    time.sleep(1)
    while True:
        user_command_input = input("Type Command: ")
        if user_command_input == "tuto":
            print("just setting up the tutorial....")
            time.sleep(1)
            print("a window will popup don't close it!!")
            os.startfile("tuto.exe")
            main()
        elif user_command_input == "mk-proj" or user_command_input == "mkpj":
            list_of_templates = ["\n\n1)Console APP\n", "2)GUI APP\n", "3)Web APP\n"]
            for i in list_of_templates:
                print(i)
            print("Select One..\n")
            selection = input("Select: ")
            if selection == "1":
                Console_APP()
                break
            elif selection == "2":
                GUIAPP()
                break
            elif selection == "3":
                Web_APP()
                break
            else:
                print(f'{user_command_input} command is not available or does not exists')


main()
