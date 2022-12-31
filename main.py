import re
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
            a = x.find(" module ", a)
            b = x.find(" endmodule ", a)
            if a >= 0 and b >= 0:
                modules.append(x[a:b])
            a = b
        f.close()
        self.modules = modules
        return modules

class Module:
    def __init__(self,module):
        self.module = module
        self.inputs = self.get_inputs()
        self.outputs = self.get_outputs()
        self.module_name = self.get_module_name()

    def get_module_name(self):
        module = self.module.split(';')
        operation = module[0]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        module_name = operation[:p1]
        self.module_name = module_name
        return module_name

    def get_inputs(self,):
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

    def get_outputs(self, ):
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


def main():
    p1 = Parser()
    x = p1.parse_modules("testing.txt")[4]
    op = Module(x)
    print(x)
    op.get_module_name()
    print(op.get_outputs())
    print(op.get_inputs())
    print(op.get_module_name())
    print(op.module_name)
    print(op.inputs)
    print(op.outputs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
