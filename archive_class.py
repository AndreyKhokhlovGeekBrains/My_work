from typing import Union, List

class Archive:
    _instance = None
    archive_text: List[str] = []
    archive_number: List[Union[int, float]] = []
    
    def __new__(cls, text: str, number: Union[int, float]):
        if cls._instance is None:
            cls._instance = super(Archive, cls).__new__(cls)
            cls.archive_text = []
            cls.archive_number = []
            return cls._instance
        return cls._instance
        
    
    def __init__(self, text: str, number: Union[int, float]) -> None:
        self.text = text
        self.number = number
        Archive._instance.archive_text.append(self.text)
        Archive._instance.archive_number.append(self.number)
        
    def __str__(self) -> str:
        return f'Text is {self.text} and number is {self.number}. Also {Archive.archive_text} and {Archive.archive_number}'
    
    def __repr__(self) -> str:
        return f"Archive('{self.text}', {self.number})"


if __name__ == '__main__':
    archive1 = Archive("Запись 1", 42)
    archive2 = Archive("Запись 2", 3.14)
    
    print(archive1)
    print(archive1.__repr__())
    
