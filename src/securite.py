from datetime import datetime
from paquets import Paquet
from equipement import Equipement

class RegleFiltrage:
    def __init__(self, action, ip_source, protocole, port_destination, plage_reseau):
        self.action = action
        self.ip_source = ip_source
        self.protocole = protocole
        self.port_destination = port_destination
        self.plage_reseau = plage_reseau
    def correspond(self, paquet):
        if self.ip_source != paquet.source:
            return False
        if self.protocole != paquet.protocole:
            return False
        return True
    def __str__(self):
        return(
            f"Règle(Action = {self.action}, "
            f"IP Source = {self.ip_source}, "
            f"Protocole = {self.protocole})"
        )
    
class EntreeJournal:
    def __init__(self, paquet, decision):
        self.horodatage = datetime.now()
        self.paquet = paquet
        self.decision = decision
    def __str__(self):
        return( f"{self.horodatage} :: {self.paquet} :: Decision... {self.decision}" )
    
class Firewall(Equipement):
    def __init__(self, ip, nom, marque, login, mot_de_passe):
        
