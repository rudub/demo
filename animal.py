import sys


def dog():
    print('woof')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        print('hello')

if __name__ == '__main__':
   main()
