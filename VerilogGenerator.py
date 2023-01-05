
class Generator:

    Inputs = []
    Outputs = []
    module_name = ""
    time_unit = 1
    time_precision = 1
    wait = 10
    number_of_tests = 100000
    filepath = ""

    def __init__(self, module_name, ports, filepath):
        self.module_name = module_name
        self.__get_inputs_outputs(ports)
        self.filepath = filepath
        self.__write_file(module_name)

    def __get_inputs_outputs(self, ports):
        for port in ports:
            if port.direction == "input":
                self.Inputs.append(port)
            elif port.direction == "output":
                self.Outputs.append(port)

    def __write_file(self, module_name):
        filename = self.filepath + module_name + "_tb.v"
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
        for port in self.Inputs:
            bits += port.size
        if bits < 17:
            file.write("\n    //Sequence\n    reg [" + str(bits - 1) + ":0] sequence = 0;\n")
        else:
            file.write("\n    //Randomization\n    integer seed = 5;\n")

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

        if bits < 17:       # generate directed testbench if input bits are less than 17 (less than 100000 combination)
            file.write("\n      //Directed Stimulus Generation\n"
                       "      repeat(" + str(2**bits + 1) + ")\n      begin\n")
            file.write("          #" + str(self.wait) + ";\n")
            start = 0
            end = -1
            for port in self.Inputs:
                end += port.size
                file.write("            " + port.name + " = sequence[" + str(end) + ":" + str(start) + "];\n")
                start = end + 1
            file.write("            sequence = sequence + 1;\n      end\n")
        else:       # if input bits are more than 16 generate randomized test cases instead
            file.write("\n      //Randomized Stimulus Generation\n"
                       "    repeat(" + str(self.number_of_tests) + ")\n      begin\n")
            file.write("          #" + str(self.wait) + ";\n")
            for port in self.Inputs:
                file.write("            " + port.name + " = $random(seed);\n")
            file.write("        end\n")

        file.write("\n      //Testing design behaviour against don't care inputs\n")
        file.write("          #" + str(self.wait) + ";\n")
        for port in self.Inputs:
            file.write("            " + port.name + " = 1'bX;\n")

        file.write("\n      #" + str(self.wait) + ";\n")
        file.write("      $finish;\n  end\n")

        file.write("    \ninitial   //Analysis\n   begin\n")
        text = "        $display(\"             Time\"   "
        for port in self.Inputs:
            text += ", ,\"" + port.name + "\" "
        for port in self.Outputs:
            text += ", ,\"" + port.name + "\" "
        text += ");\n"
        file.write(text)

        text = "        $monitor($time   "
        for port in self.Inputs:
            text += ", ," + port.name + " "
        for port in self.Outputs:
            text += ", ," + port.name + " "
        text += ");\n"
        file.write(text)

        file.write("\n  end\nendmodule\n")
        file.close()
