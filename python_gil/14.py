class SomeCls:
    __K = 3.14

    def get_K(self):
        return self.__K
    
_SomeCls__k = "zdec"

obj = SomeCls()
print(obj.get_K())
