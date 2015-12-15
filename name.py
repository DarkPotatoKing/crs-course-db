class Name(object):
    """Name object"""
    def __init__(self, name):
        super(Name, self).__init__()
        name = name.split(',')
        self.firstname = name[1].strip()
        self.surname = name[0].strip()

    def __repr__(self):
        return ', '.join([self.surname, self.firstname])


if __name__ == '__main__':
    n = Name('AGPAOA, JERWIN')
    print n