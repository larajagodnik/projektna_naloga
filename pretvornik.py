from tkinter import *
from tkinter.ttk import *


# tkinter.ttk: knjižnica za zvezke

# 90 S = 100 G
# 1 m/s = 3,6 km/h
# 1 milja = 1609.344 m

PI = 3.14159265358979323846


class PretvornikModel:

 ### dolzina

    def pretvori_dolzina(self, *args):
        try:
            vrednost = float(self.DolzinaTextL.get())
        except ValueError:
            vrednost = 0
        vmesna = vrednost * self.DolzinaGledeNaM[self.IzbiraDolzinaL.get()]
        koncna = vmesna / self.DolzinaGledeNaM[self.IzbiraDolzinaD.get()]
        self.DolzinaTextD.set(round(koncna, 10))

        # try: preveri ce je stevilka, drugace 0


 ### masa

    def pretvori_masa(self, *args):
        try:
            vrednost = float(self.MasaTextL.get())
        except ValueError:
            vrednost = 0
        vmesna = vrednost * self.MasaGledeNaG[self.IzbiraMasaL.get()]
        koncna = vmesna / self.MasaGledeNaG[self.IzbiraMasaD.get()]
        self.MasaTextD.set(round(koncna, 10))


 ### kot

    def stopinje_v_radiani(self, kot):
        return PI / 180 * kot

    def radiani_v_stopinje(self, kot):
        return 180 / PI * kot

    def stopinje_v_grad(self, kot):
        return 10 / 9 * kot

    def grad_v_stopinje(self, kot):
        return 9 / 10 * kot

    def radiani_v_grad(self, kot):
        return self.radiani_v_stopinje(self.stopinje_v_grad(kot))

    def grad_v_radiani(self, kot):
        return self.grad_v_stopinje(self.stopinje_v_radiani(kot))  



    def pretvori_kot(self, *args):
        try:
            text = float(self.KotText.get())
        except ValueError:
            text = 0
        
        if self.IzbiraKot.get() == "stopinje":
            self.Vhod_KotS.delete(0, END)
            self.Vhod_KotS.insert(0, "%.2f" % (text))
            self.Vhod_KotR.delete(0, END)
            self.Vhod_KotR.insert(0, "%.2f" % (self.stopinje_v_radiani(text)))
            self.Vhod_KotG.delete(0, END)
            self.Vhod_KotG.insert(0, "%.2f" % (self.stopinje_v_grad(text)))

        elif self.IzbiraKot.get() == "radiani":
            self.Vhod_KotS.delete(0, END)
            self.Vhod_KotS.insert(0, "%.2f" % (self.radiani_v_stopinje(text)))
            self.Vhod_KotR.delete(0, END)
            self.Vhod_KotR.insert(0, "%.2f" % (text))
            self.Vhod_KotG.delete(0, END)
            self.Vhod_KotG.insert(0, "%.2f" % (self.radiani_v_grad(text)))

        elif self.IzbiraKot.get() == "grad":
            self.Vhod_KotS.delete(0, END)
            self.Vhod_KotS.insert(0, "%.2f" % (self.grad_v_stopinje(text)))
            self.Vhod_KotR.delete(0, END)
            self.Vhod_KotR.insert(0, "%.2f" % (self.grad_v_radiani(text)))
            self.Vhod_KotG.delete(0, END)
            self.Vhod_KotG.insert(0, "%.2f" % (text))


        # izbriši vrednost v okvirčku in vpiši novo
        # delete(0, end): od indeksa 0 do konca
        # insert(0, ...): na mesto indeksa 0

        
 ### hitrost

    def metriS_v_kilometriH(self, hitrost):
       return hitrost * 3.6

    def kilometriH_v_metriS(self, hitrost):
        return hitrost / 3.6

    def metriS_v_miljaH(self, hitrost):
        return (3600 / 1609.344) * hitrost

    def miljaH_v_metriS(self, hitrost):
        return (1609.344 / 3600) * hitrost

    def kilometriH_v_miljaH(self, hitrost):
        return self.kilometriH_v_metriS(self.metriS_v_miljaH(hitrost))

    def miljaH_v_kilometriH(self, hitrost):
        return self.miljaH_v_metriS(self.metriS_v_kilometriH(hitrost))


    
    def pretvori_metriS(self, *args):
        try:
            text = float(self.MetriSText.get())
        except ValueError:
            text = 0
        self.Vhod_KilometriH.delete(0, END)
        self.Vhod_KilometriH.insert(0, "%.2f" % (self.metriS_v_kilometriH(text)))
        self.Vhod_MiljaH.delete(0, END)
        self.Vhod_MiljaH.insert(0, "%.2f" % (self.metriS_v_miljaH(text)))
        

    def pretvori_kilometriH(self, *args):
        try:
            text = float(self.KilometriHText.get())
        except ValueError:
            text = 0
        self.Vhod_MetriS.delete(0, END)
        self.Vhod_MetriS.insert(0, "%.2f" % (self.kilometriH_v_metriS(text)))
        self.Vhod_MiljaH.delete(0, END)
        self.Vhod_MiljaH.insert(0, "%.2f" % (self.kilometriH_v_miljaH(text)))
        

    def pretvori_miljaH(self, *args):
        try:
            text = float(self.MiljaHText.get())
        except ValueError:
            text = 0
        self.Vhod_MetriS.delete(0, END)
        self.Vhod_MetriS.insert(0, "%.2f" % (self.miljaH_v_metriS(text)))
        self.Vhod_KilometriH.delete(0, END)
        self.Vhod_KilometriH.insert(0, "%.2f" % (self.miljaH_v_kilometriH(text))) 
        
                                
                     

