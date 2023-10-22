def zxc(z,x,c,v):
    lst = [z,x,c,v]
    del lst[:-2:]
    return lst

if __name__ == "__main__":
    print(zxc(2,0,3,3))