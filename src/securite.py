from datetime import datetime
from equipements import Equipement
from Paquets import Paquet

class RegleFiltrage:
    '''
    Représente une règle utilisée par le firewall pour authoriser ou bloquer des paquets
    '''
    def __init__(self, action, ip_source, protocole, port_destination, plage_reseau):
        self.action = action
        self.ip_source = ip_source
        self.protocole = protocole
        self.port_destination = port_destination
        self.plage_reseau = plage_reseau

    # Première difficulté que je rencontre : 
    # Dans notre diagramme de classe de départ, la classe Paquet ne prennait pas en paramètre le port de destination du paquet ce qui limitait donc les options de filtrage pour avoir accès au réseau. 
    # Au départ j'ai fait une version sans cet attribut et sans filtrage par plage réseau et ça marchait mais vu que ça ne répondait pas aux attentes du tp, nous avons modifier notre diagramme et par conséquent j'ai dû refaire ma méthode "correspond" mais cette fois j'ai été assisté par une IA car je ne trouvais pas comment filtrer par plage réseau.
    
    """ def correspond(self, paquet):
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
        ) """
    
    def correspond(self, package:Paquet):
        if self.ip_source != "*" and self.ip_source != package.source:
            return False
        if self.protocole != "*" and self.protocole != package.protocole:
            return False
        if self.port_destination != "*" and self.port_destination != package.port_destination:
            return False
        if self.plage_reseau != "*":
            if not package.destination.startswith(self.plage_reseau):
                return False
        return True
    
    def __str__(self):
        return(
            f"Règle(Action = {self.action}, "
            f"IP Source = {self.ip_source}, "
            f"Protocole = {self.protocole}, "
            f"Port de destination = {self.port_destination}, "
            f"Plage réseau = {self.plage_reseau})"
        )
    
class EntreeJournal:
    ''' 
    Lorsqu'un paquet est envoyé, ses informations sont stockés en tant qu'une entrée du journal du firewall 
    '''
    def __init__(self, package: Paquet, decision: str):
        self.horodatage = datetime.now()
        self.package = package
        self.decision = decision
    def __str__(self):
        return( f"{self.horodatage} :: {self.package} :: Decision... {self.decision}" )
    
class Firewall(Equipement):
    '''
    Cette classe représente un firewall chargé d'inspecter les paquets et d'appliquer des règles de filtrage
    '''
    def __init__(self, nom, marque, adresse_ip, login, mot_de_passe):
        super().__init__(nom, marque, adresse_ip )
        self.regles = []
        self.journal = []
        self.login = login
        self.mot_de_passe = mot_de_passe
        self.paquets_envoyes = 0
        self.paquets_envoyes = 0
    
    def activer(self):
        self._statut = True
        return f"{self._nom} actif"
 
    def desactiver(self):
        self._statut = False
        return f"{self._nom} inactif"
 
    def est_actif(self):
        return self._statut
    def authentifier(self, login, password):
        if self.login == login and self.mot_de_passe == password:
            print("Authentification reussie.")
            return True
        print("Echec d'authentification.")
        return False
    def ajouter_regle(self, rule):
        self.regles.append(rule)
    def supprimer_regle(self, i):
        if i >= 0 and len(self.regles) - 1 >= i:
            self.regles.pop(i)
    def inspecter_paquet(self, package):
        for rule in self.regles:
            if rule.correspond(package):
                if rule.action == "authoriser":
                    self.journaliser(package, "AUTHORISE")
                    return True
                elif rule.action == "bloquer":
                    self.journaliser(package, "BLOQUE")
                    return False
    def journaliser(self, package: Paquet, decision: str):
        entree = EntreeJournal(package, decision)
        self.journal.append(entree)
    def get_journal(self):
        return self.journal
    def __str__(self):
        base = super().__str__()
        return f"{base} | Regles: {len(self.regles)}"
        
        

    
