class Henkilo:
    def __init__(self, name, gender, friends, holiton, lihaton):
        self.name = name
        self.gender = gender
        self.friends = friends
        self.holiton = holiton
        self.lihaton = lihaton

Anna = Henkilo("Anna", "woman", [], "holiton", "lihaa")
Sanna = Henkilo("Sanna", "other", [Anna], "holillinen", "lihaa")
Janna = Henkilo("Janna", "woman", [Manna, Salli], "holillinen", "lihaa")
Manna = Henkilo("Manna", "woman", [], "holillinen", "kasvis")
Jaakko = Henkilo("Jaakko", "man", [Lalli], "holiton", "lihaa")
Kaakko = Henkilo("Kaakko", "man", [Jaakko, Salli], "holiton", "lihaa")
Saakko = Henkilo("Saakko", "other", [Malli, Lalli, Laakko], "holillinen", "lihaa")
Laakko = Henkilo("Laakko", "man", [Saakko], "holillinen", "kasvis")
Salli = Henkilo("Salli", "woman", [Kaakko, Janna], "holiton", "lihaa")
Lalli = Henkilo("Lalli", "man", [Paavi], "holillinen", "piispa")
Malli = Henkilo("Malli", None, [Saakko], "holillinen", "lihaa")
Nalli = Henkilo("Nalli", "other", [], "holillinen", "kasvis")

testiukkoja = [Sanna, Janna, Manna, Jaakko, Anna, Kaakko, Saakko, Laakko, Salli, Lalli, Malli, Nalli]
def tuolista():
    return testiukkoja