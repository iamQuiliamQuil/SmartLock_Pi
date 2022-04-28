import uuid

class UUIDManagerSingleton(object):
    registered_uuids = []

    #https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/#:~:text=Singleton%20pattern%20is%20a%20design,of%20access%20for%20a%20resource.
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(UUIDManagerSingleton, cls).__new__(cls)
        return cls.instance
    
    def generateUUID(self):
        new_uuid = uuid.uuid4()
        self.registered_uuids.append(new_uuid)
        return str(new_uuid) #we let the user interact with uuids as strings for convenience

    def UUIDIsValid(self, sent_uuid):
        return True if uuid.UUID(sent_uuid) in self.registered_uuids else False

    def displayUUIDs(self):
        print(self.registered_uuids)

    #def removeUUID(self, uuid_to_be_removed):
