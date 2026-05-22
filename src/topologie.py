from equipements import Equipement
class Lien: 
    def __init__(self, equipement1:Equipement, equipement2:Equipement, bande_passante, latence):
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
    def ajouter_equipement(self, equipement:Equipement):
        self.equipements[equipement.ip] = equipement
        print(f"Equipement {equipement.nom} ({equipement.ip}) ajoute.")
    def supprimer_equipement(self, ip):
        if ip in self.equipements:
            del self.equipements[ip]
            self.liens = [l for l in self.liens
                          if l.equipement1.ip != ip and l.equipement2.ip != ip]
            print(f"Equipement {self.equipements[ip].nom} supprime.")
        else:
            print(f"Equipement {ip} introuvable.")
    def ajouter_lien(self, lien):
        self.liens.append(lien)
    def supprimer_lien(self, ip1, ip2):
        for lien in self.liens :
            if(lien.equipement1.ip == ip1 and lien.equipement2.ip == ip2) or (lien.equipement1.ip == ip2 and lien.equipement2.ip == ip1):
                self.liens.remove(lien)
                break
    def get_lien(self, ip1, ip2):
        for lien in self.liens:
            if ((lien.equipement1.ip == ip1 and lien.equipement2.ip == ip2) or
                    (lien.equipement1.ip == ip2 and lien.equipement2.ip == ip1)):
                return lien
        return None
    def get_equipement(self, ip):
        return self.equipements[ip]
    def get_voisins(self, ip):
        voisins=[]
        for lien in self.liens: 
            if(lien.equipement1.ip == ip):
                voisins.append(lien.equipement2)
            elif(lien.equipement2.ip == ip):
                voisins.append(lien.equipement1)
        return voisins
    def afficher(self):
        print("TOPOLOGIE DU RESEAU") 
        for equip in self.equipements.values():
            print(equip)
        for lien in self.liens:
            print(lien) 
    def trouver_chemin(self, source, destination):
        visite = []
        file = [[source]]
        while file :
            chemin = file.pop(0)
            ip_actu = chemin[-1]
            if(ip_actu == destination):
                return chemin
            if(ip_actu not in visite):
                visite.append(ip_actu)
                for voisin in self.get_voisins(ip_actu):
                    if(voisin.ip not in visite):
                        file.append(chemin + [voisin.ip])
        return [] 
    
    
                
        


    