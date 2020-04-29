__all__ = ['dog']

class mydog():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('my dog name is {}'.format(self.name))

def dog():
    obj = mydog('Cessar')
    return obj

class mycat():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('my cat name is {}'.format(self.name))

def cat():
    obj = mydog('Julie')
    return obj



if __name__ == '__main__':
    dog()
    cat()
