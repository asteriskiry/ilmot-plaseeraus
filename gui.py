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

        # Olion attribuutit, toiseen tallentuu osallistujamäärä, toiseen pöytien määrä
        self.koko = StringVar()
        self.poydat = StringVar()

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

        # Haetaan olion attribuuteista arvot sekä muunnetaan ne floatista inttiin
        osallistujat = int(self.koko.get())
        poydat = int(self.poydat.get())
        poytaosallistujat = int(osallistujat/poydat)

        # Iteroidaan osallistujat "pöytiin" eli oikeille paikoille framea
        # Tallennetaan osallistuja buttonit listaan, jotta osallistujia voidaan myöhemmin käsitellä jos tarvetta
        osallistujalista = []
        for i in range(poydat):
            ypos = 20
            xpos = 200 * i
            for i in range(1, poytaosallistujat+1):
                btnOsallistuja = Button(self.frame2, text="Nimi")
                if (i % 2 == 0):
                    xpos += 40
                    ypos -= 28
                    btnOsallistuja.place(x = xpos, y = ypos)
                    xpos -= 40
                else:
                    btnOsallistuja.place(x = xpos, y = ypos)
                osallistujalista.append(btnOsallistuja)
                ypos += 28

# Ikkunan alustus ja suorittaminen
mainWindow = Tk()
mainWindow.geometry('600x380')

mainFrame = GUI(mainWindow)

mainWindow.mainloop()
