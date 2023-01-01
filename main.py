import re


class Parser:
    def __init__(self):
        self.modules = []

    def parse_modules(self, file_location):
        f = open(file_location, "r")
        s = f.read()
        s = s.split('\n')
        temp = " "
        x = " " + temp.join(s) + " "
        a = 0
        b = 0
        modules = []
        while a >= 0 and b >= 0:
            a = x.find(" module ", a)
            b = x.find(" endmodule ", a)
            if a >= 0 and b >= 0:
                modules.append(x[a:b])
            a = b
        f.close()
        self.modules = modules
        return modules


class Module:
    def __init__(self, module):
        self.module = module
        self.inputs = self.__get_inputs()
        self.outputs = self.__get_outputs()
        self.module_name = self.__get_module_name()
        self.always_blocks = self.__get_always_blocks()

    def __get_module_name(self):
        module = self.module.split(';')
        operation = module[0]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        module_name = operation[:p1]
        self.module_name = module_name
        return module_name

    def __get_inputs(self, ):
        module = self.module.split(';')
        operation = module[0]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        p2 = operation.find(')')
        operation = operation[p1 + 1:p2]
        operation = operation.strip(" ")
        operation = operation.split(",")
        inputs = []
        outputs = []
        for i in range(len(operation)):
            operation[i] = operation[i].strip(" ")
            ans = re.findall("([^\s]+)", operation[i])
            type = ans[0]
            ans = ans[1:]
            rest = ""
            for e in ans:
                rest = rest + e + " "
            if type == "input":
                inputs.append(rest.strip(" "))
            else:
                outputs.append(rest.strip(" "))
        self.inputs = inputs
        return inputs

    def __get_outputs(self, ):
        module = self.module.split(';')
        operation = module[0]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        p2 = operation.find(')')
        operation = operation[p1 + 1:p2]
        operation = operation.strip(" ")
        operation = operation.split(",")
        inputs = []
        outputs = []
        for i in range(len(operation)):
            operation[i] = operation[i].strip(" ")
            ans = re.findall("([^\s]+)", operation[i])
            type = ans[0]
            ans = ans[1:]
            rest = ""
            for e in ans:
                rest = rest + e + " "
            if type == "input":
                inputs.append(rest.strip(" "))
            else:
                outputs.append(rest.strip(" "))
        self.outputs = outputs
        return outputs

    def __get_always_blocks(self, ):
        list_of_always_blocks = []
        module = self.module
        ans = re.search(r"(always)\s*@", module)
        while ans:
            module = module[ans.start():] + " "
            start = module.find(" begin ")
            a = module.find(" begin ", start)
            b = module.find(" end ")
            temp = start + 1
            u = start + 1
            while b > a and (a >= 0):
                a = module.find(" begin ", u)  # match every begin and end until you find end without a begin
                u = a + 1
                if a == -1: break
                b = module.find(" end ", temp)
                temp = b + 1
            list_of_always_blocks.append(module[:b + 4])
            module = module[b + 4:]
            ans = re.search(r"(always)\s*@", module)
        return list_of_always_blocks


def main():
    p1 = Parser()
    x = p1.parse_modules("testing.txt")[3]
    m1 = Module(x)
    print(m1.module_name)
    print(m1.inputs)
    print(m1.outputs)
    print(m1.always_blocks)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
