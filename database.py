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
            lines = [i.replace('Add to my desired classes', '').strip() for i in lines]

        courses = list()
        for i, val in enumerate(lines[::6]):
            # print i, val
            courses.append(lines[i*6:i*6+6])

        self.courses = list()
        for i in courses:
            # print i[2]
            self.courses.append(Course(i[0], i[1], i[2], i[3], i[4], i[5]))

        # for i in self.courses:
        #     print i

    def __repr__(self):
        return '\n\n'.join([str(i) for i in self.courses])

    def filter_by_surname(self, surnames):
        surnames = [i.upper() for i in surnames]
        self.courses = filter(lambda x: x.professor.surname in surnames, self.courses)
        # print self

    def sort_by_chance(self):
        self.courses.sort(key = lambda x: float(x.slots) / float(x.demand), reverse = True)
        # print self

if __name__ == '__main__':
    d = Database('sample.txt')
    d.filter_by_surname(['Perez','De Guzman','Alvares','Agpaoa','Fronda','Mendoza'])
    d.sort_by_chance()
    print d