#############################################################################

class PretvornikVmesnik(PretvornikModel):
    def __init__ (self, okno):
        self.zvezek = Notebook(okno)
        self.zvezek.pack()

        self.dolzina = Frame(self.zvezek)
        self.masa = Frame(self.zvezek)
        self.kot = Frame(self.zvezek)
        self.hitrost = Frame(self.zvezek)
    
##########################    Dolžina    ##################################

        self.zvezek.add(self.dolzina, text = "Dolžina")
        self.DolzinaGledeNaM = dict(mm = 0.001, cm = 0.01, dm = 0.1, m = 1,
                                    km = 1000, milja = 1609.344, inč = 39.37)

  ## Izbirni menu
    #levi
        self.IzbiraDolzinaL = StringVar()  
        self.Combobox_DolzinaL = (Combobox(self.dolzina, textvariable = self.IzbiraDolzinaL,
                                    values = ('mm', 'cm', 'dm', 'm', 'km', 'milja', 'inč'),
                                    state = "readonly", width=12))
        self.Combobox_DolzinaL.current(3)
        self.IzbiraDolzinaL.trace("w", self.pretvori_dolzina)
        self.Combobox_DolzinaL.grid(row=1, column=1, padx=5, pady=5)


    #desni
        self.IzbiraDolzinaD = StringVar()
        self.Combobox_DolzinaD = (Combobox(self.dolzina, textvariable = self.IzbiraDolzinaD,
                                    values = ('mm', 'cm', 'dm', 'm', 'km', 'milja', 'inč'),
                                    state = "readonly", width=12))
        self.Combobox_DolzinaD.current(3)
        self.IzbiraDolzinaD.trace("w", self.pretvori_dolzina)
        self.Combobox_DolzinaD.grid(row=1, column=3, padx=5, pady=5)


  ## Okvirčki za količino
    #levi
        self.DolzinaTextL = StringVar(value = 0)
        self.Vhod_DolzinaL = Entry(self.dolzina, textvariable = self.DolzinaTextL, width=10)
        self.DolzinaTextL.trace("w", self.pretvori_dolzina)
        self.Vhod_DolzinaL.grid(row=2, column=1, padx=5, pady=5, sticky = W)


    #desni
        self.DolzinaTextD = StringVar()
        self.Vhod_DolzinaD = Entry(self.dolzina, textvariable = self.DolzinaTextD,
                                    width=10, state = "readonly") 
        self.Vhod_DolzinaD.grid(row=2, column=3, padx=5, pady=5, sticky = W)


 ## Besedilo (pretvori, iz, v, enota) 
        self.PretvornikVmesnik = Label(self.dolzina, text = "Pretvori")
        self.PretvornikVmesnik.grid(row=0, column=0, padx=5, pady=5, sticky = W)

        self.Iz = Label(self.dolzina, text = "Iz")
        self.Iz.grid(row=1, column=0, padx=5, pady=5, sticky = E)

        self.V = Label(self.dolzina, text = "v")
        self.V.grid(row=1, column=2, padx=5, pady=5)

        self.JeEnako = Label(self.dolzina, text = "=")
        self.JeEnako.grid(row=2, column=2, padx=5, pady=5)

        self.EnotaL = Label(self.dolzina, textvariable = self.IzbiraDolzinaL)
        self.EnotaL.grid(row=2, column=1, padx=5, pady=5, sticky = E)

        self.EnotaD = Label(self.dolzina, textvariable = self.IzbiraDolzinaD)
        self.EnotaD.grid(row=2, column=3, padx=5, pady=5, sticky = E)


        # StringVar: za spreminjanje imena v okvrčku
        # Combobox = DropdownMenu
        # textvariable: katero ime v okvirčku
        # pading (padx, pady): prostor okoli okvirčka v pikslih
        # trace: posodabljanje pri spremenljivih (podobno kot event)
        # trace("w", ...): w - lahko pišeš
        # state = readonly: samo za branje
        # sticky: kam postavi objekt v celici (opcija za grid)
        

