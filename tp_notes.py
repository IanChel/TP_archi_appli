class Student:
    def __init__(self, name, math, physics, it):
        self.name = name
        self.grades = {
            "Mathématiques": math,
            "Physique": physics,
            "Informatique": it
        }

    @property
    def average(self):
        return sum(self.grades.values()) / len(self.grades)


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_rankings(self):
        if not self.students:
            return

        subjects = ["Mathématiques", "Physique", "Informatique"]
        
        for subject in subjects:
            print(f"--- Classement en {subject} ---")
            sorted_students = sorted(self.students, key=lambda s: s.grades[subject], reverse=True)
            for student in sorted_students:
                print(f"{student.name} : {student.grades[subject]}")
            print()

        print("--- Classement Général (Moyenne) ---")
        sorted_avg = sorted(self.students, key=lambda s: s.average, reverse=True)
        for student in sorted_avg:
            print(f"{student.name} : {student.average:.2f}")

    def rank_matter_1(self):
        # Tri décroissant pour la 1ère matière listée (ici Mathématiques)
        sorted_students = sorted(self.students, key=lambda s: s.grades["Mathématiques"], reverse=True)
        for student in sorted_students:
            print(f"{student.name} : {student.grades['Mathématiques']}")


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

# Pour tester le bon fonctionnement de la proposition
school_class.display_rankings()

# Appel à la méthode de la question 3
school_class.rank_matter_1()
