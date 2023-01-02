import re
from VerilogParser import Parser, Module

def main():
    p1 = Parser()
    m = p1.parse_modules("testing.txt")
    m1 = Module(m[1])  # calling this on idx 0,1 and 2 cause problems from get_non_blocking fucntion please fix ASAP
    #print(m[1])
    print(m1.inputs)
    print(m1.outputs)
    print(m1.variables, end = ' ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
