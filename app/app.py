#!/usr/bin/env python3

def main():
    print("Hello world !")
    n1 = 1
    n2 = 2
    n3 = add(n1, n2)
    result = "{} + {} = {}".format(n1, n2, n3)
    print(result)

def add(n1, n2):
    return n1 + n2

if __name__ == '__main__':
    main()