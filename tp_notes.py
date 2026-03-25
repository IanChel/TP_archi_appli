class Etudiant:
    def __init__(self, nom, note_mathematiques, note_physique, note_informatique):
        self.nom = nom
        self.notes = {
            "Mathématiques": note_mathematiques,
            "Physique": note_physique,
            "Informatique": note_informatique
        }
    
    @property
    def moyenne(self):
        return sum(self.notes.values()) / len(self.notes)

class GroupeEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
