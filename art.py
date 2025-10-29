from colors import Colors
print("Hello")
print(f"{Colors.RED}This is red text{Colors.RESET}")
print(f"{Colors.BLUE}{chr(0x2588)*3}{Colors.RESET}")
print(" ")

#Using a 2d array, try to recreate something like this in the terminal:
#https://www.clipartmax.com/png/middle/133-1334472_mario-clipart-8bit-super-mario-8-bit.png

#Note: You get ONE print statement


def main():
    colors=[
        
    ]
    
    print_statement=""

    colors.append([Colors.RESET, Colors.RESET, Colors.RESET, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RESET, Colors.RESET, Colors.RESET, Colors.RESET], )
    colors.append([Colors.RESET, Colors.RESET, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RESET], )
    colors.append([Colors.RESET, Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.GREEN, Colors.YELLOW, Colors.RESET, Colors.RESET, Colors.RESET], )
    colors.append([Colors.RESET, Colors.GREEN, Colors.YELLOW, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.RESET], )
    colors.append([Colors.RESET, Colors.GREEN, Colors.YELLOW, Colors.GREEN, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW], )
    colors.append([Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RESET], )
    colors.append([Colors.RESET, Colors.RESET, Colors.RESET, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.RESET, Colors.RESET], )
    colors.append([Colors.RESET, Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.RED, Colors.GREEN, Colors.GREEN, Colors.RED, Colors.GREEN, Colors.GREEN, Colors.RESET, Colors.RESET], )
    colors.append([Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RED, Colors.GREEN, Colors.GREEN, Colors.RED, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RESET], )
    colors.append([Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN], )
    colors.append([Colors.YELLOW, Colors.YELLOW, Colors.GREEN, Colors.RED, Colors.YELLOW, Colors.RED, Colors.RED, Colors.YELLOW, Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.YELLOW], )
    colors.append([Colors.YELLOW, Colors.YELLOW, Colors.YELLOW, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.YELLOW, Colors.YELLOW, Colors.YELLOW], )
    colors.append([Colors.YELLOW, Colors.YELLOW, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.YELLOW, Colors.YELLOW], )
    colors.append([Colors.RESET, Colors.RESET, Colors.RED, Colors.RED, Colors.RED, Colors.RESET, Colors.RESET, Colors.RED, Colors.RED, Colors.RED, Colors.RESET, Colors.RESET], )
    colors.append([Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RESET, Colors.RESET, Colors.RESET, Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RESET], )
    colors.append([Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.RESET, Colors.RESET, Colors.RESET, Colors.RESET, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN], )

    for i in range(len(colors)):
        for j in range(len(colors[i])):
            print_statement+=f"{colors[i][j]}"
            print_statement+=f"{chr(0x2588)*2}"
        print_statement+="\n"

    print(print_statement)


if __name__=="__main__":
    main()