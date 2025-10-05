class School:
    def __init__(self):
        self.students = []
        self.unique_name = set()
        self.added_list = []

    def add_student(self, name, grade):
        if name not in self.unique_name:
            self.students.append(Student(name, grade))
            self.added_list.append(True)
            self.unique_name.add(name)
        else:
            self.added_list.append(False)

    def roster(self):
        if not self.students:
            return []
            
        map = {}
        for i in self.students:
            map[i.name] = i.grade

        sorted_students = sorted(map.items(), key=lambda x: (x[1], x[0]))
        return [i[0] for i in sorted_students]

    def grade(self, grade_number):
        result = []
        for i in self.students:
            if grade_number == i.grade:
                result.append(i.name)
        
        return sorted(result)
        

    def added(self):
        return self.added_list

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade