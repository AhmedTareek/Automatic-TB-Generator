from VerilogParser import Parser, Module
from VerilogGenerator import Generator


def main():
    p1 = Parser()
    m = p1.parse_modules("testing.txt")
    for i in range(6):
        m1 = Module(m[i])
        for var in m1.variables:
            print(var.name,end=' ')
            print(var.direction, end=' ')
        print("")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
