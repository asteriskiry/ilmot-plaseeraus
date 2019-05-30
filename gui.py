from tkinter import *
from Plaseerausver2 import plaseeraus
from Plaseerausver2 import excel
from Ukkelit import *

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
        self.checkOne = None
        self.checkTwo = None
        self.poydat = StringVar()
        self.paikka1 = StringVar()
        self.paikka2 = StringVar()
        self.buttonit = []
        self.labels = []

        # Kutsutaan vaihetta jossa luodaan nappulat sun muut
        self.content()

    def content(self):
        
        # Luodaan ykkös frameen tekstit, syötekentät sekä submit button
        lblOtsikko1 = Label(self.frame1, text="Syötä pöytien määrä:").pack(pady=2)
        ePoydat = Entry(self.frame1, textvariable=self.poydat).pack()
        lblExcel = Label(self.frame1, text="Tallennetaanko exceliin?").pack(pady=2)
        buttonFrame = Frame(self.frame1)
        self.checkOne = Checkbutton(buttonFrame, text="Ruoka?").pack(pady=2, side = LEFT)
        self.checkTwo = Checkbutton(buttonFrame, text="Juoma?").pack(pady=2, side = LEFT)
        buttonFrame.pack()
        buttonFrame2 = Frame(self.frame1)
        bSuorita = Button(buttonFrame2, text="Suorita", width = 6, command=self.suorita).pack(pady=2, padx=4, side = LEFT)
        bVaihto = Button(buttonFrame2, text="Vaihto", width = 6, command=self.vaihtoikkuna).pack(pady=2, padx=4, side = LEFT)
        bExcel = Button(buttonFrame2, text="Excel", width = 6, command=self.excelCheck).pack(pady=2, padx=4, side = LEFT)
        buttonFrame2.pack()

    # Submit buttonin toiminnallisuus
    def suorita(self):
        # Ruudun ja listojen tyhjennys uutta 'Suorita' painallusta varten
        if len(self.buttonit) > 0:
            for i in self.buttonit:
                i[0].destroy()
        self.buttonit.clear()
        if len(self.labels) > 0:
            for i in self.labels:
                i.destroy()
        self.labels.clear()

        # Haetaan olion attribuuteista arvot sekä muunnetaan ne floatista inttiin
        henkilot = list(plaseeraus())
        try:
            osallistujat = len(henkilot)
            poydat = int(self.poydat.get())
        except ValueError:
            return
        poytaosallistujat = int(osallistujat/poydat)

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
                if valittuhenkilo is None:
                    henkilot.remove(valittuhenkilo)
                    valittuhenkilo = Henkilo("Tyhjä", "Tyhjä", [], "Tyhjä", "Tyhjä")
                self.buttonit.append([Button(self.frame2, text=valittuhenkilo.name, width = 6, command=lambda c=paikkanro, d=valittuhenkilo: self.lisatiedot(c, d)), paikkanro, valittuhenkilo, 0, 0])
                if (i % 2 != 0):
                    xpos += 60
                    ypos -= 28
                    self.buttonit[paikkanro][0].place(x = xpos, y = ypos)
                    self.buttonit[paikkanro][3] = xpos
                    self.buttonit[paikkanro][4] = ypos
                    xpos -= 60
                else:
                    self.buttonit[paikkanro][0].place(x = xpos, y = ypos)
                    self.buttonit[paikkanro][3] = xpos
                    self.buttonit[paikkanro][4] = ypos
                ypos += 28
                paikkanro += 1
                if valittuhenkilo.name != "Tyhjä":
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

    def vaihtoikkuna(self):
        if len(self.buttonit) < 2:
            return
        top = Toplevel()
        top.geometry('350x170')
        top.title("Vaihtoikkuna")
        lblVaihto = Label(top, text="Vaihtoikkuna! Suorita alla paikan vaihto syöttämällä paikkanrot.").pack(pady=2)
        lblPaikka1 = Label(top, text="Ensimmäinen paikkanro:").pack(pady=2)
        ePaikka1 = Entry(top, textvariable=self.paikka1).pack()
        lblPaikka2 = Label(top, text="Vaihdettava paikkanro:").pack(pady=2)
        ePaikka2 = Entry(top, textvariable=self.paikka2).pack()
        suoritaVaihto = Button(top, text="Vaihda", command=self.vaihto).pack(pady=2)
        pois = Button(top, text="Pois", command=top.destroy).pack(pady=2)

    def vaihto(self):
        try:
            paikka1Int = int(self.paikka1.get())
            paikka2Int = int(self.paikka2.get())
        except ValueError:
            return
        try:
            paikka1hlo = self.buttonit[paikka1Int]
            paikka2hlo = self.buttonit[paikka2Int]
        except IndexError:
            return
        uusipaikka1hlo = [Button(self.frame2, text=paikka2hlo[2].name, width = 6, command=lambda c=paikka1hlo[1], d=paikka2hlo[2]: self.lisatiedot(c, d)), paikka1hlo[1], paikka2hlo[2], paikka1hlo[3], paikka1hlo[4]]
        uusipaikka2hlo = [Button(self.frame2, text=paikka1hlo[2].name, width = 6, command=lambda c=paikka2hlo[1], d=paikka1hlo[2]: self.lisatiedot(c, d)), paikka2hlo[1], paikka1hlo[2], paikka2hlo[3], paikka2hlo[4]]
        uusipaikka1hlo[0].place(x = uusipaikka1hlo[3], y = uusipaikka1hlo[4])
        uusipaikka2hlo[0].place(x = uusipaikka2hlo[3], y = uusipaikka2hlo[4])
        paikka1hlo[0].destroy()
        paikka2hlo[0].destroy()
        self.buttonit[paikka1Int] = uusipaikka1hlo
        self.buttonit[paikka2Int] = uusipaikka2hlo
    
    # Exceliin
    def excelCheck(self):
        if len(self.buttonit) == 0:
            return
        poyta = list()
        for i in self.buttonit:
            poyta.append(i[2])
        excel(self.checkOne, self.checkTwo, self.poydat, poyta)

# Ikkunan alustus ja suorittaminen
if __name__ == '__main__':
    mainWindow = Tk()
    mainWindow.geometry('600x380')
    mainFrame = GUI(mainWindow)
    mainWindow.mainloop()