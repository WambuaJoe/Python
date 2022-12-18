# file for testing python code for my projects before pushing to my git repo

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)

    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{:d} argument:".format(count - 1))
    else:
        print("{:d} arguments:".format(count - 1))

    for i in range(1, count):
        print("{:d}: {:s}".format((i), argv[i])