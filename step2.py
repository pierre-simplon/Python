# On importe les modules qui vont nous permettre de traiter les données
# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv

# Declaration du path localisant les fichiers dezippés
path='/home/bnp-renault-014/Code/python/Projet/constantes-nourrissons/'

# Definition d'une fonction permettant de charger les references depuis les fichiers en fonction du genre
def charger_fichier(gender):
    # initialisation des deciles des poids
    d5_poids=[]
    d25_poids=[]
    d50_poids=[]
    d75_poids=[]
    d95_poids=[]
    # initialisation des deciles des tailles
    d5_tailles=[]
    d25_tailles=[]
    d50_tailles=[]
    d75_tailles=[]
    d95_tailles=[]
    # initialisation des deciles des ranes
    d5_cranes=[]
    d25_cranes=[]
    d50_cranes=[]
    d75_cranes=[]
    d95_cranes=[]
    # Cas des filles
    if gender=="f":
        name_gender='fille'
    if gender=="g":
        name_gender='garcon'
    with open(f'{path}poids-age-{name_gender}-0-60.csv','r') as csv_file:
        try:
            reader = csv.reader(csv_file, delimiter=';')
            headers = next(reader)
            for row in reader:
                d5_poids.append(float(row[7]))
                d25_poids.append(float(row[10]))
                d50_poids.append(float(row[11]))
                d75_poids.append(float(row[12]))
                d95_poids.append(float(row[15]))
        finally:
            csv_file.close()
    with open(f'{path}taille-age-{name_gender}-0-60.csv','r') as csv_file:
        try:
            reader = csv.reader(csv_file, delimiter=';')
            headers = next(reader)
            for row in reader:
                d5_tailles.append(float(row[8]))
                d25_tailles.append(float(row[11]))
                d50_tailles.append(float(row[12]))
                d75_tailles.append(float(row[13]))
                d95_tailles.append(float(row[16]))
        finally:
            csv_file.close()
    with open(f'{path}perim-cra-age-{name_gender}-0-60.csv','r') as csv_file:
        try:
            reader = csv.reader(csv_file, delimiter=';')
            headers = next(reader)
            for row in reader:
                d5_cranes.append(float(row[8]))
                d25_cranes.append(float(row[11]))
                d50_cranes.append(float(row[12]))
                d75_cranes.append(float(row[13]))
                d95_cranes.append(float(row[16]))
        finally:
            csv_file.close()      
    return [[d5_poids,d5_tailles,d5_cranes],[d25_poids,d25_tailles,d25_cranes],[d50_poids,d50_tailles,d50_cranes],[d75_poids,d75_tailles,d75_cranes],[d95_poids,d95_tailles,d95_cranes]]

# Récupération des mesures dans le fichier mesures.csv
mois=[]
poids=[]
taille=[]
crane=[]
with open('/home/bnp-renault-014/Code/python/Projet/mesures.csv','r') as csvfile:
  try:
      readcsv = csv.reader(csvfile, delimiter=';')
      headers = next(readcsv) 
      for row in readcsv:
          # lecture des ages mesurés
          mois.append(int(row[0]))
          # lecture des poids mesurés         
          poids.append(float(row[1]))
          # lecture des tailles mesurées 
          taille.append(float(row[2]))
          # lecture des cranes mesurés 
          crane.append(float(row[3]))
  finally:
      csvfile.close()          

# Debut de l'interaction avec l'utilisateur
print('Bienvenu dans ce programme de vérification des constantes de votre nourrison !')
genre="O"
while (genre !="f") and (genre !="g"):
    genre = input('Entrez le genre de votre nourisson ("f" pour fille "g" pour garçon): ')
    if (genre !="f") and (genre !="g"):
        print("Veuillez saisir un 'f' ou un 'g' uniquement !")

# Import des courbes de référence depuis les different fichiers contenus dans le zip
if genre=="f":
    [[d5_poids,d5_tailles,d5_cranes],[d25_poids,d25_tailles,d25_cranes],[d50_poids,d50_tailles,d50_cranes],[d75_poids,d75_tailles,d75_cranes],[d95_poids,d95_tailles,d95_cranes]]=charger_fichier("f")
if genre=="g":
    [[d5_poids,d5_tailles,d5_cranes],[d25_poids,d25_tailles,d25_cranes],[d50_poids,d50_tailles,d50_cranes],[d75_poids,d75_tailles,d75_cranes],[d95_poids,d95_tailles,d95_cranes]]=charger_fichier("g")

# Affichage des mesures des poids en fonction de l'age
fig,(fig1,fig2,fig3) = plt.subplots(1,3)
fig1.set_xlabel('Age en mois')
fig1.set_ylabel('Poids en kg')
fig2.set_xlabel('Age en mois')
fig2.set_ylabel('Tailles en cm')
fig3.set_xlabel('Age en mois')
fig3.set_ylabel('Périmètre cranien en cm')

fig1.scatter(mois,poids,color='black')

# Affiche les courbes des poids de reference
fig1.plot(range(0,61),d5_poids,label='5% Poids',color='blue')
fig1.plot(range(0,61),d25_poids,label='25% Poids',color='orange')
fig1.plot(range(0,61),d50_poids,label='50% Poids',color='green')
fig1.plot(range(0,61),d75_poids,label='75% Poids',color='red')
fig1.plot(range(0,61),d95_poids,label='95% Poids',color='plum')

# Affichage des mesures des tailles en fonction de l'age
fig2.scatter(mois,taille,color='black')
# Affiche les courbes des tailles de reference
fig2.plot(range(0,61),d5_tailles,label='5% Tailles',color='blue')
fig2.plot(range(0,61),d25_tailles,label='25% Tailles',color='orange')
fig2.plot(range(0,61),d50_tailles,label='50% Tailles',color='green')
fig2.plot(range(0,61),d75_tailles,label='75% Tailles',color='red')
fig2.plot(range(0,61),d95_tailles,label='95% Tailles',color='plum')

# Affichage des mesures des cranes en fonction de l'age
fig3.scatter(mois,crane,color='black')
# Affiche les courbes des cranes de reference
fig3.plot(range(0,61),d5_cranes,label='5% Périmètre cranien',color='blue')
fig3.plot(range(0,61),d25_cranes,label='25% Périmètre cranien',color='orange')
fig3.plot(range(0,61),d50_cranes,label='50% Périmètre cranien',color='green')
fig3.plot(range(0,61),d75_cranes,label='75% Périmètre cranien',color='red')
fig3.plot(range(0,61),d95_cranes,label='95% Périmètre cranien',color='plum')

# Ajout d'un titre
fig.suptitle('Les courbes de référence et vos mesures')

# Localisation des legendes
fig1.legend(loc='upper left')
fig2.legend(loc='upper left')
fig3.legend(loc='lower right')

plt.show()



