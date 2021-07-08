import sys

def cat():
    print('Meow!')

def main():
    if sys.argv[1]=='cat':
        cat()
    else:
        print('hello')

if __name__ == '__main__':
   main()
