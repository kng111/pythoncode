class Mixin:
    def mixin_method(self):
        print('Mixin method 1')

class MyClass(Mixin):
    def my_method(self):
        print("My method")
        return(1)

obj = MyClass()


def prs():
    if obj.mixin_method() == None:
        print("Миксины - это особый вид мнодеств наследования в python, которые используются для предоставления дополнительной функциональности классам.")

if __name__ == "__main__":
    try:
        prs()
    
    except Exception as e:
        
        print(f"Ошибка: {e}")
