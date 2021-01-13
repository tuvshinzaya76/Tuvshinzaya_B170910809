from ValuesType import *
class Model(object):
    name = CharField(max_length=50, not_null=True, default="name")
    code = CharField(max_length=50, not_null=True, default="code", primary_key=True)
    age = IntegerField(max_length=10, not_null=True, auto_increment=True)
    def getClassName(self):
        return self.__class__.__name__
class Color(object):
    id = IntegerField(primary_key=True)
    color = CharField(max_length=255)
    name = CharField(max_length=255)
class ChatType(object):
    id = IntegerField(primary_key=True)
    name = CharField(max_length = 255)

class Chat(object):
    id = CharField(max_length = 100,primary_key=True)
    name = CharField(max_length=255,null = True)
    description = CharField(max_length=255,null = True)
    bg_color = ForeignKey(Color,related_name="bgColor",default=0)
    state = IntegerField()
    type = ForeignKey(ChatType,related_name="typeId",default=0)

