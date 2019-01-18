
def idGenerator(collection):
    """ Function to generate ID for collection """

    # If collection is empty return 1 else add 1 to id of last object
    if len(collection) == 0:
        return 1
    else:
        return collection[-1]['id']+1
    # len(collection)+1