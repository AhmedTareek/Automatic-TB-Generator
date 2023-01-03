
class Variable:
    name = ""
    pinType = ""
    dataType = ""
    size = 0

    def __init__(self, name, pin_type, data_type, size):
        self.name = name
        self.pinType = pin_type
        self.dataType = data_type
        self.size = size


class Generator:

    Inputs = []
    Outputs = []
    module_name = ""
    time_unit = 1
    time_precision = 1
    wait = 10

    def __init__(self, module_name):
        self.module_name = module_name
        in1 = Variable("A", "input", "wire", 1)
        in2 = Variable("B", "input", "wire", 1)
        in3 = Variable("C", "input", "wire", 2)
        in4 = Variable("D", "input", "wire", 2)
        out1 = Variable("F", "output", "wire", 3)
        variables = [in1, in2, in3, in4, out1]
        self.__get_inputs_outputs(variables)
        self.__write_file(module_name)

    def __get_inputs_outputs(self, variables):
        for variable in variables:
            if variable.pinType == "input":
                self.Inputs.append(variable)
            elif variable.pinType == "output":
                self.Outputs.append(variable)

    def __write_file(self, module_name):
        filename = module_name + "_tb.v"
        file = open(filename, "w")

        text = "`timescale " + str(self.time_unit) + "ns / " + str(self.time_precision) + "ps\n\n"
        file.write(text)
        text = "module " + module_name + "_tb ();\n\n"
        file.write(text)
        text = "    //Inputs\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "    reg "
            if tb_input.size > 1:
                text += " [" + str(tb_input.size - 1) + ":0] "
            text += tb_input.name + ";\n"
            file.write(text)
        text = "\n    //Outputs\n"
        file.write(text)
        for tb_output in self.Outputs:
            text = "    wire "
            if tb_output.size > 1:
                text += " [" + str(tb_output.size - 1) + ":0] "
            text += tb_output.name + ";\n"
            file.write(text)

        text = "\n    //Instantiate the Design Under Test (DUT)\n"
        file.write(text)
        text = "    " + self.module_name + " DUT (\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "        ." + tb_input.name + "(" + tb_input.name + "),\n"
            file.write(text)
        for tb_output in self.Outputs:
            text = "        ." + tb_output.name + "(" + tb_output.name + "),\n"
            file.write(text)
        text = "    );\n"
        file.write(text)

        text = "\n  initial     //Stimulus\n   begin\n     //Initialize Inputs\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "        " + str(tb_input.name) + " = " + str(0) + ";\n"
            file.write(text)

        bits = 0
        for variable in self.Inputs:
            bits += variable.size

        file.write("\n      //Algorithmic Stimulus Generation\n")
        for i in range(1, 2**bits):
            file.write("\n      #" + str(self.wait) + ";\n")
            temp = i
            for variable in self.Inputs:
                file.write("        " + variable.name + " = " + str(temp % (2**variable.size)) + ";\n")
                temp //= (2**variable.size)

        file.write("        $finish;\n  end\n")

        file.write("    \ninitial   //Analysis\n   begin\n")
        text = "        $display(Time   "
        for variable in self.Inputs:
            text += ", ,\"" + variable.name + "\" "
        for variable in self.Outputs:
            text += ", ,\"" + variable.name + "\" "
        text += ");\n"
        file.write(text)

        text = "        $monitor($time   "
        for variable in self.Inputs:
            text += ", ," + variable.name + " "
        for variable in self.Outputs:
            text += ", ," + variable.name + " "
        text += ");\n"
        file.write(text)

        file.write("\n  end\nendmodule\n")
        file.close()
