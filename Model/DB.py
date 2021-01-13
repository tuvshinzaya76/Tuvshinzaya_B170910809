def createTable(name,fields):
    query = "CREATE TABLE "+str(name)+" ("
    for field in fields:
        query+="'"+field[0]+"' "+field[1].getQuery()+"\n"
    for field in fields:
        if field[1].primary_key:
            query += "" + field[1].getPrimaryKey(field[0]) + "\n"
        if field[1].foreign_key:
            query += "" + field[1].getForeignKeyQuery(field[0]) + "\n"
    query += " ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=56 ;"
    print(query)
    return True