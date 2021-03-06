from course import Course
from extractor import Extractor

class Database(object):
    """Database object for list of courses"""
    def __init__(self, filename):
        super(Database, self).__init__()
        Extractor.extract(filename)

        lines = ''
        with open(filename, 'r') as f:
            lines = f.readlines()

        self.courses = list()

        for i in lines:
            x = i.split(',')
            x = [y.strip('()"') for y in x]
            self.courses.append(Course(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

    def __repr__(self):
        return '\n\n'.join([str(i) for i in self.courses])

    def filter_by_surname(self, surnames):
        surnames = [i.upper() for i in surnames]
        self.courses = filter(lambda x: x.professor.surname in surnames, self.courses)
        # print self

    def sort_by_chance(self):
        self.courses.sort(key = lambda x: float(x.slots) / float(x.demand), reverse = True)
        # print self

    def total_chance(self):
        chance = 1.0
        for i in self.courses:
            chance *= 1 - min(1.0, float(i.slots) / float(i.demand))
        return 1- chance

    def first(self, num):
        self.courses = self.courses[:num]

    def __len__(self):
        return len(self.courses)

if __name__ == '__main__':
    d = Database('sample.csv')
    print d
    # d.filter_by_surname(['Perez','De Guzman','Alvares','Agpaoa','Fronda','Mendoza'])
    # d.sort_by_chance()
    # print d
    # d.first(9)
    # print d.total_chance()
    # print len(d)
