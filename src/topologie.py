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
    def supprimer_equipement(self, ip):
        if ip in self.equipements:
            del self.equipements[ip]
    def ajouter_lien(self, lien):
        self.liens.append(lien)
    def supprimer_lien(self, ip1, ip2):
        for lien in self.liens :
            if(lien.equipiment1.ip = ip1 and lien.equipement2.ip = ip2) or (lien.equipiment1.ip = ip2 and lien.equipement2.ip = ip1)
                self.liens.remove(lien)
                break
    def get_equipement(self, ip):
        return self.equipements[ip]
    


    