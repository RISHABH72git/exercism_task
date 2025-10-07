class Garden:
    PLANT_MAP = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }
    
    default_student = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = sorted(students) if students else Garden.default_student

    def plants(self, name):
        diagram_split = self.diagram.split("\n")
        name_index = self.students.index(name)
        result = []
        for i in diagram_split:
            count = 0
            for j in range(0,len(i),2):
                if name_index == count:
                    result.extend(list(i[j:j+2]))
                count+=1
        return [Garden.PLANT_MAP[i] for i in result]
        
