class mycat():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('my cat name is {}'.format(self.name))

def main():
    obj = mycat('Cessar')
    print(obj)


if __name__ == '__main__':
    main()
