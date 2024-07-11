import csv
from typing import List

class Student:
    def __init__(self, name: str, subjects_file: str) -> None:
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    
    def load_subjects(self, path: str) -> None:
        with open(path, 'r', encoding='UTF-8') as f_read:
            csv_reader = csv.reader(f_read)
            for row in csv_reader:
                for item in row:
                    self.subjects[item] = {"grades": [], "test_score": []}
        
    def __setattr__(self, name: str, value: str) -> None:
        if name == 'name':
            name1, name2, *_ = value.split(" ")
            if not (name1[0].isupper() and name2[0].isupper() and name1.isalpha() and name2.isalpha()):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)
        
    def __getattr__(self, name): # is called when an attribute lookup fails
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")
           
    # def __getattribute__(self, name: str) -> str:
    #     if name == 'subjects':
    #         subjects = super().__getattribute__(name)
    #         return f'Студент: {self.name}\nПредметы: {", ".join(subjects.keys())}'
    #     return super().__getattribute__(name)
    
    def __str__(self) -> str:
        subjects_list = [subject for subject in self.subjects if self.subjects[subject]['grades']]
        return f'Студент: {self.name}\nПредметы: {", ".join(subjects_list)}'
    
    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {"grades": [], "test_score": []}
        if isinstance(grade, int) and 2 <= grade <= 5:
            self.subjects[subject]['grades'].append(grade)
        else:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        
    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {"grades": [], "test_score": []}
        if isinstance(test_score, int) and 0 <= test_score <= 100:
            self.subjects[subject]['test_score'].append(test_score)
        else:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
            
    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        test_score_list = self.subjects[subject]['test_score']
        if len(test_score_list) == 0:
            return 0
        return sum(test_score_list) / len(test_score_list)
        
    def get_average_grade(self):
        my_sum = 0
        count = 0
        for subject in self.subjects:
            grades_list = self.subjects[subject]['grades']
            my_sum += sum(grades_list)
            count += len(grades_list)
        return my_sum / count
    

if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_grade("Физика", 2)
    student.add_test_score("Математика", 85)
    print(student.name)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
    
