def sestej_seznam(sez):
    delna_vsota =  0
    delne_vsote = []
    for element in sez:
        delna_vsota += element
        delne_vsote.append(delna_vsota)
    return delne_vsote