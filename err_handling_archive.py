from typing import Any, Union

class InvalidTextError(ValueError):
    pass

class InvalidNumberError(ValueError):
    pass

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number
        
    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'text':
            if not value.replace(' ', '').isalpha() or not value:
                raise InvalidTextError(f'Invalid text: {value}. Text should be a non-empty string.')
            
        if name == 'number':
            if not isinstance(value, float) or value < 0:
                raise InvalidNumberError(f'Invalid number: {value}. Number should be a positive integer or float.')
            
        return super().__setattr__(name, value)
        

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'
    


archive_instance = Archive("Sample text", 42.5)
print(archive_instance)
