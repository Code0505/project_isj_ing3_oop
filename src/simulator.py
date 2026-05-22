""" class SimulateurTrafic:
    # Simule la transmission de paquets à travers la topologie.

    def __init__(self, topologie):
        self.topologie   = topologie
        self.statistiques = Statistiques()

    def calculer_chemin(self, source, destination):
    #Trouve le chemin entre source et destination via la topologie.
        return self.topologie.trouver_chemin(source, destination)

    def transmettre(self, paquet, chemin):
        #
        Transmet le paquet saut par saut le long du chemin.
        Retourne True si le paquet est livré, False sinon.
        
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
        #
        Calcule le chemin puis transmet le paquet.
        Retourne le chemin parcouru sous forme de liste.
    
        chemin = self.calculer_chemin(paquet.source, paquet.destination)
        self.transmettre(paquet, chemin)
        return chemin"""