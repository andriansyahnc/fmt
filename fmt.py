from enum import Enum

class Repository:

    data = {}

    def __init__(self):
        self.data = {}
    
    @classmethod
    def Register(self, itemName, itemContent, itemType):
        if itemName in self.data:
            return
        self.data[itemName] = {
            'value': itemContent,
            'type': "JSON" if itemType == 1 else "XML"
        }
    
    @classmethod
    def Retrieve(self, itemName):
        if itemName not in self.data:
            print("Not found")
            return
        return self.data[itemName]['value']
    
    @classmethod
    def GetType(self, itemName):
        if itemName not in self.data:
            print("Not found")
            return
        return self.data[itemName]['type']
    
    def Deregister(self, itemName):
        if itemName in self.data:
            delattr(self.data, itemName)
        print("Not Found")
            
    
