import re

from VerilogParser import Parser, Module


def vector_size(name):
    name = name.strip()
    print("Size of : ", name)
    if re.search('^\[', name) or re.search("\[", name):
        left = re.findall('\[(.*):', name)[0]
        right = re.findall('\[.*:(.*)\]', name)[0]
        return abs(int(left) - int(right)) + 1
    return 1


def main():
    p1 = Parser()
    m = p1.parse_modules("testing.txt")
    print(m[3])
    m1 = Module(m[3])  # calling this on idx 0,1 and 2 cause problems from get_non_blocking fucntion please fix ASAP
    print(m1.module_name)
    print(m1.non_blocking)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
