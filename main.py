import re

from VerilogParser import Parser, Module


def main():
    p1 = Parser()
    m = p1.parse_modules("testing.txt")
    a = m[3]
    x = Module(a)
    print(x.name)
    x = x.always_blocks[1].text
    print(re.findall(r"if\s*\(.+?\)\s*begin.*?end", x))
    y = re.search(r"if\s*\(.+?\)\s*begin", a)
    if y:
        print(y.start())
        print(a[y.start():])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
