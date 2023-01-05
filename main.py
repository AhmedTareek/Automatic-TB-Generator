import re
from VerilogParser import Parser, Module, If_statement
from VerilogGenerator import Generator


def main():
    filepath = input("Enter The path of the .v file: ")
    p1 = Parser(filepath)
    index = filepath.rfind('\\') + 1
    filepath = filepath[:index]
    mod = p1.modules
    for module in mod:
        print(module)
        m1 = Module(module)
        mod_name = m1.name
        ports = m1.variables
        Generator(mod_name, ports, filepath)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
