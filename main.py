#!/usr/bin/env python3
import sqlite3
import os
import sys

#******************************** Get DATA *******************************
i=0
def Get_data():
	global i
	global j
	i=0
	db = sqlite3.connect('test.db')
	cursor = db.execute('select * from stock',[1,2,3,4,5,6,7])
	for row in cursor:
		text="Item_"+str(i)
		values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
		print(text+values)
		i=i+1

def Insert_data():
	db = sqlite3.connect('test.db')
	db.execute('insert into stock (ITEM_Id,ITEM_Name,ITEM_Category,ITEM_Begin,ITEM_Expire,ITEM_Quantity,ITEM_Unit,ITEM_Place) values (?,?,?,?,?,?,?,?,?)',[ITEM_ID_VALUE.get(),ITEM_NAME_VALUE.get(),ITEM_CATEGORY.get(),ITEM_BEGIN.get(),ITEM_EXPIRE.get(),ITEM_QUANTITY.get(),ITEM_UNIT.get(),ITEM_PLACE.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('test.db')
	db.execute('update stock set ITEM_Id = ? ,ITEM_Name = ?,ITEM_Begin = ?,ITEM_Expire = ?  roduct_Quantity = ?,ITEM_Unit = ?,ITEM_Place where ITEM_Id = ?',(ITEM_ID_VALUE.get(),ITEM_NAME_VALUE.get(),ITEM_CATEGORY.get(),ITEM_BEGIN.get(),ITEM_EXPIRE.get(),ITEM_QUANTITY.get(),ITEM_UNIT.get(),ITEM_PLACE.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('test.db')
	db.execute('delete from stock where ITEM_Id = ?',( ITEM_ID_VALUE.get(),))
	db.commit()

ITEM_ID_VALUE = str()
ITEM_NAME_VALUE = str()
ITEM_CATEGORY = str()
ITEM_BEGIN = str()
ITEM_EXPIRE = str()
ITEM_QUANTITY = str()
ITEM_UNIT = str()
ITEM_PLACE = str()
argv_len = len(sys.argv)

if __name__=='__main__':
	#Get_data()
	dblength = i
	for x in range(0, argv_len):
		if sys.argv[x] == "-f":
			CLI_filename = sys.argv[x+1]
			filename = CLI_filename
			filenames.append(filename)
			filecheck = True
		if sys.argv[x] == "-h":
			print ('-h for help\n-f file\n-l list items\n-a add item\n-u update\n-d delete')
		if sys.argv[x] == "-a":
			ITEM_ID_VALUE = str(dblength+1)
			ITEM_NAME_VALUE = raw_input("Name of the item:")
			ITEM_CATEGORY = raw_input("Category of the item:")
			ITEM_BEGIN = raw_input("Start date:")
			ITEM_EXPIRE = raw_input("Expiring date:")
			ITEM_QUANTITY = raw_input("Quantity:")
			ITEM_UNIT = raw_input("Unit:")
			ITEM_PLACE = raw_input("Place:")
			Insert_data()
		if sys.argv[x] == "-d":
			ITEM_ID_VALUE = sys.argv[x+1]  
			Delete_data()
		if sys.argv[x] == "-u":
			ITEM_ID_VALUE = sys.argv[x+1]
			ITEM_NAME_VALUE = raw_input("Name of the item:")
			ITEM_CATEGORY = raw_input("Category of the item:")
			ITEM_BEGIN = raw_input("Start date:")
			ITEM_EXPIRE = raw_input("Expiring date:")
			ITEM_QUANTITY = raw_input("Quantity:")
			ITEM_UNIT = raw_input("Unit:")
			ITEM_PLACE = raw_input("Place:")
			Update_data()
		if sys.argv[x] == "-l":
			Get_data()
	
