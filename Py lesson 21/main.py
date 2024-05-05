import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def read_json_file(self):
        with open("students.json", "r") as json_file:
            self.scores = json.load(json_file)

    def average_score(self):
        score_ = {}
        for i in self.scores["students"]:
            name = i["name"]
            grades = i["grades"]
            average = sum(grades) / len(grades)
            score_[name] = average
        return score_

    def add_json(self):
        with open("written.json", "w") as json_file:
            json.dump(self.average_score(), json_file)


student = Student("Charles", 21, [90, 51, 88])
student.read_json_file()
student.add_json()
