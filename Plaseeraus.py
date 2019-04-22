import random
import xlsxwriter
# Alkuun oliolista osallistujista
# TODO lisää Juuson text_preprocessing_template.py viittaus alkuun, että nimet halutussa muodossa
# Lisätään tuo tokenizer myöhemmin hienosäädössä

lajittelemattomat = [Participant.objects.filter(event_type=uid)]
# lajittelemattomat listaan
shuffle(lajittelemattomat)

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

poyta = [[round(n/2)][2]]
# poyta.[x][y], jos x on parillinen nainen oikealla, parittomalla nainen vasemmalla
# eli jos [0][0] niin nainen menee x ja mies y


def istumaan(henkilo):
    global iN
    global jN
    global iM
    global jM
    if henkilo.gender != 'man' and henkilo:
        # On siis nainen tai muu
        if iN % 2 == 0 and jN % 2 == 0 and poyta[iN][jN] is None:
            # On siis parillinen ja parillinen
            henkilo = poyta[iN][jN]
            iN += 1
        elif iN % 2 == 0 and jN % 2 == 1 and poyta[iN][jN] is None:
            # On siis parillinen ja pariton
            henkilo = poyta[iN][jN]
            jN += 1
        elif poyta[iN][jN]:
            if jN == 2:
                jN = 0
            if iN == round(n/2):
                iN = 0
            if poyta[iN+1][jN] is None:
                poyta[iN+1][jN] = henkilo
            elif poyta[iN][jN+1] is None:
                poyta[iN][jN+1] = henkilo

        if jN == 2:
            jN = 0

    if henkilo.gender != 'woman' and henkilo:
        # On siis mies tai muu
        if iM % 2 == 1 and jM % 2 == 1 and poyta[iM][jM] is None:
            # On siis pariton ja pariton
            henkilo = poyta[iM][jM]
            jM += 1
        elif iM % 2 == 1 and jM % 2 == 0 and poyta[iM][jM] is None:  # on siis parillinen ja pariton
            henkilo = poyta[iM][jM]
            iM += 1
        elif poyta[iM][jM]:
            if jM == 2:
                jM = 0
            if iM == round(n/2):
                iM = 0
            if poyta[iM + 1][jM] is None:
                poyta[iM + 1][jM] = henkilo
            elif poyta[iM][jM + 1] is None:
                poyta[iM][jM + 1] = henkilo

        if jM == 2:
            jM = 0
        if iM == round(n/2):
            iM = 0

    lajittelemattomat.remove(henkilo)


def poytaseurueistumaan(henkilo):
    for h in henkilo.friends:
        if henkilo.friends(h):
            istumaan(h)

# TODO lisää jokin, jolla mennään eteenpäin lista


def plaseeraus():
    global kohta
    while kohta < n:
        global x
        global y
        istumaan(lajittelemattomat[kohta])
        kohta += 1

        while poyta[x][y] and poyta[x+1][y] and poyta[x+1][y+1] and poyta[x][y+1]:
            poytaseurueistumaan(poyta[x][y])
            x += 1
            y += 1
            if y == 2:
                y = 0
    return poyta


def excel():
    # Koodi exceliin
    workbook = xlsxwriter.Workbook('plaseeraus.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    # Käyttöliittymästä true/false food ja drink attribuutteihin
    if food is None and drink is None:
        while row < n + 1:
            worksheet.write(row, col, poyta[row][col].name)
            worksheet.write(row, col + 1, poyta[row][col + 1].name)
            row += 1

    elif food is None and drink:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].holiton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].holiton)
            row += 1

    elif food and drink is None:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].lihaton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].lihaton)
            row += 1

    elif food and drink:
        while row < n+1:
            worksheet.write(row, col, poyta[row][col].name + ',' + poyta[row][col].holiton + ', ' + poyta[row][col].lihaton)
            worksheet.write(row, col + 1, poyta[row][col+1].name + ',' + poyta[row][col+1].holiton + ', ' + poyta[row][col+1].lihaton)
            row += 1

    workbook.close()
    return plaseeraus.xlsx
