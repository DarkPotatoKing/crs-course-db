from name import Name

class Course(object):
    """An object to represent a course offered on CRS"""
    def __init__(self, code, description, units, schedule, remarks, slots, demand):
        super(Course, self).__init__()
        self.code = int(code)
        self.units = str(units)
        self.schedule = str(schedule)
        self.remarks = str(remarks)

        description = description.split('***')
        self.name = ' '.join(description[:-1])
        self.section = self.name.split()[-1]
        self.name = ' '.join(self.name.split()[:-1])
        self.professor = Name(description[-1])
        self.slots = self.force_int(slots.split('/')[0])
        self.demand = demand

    def force_int(self, x):
        while True:
            try:
                int(x)
                return int(x)
            except:
                x = x[:-1]
        r

    def __repr__(self):
        attributes = list()
        attributes.append(['Code' , self.code])
        attributes.append(['Name' , self.name])
        attributes.append(['Section' , self.section])
        attributes.append(['Prof' , self.professor])
        attributes.append(['Units', self.units])
        attributes.append(['Sched', self.schedule])
        attributes.append(['Remarks', self.remarks])
        attributes.append(['Slots', self.slots])
        attributes.append(['Demand', self.demand])
        return '\n'.join([self.width(i,20) + str(j) for i, j in attributes])

    def width(self, s, w):
        return s + ' ' * (int(w) - len(s))

if __name__ == '__main__':
    c = Course('112312312', 'Subj 1 XYZ***SUR\tFIR',3,'TTh 2:30PM-4PM lec PH 222','','25 / 25',72)
    print c