#!/usr/bin/env python3
import sqlite3
import os

#******************************** Get DATA *******************************
i=0
def Get_data():
	global i
	global j
	i=0
	tree.delete(*tree.get_children())
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from stock')
	for row in cursor:
		tree.insert('', 'end', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3]))
		i=i+1

def Insert_data():
	db = sqlite3.connect('test.db')
	db.execute('insert into stock (Product_Id,Product_Name,Product_Category,Product_Begin,Product_Expire,Product_Quantity,Product_Unit,Product_Place) values (?,?,?,?,?,?,?,?,?)',[PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_CATEGORY.get(),PRODUCT_BEGIN.get(),PRODUCT_EXPIRE.get(),PRODUCT_QUANTITY.get(),PRODUCT_UNIT.get(),PRODUCT_PLACE.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('test.db')
	db.execute('update stock set Product_Id = ? ,Product_Name = ?,Product_Begin = ?,Product_Expire = ?  roduct_Quantity = ?,Product_Unit = ?,Product_Place where Product_Id = ?',(PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_CATEGORY.get(),PRODUCT_BEGIN.get(),PRODUCT_EXPIRE.get(),PRODUCT_QUANTITY.get(),PRODUCT_UNIT.get(),PRODUCT_PLACE.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('test.db')
	db.execute('delete from stock where Product_Id = ?',(PRODUCT_CATEGORY.get(),))
	db.commit()

global PRODUCT_ID_VALUE
global PRODUCT_NAME_VALUE
global PRODUCT_CATEGORY
global PRODUCT_BEGIN
global PRODUCT_EXPIRE
global PRODUCT_QUANTITY
global PRODUCT_UNIT
global PRODUCT_PLACE

if __name__=='__main__':
    for x in range(0, argv_len):
        if sys.argv[x] == "-f":
            CLI_filename = sys.argv[x+1]
            filename = CLI_filename
            filenames.append(filename)
            filecheck = True
        if sys.argv[x] == "-h":
            print ('-h for help\n-f file\n-l list items\n-a add item')
        if sys.argv[x] == "-a":
            mode_exe = True
        if sys.argv[x] == "-l":
            mode_graph = True                    
        if sys.argv[x] == "-statements":
            mode_state = True    
        if sys.argv[x] == "-steps":
            steps = int(sys.argv[x+1])
        if sys.argv[x] == "-start":
            starts.append(sys.argv[x+1])

