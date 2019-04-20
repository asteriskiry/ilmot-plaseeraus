import random
# Alkuun oliolista osallistujista

lajittelemattomat = [Participant.objects.filter(event_type=uid)]
# lajittelemattomat listaan
shuffle(lajittelemattomat)

kohta = 0
i = 0
j = 0
n = len(lajittelemattomat)

poyta = [[n][2]]
# poyta.[x][y], jos x on parillinen nainen oikealla, parittomalla nainen vasemmalla
# eli jos [0][0] niin nainen menee x ja mies y

while kohta < n:
    if lajittelemattomat[kohta].sukupuoli != 'mies' and lajittelemattomat[kohta] != null:
        # On siis nainen tai muu
        if i % 2 == 0 and j % 2 == 0 and poyta[i][j] == null:
            # On siis parillinen ja parillinen
            lajittelemattomat[kohta] = poyta[i][j]
            i += 1
        elif i % 2 == 0 and j % 2 == 1 and poyta[i][j] == null:
            # On siis parillinen ja pariton
            lajittelemattomat[kohta] = poyta[i][j]
            j += 1
        elif poyta[i][j] != null:
            if j == 2:
                j = 0
            if i == n:
                i = 0
            if poyta[i+1][j] == null:
                poyta[i+1][j] = lajittelemattomat[kohta]
            elif poyta[i][j+1] == null:
                poyta[i][j+1] = lajittelemattomat[kohta]
        kohta += 1

        if j == 2:
            j = 0

    if lajittelemattomat[kohta].sukupuoli != 'nainen':
        # On siis mies tai muu
        if i % 2 == 1 and j % 2 == 1 and poyta[i][j] == null:
            # On siis parillinen ja parillinen
            lajittelemattomat[kohta] = poyta[i][j]
            j += 1
        elif i % 2 == 1 and j % 2 == 0 and poyta[i][j] == null:  # on siis parillinen ja pariton
            lajittelemattomat[kohta] = poyta[i][j]
            i += 1
        elif poyta[i][j] != null:
            if j == 2:
                j = 0
            if i == n:
                i = 0
            if poyta[i + 1][j] == null:
                poyta[i + 1][j] = lajittelemattomat[kohta]
            elif poyta[i][j + 1] == null:
                poyta[i][j + 1] = lajittelemattomat[kohta]
        kohta += 1

        if j == 2:
            j = 0
        if i == round(n/2):
            n = 0
