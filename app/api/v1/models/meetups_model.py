class Meetup:
    """
    This class represents the meetup model.
    """
    def __init__(self, meetup_list):
        """
        Initialize meetups list.
        """
        self.meetup_list = meetup_list

    def show_meetups(self):
        """
        Show the meetups.
        """
        return self.meetup_list

    def add_meetup(self, meetup):
        """
        Append meetups to the meetup_list.
        """
        self.meetup_list.append(meetup)  

    def delete_meetup(self, index):
        """
        Delete meetup.
        """
        del_meetup = [del_meetup for del_meetup in self.meetup_list if del_meetup["id"] == index]
        if del_meetup:
            self.meetup_list.remove(del_meetup[0])
            return True 