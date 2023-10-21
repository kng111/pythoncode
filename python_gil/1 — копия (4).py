
def xx():
    def fucn(num):
        return num

    def in_(num):
        return(num * 3)


    def func_(num):
        return(num + 3)

    print(fucn(in_(func_(10))))

if __name__ == "__main__":
    xx()
    print("отработал")