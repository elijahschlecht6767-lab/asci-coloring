from colors import Colors
import os
import time

def clear_screen():
    """this checks the operating system"""
    if os.name == 'nt': # For Windows
        _ = os.system('cls')
    else: # For macOS and Linux
        _ = os.system('clear')


def main():
    reset=Colors.BLACK
    red=Colors.RED
    yellow=Colors.YELLOW
    green=Colors.GREEN

    clear_screen()
    for i in range(60):
        colors=[
        
        ]
    
        print_statement=""

        colors.append([reset, reset, reset, reset, reset, red, red, red, red, red, reset, reset, reset, reset, reset, reset], )
        colors.append([reset, reset, reset, reset, red, red, red, red, red, red, red, red, red, reset, reset, reset], )
        colors.append([reset, reset, reset, reset, green, green, green, yellow, yellow, green, yellow, reset, reset, reset, reset, reset], )
        colors.append([reset, reset, reset, green, yellow, green, yellow, yellow, yellow, green, yellow, yellow, yellow, reset, reset, reset], )
        colors.append([reset, reset, reset, green, yellow, green, green, yellow, yellow, yellow, green, yellow, yellow, yellow, reset, reset], )
        colors.append([reset, reset, reset, green, green, yellow, yellow, yellow, yellow, green, green, green, green, reset, reset, reset], )
        colors.append([reset, reset, reset, reset, reset, yellow, yellow, yellow, yellow, yellow, yellow, yellow, reset, reset, reset, reset], )
        colors.append([reset, reset, reset, reset, green, green, red, green, green, red, green, green, reset, reset, reset, reset], )
        colors.append([reset, reset, reset, green, green, green, red, green, green, red, green, green, green, reset, reset, reset], )
        colors.append([reset, reset, green, green, green, green, red, red, red, red, green, green, green, green, reset, reset], )
        colors.append([reset, reset, yellow, yellow, green, red, yellow, red, red, yellow, red, green, yellow, yellow, reset, reset], )
        colors.append([reset, reset, yellow, yellow, yellow, red, red, red, red, red, red, yellow, yellow, yellow, reset, reset], )
        colors.append([reset, reset, yellow, yellow, red, red, red, red, red, red, red, red, yellow, yellow, reset, reset], )
        colors.append([reset, reset, reset, reset, red, red, red, reset, reset, red, red, red, reset, reset, reset, reset], )
        colors.append([reset, reset, reset, green, green, green, reset, reset, reset, reset, green, green, green, reset, reset, reset], )
        colors.append([reset, reset, green, green, green, green, reset, reset, reset, reset, green, green, green, green, reset, reset], )

        for i in range(len(colors)):
            for j in range(len(colors[i])):
                print_statement+=f"{colors[i][j]}"
                print_statement+=f"{chr(0x2588)*2}"
            print_statement+="\n"

        print(print_statement)
        time.sleep(.5)
        clear_screen()








        colors=[
        
        ]
    
        print_statement=""

        colors.append([reset, reset, reset, reset, reset, reset, reset, reset, reset, reset, reset, reset, reset, yellow, yellow, yellow], )
        colors.append([reset, reset, reset, reset, reset, reset, red, red, red, red, red, reset, reset, yellow, yellow, yellow], )
        colors.append([reset, reset, reset, reset, reset, red, red, red, red, red, red, red, red, red, yellow, yellow], )
        colors.append([reset, reset, reset, reset, reset, green, green, green, yellow, yellow, green, yellow, reset, red, red, red], )
        colors.append([reset, reset, reset, reset, green, yellow, green, yellow, yellow, yellow, green, yellow, yellow, red, red, red], )
        colors.append([reset, reset, reset, reset, green, yellow, green, green, yellow, yellow, yellow, green, yellow, yellow, yellow, red], )
        colors.append([reset, reset, reset, reset, green, green, yellow, yellow, yellow, yellow, green, green, green, green, green, reset], )
        colors.append([reset, reset, reset, reset, reset, reset, yellow, yellow, yellow, yellow, yellow, yellow, yellow, green, reset, reset], )
        colors.append([reset, reset, green, green, green, green, green, red, green, green, green, red, green, reset, reset, reset], )
        colors.append([reset, green, green, green, green, green, green, green, red, green, green, green, red, green, reset, green], )
        colors.append([yellow, yellow, green, green, green, green, green, green, red, red, red, red, red, reset, reset, green], )
        colors.append([yellow, yellow, yellow, reset, red, red, green, red, red, yellow, red, red, yellow, red, green, green], )
        colors.append([reset, yellow, reset, green, red, red, red, red, red, red, red, red, red, red, green, green], )
        colors.append([reset, reset, green, green, green, red, red, red, red, red, red, red, red, red, green, green], )
        colors.append([reset, green, green, green, red, red, red, red, red, red, red, reset, reset, reset, reset, reset], )
        colors.append([reset, green, reset, reset, red, red, red, red, reset, reset, reset, reset, reset, reset, reset, reset], )

        for i in range(len(colors)):
            for j in range(len(colors[i])):
                print_statement+=f"{colors[i][j]}"
                print_statement+=f"{chr(0x2588)*2}"
            print_statement+="\n"

        print(print_statement)
        time.sleep(.5)
        clear_screen()


if __name__=="__main__":
    main()