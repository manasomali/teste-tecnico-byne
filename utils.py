import json

class DataModifier():
    def __init__(self, filename):
        self.filename = filename


    def getData(self):
        with open(self.filename, "r") as read_file:
            data = json.load(read_file)
        
        return data
    

    def addData(self, user):
        data=self.getData()
        data[user] = 0
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)


    def updateData(self, user, increment):
        data=self.getData()
        data[user] = data[user]+increment
        with open(self.filename, "w+") as read_file:
            json.dump(data, read_file, indent=4)
