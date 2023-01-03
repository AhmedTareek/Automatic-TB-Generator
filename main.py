from VerilogParser import Parser, Module
from VerilogGenerator import Generator


def main():
    p1 = Parser("testing.txt")
    s = p1.text
    print(s)
    g = Generator("test")

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
