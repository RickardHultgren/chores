#!/usr/bin/env python3
import sqlite3
import os
import sys

#******************************** Get DATA *******************************
i=0
ITEM_ID = str()
ITEM_NAME_VALUE = str()
ITEM_CATEGORY = str()
ITEM_BEGIN = str()
ITEM_EXPIRE = str()
ITEM_QUANTITY = str()
ITEM_UNIT = str()
ITEM_PLACE = str()
argv_len = len(sys.argv)

#conn  = sqlite3.connect('test.db')
#c = conn.cursor()

def Get_data():
	global i
	global j
	i=0
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	cursor = conn.execute("SELECT * FROM Things") 
	for row in cursor: 
	#	print row, 
  
	#cursor = db.execute('select * from stock',[1,2,3,4,5,6,7])
	#for row in c.execute('SELECT * FROM stocks ORDER BY item_name'):
		print(row)
		#i=i+1

def Insert_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c

	conn  = sqlite3.connect('test.db')
	c = conn.cursor()	
	i = 0
	try:
		cursor = conn.execute("SELECT * FROM Things") 
		for row in cursor: 
			i = i + 1
		ITEM_ID = i
	except:
		pass
	c.execute('CREATE TABLE IF NOT EXISTS Things (item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_unit text,item_place text)')
	c.execute("INSERT INTO Things (item_id,item_name,item_category,item_begin,item_expire,item_quantity,item_unit,item_place) VALUES(?, ?, ?, ?, ?, ?, ?, ? )", (ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE))
	#c.execute("INSERT INTO stock VALUES ( ITEM_ID , ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE )")
	conn.commit()

def Update_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	c.execute('UPDATE Things SET item_name = ?, item_category = ?, item_begin = ?,item_expire = ?, product_quantity = ?,item_unit = ?,item_place = ? WHERE item_id = ?', (ITEM_NAME_VALUE , ITEM_CATEGORY , ITEM_BEGIN , ITEM_EXPIRE , ITEM_QUANTITY , ITEM_UNIT , ITEM_PLACE,  ITEM_ID))
	conn.commit()

def Delete_data():
	conn  = sqlite3.connect('test.db')
	c = conn.cursor()
	#global c
	c.execute('delete from stock where ITEM_Id = ?',( ITEM_ID_VALUE.get(),))
	conn.commit()

if __name__=='__main__':
	#Get_data()
	#global c
	#conn  = sqlite3.connect('test.db')
	#c = conn.cursor()	
	#c.execute('CREATE TABLE IF NOT EXISTS RecordONE (item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_Unit text,item_place text))')
	#try:
	#	c.execute('''CREATE TABLE stocks
	#		(item_id text,item_name text,item_category text,item_begin text,item_expire text,item_quantity text,item_Unit text,item_place text)''')
	#except:
	#	pass
	#conn.commit
	#conn.close
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
			ITEM_ID = str(dblength+1)
			try:
				ITEM_NAME_VALUE = input("Name of the item:")
				ITEM_CATEGORY = input("Category of the item:")
				ITEM_BEGIN = input("Start date:")
				ITEM_EXPIRE = input("Expiring date:")
				ITEM_QUANTITY = input("Quantity:")
				ITEM_UNIT = input("Unit:")
				ITEM_PLACE = input("Place:")
			except:
				ITEM_NAME_VALUE = raw_input("Name of the item:")
				ITEM_CATEGORY = raw_input("Category of the item:")
				ITEM_BEGIN = raw_input("Start date:")
				ITEM_EXPIRE = raw_input("Expiring date:")
				ITEM_QUANTITY = raw_input("Quantity:")
				ITEM_UNIT = raw_input("Unit:")
				ITEM_PLACE = raw_input("Place:")
			Insert_data()			
		if sys.argv[x] == "-d":
			ITEM_ID = sys.argv[x+1]  
			Delete_data()
		if sys.argv[x] == "-u":
			ITEM_ID = sys.argv[x+1]
			try:
				ITEM_NAME_VALUE = input("Name of the item:")
				ITEM_CATEGORY = input("Category of the item:")
				ITEM_BEGIN = input("Start date:")
				ITEM_EXPIRE = input("Expiring date:")
				ITEM_QUANTITY = input("Quantity:")
				ITEM_UNIT = input("Unit:")
				ITEM_PLACE = input("Place:")
			except:
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
	

	

	

	

	
