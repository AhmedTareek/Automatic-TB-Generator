from VerilogParser import Parser, Module
from VerilogGenerator import Generator


def main():
    p1 = Parser("testing.txt")
    s = p1.text
    print(s)
    g = Generator("test")

    # p1 = Parser()
    # m = p1.parse_modules("testing.txt")
    # m1 = Module(m[10])
    # print(m1.cases)

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
