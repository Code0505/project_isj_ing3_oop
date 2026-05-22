from equipements import Routeur, Switch, Serveur,PointAccesWifi, Terminal
from paquets import Paquet,SimulateurTrafic
from topologie import Topologie, Lien
from securite import RegleFiltrage,Firewall
# from simulateur import SimulateurTrafic
from Moniteur import Moniteur


class MenuInteractif:

    def __init__(self):
        self.topologie = Topologie()
        self.simulateur = SimulateurTrafic(self.topologie)
        self.moniteur = Moniteur(self.topologie)

    def lancer(self):
        print("=" * 50)
        print("   SIMNet")
        print("   Simulateur de Reseau Intelligent")
        print("=" * 50)

        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Gerer les equipements")
            print("2. Simuler le trafic reseau")
            print("3. Gerer le Firewall")
            print("4. Afficher les statistiques")
            print("5. Generer un rapport")
            print("6. Afficher la topologie")
            print("0. Quitter")
            print("==========================")

            choix = input("\nChoix: ")

            if choix == "1":
                self.menu_equipements()
            elif choix == "2":
                self.menu_trafic()
            elif choix == "3":
                self.menu_firewall()
            elif choix == "4":
                self.menu_statistiques()
            elif choix == "5":
                self.moniteur.generer_rapport()
            elif choix == "6":
                self.topologie.afficher()
            elif choix == "0":
                print("\nAu revoir !")
                break
            else:
                print("Choix invalide, reessayez.")

    def menu_equipements(self):
        while True:
            print("\n--- Gestion des equipements ---")
            print("1. Ajouter un equipement")
            print("2. Supprimer un equipement")
            print("3. Ajouter un lien")
            print("4. Supprimer un lien")
            print("0. Retour")

            c = input("Choix: ")

            if c == "1":
                self.ajouter_equipement()
            elif c == "2":
                ip = input("IP: ")
                self.topologie.supprimer_equipement(ip)
            elif c == "3":
                self.ajouter_lien()
            elif c == "0":
                break
            else:
                print("Choix invalide.")

    def ajouter_equipement(self):
        t = input("Type: ")
        nom = input("Nom: ")
        marque = input("Marque: ")
        adresse_ip = input("Adresse IP: ")

        if t == "Routeur":
            e = Routeur(nom, marque,adresse_ip)
        elif t == "Switch":
            e = Switch(nom, marque, adresse_ip)
        elif t == "Serveur":
            e = Serveur(nom, marque, adresse_ip)
        elif t == "Firewall":
            login = input("Login: ")
            mdp = input("Mot de passe : ")
            e = Firewall(nom, marque,adresse_ip, login, mdp)
        elif t == "PointAccesWifi":
            ssid = input("SSID: ")
            e = PointAccesWifi(nom, marque, adresse_ip, ssid)
        elif t == "Terminal":
            type_t = input("Type: ")
            e = Terminal(nom, marque, adresse_ip, type_t)
        else:
            print("Type invalide.")
            return
        e.activer()
        self.topologie.ajouter_equipement(e)

    def ajouter_lien(self):
        ip1 = input("IP1: ")
        ip2 = input("IP2: ")

        e1 = self.topologie.get_equipement(ip1)
        e2 = self.topologie.get_equipement(ip2)

        if not e1 or not e2:
            print("Un des equipements est introuvable.")
            return

        bp = float(input("Bande passante(Mbps) : "))
        lat = float(input("Latence (ms) : "))

        lien = Lien(e1, e2, bp, lat)
        self.topologie.ajouter_lien(lien)
    def _supprimer_lien(self):
        ip1 = input("IP equipement 1 : ").strip()
        ip2 = input("IP equipement 2 : ").strip()
        self.topologie.supprimer_lien(ip1, ip2)

    def menu_trafic(self):
        print("\n--- Simulation de trafic ---")
        print("Protocoles : TCP, UDP, ICMP")
        src = input("Source: ")
        dst = input("Destination: ")
        proto = input("Protocole: ").upper()
        taille = input("Taille: ")
        prio = input("Priorite: ")
        port = input("Port: ")

        p = Paquet(src, dst, proto, taille, prio, port)

        chemin = self.simulateur.envoyer_paquet(p)

        if chemin:
            print(f"Chemin: {' -> '.join(chemin)}")
            print("Paquet livre avec succes.")
        else:
           print("Destination inatteignable ou aucun chemin trouver.")
    

    def menu_firewall(self):
        
        fw = None
        for e in self.topologie.equipements.values():
            if isinstance(e, Firewall):
                fw = e
                break

        if not fw:
            print("Aucun Firewall dans la topologie.")
            return

        print(f"\n--- Firewall : {fw} ---")
        login = input("Login : ")
        mdp = input("Mot de passe : ")

        if not fw.authentifier(login, mdp):
            print("Acces refuse.")
            return

        while True:
            print("\n--- Gestion du firewall ---")
            print("1. Ajouter une règle")
            print("2. Supprimer une règle")
            print("3. Consulter le journal")
            print("0. Retour")

            c = input("Choix: ")

            if c == "1":
                action = input("Action: ")
                adresse_ip = input("IP: ")
                proto = input("Proto: ")
                port = input("Port: ")
                plage = input("Plage: ")
                r = RegleFiltrage(action, adresse_ip, proto, port, plage)
                fw.ajouter_regle(r)
            elif c == "2":
                i = int(input("Index: "))
                fw.supprimer_regle(i)
            elif c == "3":
                for j in fw.get_journal():
                    print(j)
            elif c == "0":
                print("Choix invalide.")
                break

    def menu_statistiques(self):
        print("\n--- Statistiques reseau ---")
 
        stats = self.moniteur.collecter()
        
        print(f"Paquets envoyes : {stats['paquets_envoyes']}")
        print(f"Paquets perdus  : {stats['paquets_perdus']}")
        print(f"Debit total     : {stats['debit_total']} octets")

        taux= self.moniteur.get_taux_utilisation_liens()
        
        if not taux:
            print("  Aucune donnee.")
        else:
            for lien, valeur in taux.items():
                print(f"  {lien} : {valeur}%")
        
        print("\nEquipements actifs :")
        actifs = self.moniteur.get_equipements_actifs()
        if not actifs:
            print("  Aucun equipement actif.")
        else:
            for equip in actifs:
                print(f"  {equip}")
 
        print("\nHistorique (10 derniers paquets) :")
        historique = self.simulateur.statistiques.get_historique()
        if not historique:
            print("  Aucun paquet enregistre.")
        else:
            for entree in historique:
                print(f"  {entree}")
 
if __name__ == "__main__":
    menu = MenuInteractif()
    menu.lancer()
