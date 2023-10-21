
def zxc():
    dct1 = {"Hello": 'word', '1':1}
    dct2 = {v: k for k, v in dct1.items()}

    print(dct2)

if __name__ == "__main__":
    zxc()