class IDHandler:
    def __init__(self, id):
        self.id = id
        self.id += 58

    def __str__(self):
        return f'IDHandler object with id={self.id}'

handler_object = IDHandler(11)
print(handler_object)
