#The following program calculates the grade, mean grade, and grade variance for any student
#depending on how much sleep and the energy level of the student. It will also calculate the difficulty level

class Assignment:
    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty

    def get_name(self) -> str:
        return self.name

    def get_difficulty(self) -> float:
        return self.difficulty

    def __str__(self) -> str:
        return self.name


class AssignmentResult:
    def __init__(self, id: int, assignment: Assignment, grade: float):
        self.id = id
        self.assignment = assignment
        self.grade = grade

    def get_id(self) -> int:
        return self.id

    def get_grade(self) -> float:
        return self.grade

    def get_assignment(self) -> Assignment:
        return self.assignment


class Student:
    def __init__(self, id: int, first_name: str, last_name: str, town: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.town = town
        self.grades = []
        self.energy = 1

    def get_id(self) -> int:
        return self.id

    def get_first_name(self) -> str:
        return self.first_name

    def set_first_name(self, name: str):
        self.first_name = name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, name: str):
        self.last_name = name

    def get_town(self) -> str:
        return self.town

    def set_town(self, town: str):
        self.town = town

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def get_grade(self) -> float:
        if len(self.grades) == 0:
            return 0
        if len(self.grades) > 2:
            # calculate old mean grade before assigning new mean grade
            return sum(self.grades[2:]) / (len(self.grades) - 1)
        return sum(self.grades) / len(self.grades)


    def assign(self, assignment: Assignment) -> AssignmentResult:
        grade = 1 - self.energy * assignment.get_difficulty()
        if grade < 0:
            grade = 0
        self.grades.append(grade)
        self.grades.sort()
        self.energy = self.energy - self.energy * assignment.get_difficulty()
        assignment_result = AssignmentResult(self.id, assignment, grade)
        return assignment_result

    def sleep(self, hours: float):
        self.energy = min((1, self.energy * (1 + hours / 10)))

    def get_energy(self):
        return self.energy


class Course:
    def __init__(self, students: list):
        self.students = students

    def get_mean_grade(self) -> float:
        total = sum(student.get_grade() for student in self.students)
        return total / len(self.students) if self.students else 0

    def get_max_grade(self) -> float:
        max_grade = max(student.get_grade() for student in self.students) if self.students else 0
        return max_grade

    def get_min_grade(self) -> float:
        min_grade = min(student.get_grade() for student in self.students) if self.students else 0
        return min_grade

    def get_median_grade(self) -> float:
        grades = [student.get_grade() for student in self.students]
        grades.sort()
        n = len(grades)
        if n % 2 != 0:
            return grades[n // 2]
        return (grades[n // 2 - 1] + grades[n // 2]) / 2 if n > 0 else 0

    def get_grade_variance(self) -> float:
        mean = self.get_mean_grade()
        total = sum((student.get_grade() - mean) ** 2 for student in self.students)
        return total / len(self.students) if self.students else 0

    def get_grade_std_dev(self) -> float:
        return self.get_grade_variance() ** 0.5 if self.students else 0

    def assign(self, name: str, difficulty: float) -> None:
        assignment = Assignment(name, difficulty)
        for student in self.students:
            assignment_result = student.assign(assignment)


#external sources : chatgpt


        
