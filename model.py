from os import listdir, getcwd
from os.path import isfile, join
import inspect
import importlib
DB_NAME = "chat_module"
class Field(object):
    primary_key = False
    not_null = None
    max_length = 11
    default = None
    auto_increment = None
    f_type = ""
    foreign_key = False
    def __init__(self,**args):
        for key, value in args.items():
            if key == 'primary_key':
                self.primary_key = value
            elif key == 'not_null':
                self.not_null = value
            elif key == 'max_length':
                self.max_length = value
            elif key == 'default':
                self.default = value
    def getQuery(self):
        query = self.f_type+"("+str(self.max_length)+")"
        if self.not_null:
            query += " NOT NULL"
        if bool(self.default):
            query += " DEFAULT '"+str(self.default)+"'"
        if self.auto_increment:
            query += " AUTO_INCREMENT"
        query+=","
        return query
    def getPrimaryKey(self,att_name):
        query = ""
        if self.primary_key:
            query += "PRIMARY KEY("+str(att_name)+"),"
        return query
class CharField(Field):
    f_type = "VARCHAR"

class IntagerField(Field):
    f_type = "INT"

class ForeignField(Field):
    obj = None
    foreign_key = True
    def __init__(self,obj):
        self.obj = obj
    def getQuery(self):
        return self.obj.findPrimaryKey(self.obj)[1].getQuery()
    def getForeignKeyQuery(self,att_name):
        query = "FOREIGN KEY ('"+str(att_name)+"') REFERENCES Persons('"+str(att_name)+"'), "
        return query

class Person(object):
    id = CharField(max_length = 10, not_null= True,primary_key=True)
    name = CharField(max_length = 255, not_null= True, default="Tuvshinzaya") 
    def findPrimaryKey(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        all_attribute = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        for attr in all_attribute:
            if attr[1].primary_key:
                return attr
        return None
class Model(object):
    name = CharField(max_length = 50, not_null = True, default = "name")
    code = CharField(max_length = 50, not_null = True, default = "code",primary_key= True)
    age = IntagerField(max_length = 10, not_null = True, auto_increment = True)
    tmp = ForeignField(Person)
    def __init__(self,**args):
        attributes = inspect.getmembers(self,lambda a:not(inspect.isroutine(a)))
        all_attribute = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        query = "CREATE TABLE IF EXISTS '"+self.getClassName()+"' ("
        for attr in all_attribute:
            query += "'"+attr[0]+"' "+attr[1].getQuery()+"\n"
        for attr in all_attribute:
            if attr[1].primary_key:
                query += ""+attr[1].getPrimaryKey(attr[0])+"\n"
            if attr[1].foreign_key:
                query += ""+attr[1].getForeignKeyQuery(attr[0])+"\n"
        query+=" ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=56 ;"
        print(query)
    def getClassName(self):
        return self.__class__.__name__
    def findPrimaryKey(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        all_attribute = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        for attr in all_attribute:
            if attr[1].primary_key:
                return attr
        return None

def main():
    st = Model()
if(__name__ == "__main__"):
    main()