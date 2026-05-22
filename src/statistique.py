from collections import deque
from paquets import Paquet


class Statistiques:

    def __init__(self):
        self.paquets_envoyes = 0
        self.paquets_perdus  = 0
        self.debit_cumule    = 0.0
        self.temps_transit   = 0.0
        # deque avec maxlen=10 : garde automatiquement les 10 derniers paquets
        self.historique      = deque(maxlen=10)

    def enregistrer_paquet(self, paquet: Paquet, succes: bool, transit: float):

        self.paquets_envoyes += 1

        if succes:
            self.debit_cumule  += paquet.taille
            self.temps_transit += transit
            self.historique.append(f"[OK]  {paquet} | transit={transit} ms")
        else:
            self.paquets_perdus += 1
            self.historique.append(f"[KO]  {paquet} | PERDU")

    def get_historique(self) -> list:
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

# Test de la classe

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
    print("\nAprès reset :")
    print(stats)