
class Model(object):
    """ Class base model."""

    def __init__(self, collection):
        """ Initialize object """
        self.collection = collection

    def save(self, data):
        """ save object."""
        self.collection.append(data)
        return data

    def exists(self, key, value):
        """ Check if object exists."""
        items = [item for item in self.collection if item[key] == value]
        return len(items) > 0

    # find one item
    def getOne(self, key, value): 
        """ Fetch items """
        items = [item for item in self.collection if item[key] == value]
        return items[0]

    def getAll(self):
        """ get all """
        return self.collection

    def delete(self, key, item_id):
        items = [item for item in self.collection if item[key] == item_id] 
        self.collection.remove(items[0])
        return True



       
    
        