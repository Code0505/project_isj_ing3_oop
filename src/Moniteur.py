from collections import deque
from datetime import datetime


class Moniteur:

    def __init__(self, topologie):

        self.topologie = topologie
        self.paquets_envoyes = 0
        self.paquets_perdus = 0
        self.debit_total = 0

        self.historique = deque(maxlen=10)

        self.statistiques_equipements = {}

        self.utilisation_liens = {}

    def ajouter_equipement(self, equipement):

        self.statistiques_equipements[equipement.nom] = {
            "statut": "ACTIF",
            "paquets_transmis": 0,
            "paquets_perdus": 0
        }

    def changer_statut(self, equipement):

        if equipement.est_actif():
            statut = "ACTIF"
        else:
            statut = "INACTIF"

        if equipement.nom in self.statistiques_equipements:
            self.statistiques_equipements[equipement.nom]["statut"] = statut

    def enregistrer_paquet(self, equipement, paquet):

        self.paquets_envoyes += 1

        self.debit_total += int(paquet.taille)

        if equipement.nom not in self.statistiques_equipements:
            self.ajouter_equipement(equipement)

        self.statistiques_equipements[equipement.nom]["paquets_transmis"] += 1

        self.historique.append({
            "heure": datetime.now().strftime("%H:%M:%S"),
            "source": paquet.source,
            "destination": paquet.destination,
            "protocole": paquet.protocole,
            "taille": int(paquet.taille),
            "priorite": int(paquet.priorite),
            "port_destination": str(paquet.port_destination)
        })

    def enregistrer_paquet_perdu(self, equipement):

        self.paquets_perdus += 1

        if equipement.nom not in self.statistiques_equipements:
            self.ajouter_equipement(equipement)

        self.statistiques_equipements[equipement.nom]["paquets_perdus"] += 1

    def mettre_a_jour_lien(self, lien, utilisation):

        self.utilisation_liens[str(lien)] = utilisation
    def get_equipements_actifs(self):
        return [e for e in self.topologie.equipements.values() if e.est_actif()]

    def collecter(self):

        return {
            "paquets_envoyes": self.paquets_envoyes,
            "paquets_perdus": self.paquets_perdus,
            "debit_total": self.debit_total,
            "equipements": self.statistiques_equipements
        }

    def get_taux_utilisation_liens(self):

        return self.utilisation_liens

    def afficher_historique(self):

        print("===== HISTORIQUE DES PAQUETS =====")

        if len(self.historique) == 0:
            print("Aucun paquet enregistré")
            return

        for paquet in self.historique:
            print(
                f"[{paquet['heure']}] "
                f"{paquet['source']} -> "
                f"{paquet['destination']} | "
                f"{paquet['protocole']} | "
                f"{paquet['taille']} octets | "
                f"Priorité {paquet['priorite']}"
                f" | Port de destination : {paquet['port_destination']}"
            )

    def generer_rapport(self, nom_fichier="rapport_simnet.txt"):

        with open(nom_fichier, "w", encoding="utf-8") as fichier:

            fichier.write("===== RAPPORT SIMNET =====")
            fichier.write(f"Date : {datetime.now()}")

            fichier.write("===== STATISTIQUES =====")
            fichier.write(f"Paquets envoyés : {self.paquets_envoyes}")
            fichier.write(f"Paquets perdus : {self.paquets_perdus}")
            fichier.write(f"Débit total : {self.debit_total} octets")

            fichier.write("===== EQUIPEMENTS =====")

            for nom, stats in self.statistiques_equipements.items():

                fichier.write(f"Equipement : {nom}")
                fichier.write(f"Statut : {stats['statut']}")
                fichier.write(f"Paquets transmis : {stats['paquets_transmis']}")
                fichier.write(f"Paquets perdus : {stats['paquets_perdus']}")

            fichier.write("===== UTILISATION DES LIENS =====")

            for lien, valeur in self.utilisation_liens.items():
                fichier.write(f"{lien} : {valeur}%")

            fichier.write("===== HISTORIQUE =====")

            for paquet in self.historique:

                ligne = (
                    f"[{paquet['heure']}] "
                    f"{paquet['source']} -> "
                    f"{paquet['destination']} | "
                    f"{paquet['protocole']} | "
                    f"{paquet['taille']} octets | "
                    f"Priorité {paquet['priorite']} | "
                    f"Port de destination : {paquet['port_destination']} | ")

                fichier.write(ligne)

        print(f"Rapport généré : {nom_fichier}")
