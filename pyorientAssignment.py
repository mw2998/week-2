
import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "admin")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 22.532498
lat2 = 22.552317

lng1 = 114.044329
lng2 = 114.076644

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

for record in records:
	print record.price


# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: '
print 'max price: ' 
print 'average price: '

client.db_close()


#Below this my own work
import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "8241EA05F8DA25AB59A7D5C65988FAF3B85DAECC5C8FFB4FD7A1D97DDA7B9DEA")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
    client.db_open( db_name, db_username, db_password )
    print db_name + " opened successfully"
else:
    print "database [" + db_name + "] does not exist! session ending..."
    sys.exit()
    
lat1 = 22.535868
lat2 = 22.552515

lng1 = 114.038771
lng2 = 114.077352

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'
records = client.command(query.format(lat1, lat2, lng1, lng2))

record = records[0]
print type(record)
print record

print record.price

numListings = len(records)
print 'received ' + str(numListings) + ' records'



client.db_close()

#Below is my results
#soufun opened successfully
#<class 'pyorient.types.OrientRecord'>
#{'@Listing':{'development': '\xe7\xa6\x8f\xe7\x94\xb0-\xe7\xa6\x8f\xe7\x94\xb0\xe4\xb8\xad\xe5\xbf\x83\xe5\x8c\xba-\xe6\xb8\xaf\xe4\xb8\xbd\xe8\xb1\xaa\xe5\x9b\xad', 'city': '\xe6\xb7\xb1\xe5\x9c\xb3', 'longitude': 114.072914, 'description': '3\xe5\xae\xa42\xe5\x8e\x85', 'title': '\xe4\xb8\xad\xe5\xbf\x83\xe5\x8c\xba\xe5\x8d\x93\xe8\xb6\x8a\xe6\x97\x81\xe8\xbe\xb9 \xe8\xb1\xaa\xe5\xae\x85\xe8\x8a\xb1\xe5\x9b\xad\xe5\xb0\x8f\xe5\x8c\xba \xe7\xb2\xbe\xe8\xa3\x85\xe4\xbf\xae\xe5\x85\xa8\xe9\xbd\x90\xe5\x87\xba\xe7\xa7\x9f', 'price': 11000L, 'time': [], 'prec': 1, 'latitude': 22.536123, 'link': '/chuzu/3_169543455_1.htm', 'details': '\xe6\x95\xb4\xe7\xa7\x9f|105\xe3\x8e\xa1|\xe7\xb2\xbe\xe8\xa3\x85\xe4\xbf\xae|12/42\xe5\xb1\x82|\xe6\x9c\x9d\xe5\x8d\x97', 'conf': 80, 'address': '\xe6\xb5\xb7\xe7\x94\xb0\xe8\xb7\xaf2\xe5\x8c\x97\xe9\x97\xa8', 'timeformat': [], 'level': '\xe9\x81\x93\xe8\xb7\xaf'},'version':8,'rid':'#12:1345092'}
#11000
#received 3810 records
