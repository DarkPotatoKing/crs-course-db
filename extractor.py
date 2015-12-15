class Extractor(object):
    """Object for extracting data from unformatted text file."""
    @classmethod
    def extract(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines = [i.strip() for i in lines]
        lines = filter(lambda x: x != '', lines)
        with open(filename, 'w') as f:
            for i in lines:
                f.write(str(i) + '\n')

if __name__ == '__main__':
    Extractor.extract('sample.txt')