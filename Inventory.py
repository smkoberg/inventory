"""
Enter Mode:
    Add Products (Add to stock)
    Remove Products (Sell / Give Away)
    Update Inventory
"""
from winsound import Beep
import os
import sqlite3

Freq = 1000
Dur = 175

def beep():
	Beep(Freq, Dur)

def clear():
	os.system('cls')
	
def add_products():

	status = ""
	qty = 0
	
	while status != "x":
		
		print "Add item to the DB: ", qty
		print "(press 'x' to exit)"
		
		connect = sqlite3.connect("inventory.db")
		
		sql = connect.cursor()
		
		status = raw_input("Enter an item ID: ")
		
		sql.execute("SELECT * FROM items WHERE item_id = '%s'" %(status))
		
		if sql.fetchall():
		
			sql.execute("UPDATE items SET item_qty = item_qty + 1 WHERE item_id = '%s'" %(status))
		
			connect.commit()
			connect.close()
			
			beep()
		
			qty += 1
		
		else:
			
			clear()
			print "Item ID %s doesn't exist in the database.\nPlease create it before adding." %(status)
			
			raw_input("Press Enter to continue")
		
		clear()
		
	clear()

def remove_products():
	
	status = ""
	
	while status == "":
		
		print "Removing Products from the DB"
		
		status = raw_input("Enter an Option")
	
	clear()

def update_inventory():
	
	status = ""
	
	while status == "":
		
		print "Updating Inventory"
		
		status = raw_input("Enter an Option")
	
	clear()

def enter_category():
	
	cat = raw_input("Enter Item Category: ")
	
	clear()
	
	return cat

def enter_description():
	
	desc = raw_input("Enter Item Description: ")
	
	clear()
	
	return desc

def enter_id():
	
	id = raw_input("Enter Unique ID number (UPC): ")
	
	clear()
	
	return id

def enter_price():
	
	price = raw_input("Enter item cost (nn.nn): $")
	
	clear()
	
	return price

def enter_size():
	
	size = raw_input("Enter item size: ")
	
	clear()
	
	return size

def id_exists(id):
		
		clear()
		
		print "ID %s already exists in Database" %(id)
		
		raw_input("Press Enter to continue")
		
		clear()

def add_new_item(cat, desc, size, id, price):
	
	connect = sqlite3.connect("inventory.db")
	
	sql = connect.cursor()
	try:	
		
		sql.execute("INSERT INTO items VALUES ('%s', '%s', '%s', '%s', 0, '%s')" %(id, desc, size, cat, price))
		
		connect.commit()
		connect.close()
	
	except sqlite3.IntegrityError:
		
		id_exists(id)
		
def create_item():
	
	status = ""
	item_category = ""
	item_id_number = ""
	item_description = ""
	item_price = ""
	item_size = ""
	
	while status != "x":
		
		print "Creating a New Item.\n('x' to exit)\n"
		
		print "1 - Enter Item Category: ", str(item_category)
		print "2 - Enter Item Description: ", str(item_description)
		print "3 - Enter Item Size: ", str(item_size)
		print "4 - Enter Item ID number (UPC): ", str(item_id_number)
		print "5 - Enter Item Sale Price: $", str(item_price)
		print "6 - Add new Item to the database."
		
		status = raw_input("\nEnter an Option: ")
		
		if status == "1":
			clear()
			item_category = enter_category()
		elif status == "2":
			clear()
			item_description = enter_description()
		elif status == "3":
			clear()
			item_size = enter_size()
		elif status == "4":
			clear()
			item_id_number = enter_id()
		elif status == "5":
			clear()
			item_price = enter_price()
		elif status == "6":
			clear()
			add_new_item(item_category, item_description, item_size, item_id_number, item_price)
	
	clear()

def check_item():
	
	status = ""
	
	while status != "x":
		
		print "Enter ID to check for in the database:\n('x' to exit)"
		
		status = raw_input("ID #: ")
		
		connect = sqlite3.connect("inventory.db")
		
		sql = connect.cursor()
		try:	
		
			sql.execute("SELECT * FROM items WHERE item_id = %s" %(status))
			
			results = sql.fetchall()
			
			for i in results:
				print unicode(i)
			
			connect.close()
		
		except:
			print "Somethings wrong"
			
def main():

	status = ""

	while status != "x":
		clear()
		print "Please select a function:\n"
		print "1 - Add Products."
		print "2 - Remove Products."
		print "3 - Update Inventory."
		print "4 - Create New Item."
		print "5 - Check ID.\n"
		status = raw_input("Choose Wisely: ")

		if status == "1":
			clear()
			Beep(Freq, Dur)
			add_products()
		elif status == "2":
			clear()
			remove_products()
		elif status == "3":
			clear()
			update_inventory()
		elif status == "4":
			clear()
			create_item()
		elif status == "5":
			clear()
			check_item()
			

main()

clear()
