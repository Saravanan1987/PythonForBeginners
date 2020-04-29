import sys
def fileread(f):
    with open(f, 'r') as fh:
        print(fh.read())


if __name__ == '__main__':
    try:
        fileread(sys.argv[1])
    except:
        pass
