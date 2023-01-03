import re

from VerilogParser import Parser, Module


def main():
    p1 = Parser("testing.txt")
    for m in p1.modules:
        m1 = Module(m)
        a = m1.assign_statements
        for i in a:
            print(i.text)
            print(i.delay)
            print(i.left_hand_side, i.rigt_hand_side)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
