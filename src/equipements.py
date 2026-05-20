from paquets import Paquet
from abc import ABC, abstractmethod


class Equipement(ABC):
    """ Classe parent de tous les equipements reseau. """

    def __init__(self,nom,marque,adresse_ip):
        
        self._nom = str(nom) 
        self._marque = str(marque)
        self._ip = str(adresse_ip) 
        self._statut = False
    @abstractmethod
    def activer(self):
        self._statut = True
        return f"{self._nom} active "
    @abstractmethod
    def desactiver(self):
        self._statut = False
        return f"{self._nom} desactive "
    @abstractmethod
    def est_actif(self):
        return self._statut
    @abstractmethod
    def __str__(self):
        if self._statut:
            statut= "ACTIF" 
        else:
            statut= "INACTIF"
        return f"[{statut}] {self._nom} ({self._marque}) -- {self._ip}"

    
class Routeur(Equipement):
    """ Routeur reseau et herite d' Equipement"""
    def __init__ (self,nom,marque,adresse_ip):
        super().__init__(nom,marque,adresse_ip)
        # la table de routage est un dictionaire
        self._table_routage= {}
    
    def activer(self):
        self._statut = True
        return f"{self._nom} actif "
    
    def desactiver(self):
        self._statut = False
        return f"{self._nom} Inactif "
   
    def est_actif(self):
        return self._statut
    def ajouter_route(self,destination,passerelle,interface):
        """Permet d'ajouter une entree a la table de routage. """
        self._table_routage[destination] = {
            'passerelle': passerelle,
            'interface': interface 
        }
        print (f" Route ajoutee : {destination} via {passerelle} ({interface})")
    def supprimer_route(self,destination):
        """Permet de supprimer une route"""
        if destination in self._table_routage:
            del self._table_routage[destination]
            print(f"Route {destination} supprimee.")
        else:
            print(f"Route {destination} introuvable.")
    def get_table_routage(self):
        """ Retourne la table de routage complete."""
        return self._table_routage
    def routeur_paquet(self,paquet):
        """Trouve la passerelle pour un paquet"""
        for reseau,info in self._table_routage.items():
            if paquet.startswith(reseau.split('/')[0].rsplit('.',1)[0]):
                return info['passerelle']
        return "passerelle_par_defaut"
    def __str__(self):
        base = super().__str__()
        return f"{base} | Routes: {len(self._table_routage)}"

class Switch(Equipement):
    """Switch reseau - gere les VLANs."""
    def __init__(self, nom, marque, adresse_ip):
        super().__init__(nom, marque, adresse_ip)
        self._vlans = {1: 'default'} # Vlan 1 par defaut
        self._ports = {}
    
    def activer(self):
        self._statut = True
        return f"{self._nom} actif "
    
    def desactiver(self):
        self._statut = False
        return f"{self._nom} Inactif "
   
    def est_actif(self):
        return self._statut
    def ajouter_vlan(self,vlan_id,nom):
        """Ajoute un VLAN. vlan_id doit etre entre 1 et 4094"""
        if not (1 <= vlan_id <= 4094):
            print(f"Erreur: VLAN ID {vlan_id} invalide")
            print(f"Entrez un id dans l'interval (1-4094)")
            return
        self._vlans[vlan_id]=nom
        print(f"VLAN {vlan_id} ({nom}) ajoute avec succes")

    def supprimer_vlan(self, vlan_id):
        if vlan_id == 1:
            print(f" Impossible de supprimer le VLAN 1 (defaut).")
            return 
        if vlan_id in self._vlans:
            del self._vlans[vlan_id]
            print(f"VLAN {vlan_id} supprimer")
        else:
            print(f"VLAN {vlan_id} introuvable")
    def assigner_port(self,port,vlan_id):
        if vlan_id not in self._vlans:
            print(f"Erreur : VLAN {vlan_id} inexistant.")
            return 
        self._ports[port] = vlan_id
        print(f" Port {port} - VLAN {vlan_id} ({self._vlans[vlan_id]}).")
    def get_vlans(self):
        return self._vlans
    def __str__(self):
        base = super().__str__()
        return f"{base} | VLANs: {len(self._vlans)}"
    
class Serveur(Equipement):
    """Serveur reseau - expose des services."""
    def __init__(self,nom,marque,adresse_ip):
        super().__init__(nom,marque,adresse_ip)
        self._services = []
    def exposer_service(self,service):
        """Utiliser pour demarrer un service sur ce serveur."""
        service = service.upper()
        if service in self._services:
            print(f"{service} deja expose.")
        else:
            self._services.append(service)
            print(f" Service {service} demarre sur {self._nom}.")
    def retirer_service(self,service):
        service=service.upper()
        if service in self._services:
            self._services.remove(service)
            print(f"Services {service} arrete.")
        else:
            print(f" Service {service} non trouve. ")
    def get_services(self):
        return self._services
    
    def activer(self):
        self._statut = True
        return f"{self._nom} actif "
    
    def desactiver(self):
        self._statut = False
        return f"{self._nom} Inactif "
   
    def est_actif(self):
        return self._statut
    def __str__(self):
        base = super().__str__()
        if self._services:
            service = ",".join(self._services) 
        else:
            service = "aucun"
        return f"{base} | Services offert: [{service}]"
class Terminal(Equipement):
    """Terminal Reseau utilisateur final"""
    def __init__(self,nom,marque,adresse_ip,type_terminal):
        super().__init__(nom,marque,adresse_ip)
        self._type_terminal =str(type_terminal)
    def envoyer_paquet(self,paquet:Paquet):
        if not self._statut:
            print(f"{self._nom} est eteint, impossible d'envoyer.")
            return
        print(f"{self._nom} envoie: {paquet}")
     
    def activer(self):
        self._statut = True
        return f"{self._nom} actif "
    
    def desactiver(self):
        self._statut = False
        return f"{self._nom} Inactif "
   
    def est_actif(self):
        return self._statut
   
    def __str__(self):
        base = super().__str__()
        return f"{base} | Type: {self._type_terminal}"
    

class PointAccesWifi(Equipement):
    """Point d'access Wi-Fi - diffuse un reseau sans fil."""
    def __init__(self,nom,marque,adresse_ip,ssid,canal = 6,frequence = 2.4):
        super().__init__(nom,marque,adresse_ip)
        self._ssid= str(ssid)
        self._canal= int(canal)
        self._frequence= float(frequence)
    
    def activer(self):
        self._statut = True
        return f"{self._nom} actif "
    
    def desactiver(self):
        self._statut = False
        return f"{self._nom} Inactif "
   
    def est_actif(self):
        return self._statut
    def get_ssid(self):
        return self._ssid
    def set_canal(self,canal,frequence=None):
        """Permet de changer le canal et la frequence si une valeur ne l'est pas attribuer"""
        if canal in {1,2,3,4,5,6,7,8,9,10,11,12,13,14}:
            self._canal=canal
        else:
            print(f"Erreur:numero de canal dans l'interval [1,14]")
        if frequence is not None:
            self._frequence=frequence
        print(f"Canal mis a {self._canal} ({self._frequence} GHz).")
    def __str__(self):
        base=super().__str__()
        return f"{base} | SSID:{self._ssid} | Canal: {self._canal} ({self._frequence}GHz) "
    
    
# testeur de classe

if __name__ =="__main__":
    te= Terminal("PC_Bureau","Lenovo","192.168.1.100","Bureau")
    te.activer()
    p= Paquet("192.168.1.10","10.0.0.1","TCP","512","1","80")

    te.envoyer_paquet(p)



    ap= PointAccesWifi("AP_Labo","Tp-Link","192.168.0.1","GTR3-Lab",canal=9)
    ap.activer()
    print(ap.get_ssid())
    print(ap)
    ap.set_canal(11,2.4)
    serv= Serveur("SRV_Web","Dell","10.0.2.1")
    serv.activer()
    serv.exposer_service("https")
    serv.exposer_service("SSh")
    print(serv)
    print(serv.get_services())
    sw= Switch("SW_Distrib","HP","10.0.0.2")
    sw.activer()
    sw.ajouter_vlan(10,"RH")
    sw.ajouter_vlan(-1,"IT")
    sw.assigner_port(1,10)
    sw.assigner_port(1,35)
    print(sw)
    print(sw.get_vlans())

    r=Routeur("R_Core","Cisco","10.0.0.1")
    r.activer()
    r.ajouter_route("192.168.1.0/24","192.168.1.254","eth0")
    r.ajouter_route("10.0.0.0/8","10.0.0.254","eth1")
    print(r)
    print(r.get_table_routage())
            