##########################    Masa   ##################################

        self.zvezek.add(self.masa, text = "Masa")                

        self.MasaGledeNaG = dict(mg = 0.001, g = 1, dg = 10,
                                        kg = 1000, tona = 1000000)

  ## Izbirni menu
    #levi
        self.IzbiraMasaL = StringVar()
        self.Combobox_MasaL = (Combobox(self.masa, textvariable = self.IzbiraMasaL,
                                    values = ('mg', 'g', 'dg', 'kg', 'tona'),
                                    state = "readonly", width=12))
        self.Combobox_MasaL.current(1)
        self.IzbiraMasaL.trace("w", self.pretvori_masa)
        self.Combobox_MasaL.grid(row=1, column=1, padx=5, pady=5)


    #desni
        self.IzbiraMasaD = StringVar()
        self.Combobox_MasaD = (Combobox(self.masa, textvariable = self.IzbiraMasaD,
                                    values = ('mg', 'g', 'dg', 'kg', 'tona'),
                                    state = "readonly", width=12))
        self.Combobox_MasaD.current(1)
        self.IzbiraMasaD.trace("w", self.pretvori_masa)
        self.Combobox_MasaD.grid(row=1, column=3, padx=5, pady=5)


  ## Okvirčki za količino
    #levi
        self.MasaTextL = StringVar(value = 0)
        self.Vhod_MasaL = Entry(self.masa, textvariable = self.MasaTextL, width=10)
        self.MasaTextL.trace("w", self.pretvori_masa)
        self.Vhod_MasaL.grid(row=2, column=1, padx=5, pady=5, sticky = W)


    #desni
        self.MasaTextD = StringVar()
        self.Vhod_MasaD = Entry(self.masa, textvariable = self.MasaTextD,
                                    width=10, state = "readonly")
        self.Vhod_MasaD.grid(row=2, column=3, padx=5, pady=5, sticky = W)


  ## Besedilo (pretvori, iz, v, enota) 
        self.PretvornikVmesnik = Label(self.masa, text = "Pretvori")
        self.PretvornikVmesnik.grid(row=0, column=0, padx=5, pady=5, sticky = W)

        self.Iz = Label(self.masa, text = "Iz")
        self.Iz.grid(row=1, column=0, padx=5, pady=5, sticky = E)

        self.V = Label(self.masa, text = "v")
        self.V.grid(row=1, column=2, padx=5, pady=5)

        self.JeEnako = Label(self.masa, text = "=")
        self.JeEnako.grid(row=2, column=2, padx=5, pady=5)

        self.EnotaL = Label(self.masa, textvariable = self.IzbiraMasaL)
        self.EnotaL.grid(row=2, column=1, padx=5, pady=5, sticky = E)

        self.EnotaD = Label(self.masa, textvariable = self.IzbiraMasaD)
        self.EnotaD.grid(row=2, column=3, padx=5, pady=5, sticky = E)


