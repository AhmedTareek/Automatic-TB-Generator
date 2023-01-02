import re

from VerilogParser import Parser, Module


def main():
    p1 = Parser()
    m = p1.parse_modules("testing.txt")
    for i in range(len(m)):
        m1 = Module(m[i])
        print(m1.name)
        for j in m1.always_blocks:
            print(j.sensitivity_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
