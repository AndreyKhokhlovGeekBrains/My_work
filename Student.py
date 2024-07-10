import csv
from typing import List

class Student:
    def load_subjects(self, path: str) -> dict[str: list]:
        subjects_dict = {}
        with open(path, 'r', encoding='UTF-8') as f_read:
            csv_reader = csv.reader(f_read)
            for row in csv_reader:
                for item in row:
                    subjects_dict[item] = []
        return subjects_dict
        
    def __init__(self, name: str, subjects_file: str) -> None:
        self.name = name
        self.subjects = self.load_subjects(subjects_file)
        
    def __setattr__(self, name: str, value: str) -> None:
        if name == 'name':
            name1, name2, *_ = value.split(" ")
            if name1[0].isupper() and name2[0].isupper() and name1.isalpha() and name2.isalpha():
                super().__setattr__(name, value)
            else:
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)
           
    def __getattribute__(self, name: str) -> str:
        if name == 'subjects':
            subjects = super().__getattribute__(name)
            return f'Студент: {self.name}\nПредметы: {', '.join(subjects.keys())}'
            # return f'Студент: {self.name}\nПредметы: {subjects}'
        return super().__getattribute__(name)
    
    def __str__(self) -> str:
        subjects = super().__getattribute__('subjects')
        subjects_list = [key for key, value in subjects.items() if value]
        return f'Студент: {self.name}\nПредметы: {', '.join(subjects_list)}'
    
    def add_grade(self, subject, grade):
        if isinstance(grade, int) and 2 <= grade <= 5:
            subjects = super().__getattribute__('subjects')
            subjects[subject].append(grade)
        else:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        
    def add_test_score(self, subject, test_score):
        if isinstance(test_score, int) and 0 <= test_score <= 100:
            subjects = super().__getattribute__('subjects')
            subjects[subject].append(test_score)
        else:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
            
    def get_average_test_score(self, subject):
        pass
        
    def get_average_grade(self):
        subjects = super().__getattribute__('subjects')
        count = 0
        sum = 0
        for subject, value in subjects.items():
            if value:
                sum += value[0]
                count += 1
        return sum / count
     
    

if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
    
