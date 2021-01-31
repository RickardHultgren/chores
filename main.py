#!/usr/bin/env python3
import sqlite3
import os

#******************************** Get DATA *******************************
i=0
def Get_data():
	global i
	global j
	i=0
	#tree.delete(*tree.get_children())
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from stock')
	for row in cursor:
		tr = sys.argv[x+1]', text="Item_"+str(i), values=(row[0],row[1],row[2],row[3]))
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
	db.execute('delete from stock where Product_Id = ?',( PRODUCT_ID_VALUE.get(),))
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
global PRODUCT_ID_VALUE
global PRODUCT_NAME_VALUE
global PRODUCT_CATEGORY
global PRODUCT_BEGIN
global PRODUCT_EXPIRE
global PRODUCT_QUANTITY
global PRODUCT_UNIT
global PRODUCT_PLACE
global i
dblength = i
    for x in range(0, argv_len):
        if sys.argv[x] == "-f":
            CLI_filename = sys.argv[x+1]
            filename = CLI_filename
            filenames.append(filename)
            filecheck = True
        if sys.argv[x] == "-h":
            print ('-h for help\n-f file\n-l list items\n-add add item')
        if sys.argv[x] == "-add":
PRODUCT_ID_VALUE = dblength+1
PRODUCT_NAME_VALUE = sys.argv[x+1]
PRODUCT_CATEGORY = sys.argv[x+2]
PRODUCT_BEGIN = sys.argv[x+3]
PRODUCT_EXPIRE = sys.argv[x+4]
PRODUCT_QUANTITY = sys.argv[x+5]
PRODUCT_UNIT = sys.argv[x+6]
PRODUCT_PLACE = sys.argv[x+7]
Insert_data()
        if sys.argv[x] == "-del":
            PRODUCT_ID_VALUE = sys.argv[x+1]  
            Delete_data()
        if sys.argv[x] == "-update":
PRODUCT_ID_VALUE = sys.argv[x+1]
###identify by name or number?
PRODUCT_NAME_VALUE = sys.argv[x+1]
PRODUCT_CATEGORY = sys.argv[x+2]
PRODUCT_BEGIN = sys.argv[x+3]
PRODUCT_EXPIRE = sys.argv[x+4]
PRODUCT_QUANTITY = sys.argv[x+5]
PRODUCT_UNIT = sys.argv[x+6]
PRODUCT_PLACE = sys.argv[x+7]
Update_data()
        

	
