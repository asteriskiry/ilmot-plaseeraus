import random
# Alkuun oliolista osallistujista

lajittelemattomat = [Participant.objects.filter(event_type=uid)]
# lajittelemattomat listaan
shuffle(lajittelemattomat)

kohta = 0
i = 0
j = 0
k = 0
n = len(lajittelemattomat)

poyta = [[n][2]]
# poyta.[x][y], jos x on parillinen nainen oikealla, parittomalla nainen vasemmalla
# eli jos [0][0] niin nainen menee x ja mies y

def istumaan(henkilo):
    if henkilo.sukupuoli != 'mies' and henkilo != null:
        # On siis nainen tai muu
        if i % 2 == 0 and j % 2 == 0 and poyta[i][j] == null:
            # On siis parillinen ja parillinen
            henkilo = poyta[i][j]
            i += 1
        elif i % 2 == 0 and j % 2 == 1 and poyta[i][j] == null:
            # On siis parillinen ja pariton
            henkilo = poyta[i][j]
            j += 1
        elif poyta[i][j] != null:
            if j == 2:
                j = 0
            if i == n:
                i = 0
            if poyta[i+1][j] == null:
                poyta[i+1][j] = henkilo
            elif poyta[i][j+1] == null:
                poyta[i][j+1] = henkilo
        kohta += 1

        if j == 2:
            j = 0

    if henkilo.sukupuoli != 'nainen' and henkilo != null:
        # On siis mies tai muu
        if i % 2 == 1 and j % 2 == 1 and poyta[i][j] == null:
            # On siis pariton ja pariton
            henkilo = poyta[i][j]
            j += 1
        elif i % 2 == 1 and j % 2 == 0 and poyta[i][j] == null:  # on siis parillinen ja pariton
            henkilo = poyta[i][j]
            i += 1
        elif poyta[i][j] != null:
            if j == 2:
                j = 0
            if i == n:
                i = 0
            if poyta[i + 1][j] == null:
                poyta[i + 1][j] = henkilo
            elif poyta[i][j + 1] == null:
                poyta[i][j + 1] = henkilo

        if j == 2:
            j = 0
        if i == round(n/2):
            n = 0

    lajittelemattomat.remove(henkilo)

def poytaseurueIstumaan(henkilo):
    for h in henkilo.poytaseurue:
        if henkilo.poytaseurue(h) != null:
            istumaan(h)

#TODO lisää jokin, jolla mennään eteenpäin lista