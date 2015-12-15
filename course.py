from name import Name

class Course(object):
    """An object to represent a course offered on CRS"""
    def __init__(self, code, title, professor, units, schedule, slots):
        super(Course, self).__init__()
        self.code = int(code)
        title = title.split()
        self.name = ' '.join(title[:-1])
        self.section = title[-1]
        self.professor = Name(professor)
        self.units = float(units)
        self.schedule = schedule
        slots = slots.split()
        self.slots = int(slots[0])
        self.demand = int(slots[-1])

    def __repr__(self):
        attributes = list()
        attributes.append(['Code' , self.code])
        attributes.append(['Name' , self.name])
        attributes.append(['Section' , self.section])
        attributes.append(['Prof' , self.professor])
        attributes.append(['Units', self.units])
        attributes.append(['Sched', self.schedule])
        attributes.append(['Slots', self.slots])
        attributes.append(['Demand', self.demand])
        return '\n'.join([self.width(i,20) + str(j) for i, j in attributes])

    def width(self, s, w):
        return s + ' ' * (int(w) - len(s))

if __name__ == '__main__':
    c = Course("42503",
               "Philo 1 SUV",
               "OCAMPO, MA. LIZA RUTH",
               "3.0",
               "S 10AM-1PM lec PH 222",
               "25 / 25 72")
    print c