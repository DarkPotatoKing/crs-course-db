class Extractor(object):
    """Object for extracting data from unformatted text file."""
    @classmethod
    def extract(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines = [i.strip().strip(',').strip() for i in lines]
        lines = [i.replace(', ', '\t') for i in lines]
        lines = filter(lambda x: x != '', lines)

        s = ''
        for i in lines:
            try:
                int(i.split(',')[0])
                s += '\n'
            except:
                s += '***'
            s += i

        with open(filename, 'w') as f:
            f.write(s.lstrip())

if __name__ == '__main__':
    Extractor.extract('sample.csv')