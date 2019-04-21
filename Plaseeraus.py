import random
# Alkuun oliolista osallistujista

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
    if henkilo.sukupuoli != 'mies' and henkilo != null:
        # On siis nainen tai muu
        if iN % 2 == 0 and jN % 2 == 0 and poyta[iN][jN] == null:
            # On siis parillinen ja parillinen
            henkilo = poyta[iN][jN]
            iN += 1
        elif iN % 2 == 0 and jN % 2 == 1 and poyta[iN][jN] == null:
            # On siis parillinen ja pariton
            henkilo = poyta[iN][jN]
            jN += 1
        elif poyta[iN][jN] != null:
            if jN == 2:
                jN = 0
            if iN == round(n/2):
                iN = 0
            if poyta[iN+1][jN] == null:
                poyta[iN+1][jN] = henkilo
            elif poyta[iN][jN+1] == null:
                poyta[iN][jN+1] = henkilo

        if jN == 2:
            jN = 0

    if henkilo.sukupuoli != 'nainen' and henkilo != null:
        # On siis mies tai muu
        if iM % 2 == 1 and jM % 2 == 1 and poyta[iM][jM] == null:
            # On siis pariton ja pariton
            henkilo = poyta[iM][jM]
            jM += 1
        elif iM % 2 == 1 and jM % 2 == 0 and poyta[iM][jM] == null:  # on siis parillinen ja pariton
            henkilo = poyta[iM][jM]
            iM += 1
        elif poyta[iM][jM] != null:
            if jM == 2:
                jM = 0
            if iM == round(n/2):
                iM = 0
            if poyta[iM + 1][jM] == null:
                poyta[iM + 1][jM] = henkilo
            elif poyta[iM][jM + 1] == null:
                poyta[iM][jM + 1] = henkilo

        if jM == 2:
            jM = 0
        if iM == round(n/2):
            iM = 0

    lajittelemattomat.remove(henkilo)


def poytaseurueistumaan(henkilo):
    for h in henkilo.poytaseurue:
        if henkilo.poytaseurue(h) != null:
            istumaan(h)

# TODO lisää jokin, jolla mennään eteenpäin lista


while kohta < n:
    global x
    global y
    istumaan(lajittelemattomat[kohta])
    kohta += 1

    while poyta[x][y] != null and poyta[x+1][y] != null and poyta[x+1][y+1] != null and poyta[x][y+1]:
        poytaseurueistumaan(poyta[x][y])
        x += 1
        y += 1
        if y == 2:
            y = 0
