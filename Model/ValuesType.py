import inspect
class Field(object):
    primary_key = False
    not_null = None
    max_length = 11
    default = None
    auto_increment = None
    f_type = ""
    foreign_key = False
    db_index = False
    related_name = ""
    obj = None
    def __init__(self,obj = None,**args):
        if bool(obj):
            self.obj = obj
        for key, value in args.items():
            if key == 'primary_key':
                self.primary_key = value
            elif key == 'not_null':
                self.not_null = value
            elif key == 'max_length':
                self.max_length = value
            elif key == 'default':
                self.default = value
            elif key == 'db_index':
                self.db_index = value
            elif key == 'related_name':
                self.related_name = value

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
    def getIndexQuery(self,att_name):
        query = "CREATE INDEX '"
        query += "idx_"+str(att_name)+"' ON "+str(self.__class__.__name__)+"("+str(att_name)+")"
        return query
class CharField(Field):
    f_type = "VARCHAR"

class IntegerField(Field):
    f_type = "INT"

class ForeignKey(Field):
    obj = None
    foreign_key = True
    def getQuery(self):
        return self.obj.findPrimaryKey(self.obj)[1].getQuery()
    def getForeignKeyQuery(self,att_name):
        query = "FOREIGN KEY ('"+str(att_name)+"') REFERENCES Persons('"+str(att_name)+"'), "
        return query

class Model(object):
    def getClassName(self):
        return self.__class__.__name__
    def findPrimaryKey(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        all_attribute = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        for attr in all_attribute:
            if attr[1].primary_key:
                return attr
        return None