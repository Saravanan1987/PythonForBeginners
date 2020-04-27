""" Program to demonstarte iterators"""

class myRange:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.value:
            raise StopIteration()
        else:
            return self.index

def custom_range():
    for count in myRange(5):
        print("For loop iteration:{count}".format(count = count))

def iterator_demo():
    obj = myRange(5).__iter__()
    try:
        print(obj.__next__())
        print(obj.__next__())
        print(obj.__next__())
        print(obj.__next__())
        print(obj.__next__())
        print(obj.__next__())
    except StopIteration:
       print("Iteration has crossed the threshold value")


if __name__ == '__main__':
    custom_range()
    iterator_demo()
