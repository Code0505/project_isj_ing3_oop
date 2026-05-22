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
