from collections.abc import Iterable, Iterator

def add_matter_4(cls):
    """
    Décorateur de classe qui modifie le constructeur
    pour ajouter systématiquement une 4ème matière à tous les étudiants.
    """
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        # Récupère une note optionnelle, sinon met 10 par défaut respectant l'énoncé
        matter_4_grade = kwargs.pop('matter_4_grade', 10)
        original_init(self, *args, **kwargs)
        self.grades["Anglais"] = matter_4_grade

    cls.__init__ = new_init
    return cls

@add_matter_4
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


class Matter1Iterator(Iterator):
    def __init__(self, students):
        # Trie la liste lors de l'initialisation de l'itérateur
        self._sorted_students = sorted(students, key=lambda s: s.grades["Mathématiques"], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index < len(self._sorted_students):
            student = self._sorted_students[self._index]
            self._index += 1
            return student
        raise StopIteration


class Matter2Iterator(Iterator):
    def __init__(self, students):
        self._sorted_students = sorted(students, key=lambda s: s.grades["Physique"], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index < len(self._sorted_students):
            student = self._sorted_students[self._index]
            self._index += 1
            return student
        raise StopIteration


class Matter3Iterator(Iterator):
    def __init__(self, students):
        self._sorted_students = sorted(students, key=lambda s: s.grades["Informatique"], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index < len(self._sorted_students):
            student = self._sorted_students[self._index]
            self._index += 1
            return student
        raise StopIteration

class Matter4Iterator(Iterator):
    def __init__(self, students):
        self._sorted_students = sorted(students, key=lambda s: s.grades.get("Anglais", 0), reverse=True)
        self._index = 0

    def __next__(self):
        if self._index < len(self._sorted_students):
            student = self._sorted_students[self._index]
            self._index += 1
            return student
        raise StopIteration

def add_iter_matter_4(cls):
    """
    Décorateur de classe qui injecte la méthode iter_matter_4
    dans la classe SchoolClass.
    """
    def iter_matter_4(self):
        return Matter4Iterator(self.students)
    
    cls.iter_matter_4 = iter_matter_4
    return cls

@add_iter_matter_4
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SchoolClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialise students seulement la première fois
        if not hasattr(self, 'students'):
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        # Renvoie l'itérateur de la matière 1
        return Matter1Iterator(self.students)

    def iter_matter_2(self):
        return Matter2Iterator(self.students)

    def iter_matter_3(self):
        return Matter3Iterator(self.students)

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

    def rank_matter_2(self):
        # Tri décroissant pour la 2ème matière
        sorted_students = sorted(self.students, key=lambda s: s.grades["Physique"], reverse=True)
        for student in sorted_students:
            print(f"{student.name} : {student.grades['Physique']}")

    def rank_matter_3(self):
        # Tri décroissant pour la 3ème matière
        sorted_students = sorted(self.students, key=lambda s: s.grades["Informatique"], reverse=True)
        for student in sorted_students:
            print(f"{student.name} : {student.grades['Informatique']}")


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

# Pour tester le bon fonctionnement de la proposition
school_class.display_rankings()

# Appel à la méthode de la question 3
school_class.rank_matter_1()

# Appels aux méthodes de la question 4
school_class.rank_matter_2()
school_class.rank_matter_3()

# Parcours via l'itérateur (Question 5)
print("--- Parcours via l'itérateur (Matière 1) ---")
for student in school_class:
    print(f"{student.name} : {student.grades['Mathématiques']}")

# Parcours via les nouveaux itérateurs (Question 6)
print("--- Parcours via l'itérateur (Matière 2) ---")
for student in school_class.iter_matter_2():
    print(f"{student.name} : {student.grades['Physique']}")

print("--- Parcours via l'itérateur (Matière 3) ---")
for student in school_class.iter_matter_3():
    print(f"{student.name} : {student.grades['Informatique']}")

# Vérification du décorateur de classe (Question récente)
print("--- Vérification de la 4ème matière ajoutée par le décorateur ---")
for student in school_class.students: # parcours brut
    print(f"{student.name} a {student.grades.get('Anglais')} en Anglais. (Moyenne automatiquement recalculée à {student.average:.2f})")

# Parcours via l'itérateur injecté par décorateur (Dernière question)
print("--- Parcours via l'itérateur injecté (Matière 4 - Anglais) ---")
for student in school_class.iter_matter_4():
    print(f"{student.name} : {student.grades.get('Anglais')} en Anglais")

# Vérification du Singleton (Dernière question)
print("--- Vérification du Singleton ---")
another_school_class = SchoolClass()
print(f"Les deux instances sont-elles identiques ? {school_class is another_school_class}")
print(f"Nombre d'élèves dans la 'nouvelle' instance : {len(another_school_class.students)}")
