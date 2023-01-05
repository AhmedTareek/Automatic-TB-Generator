import re

from VerilogParser import Parser, Module, If_statement
from VerilogGenerator import Generator

def main():
    p1 = Parser("DecMuxAdd1.v")
    mod = p1.modules
    print(mod[0])
    m1 = Module(mod[0])
    mod_name = m1.name
    ports = m1.variables
    g1 = Generator(mod_name,ports)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
