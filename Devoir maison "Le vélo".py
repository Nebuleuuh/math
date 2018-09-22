prix = 25
client = 100
recette = 0

# Il faut faire un while qui rajoute 0,5 au prix
# A chaque 0,5 ajouté il faut retirer 1 client
# Et à chaque fois il faut les faire se multiplier (dans le genre : prix * nombre_client)

maliste = []


while client > 1:
    prix = prix + 0.5
    client = client - 1
    recette = prix * client
    print("Pour", client,"le prix d'un vélo sera : ", prix, "et la recette totale sera : ",recette)
    maliste.append(recette)
print(max(maliste))

print("La recette quotidienne du loueur sera de", max(maliste),"euros","pour 75 vélos loués à 37,5€.")


