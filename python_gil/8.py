

def zxc(frs, tw):
    def per(frs):
        # Преобразовываем строку к нижнему регистру
        stroka = str(frs).lower()
        # Заменяем "hello" на "Goodbye"
        stroka = stroka.replace("hello", "Goodbye")
        return stroka
    
    def two(tw):
        # Преобразовываем строку к нижнему регистру
        stroka = str(tw).lower()
        # Заменяем первые два "run" на "stop"
        stroka = stroka.replace("run", "stop", 2)
        return stroka
    
    # Вызываем функции и возвращаем результат
    return per(frs), two(tw)

# Вызываем функцию и печатаем результат
if __name__ == "__main__":
    print(zxc('Hello, world!', 'Run Run Run!'))
