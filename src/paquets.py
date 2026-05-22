class Paquet:
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
        class Paquet:
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
from collections import deque

class Statistiques:
    """Collecte les statistiques de trafic du simulateur."""

    def __init__(self):
        self.paquets_envoyes = 0
        self.paquets_perdus  = 0
        self.debit_cumule    = 0.0
        self.temps_transit   = 0.0
        self.historique      = deque(maxlen=10)

    def enregistrer_paquet(self, paquet, succes, transit):
        self.paquets_envoyes += 1
        if succes:
            self.debit_cumule  += paquet.taille
            self.temps_transit += transit
            self.historique.append(f"[OK]  {paquet} | transit={transit} ms")
        else:
            self.paquets_perdus += 1
            self.historique.append(f"[KO]  {paquet} | PERDU")

    def get_historique(self):
        return list(self.historique)

    def reset(self):
        self.paquets_envoyes = 0
        self.paquets_perdus  = 0
        self.debit_cumule    = 0.0
        self.temps_transit   = 0.0
        self.historique.clear()

    def __str__(self):
        return (
            f"Statistiques(\n"
            f"  Paquets envoyés : {self.paquets_envoyes}\n"
            f"  Paquets perdus  : {self.paquets_perdus}\n"
            f"  Débit cumulé    : {self.debit_cumule} octets\n"
            f"  Temps transit   : {self.temps_transit} ms\n"
            f")"
        )
Et dans les autres fichiers qui ont besoin de Statistiques, l'import sera :
pythonfrom paquets import Paquet, Statistiques