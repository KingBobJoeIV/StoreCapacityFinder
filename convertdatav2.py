import csv, sqlite3

def updateDB():
	con = sqlite3.connect("store.db") # change to 'sqlite:///your_filename.db'
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS my_table (StoreName,Type,x,y,TotalCapacitance,NumPeople,RateofTraffic);") # use your column names here

	with open('store.csv','r') as fin: # `with` statement available in 2.5+
	    # csv.DictReader uses first line in file for column headings by default
	    dr = csv.DictReader(fin) # comma is default delimiter
	    #to_db = [(i['StoreName'], i['Type'],i['x'],i['y'],i['TotalCapacitance'],i['NumPeople'],i['RateofTraffic']) for i in dr]
	    for i in dr:
	    	#print(i['NumPeople'], i['StoreName'], i['Type'])
	    	sql_update_query = """UPDATE my_table SET NumPeople = """ + i['NumPeople'] + """ WHERE StoreName = '""" + i['StoreName'] + """'"""
	    	print(sql_update_query)
	    	cur.execute(sql_update_query)

	#cur.executemany("INSERT OR REPLACE INTO my_table (StoreName,Type,x,y,TotalCapacitance,NumPeople,RateofTraffic) VALUES (?,?,?,?,?,?,?);", to_db)
	con.commit()
	con.close()
