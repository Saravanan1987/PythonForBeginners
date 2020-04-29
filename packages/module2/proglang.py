__all__ = ['mypython']

class clang():
    def __init__(self, author):
        self.author = author

    def __str__(self):
        return ('The author of C language is {}'.format(self.author))


class python():
    def __init__(self, author):
        self.author = author

    def __str__(self):
        return ('The author of python is {}'.format(self.author))


def myclang():
    obj = clang('Dennis Ritchie')
    return obj

def mypython():
    obj = python('Guido Van Rossum')
    return obj

if __name__ == '__main__':
    myclang()
    mypython()
  
