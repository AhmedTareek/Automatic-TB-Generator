import re


class Parser:
    def __init__(self):
        self.modules = []

    def parse_modules(self, file_location):
        """
        it first open the file location and read it the remove the comments from it and search for module-endmodule then
        add them to the modules list
        :param file_location: the location of file in your machine you want to parse
        :return: list of stings
        """
        f = open(file_location, "r")
        s = f.read()
        s = self.__remove_comments(s)
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

    def __remove_comments(self,text):
        """
        it remove all the /* .. */ blocks at first then search for any //... and remove it until the end of line
        :param text: the text you want to remove the comments from
        :return: new string with the comments removed
        """
        x = re.sub(' +', ' ', text)  # to remove extra spaces
        a = re.sub(r"/\*[\s\S]*?\*/", "", x)
        a = re.sub(r"//.*", "", a)
        return a


class Module:
    def __init__(self, module):
        self.module = module
        self.inputs = self.__get_inputs()
        self.outputs = self.__get_outputs()
        self.module_name = self.__get_module_name()
        self.always_blocks = self.__get_always_blocks()
        self.non_blocking = self.__get_non_blocking_assignment()

    def __get_module_name(self):
        """
        this function search for the word after module and return it as its the module name
        :return: string
        """
        module = self.module.split(';')
        operation = module[0]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        module_name = operation[:p1]
        self.module_name = module_name
        return module_name

    def __get_inputs(self,):
        """
        it searches for any appearance of the word input in all the code and get the words after it until it reaches
        [";", "," . ")"]
        :return: list of strings
        """
        module = self.module.split(';')
        operation = module[0]
        others = module[1:]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        p2 = operation.find(')')
        operation = operation[p1 + 1:p2]
        operation = operation.strip(" ")
        operation = operation.split(",")
        inputs = []
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
        others = ";".join(others)
        l1 = re.findall(r"(?<=input)\s+\w+;", others)
        l2 = re.findall(r"(?<=input\s)\s*\w*\s*\[\d:\d]\s+\w+", others)
        for e in l1:
            e = e.strip(" ")
            e = e[:-1]  # to remove the semicolon at the end
            e = re.sub(' +', ' ', e)  # to remove extra spaces
            inputs.append(e)
        for e in l2:
            e = e.strip(" ")
            e = re.sub(' +', ' ', e)  # to remove extra spaces
            inputs.append(e)

        return inputs

    def __get_outputs(self, ):
        """
        it searches for any appearance of the word output in all the code and get the words after it until it reaches
        [";", "," . ")"]
        :return:
        """
        module = self.module.split(';')
        operation = module[0]
        others = module[1:]
        operation = operation.strip(" ")
        operation = operation[6:]
        operation = operation.strip(" ")
        p1 = operation.find('(')
        p2 = operation.find(')')
        operation = operation[p1 + 1:p2]
        operation = operation.strip(" ")
        operation = operation.split(",")
        outputs = []
        for i in range(len(operation)):
            operation[i] = operation[i].strip(" ")
            ans = re.findall("([^\s]+)", operation[i])
            type = ans[0]
            ans = ans[1:]
            rest = ""
            for e in ans:
                rest = rest + e + " "
            if type == "output":
                outputs.append(rest.strip(" "))
        others = ";".join(others)
        l1 = re.findall(r"(?<=output)\s+\w+;", others)
        l2 = re.findall(r"(?<=output\s)\s*\w*\s*\[\d:\d]\s+\w+", others)

        for e in l1:
            e = e.strip(" ")
            e = e[:-1]  # to remove the semicolon at the end
            e = re.sub(' +', ' ', e)  # to remove extra spaces
            outputs.append(e)
        for e in l2:
            e = e.strip(" ")
            e = re.sub(' +', ' ', e)  # to remove extra spaces
            outputs.append(e)

        return outputs

    def __get_always_blocks(self,):
        """
        searches the text for the word always followed by @ and may be spaces in between or not and matches until it
        find the end word
        ******it does not handle if the always is written as a one line without begin end yet******
        :return: list of strings
        """
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

    def __get_non_blocking_assignment(self, ):
        """
        please add doc
        :return:
        """
        module = self.module
        list_of_non_blocking = []
        before = []
        after = []
        val = module.split('<=', 1)
        before.append(val[0].split()[-1])
        after.append(val[1].split(';', 1)[0])
        cond = re.search(r"\<=", val[0]) or re.search(r"\<=", val[1])
        while cond:
            for str in val:
                if re.search(r"\<=", str):
                    val = str.split('<=', 1)
                    before.append(val[0].split()[-1])
                    after.append(val[1].split(';', 1)[0])
                val = str.split('<=', 1)
            cond = re.search(r"\<=", val[0]) or re.search(r"\<=", val[1])
        list_of_non_blocking.append(before)
        list_of_non_blocking.append(after)
        return list_of_non_blocking
