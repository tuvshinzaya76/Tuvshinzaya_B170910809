def createTable(name,fields):
    query = "CREATE TABLE "+str(name)+" ("
    for field in fields:
        if field[1].many_to_many:
            continue
        query+="'"+field[0]+"' "+field[1].getQuery()+"\n"
    for field in fields:
        if field[1].primary_key:
            query += "" + field[1].getPrimaryKey(field[0]) + "\n"
        if field[1].foreign_key:
            query += "" + field[1].getForeignKeyQuery(field[0]) + "\n"
        if field[1].unique:
            query += ""+field[1].getUnique(field[0])+"\n"
    query += " ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=56 ;\n\n"
    # ============MANY TO MANY====================
    for field in fields:
        if field[1].many_to_many:
            table_name = str(field[1].db_table)
            self_pk = findPrimaryKey(fields)
            att_name1 = str(name)+"_id "
            att_name2 = field[1].obj.__name__+"_id "
            query += "CREATE TABLE "+table_name+" (\n"
            query += att_name1 + field[1].obj.findPrimaryKey(field[1].obj)[1].getQuery()+"\n"
            query += att_name2 + str(self_pk[1].getQuery())+"\n"
            query += "PRIMARY KEY("+str(att_name1)+"),\n"
            query += "PRIMARY KEY("+att_name2+"),\n"
            query += "FOREIGN KEY(" + str(str(name) + "_id ") + ") REFERENCES "+str(name)+"("+att_name1+"),\n"
            query += "FOREIGN KEY(" + att_name2 + ") REFERENCES "+field[1].obj.__name__+"("+att_name2+"),\n"
            query += ") ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=56 ;\n\n"
    # ============INDEX====================
    for field in fields:
        if field[1].db_index:
            query+="\n "+field[1].getIndexQuery(field[0])
    print(query)
    return True

def findPrimaryKey(fields):
    for field in fields:
        if field[1].primary_key:
            return field