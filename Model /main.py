import sys,inspect
from Model import *
import DB
def getAllAttribute(obj):
    attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
    arr = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
    return arr

def convertToFormat(class_list):
    result = []
    for name, obj in class_list:
        try:
            if inspect.isclass(obj) and obj.getClassType(obj) == 'Model' and name != 'Model':
                tmp = {"name": name,"attribute":None}
                tmp["attribute"] = getAllAttribute(obj)
                result.append(tmp)
        except:
            v = "Model oos udamshsan table bish baina"
    return result
if __name__ == '__main__':
    all_class = inspect.getmembers(sys.modules[__name__])
    table_list = convertToFormat(all_class)
    for table in table_list:
        DB.createTable(table["name"],table["attribute"])


