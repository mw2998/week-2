

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

#for record in records:
#	print record.price


# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

#print 'min price: '
#print 'max price: ' 
#print 'average price: '



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

price=[]

for record in records:
    price.append(record.price)

totalPrice = 0
for x in price:
    totalPrice += x
averagePrice = totalPrice / len(price)
print 'average price = ' + str(averagePrice)

minPrice = 999999999
for x in price:
    if minPrice > x:
        minPrice = x
    else:
        minPrice = minPrice
print 'minPrice = ' + str(minPrice)

maxPrice = 0
for x in price:
    if maxPrice < x:
      maxPrice = x
    else:
        maxPrice = maxPrice
print ' maxPrice = ' + str(maxPrice)

client.db_close()

#received 3810 records
#average price = 9054
#minPrice = 350
#maxPrice = 168000



