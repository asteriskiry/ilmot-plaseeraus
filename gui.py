from tkinter import *

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
        self.buttonit = []

        # Haetaan olion attribuuteista arvot sekä muunnetaan ne floatista inttiin
        osallistujat = int(self.koko.get())
        poydat = int(self.poydat.get())
        poytaosallistujat = int(osallistujat/poydat)

        # Iteroidaan osallistujat "pöytiin" eli oikeille paikoille framea
        # Tallennetaan osallistuja buttonit listaan, jotta osallistujia voidaan myöhemmin käsitellä
        paikkanro = 0
        for j in range(poydat):
            ypos = 20
            xpos = 200 * j
            for i in range(poytaosallistujat):
                self.buttonit.append(Button(self.frame2, text="Nimi", command=lambda c=paikkanro: self.lisatiedot(c)))
                if (i % 2 != 0):
                    xpos += 40
                    ypos -= 28
                    self.buttonit[paikkanro].place(x = xpos, y = ypos)
                    xpos -= 40
                else:
                    self.buttonit[paikkanro].place(x = xpos, y = ypos)
                ypos += 28
                paikkanro += 1
    
    def lisatiedot(self, paikkanro):
        top = Toplevel()
        top.title("Lisätiedot")
        paikka = "Paikka: " + str(paikkanro)

        lisatiedot = Label(top, text="Lisätiedot:").pack(pady=2)
        paikkanumero = Label(top, text=paikka).pack(pady=2)
        pois = Button(top, text="Pois", command=top.destroy).pack(pady=2)



# Ikkunan alustus ja suorittaminen
mainWindow = Tk()
mainWindow.geometry('600x380')

mainFrame = GUI(mainWindow)

mainWindow.mainloop()