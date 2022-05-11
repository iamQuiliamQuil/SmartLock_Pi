import pickle
import os

import UUIDManager as um
import PhoneNumberManager as pnm

class MementoSingleton(object):
    UUIDman = None# = um.UUIDManagerSingleton()
    PhoneNumMan = None# = pnm.PhoneNumberManagerSingleton()

    #figure out a way of making sure that memento is serialized when a function is called

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            if os.path.isfile("memento.pickle"):
                with open("memento.pickle", "rb") as infile:
                    cls.instance = pickle.load(infile)
                print("Reconstructed object", test_dict_reconstructed)
            else:
                cls.instance = super(MementoSingleton, cls).__new__(cls)
                cls.instance.UUIDman = um.UUIDManagerSingleton()
                cls.instance.PhoneNumMan = pnm.PhoneNumberManagerSingleton()
        return cls.instance
    
bob = MementoSingleton()
bob.UUIDman.generateUUID()
bob.UUIDman.displayUUIDs()

#test

