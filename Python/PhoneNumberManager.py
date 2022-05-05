class PhoneNumberManagerSingleton(object):
    registered_phone_nums = []

    #https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/#:~:text=Singleton%20pattern%20is%20a%20design,of%20access%20for%20a%20resource.
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(PhoneNumberManagerSingleton, cls).__new__(cls)
        return cls.instance
    
    def addNum(self, newNum):
        self.registered_phone_nums.append(newNum)
        return "New phone number: "+newNum+" has been registered!"

    def getNums(self):
        return self.registered_phone_nums.copy()
        #returns a copy for data safety purposes. 

    def removeNum(self, numToRemove):
        if numToRemove in self.registered_phone_nums:
            self.registered_phone_nums.remove(numToRemove)
            return "Phone number: "+numToRemove+" has been removed!"
        else:
            return "Error - Phone number: "+numToRemove+" is not a registered number!"

    #def removeUUID(self, uuid_to_be_removed):


