
from statistique import Statistiques

class Paquet:
    """
     Paquet répresente un paquet circulant dans le réseau
    """
    def __init__(self, source, destination, protocole, taille, priorite, port_destination):
        self.source = source
        self.destination = destination
        self.protocole = protocole
        self.taille = taille
        self.priorite = priorite
        self.port_destination = port_destination
    def __str__(self):
        return( 
            f"Paquet(Source = {self.source}, " 
            f"Destination = {self.destination}, "
            f"Protocole = {self.protocole}, "
            f"Taille = {self.taille} octets, "
            f"Priorité = {self.priorite}, "
            f"Port = {self.port_destination})"
        )
class SimulateurTrafic:

    def __init__(self, topologie):
        self.topologie   = topologie
        self.statistiques = Statistiques()

    def calculer_chemin(self, source, destination):
        return self.topologie.trouver_chemin(source, destination)

    def transmettre(self, paquet, chemin):
        """Transmet le paquet saut par saut. Retourne True si livre."""
        if not chemin:
            self.statistiques.enregistrer_paquet(paquet, succes=False, transit=0.0)
            return False

        print(f"Transmission de : {paquet}")
        temps_total = 0.0

        for i in range(len(chemin) - 1):
            eq1 = chemin[i]
            eq2 = chemin[i + 1]
            lien = self.topologie.get_lien(eq1, eq2)
            if lien:
                temps_total += lien.latence
            print(f"  --> {eq2}")

        self.statistiques.enregistrer_paquet(paquet, succes=True, transit=temps_total)
        return True

    def envoyer_paquet(self, paquet):
        chemin = self.calculer_chemin(paquet.source, paquet.destination)
        self.transmettre(paquet, chemin)
        return chemin
