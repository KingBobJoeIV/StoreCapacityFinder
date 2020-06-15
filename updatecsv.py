import csv
import time

myData = [["StoreName", "Type", "x", "y", "TotalCapacitance", "NumPeople", "RateofTraffic"],
          ["Trader Joes","Grocery",-121,37,50,37,2],
          ["Safeway","Grocery",-120,37,100,99,-2],
          ["Staples","Supply",-119,38,25,3,5],
          ["Costco","Grocery",-118,37.5,200,200,5],
          ["Home Depot","Hardware",-118,34,75,60,-4]]

for x in range(0, 100):
    f = open('store.csv')
    csv_f = csv.reader(f)
    counter = 1
    for row in csv_f:
        try:
            #print(row[5])
            myData[counter][5] = int(myData[counter][5]) + int(row[6])
            myData[counter][5] = str(myData[counter][5])
            myData[counter][6] = str(myData[counter][6])
            #print(row[5], row[6])
            counter = counter + 1
        except:
            pass
    f.close()
    f = open('store.csv', 'w')
    with f:
        writer = csv.writer(f)
        print(myData)
        writer.writerows(myData)
    f.close()
    time.sleep(7)

#print(myData)
        