##########################    Kot    ##################################

        self.zvezek.add(self.kot, text = "Kot")

  ## Izbirni menu
        self.IzbiraKot = StringVar()
        self.Combobox_Kot = (Combobox(self.kot, textvariable = self.IzbiraKot,
                                    values = ('stopinje', 'radiani', 'grad'),
                                    state = "readonly", width=8))
        self.Combobox_Kot.current(0)
        self.IzbiraKot.trace("w", self.pretvori_kot)
        self.Combobox_Kot.grid(row=1, column=1, padx=10, pady=5)


  ## Okvirčki za količino
    #levi
        self.KotText = StringVar(value = 0)
        self.Vhod_Kot = Entry(self.kot, textvariable = self.KotText, width=10)
        self.KotText.trace("w", self.pretvori_kot)
        self.Vhod_Kot.grid(row=2, column=1, padx=10, pady=5, sticky = W)


    #desni
     #stopinje
        self.KotSText = StringVar()
        self.Vhod_KotS = Entry(self.kot, textvariable = self.KotSText, width=10)
        self.Vhod_KotS.grid(row=1, column=3, padx=10, pady=5, sticky = W)

     #radiani
        self.KotRText = StringVar()
        self.Vhod_KotR = Entry(self.kot, textvariable = self.KotRText, width=10)
        self.Vhod_KotR.grid(row=2, column=3, padx=10, pady=5, sticky = W)

     #grad
        self.KotGText = StringVar()
        self.Vhod_KotG = Entry(self.kot, textvariable = self.KotGText, width=10) 
        self.Vhod_KotG.grid(row=3, column=3, padx=10, pady=5, sticky = W)


  ## Besedilo (pretvori, stopinje, radiani, grad) 
        self.PretvornikVmesnik = Label(self.kot, text = "Pretvori")
        self.PretvornikVmesnik.grid(row=0, column=0, padx=5, pady=5)

        self.Stopinje = Label(self.kot, text = "Stopinje:")
        self.Stopinje.grid(row=1, column=2, padx=10, pady=5)

        self.Radiani = Label(self.kot, text = "Radiani:")
        self.Radiani.grid(row=2, column=2, padx=10, pady=5)

        self.Grad = Label(self.kot, text = "Grad:")
        self.Grad.grid(row=3, column=2, padx=10, pady=5)


##########################    Hitrost    ##################################

        self.zvezek.add(self.hitrost, text = "Hitrost")

  ## Besedilo (pretvori, stopinje, radiani, grad) 
        self.PretvornikVmesnik = Label(self.hitrost, text = "Pretvori")
        self.PretvornikVmesnik.grid(row=0, column=0, padx=5, pady=5)

        self.MetriS = Label(self.hitrost, text = "m/s:")
        self.MetriS.grid(row=1, column=1, padx=10, pady=5)

        self.KilometriH = Label(self.hitrost, text = "km/h:")
        self.KilometriH.grid(row=2, column=1, padx=10, pady=5)

        self.MiljaH = Label(self.hitrost, text = "mph:")
        self.MiljaH.grid(row=3, column=1, padx=10, pady=5)


  ## Okvirčki za količino
        self.MetriSText = StringVar(value = 0)
        self.Vhod_MetriS = Entry(self.hitrost, textvariable = self.MetriSText, width=10)
        self.Vhod_MetriS.grid(row=1, column=2, padx=10, pady=5, sticky = W)

        self.KilometriHText = StringVar(value = 0)
        self.Vhod_KilometriH = Entry(self.hitrost, textvariable = self.KilometriHText, width=10)
        self.Vhod_KilometriH.grid(row=2, column=2, padx=10, pady=5, sticky = W)

        self.MiljaHText = StringVar(value = 0)
        self.Vhod_MiljaH = Entry(self.hitrost, textvariable = self.MiljaHText, width=10)
        self.Vhod_MiljaH.grid(row=3, column=2, padx=10, pady=5, sticky = W)


 ## Gumbi izračunaj
        self.izracunaj_metriS = Button(self.hitrost, text = "Izračunaj", command = self.pretvori_metriS)
        self.izracunaj_metriS.grid(row=1, column=3, padx=10, pady=5)

        self.izracunaj_kilometriH = Button(self.hitrost, text = "Izračunaj", command = self.pretvori_kilometriH)
        self.izracunaj_kilometriH.grid(row=2, column=3, padx=10, pady=5)

        self.izracunaj_miljaH = Button(self.hitrost, text = "Izračunaj", command = self.pretvori_miljaH)
        self.izracunaj_miljaH.grid(row=3, column=3, padx=10, pady=5)
        


okno = Tk()
okno.title("Pretvornik enot")
aplikacija = PretvornikVmesnik(okno)
okno.mainloop
