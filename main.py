
class Parser:
    def __init__(self):
        self.modules = []

    def parse_modules(self, file_location):
        f = open(file_location, "r")
        s = f.read()
        s = s.split('\n')
        temp = " "
        x = " " + temp.join(s)
        a = 0
        b = 0
        modules = []
        while a >= 0 and b >= 0:
            a = x.find(" module", a)
            b = x.find(" endmodule", a)
            if a >= 0 and b >= 0:
                modules.append(x[a:b])
            a = b
        f.close()
        self.modules = modules
        return modules


def main():
    p1 = Parser()
    p1.parse_modules("testing.txt")
    print(p1.modules)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
