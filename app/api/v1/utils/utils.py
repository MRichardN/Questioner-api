
def idGenerator(collection):
    """ Function to generate ID for collection """

    # autoincrement id
    if len(collection) == 0:
        return 1
    else:
        return collection[-1]['id']+1