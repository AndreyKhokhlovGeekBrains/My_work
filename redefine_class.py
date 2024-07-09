from datetime import datetime


class MyStr(str):    
    def __new__(cls, value: str, author: str):
        instance = super(MyStr, cls).__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance
    
    def __str__(self) -> str:
        return f'{super().__str__()} (Автор: {self.author}, Время создания: {self.time})'
    
    def __repr__(self) -> str:
        return f"MyStr('{super().__str__()}', '{self.author}')"
        

if __name__ == '__main__':
    event = MyStr("Завершилось тестирование", "John")
    print(event)
    print(event.__repr__())
    
