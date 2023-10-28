import os
import time

#Web Development
def web_dev():
    #Selecting The Name of the project
    name = input("Type a Name: ")
    print('\n' + "Select the directory: ")
    dir = input(">>> ")
    print('\n' + f"Creating {name} Project...")
    time.sleep(1.25)
    os.system(f'mkdir {dir}\{name}')
    time.sleep(2.55)
    with open(f'{dir}{name}\main.py', "w") as file, open('templates.datas\simple_flask_code', "r") as fk_sim_code:
        code = fk_sim_code.read()
        file.write(code)
        
    print('\n' + f'{name} was created Successfully!' + '\n' + '\n')
    input("press enter to exit")
    exit(0)
#GUI applications Development
def gui_app():
    #Selecting The Name of the project
    name = input("Type a Name: ")
    print('\n' + "Select the directory: ")
    dir = input(">>> ")
    print('\n' + f"Creating {name} Project...")
    time.sleep(1.25)
    os.system(f'mkdir {dir}\{name}')
    time.sleep(2.55)
    with open(f'{dir}{name}\main.py', "w") as file, open('templates.datas\simple_gui_code', "r") as gui_sim_code:
        code = gui_sim_code.read()
        file.write(code)
        
    print('\n' + f'{name} was created Successfully!' + '\n' + '\n')
    input("press enter to exit")
    exit(0)
#Console applications Development
def console_app():
    name = input("Type a Name: ")
    print('\n' + "Select the directory: ")
    dir = input(">>> ")
    print('\n' + f"Creating {name} Project...")
    time.sleep(1.25)
    os.system(f'mkdir {dir}\{name}')
    time.sleep(2.55)
    with open(f'{dir}{name}\main.py', "w") as file, open('Templates.datas\simple_console_code', "r") as console_sim_code:
        code = console_sim_code.read()
        file.write(code)
        
    print('\n' + f'{name} was created Successfully!' + '\n' + '\n')
    input("press enter to exit")
    exit(0)

def main():
    print('Welcome to python project creation tool' + '\n' + '\n')
    alltemplates = ['1)web development', '2)GUI application', '3)Console application']
    while True:
        print('\n' + '-----------------------' + '\n')
        for i in alltemplates:
            print(i)
            print('-----------------------' + '\n')
        slector = input('Select: ')
        if slector == '1':
            print('\n' + 'Taking the Informations...' + '\n')
            web_dev()
        elif slector == '2':
            print('\n' + 'Taking the Informations...' + '\n')
            gui_app()
        elif slector == '3':
            print('\n' + 'Taking the Informations...' + '\n')
            console_app()
main()