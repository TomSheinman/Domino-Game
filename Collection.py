class Collection:
    """
    This class represents a Collection.
    """
    def __init__(self, array):
        """
        Constructor.
        :param array: list - list of objects
        """
        self.array = array

    def get_collection(self):
        """
        :return: Method that returns the array.
        """
        return self.array

    def add(self, item, option):
        """
        Method that is implemented only in subclasses, will throw an exception if used in this class.
        :param item: object - an object to add to the array
        :param option: an option to add another variable to the method
        """
        raise NotImplementedError("Subclasses only implement this!")

    def __getitem__(self, i):
        """
        Method that returns the object in position i in the array.
        :param i: Index
        :return: the object or none if index is not in the array
        """
        if i < len(self.array):
            return self.array[i]
        else:
            return None

    def __eq__(self, other):
        """
        == operator overload
        :param other: an object(Collection or subclass of collection(if its not - False) to check equality with self)
        :return: bool - True or False
        """
        if not isinstance(other, Collection):
            return False
        return self.array == other.array

    def __ne__(self, other):
        """
        != operator overload
        :param other: an object to check inequality with self, checks using opposite of == operator
        """
        return not self == other

    def __len__(self):
        """
        len function override
        """
        return len(self.array)

    def __contains__(self, item):
        """
        checks if an object is in the array
        :param item: object
        :return: True or False
        """
        for i in self.array:
            if i == item:
                return True
        return False

    def __str__(self):
        """
        str function override - returns the str representation of every item in the array without space in between
        """
        returned_str = ""
        for i in self.array:
            returned_str += str(i)
        return returned_str

    def __repr__(self):
        """
        print function override using str function
        """
        return str(self)
