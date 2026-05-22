from collections import deque
# from Paquets import Paquet


class Statistiques:
    """Collecte et agrège les métriques de transmission des paquets réseau.

    Attributes:
        paquets_envoyes (int): Nombre total de paquets émis (succès + pertes).
        paquets_perdus (int): Nombre de paquets non livrés.
        debit_cumule (float): Somme des tailles (en octets) des paquets livrés.
        temps_transit (float): Somme des temps de transit (en ms) des paquets livrés.
        historique (deque): Fenêtre glissante des 10 derniers événements de transmission.
    """

    def __init__(self):
        """Initialise les compteurs et l'historique à zéro."""
        self.paquets_envoyes = 0
        self.paquets_perdus  = 0
        self.debit_cumule    = 0.0
        self.temps_transit   = 0.0
        # deque avec maxlen=10 : garde automatiquement les 10 derniers paquets
        self.historique      = deque(maxlen=10)

    def enregistrer_paquet(self, paquet, succes: bool, transit: float):
        """Enregistre le résultat de la transmission d'un paquet.

        Met à jour les compteurs et ajoute une entrée dans l'historique.

        Args:
            paquet: Instance de Paquet transmis.
            succes (bool): True si le paquet a été livré, False s'il est perdu.
            transit (float): Temps de transit en millisecondes (0.0 si paquet perdu).
        """
        self.paquets_envoyes += 1

        if succes:
            self.debit_cumule  += paquet.taille
            self.temps_transit += transit
            self.historique.append(f"[OK]  {paquet} | transit={transit} ms")
        else:
            self.paquets_perdus += 1
            self.historique.append(f"[KO]  {paquet} | PERDU")

    def get_historique(self) -> list:
        """Retourne les 10 derniers événements de transmission.

        Returns:
            list[str]: Liste des entrées d'historique sous forme de chaînes.
        """
        return list(self.historique)

    def reset(self):
        """Remet tous les compteurs à zéro et vide l'historique."""
        self.paquets_envoyes = 0
        self.paquets_perdus  = 0
        self.debit_cumule    = 0.0
        self.temps_transit   = 0.0
        self.historique.clear()

    def __str__(self):
        """Retourne un résumé lisible des statistiques courantes.

        Returns:
            str: Représentation multi-lignes des métriques agrégées.
        """
        return (
            f"Statistiques(\n"
            f"  Paquets envoyés : {self.paquets_envoyes}\n"
            f"  Paquets perdus  : {self.paquets_perdus}\n"
            f"  Débit cumulé    : {self.debit_cumule} octets\n"
            f"  Temps transit   : {self.temps_transit} ms\n"
            f")"
        )

# Test de la classe
"""
if __name__ == "__main__":

    stats = Statistiques()

    p1 = Paquet("192.168.1.1", "10.0.0.1", "TCP", 512, 2)
    p2 = Paquet("192.168.1.2", "10.0.0.2", "UDP", 256, 1)
    p3 = Paquet("192.168.1.3", "10.0.0.3", "ICMP", 64, 3)

    stats.enregistrer_paquet(p1, succes=True,  transit=1.5)
    stats.enregistrer_paquet(p2, succes=False, transit=0.0)
    stats.enregistrer_paquet(p3, succes=True,  transit=2.3)

    print(stats)

    print("Historique :")
    for entree in stats.get_historique():
        print(f"  {entree}")

    stats.reset()
    print("Après reset :")
    print(stats)"""