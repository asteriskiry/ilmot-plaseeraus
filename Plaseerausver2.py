import random
import xlsxwriter
from numpy import reshape
from Ukkelit import *

# Alkuun oliolista osallistujista

# lajittelemattomat = [Participant.objects.filter(event_type=uid)]
# Ylempi tulee korvaamaan alemman
lajittelemattomat = list(tuolista())
# lajittelemattomat listaan
random.shuffle(lajittelemattomat)

# Kohta kertoo missä ollaan lajittelemattomien listalla
kohta = 0

n = len(lajittelemattomat)

poyta = [None] * n


def istumaan(henkilo):
    global kohta
    global n
    global poyta

    if henkilo:
        if henkilo.gender == "woman" and henkilo in lajittelemattomat:

            if kohta % 2 != 0:
                temp = kohta
                while temp < n:
                    if poyta[temp] is None:
                        poyta[temp] = henkilo
                        break
                    temp += 2

            elif kohta + 1 < round(n):
                temp = kohta + 1
                while temp < n:
                    if poyta[temp] is None:
                        poyta[temp] = henkilo
                        break
                    temp += 2

            else:
                if kohta + 1 >= n:
                    kohta = 0

                if poyta[kohta] is None:
                    poyta[kohta] = henkilo

                else:
                    for i in range(n):
                        if poyta[i] is None:
                            poyta[i] = henkilo
                            break
            if kohta + 1 >= n:
                kohta = 0

            else:
                kohta += 1

            lajittelemattomat[lajittelemattomat.index(henkilo)] = None

        elif henkilo.gender == "man" and henkilo in lajittelemattomat:
            if kohta % 2 != 1:
                temp = kohta
                while temp < n:
                    if poyta[temp] is None:
                        poyta[temp] = henkilo
                        break
                    temp += 2

            elif kohta + 1 < n:
                temp = kohta + 1
                while temp < n:
                    if poyta[temp] is None:
                        poyta[temp] = henkilo
                        break
                    temp += 2

            else:
                if kohta + 1 >= n:
                    kohta = 0

                if poyta[kohta] is None:
                    poyta[kohta] = henkilo

                else:
                    for i in range(n):
                        if poyta[i] is None:
                            poyta[i] = henkilo
                            break
            if kohta + 1 >= n:
                kohta = 0

            else:
                kohta += 1

            lajittelemattomat[lajittelemattomat.index(henkilo)] = None

        else:
            if henkilo in lajittelemattomat:
                for i in range(n):
                    if poyta[i] is None:
                        poyta[i] = henkilo
                        break
                lajittelemattomat[lajittelemattomat.index(henkilo)] = None


def poytaseurueistumaan(henkilo):
    if henkilo:
        if henkilo.friends:
            for h in henkilo.friends:
                istumaan(h)


def vaihda():
    for i in range(len(poyta)):
        if i % 2 == 0 and i % 4 != 0:
            temp = poyta[i]
            poyta[i] = poyta[i + 1]
            poyta[i + 1] = temp


def plaseeraus():
    paikka = 0
    i = 0
    while paikka < len(lajittelemattomat):
        istumaan(lajittelemattomat[paikka])
        while i < len(poyta) and poyta[i]:
            poytaseurueistumaan(poyta[i])
            i += 1
        paikka += 1
    vaihda()
    if None in poyta:
        poyta.remove(None)
    tarkista = list(tuolista())
    for i in range(len(tarkista)):
        if tarkista[i] not in poyta:
            poyta.append(tarkista[i])
    return poyta


def matriisi(lista):
    shape = (round(len(lista) / 2), 2)
    if len(lista) % 2 == 1:
        tyhja = Henkilo("-", "-", [], "-", "-")
        lista.append(tyhja)
    lista = reshape(lista, shape)
    return lista


def excel(food, drink, poytienmaara, uusipoyta):
    # Koodi exceliin
    matrix = matriisi(poyta)
    workbook = xlsxwriter.Workbook('plaseeraus.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    rivit = round(len(poyta) / 2)
    # Käyttöliittymästä true/false food ja drink attribuutteihin
    if not food and not drink:
        while row < rivit:
            worksheet.write(row, col, matrix[row][col].name)
            worksheet.write(row, col + 1, matrix[row][col + 1].name)
            row += 1

    elif not food and drink:
        while row < rivit:
            worksheet.write(row, col, matrix[row][col].name + ',' + matrix[row][col].holiton)
            worksheet.write(row, col + 1, matrix[row][col + 1].name + ',' + matrix[row][col + 1].holiton)
            row += 1

    elif food and not drink:
        while row < rivit:
            worksheet.write(row, col, matrix[row][col].name + ',' + matrix[row][col].lihaton)
            worksheet.write(row, col + 1, matrix[row][col + 1].name + ',' + matrix[row][col + 1].lihaton)
            row += 1

    elif food and drink:
        while row < rivit:
            worksheet.write(row, col,
                            matrix[row][col].name + ',' + matrix[row][col].holiton + ', ' + matrix[row][col].lihaton)
            worksheet.write(row, col + 1,
                            matrix[row][col + 1].name + ',' + matrix[row][col + 1].holiton + ', ' + matrix[row][
                                col + 1].lihaton)
            row += 1

    workbook.close()

# print(poyta)
# henkilot = plaseeraus()
# print(henkilot[0][0].name)
# for i in range(len(poyta[:,0])):
#    for j in range(len(poyta[0])):
#        print(poyta[i][j].name)
