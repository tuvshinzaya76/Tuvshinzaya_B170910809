from ValuesType import *
class Color(Model):
    id = IntegerField(primary_key=True)
    color = CharField(max_length=255)
    name = CharField(max_length=255)
class ChatType(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length = 255)

class Chat(Model):
    id = CharField(max_length = 100,primary_key=True)
    name = CharField(max_length=255,null = True)
    description = CharField(max_length=255,null = True)
    bg_color = ForeignKey(Color,related_name="bgColor",default=0)
    state = IntegerField()
    type = ForeignKey(ChatType,related_name="typeId",default=0)

