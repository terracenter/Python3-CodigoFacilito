import sys

#El primer argumento es el mismo Script
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1] == 'help':
            print("SOS")
        else:
            print(sys.argv[1])