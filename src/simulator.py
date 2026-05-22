from statistique import Statistiques


class SimulateurTrafic:
    """Simule la transmission de paquets à travers une topologie réseau.

    Orchestre le calcul de chemin et la transmission saut par saut, puis
    délègue la collecte des métriques à une instance de :class:`Statistiques`.

    Attributes:
        topologie: Objet topologie exposant ``trouver_chemin`` et ``get_lien``.
        statistiques (Statistiques): Agrégateur des métriques de transmission.
    """

    def __init__(self, topologie):
        """Initialise le simulateur avec une topologie réseau.

        Args:
            topologie: Instance de topologie réseau utilisée pour le routage.
        """
        self.topologie    = topologie
        self.statistiques = Statistiques()

    def calculer_chemin(self, source, destination):
        """Trouve le chemin entre deux équipements via la topologie.

        Args:
            source: Identifiant de l'équipement source.
            destination: Identifiant de l'équipement destination.

        Returns:
            list: Séquence ordonnée d'équipements du source au destination,
                  ou liste vide si aucun chemin n'existe.
        """
        return self.topologie.trouver_chemin(source, destination)

    def transmettre(self, paquet, chemin):
        """Transmet le paquet saut par saut le long du chemin.

        Cumule les latences de chaque lien traversé et enregistre le résultat
        dans les statistiques.

        Args:
            paquet: Instance de Paquet à transmettre.
            chemin (list): Séquence d'équipements formant le chemin de routage.

        Returns:
            bool: True si le paquet est livré, False si le chemin est vide.
        """
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
        """Calcule le chemin puis transmet le paquet.

        Combine :meth:`calculer_chemin` et :meth:`transmettre` en une seule
        opération de haut niveau.

        Args:
            paquet: Instance de Paquet à envoyer (doit exposer ``source``
                    et ``destination``).

        Returns:
            list: Chemin parcouru (peut être vide si aucun chemin trouvé).
        """
        chemin = self.calculer_chemin(paquet.source, paquet.destination)
        self.transmettre(paquet, chemin)
        return chemin
