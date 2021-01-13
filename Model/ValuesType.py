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

class IntegerField(Field):
    f_type = "INT"

class ForeignKey(Field):
    obj = None
    foreign_key = True
    def __init__(self,obj):
        self.obj = obj
    def getQuery(self):
        return self.obj.findPrimaryKey(self.obj)[1].getQuery()
    def getForeignKeyQuery(self,att_name):
        query = "FOREIGN KEY ('"+str(att_name)+"') REFERENCES Persons('"+str(att_name)+"'), "
        return query