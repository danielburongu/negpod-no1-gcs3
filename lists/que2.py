#!/usr/bin/python3
def index_find(mylist, target):
    ab = sorted(mylist)
    if target in mylist:
        return ab.index(target)
    else:
        mylist.append(target)
        ab = sorted(mylist)
        return ab.index(target)
