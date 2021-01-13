import re
class Coverter(object):
    MIGRATION_LIB = "import DB\nfrom ValuesType import *\n"
    TAB = "\t"
    def __init__(self):
        print("=======================================")
    def initialize(self):
        with open("./Model.py") as f:
            text_lines = [line.rstrip('\n') for line in f]
            created_code = ""+self.MIGRATION_LIB
            first = True
            created_code += "class Migration(object):\n"
            created_code += self.TAB+"options = ["
            for line in text_lines:
                if "class " in line:
                    if first == False :
                        created_code += "]),"
                    first = False
                    created_code += "DB.createTable('"+self.findClassName(line)+"',["
                if len(line) > 2:
                    if line[0] == "\t" and line[1] != "\t" and (bool(line in "def") == False):
                        print(line)
                    elif line[0] == " " and line[1] == " " and line[2] == " " and line[3] == " " and line[4]!= " " and ("def" in line.split()) == False :
                        attr = self.findAttribute(line)
                        created_code += "\n"+self.TAB+self.TAB+"('"+str(attr[0])+"',"+str(attr[1])+"),"
            created_code += "\n"+self.TAB+self.TAB+"])\n"+self.TAB+"]"
            self.createFile(created_code)

    def findClassName(self,text):
        text = re.sub("class", "", text, 1)
        result = ""
        import string
        for letter in text:
            if letter in string.ascii_letters or letter == " ":
                result += letter
            else:
                break
        return result
    def findAttribute(self,text):
        text = text.replace(" ","")
        text = text.replace("\t","")
        text = text.split("=",1)
        return tuple(text)
    def createFile(self, text):
        import datetime
        filename = "migration/"+str(datetime.datetime.now().strftime("%f"))+".py"
        file = open(filename, "x")
        file.write(text)
        file.close()
        import importlib.util
        spec = importlib.util.spec_from_file_location("module.name",filename)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        fields = foo.Migration.options
        for field in fields:
            print(field)