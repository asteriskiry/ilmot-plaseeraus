import random
import xlsxwriter
from Ukkelit import *
import numpy


# Alkuun oliolista osallistujista

# lajittelemattomat = [Participant.objects.filter(event_type=uid)]
# Ylempi tulee korvaamaan alemman
lajittelemattomat = list(tuolista())
# lajittelemattomat listaan
random.shuffle(lajittelemattomat)

# Kohta kertoo missä ollaan lajittelemattomien listalla
kohta = 0
# i ja j pitävät huolta, siitä mihin henkilön voi laittaa, sillä kohta saattaa hyppiä
iM = 0
jM = 0
iN = 0
jN = 0
# x ja y pitävät huolta pöydän indeksistä, jotta löydetään tyhjät kohdat
x = 0
y = 0
n = len(lajittelemattomat)

poyta = numpy.full((round(n/2), 2), Henkilo(None, None, None, None, None))#[[round(n/2), round(n/2)], [2, 2]]
# poyta.[x][y], jos x on parillinen nainen oikealla, parittomalla nainen vasemmalla
# eli jos [0][0] niin nainen menee x ja mies y


def istumaan(henkilo):
    global iN
    global jN
    global iM
    global jM
    if henkilo in lajittelemattomat:
        if henkilo.gender != "man":  # On siis nainen tai muu
            if iN % 2 == 0 and jN % 2 == 0:  # On siis parillinen ja parillinen
                poyta[iN][jN] = henkilo
                iN += 1
            elif iN % 2 == 0 and jN % 2 == 1:  # On siis parillinen ja pariton
                poyta[iN][jN] = henkilo
                jN += 1
            else:  # if poyta[iN][jN]:
                if jN == 2:
                    jN = 0
                if iN == round(n/2) or iN + 1 >= round(n/2):
                    iN = 0
                if not (poyta[iN+1][jN].name is None):
                    poyta[iN+1][jN] = henkilo
                if jN + 1 >= 2:
                    jN = 0
                elif not (poyta[iN][jN+1].name is None):
                    poyta[iN][jN+1] = henkilo
            if jN == 2:
                jN = 0

        if henkilo.gender != "woman": # On siis mies tai muu
            if iM % 2 == 1 and jM % 2 == 1: # On siis pariton ja pariton
                poyta[iM][jM] = henkilo
                jM += 1
            elif iM % 2 == 1 and jM % 2 == 0: # on siis parillinen ja pariton
                poyta[iM][jM] = henkilo
                iM += 1
            else:
                if jM == 2:
                    jM = 0
                if iM == round(n/2) or iM + 1 >= round(n/2):
                    iM = 0
                if not (poyta[iM + 1][jM].name is None):
                    poyta[iM + 1][jM] = henkilo
                if jM + 1 >= 2:
                    jM = 0
                elif not (poyta[iM][jM + 1].name is None):
                    poyta[iM][jM + 1] = henkilo
            if jM == 2:
                jM = 0
            if iM == round(n/2):
                iM = 0

        lajittelemattomat.remove(henkilo)


def poytaseurueistumaan(henkilo):
    if henkilo.friends != None:
        for h in henkilo.friends:
            istumaan(h)

# TODO lisää jokin, jolla mennään eteenpäin lista


def plaseeraus():
    global kohta
    while kohta < len(lajittelemattomat):
        global x
        global y    
        #print("len: " + str(len(lajittelemattomat)))
        #print("kohta: " + str(kohta))
        istumaan(lajittelemattomat[kohta])
        #kohta += 1

        while poyta[x][y] and poyta[x+1][y] and poyta[x+1][y+1] and poyta[x][y+1]:
            poytaseurueistumaan(poyta[x][y])
            x += 1
            y += 1
            if y == 1:
                y = 0
            if x == round(n/2)-1:
                x = 0
    print(poyta)
    return poyta.tolist()


def excel(food, drink):
    # Koodi exceliin
    workbook = xlsxwriter.Workbook('plaseeraus.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    # Käyttöliittymästä true/false food ja drink attribuutteihin
    if food == False and drink == False:
        while row < n + 1:
            worksheet.write(row, col, poyta[row][col].name)
            worksheet.write(row, col + 1, poyta[row][col + 1].name)
            row += 1

    elif food == False and drink == True:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].holiton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].holiton)
            row += 1

    elif food == True and drink == False:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].lihaton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].lihaton)
            row += 1

    elif food == True and drink == True:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].holiton + ', ' + poyta[row][col].lihaton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].holiton + ', ' + poyta[row][col+1].lihaton)
            row += 1

    workbook.close()

# print(poyta)
# henkilot = plaseeraus()
# print(henkilot[0][0].name)
# for i in range(len(poyta[:,0])):
#    for j in range(len(poyta[0])):
#        print(poyta[i][j].name)
