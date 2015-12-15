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
            self.courses.append(Course(i[0], i[1], i[2], i[3], i[4], i[5]))

        # for i in self.courses:
        #     print i


if __name__ == '__main__':
    Database('sample.txt')
