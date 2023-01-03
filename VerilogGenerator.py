
class Port:
    name = ""
    type = ""
    size = 0
    direction = ""

    def __init__(self, name, direction, size, type):
        self.name = name
        self.type = type
        self.direction = direction
        self.size = size


class Generator:

    Inputs = []
    Outputs = []
    module_name = ""
    time_unit = 1
    time_precision = 1
    wait = 10
    number_of_tests = 1000000

    def __init__(self, module_name):
        self.module_name = module_name
        in1 = Port("A", "input", 1, "wire")
        in2 = Port("B", "input", 1, "wire")
        in3 = Port("C", "input", 10, "wire")
        in4 = Port("D", "input", 10, "wire")
        out1 = Port("F", "output", 11, "wire")
        variables = [in1, in2, in3, in4, out1]
        self.__get_inputs_outputs(variables)
        self.__write_file(module_name)

    def __get_inputs_outputs(self, variables):
        for variable in variables:
            if variable.direction == "input":
                self.Inputs.append(variable)
            elif variable.direction == "output":
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

        bits = 0
        for variable in self.Inputs:
            bits += variable.size
        file.write("\n    //Sequence\n    reg [" + str(bits - 1) + ":0] sequence = 0;\n")

        text = "\n    //Instantiate the Design Under Test (DUT)\n"
        file.write(text)
        text = "    " + self.module_name + " DUT (\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "        ." + tb_input.name + "(" + tb_input.name + "),\n"
            file.write(text)
        for tb_output in self.Outputs:
            if tb_output.name != self.Outputs[-1].name:
                text = "        ." + tb_output.name + "(" + tb_output.name + "),\n"
            else:
                text = "        ." + tb_output.name + "(" + tb_output.name + ")\n"
            file.write(text)
        text = "    );\n"
        file.write(text)

        text = "\n  initial     //Stimulus\n  begin\n      //Initialize Inputs\n"
        file.write(text)
        for tb_input in self.Inputs:
            text = "        " + str(tb_input.name) + " = " + str(0) + ";\n"
            file.write(text)

        if bits < 20:
            file.write("\n      //Directed Stimulus Generation\n"
                       "      repeat(" + str(2**bits + 1) + ")\n      begin\n")
            file.write("          #" + str(self.wait) + ";\n")
            start = 0
            end = -1
            for variable in self.Inputs:
                end += variable.size
                file.write("            " + variable.name + " = sequence[" + str(end) + ":" + str(start) + "];\n")
                start = end + 1
            file.write("            sequence = sequence + 1;\n      end\n")

            # for i in range(1, 2**bits + 1):
            #     file.write("\n      #" + str(self.wait) + ";\n")
            #     temp = i
            #     for variable in self.Inputs:
            #         file.write("        " + variable.name + " = " + str(temp % (2**variable.size)) + ";\n")
            #         temp //= (2**variable.size)
        else:
            file.write("\n      //Randomized Stimulus Generation\n"
                       "    repeat(" + str(self.number_of_tests) + ")\n      begin\n")
            file.write("          #" + str(self.wait) + ";\n")
            for variable in self.Inputs:
                file.write("            " + variable.name + " = $random(seed);\n")
            file.write("        end\n")

        file.write("\n      #" + str(self.wait) + ";\n")
        file.write("      $finish;\n  end\n")

        file.write("    \ninitial   //Analysis\n   begin\n")
        text = "        $display(\"             Time\"   "
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
