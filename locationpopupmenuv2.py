import dialogv2
from convertdatav2 import updateDB

class LocationPopupMenu(dialogv2.ListMDDialog):
    def __init__(self, store_data):
        super().__init__()

        # Set all of the fields of market data
        #print("SET")
        updateDB()
        headers = "StoreName,Type,x,y,TotalCapacitance,NumPeople,RateofTraffic"
        headers = headers.split(',')

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = store_data[i]
            print(attribute_name, attribute_value)
            setattr(self, attribute_name, str(attribute_value))