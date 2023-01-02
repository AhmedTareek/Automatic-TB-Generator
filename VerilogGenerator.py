import re


class Variable:
    name = ""
    pinType = ""
    dataType = ""
    size = 0

    def __init__(self, name, pinType, dataType, size):
        self.name = name
        self.pinType = pinType
        self.dataType = dataType
        self.size = size


class Generator:

    Inputs = []
    Outputs = []
    module_name = ""
    time_unit = 1
    time_precision = 1
    def __init__(self, module_name):
        self.module_name = module_name
        in1 = Variable("A", "input", "wire", 1)
        in2 = Variable("B", "input", "wire", 1)
        in3 = Variable("C", "input", "wire", 2)
        in4 = Variable("D", "input", "wire", 2)
        out1 = Variable("F", "output", "wire", 3)
        variables = [in1, in2, in3, in4, out1]
        self.__get_inputs_outputs(variables)

    def __get_inputs_outputs(self, variables):
        for variable in variables:
            if variable.pinType == "input":
                self.Inputs.append(variable)
            elif variable.pinType == "output":
                self.Outputs.append(variable)

    def __write_file(self, module_name):
        filename = module_name + "_tb.v"
        file = open(filename, "w")

        text = "`timescale " + self.time_unit + "ns / " + self.time_precision + "ps\n\n"
        file.write(text)
        text = "module " + module_name + "_tb;\n\n"
        file.write(text)
        text = "    //Inputs\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "    reg " + tb_input.name + ";\n"
            file.write(text)
        text = "\n    //Outputs\n"
        file.write(text)
        for output in self.Outputs:
            text = "    reg " + output.name + ";\n"
            file.write(text)

        text = "\n    //Instantiate the Design Under Test (DUT)"
        text = "    " + self.module_name + " DUT"