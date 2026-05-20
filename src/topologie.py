from equipements import Equipement
class Lien: 
    def __init__(self, equipement1, equipement2, bande_passante, latence):
        self.equipement1 = equipement1 
        self.equipement2 = equipement2
        self.bande_passante = bande_passante
        self.latence = latence
    def get_equipements(self):
        return(self.equipement1, self.equipement2)
    def __str__(self):
        return f"{self.equipement1.nom} et {self.equipement2.nom}  Bande Passante : {self.bande_passante}Mbps {self.latence}"
class Topologie:
    def __init__(self):
        self.equipements = {}
        self.liens = [] 
    def ajouter_equipement(self, equipement):
        self.equipements[equipement.ip] = equipement
    def supprimer_equipement():
        
    