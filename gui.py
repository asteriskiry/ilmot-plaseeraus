from tkinter import *
from Plaseeraus import plaseeraus
from Ukkelit import tuolista

class GUI(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.title("Automaattinen plaseerausjärjestelmä")
        
        # Luodaan framet
        self.frame1 = Frame(self)
        self.frame2 = Frame(self)

        # Hoidellaan framejen layout
        self.frame1.pack(fill="x", padx=5, pady=5)
        self.frame2.pack(fill="both", expand=True, padx=5, pady=5)

        self.pack(fill="both", expand=True)

        # Olion attribuutit
        self.koko = StringVar()
        self.poydat = StringVar()
        self.buttonit = []
        self.labels = []

        # Kutsutaan vaihetta jossa luodaan nappulat sun muut
        self.content()

    def content(self):
        
        # Luodaan ykkös frameen tekstit, syötekentät sekä submit button
        lblOtsikko = Label(self.frame1, text="Syötä osallistujamäärä:").pack(pady=3)
        eKoko = Entry(self.frame1, textvariable=self.koko).pack()
        lblOtsikko2 = Label(self.frame1, text="Syötä pöytien määrä:").pack(pady=2)
        ePoydat = Entry(self.frame1, textvariable=self.poydat).pack()     
        bSuorita = Button(self.frame1, text="Suorita", command=self.suorita).pack(pady=2)

    # Submit buttonin toiminnallisuus
    def suorita(self):
        # Ruudun ja listojen tyhjennys uutta 'Suorita' painallusta varten
        if len(self.buttonit) > 0:
            for i in self.buttonit:
                i.destroy()
        self.buttonit.clear()
        if len(self.labels) > 0:
            for i in self.labels:
                i.destroy()
        self.labels.clear()

        # Haetaan olion attribuuteista arvot sekä muunnetaan ne floatista inttiin
        try:
            osallistujat = int(self.koko.get())
            poydat = int(self.poydat.get())
        except ValueError:
            return
        poytaosallistujat = int(osallistujat/poydat)
        henkilot = list(tuolista())

        # Iteroidaan osallistujat "pöytiin" eli oikeille paikoille framea
        # Tallennetaan osallistuja buttonit listaan, jotta osallistujia voidaan myöhemmin käsitellä
        paikkanro = 0
        for j in range(poydat):
            ypos = 30
            xpos = 200 * j
            self.labels.append(Label(self.frame2, text="Pöytä " + str(j+1)))
            self.labels[j].place(x = xpos + 35, y = 0)
            for i in range(poytaosallistujat):
                valittuhenkilo = henkilot[0]
                self.buttonit.append(Button(self.frame2, text=valittuhenkilo.name, width = 6, command=lambda c=paikkanro, d=valittuhenkilo: self.lisatiedot(c, d)))
                if (i % 2 != 0):
                    xpos += 60
                    ypos -= 28
                    self.buttonit[paikkanro].place(x = xpos, y = ypos)
                    xpos -= 60
                else:
                    self.buttonit[paikkanro].place(x = xpos, y = ypos)
                ypos += 28
                paikkanro += 1
                henkilot.remove(valittuhenkilo)
    
    def lisatiedot(self, paikkanro, vhenkilo):
        top = Toplevel()
        top.geometry('220x170')
        top.title("Lisätiedot")
        nimi = "Nimi: " + vhenkilo.name
        juoma = "Juoma: " + vhenkilo.holiton
        ruoka = "Ruoka: " + vhenkilo.lihaton
        paikka = "Paikka: " + str(paikkanro)

        lisatiedot = Label(top, text="Lisätiedot:").pack(pady=2)
        paikkanumero = Label(top, text=paikka).pack(pady=2)
        henknimi = Label(top, text=nimi).pack(pady=2)
        henkjuoma = Label(top, text=juoma).pack(pady=2)
        henkruoka = Label(top, text=ruoka).pack(pady=2)
        pois = Button(top, text="Pois", command=top.destroy).pack(pady=2)



# Ikkunan alustus ja suorittaminen
if __name__ == '__main__':
    mainWindow = Tk()
    mainWindow.geometry('600x380')
    mainFrame = GUI(mainWindow)
    mainWindow.mainloop()

