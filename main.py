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
	db.execute('insert into stock (Product_Id,Product_Name,Sell_Price,Quantity) values (?,?,?,?)',[PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get()])
	db.commit()

def Update_data():
	db = sqlite3.connect('test.db')
	db.execute('update stock set Product_Id = ? ,Product_Name = ?,Sell_Price = ?,Quantity = ?  where Product_Id = ?',(PRODUCT_ID_VALUE.get(),PRODUCT_NAME_VALUE.get(),PRODUCT_PRICE_VALUE.get(),PRODUCT_QUANTITY_VALUE.get(),PRODUCT_ID_VALUE.get()))
	db.commit()

def Delete_data():
	db = sqlite3.connect('test.db')
	db.execute('delete from stock where Product_Id = ?',(PRODUCT_ID_VALUE.get(),))
	db.commit()


global PRODUCT_QUANTITY_VALUE
global PRODUCT_ID_VALUE
global PRODUCT_PRICE_VALUE
global PRODUCT_NAME_VALUE


if __name__=='__main__':
    for x in range(0, argv_len):
        if sys.argv[x] == "-f":
            CLI_filename = sys.argv[x+1]
            filename = CLI_filename
            filenames.append(filename)
            filecheck = True
        if sys.argv[x] == "-h":
            print ('-h for help\n-f file\n-graph\n-start "start node"\n-steps amount of steps')
        if sys.argv[x] == "-exe":
            mode_exe = True
        if sys.argv[x] == "-graph":
            mode_graph = True                    
        if sys.argv[x] == "-statements":
            mode_state = True    
        if sys.argv[x] == "-steps":
            steps = int(sys.argv[x+1])
        if sys.argv[x] == "-start":
            starts.append(sys.argv[x+1])
    # Execute functions that are connected to the arguments:
    if filecheck == True:
        lexer()
    else:
        print("Please add file names.")

