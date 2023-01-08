from sys import argv
from src import power

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    file = argv[1]
    p = power.Power(file)
    p.readFile()

if __name__ == "__main__":
    main()