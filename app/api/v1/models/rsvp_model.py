

class Rsvp:
    """This class represents rsvp model."""
    def __init__(self, rsvp_list):
        """
        Initialize rsvp list.
        """
        self.rsvp_list = rsvp_list

    def add_rsvp(self, rsvp):
        """
        Add rsvp to the list.
        """
        self.rsvp_list.append(rsvp)

