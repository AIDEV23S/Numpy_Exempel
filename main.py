import numpy as np # importera NUMPY 

#Skapa en vektor med nollor 
arr = np.zeros(10)

#Skapa en vektor med ettor
arr2 = np.ones(4) 

#Skapa en tom vektor
arr3 = np.empty(5)

#Skapa en vektor med startvärde, stoppvärde, antal_element
arr4 = np.linspace(2,10,5)

#Skapa en vektor från en lista
lista = [2,5,7,9]
arr5 = np.array(lista)

#Lägg till talet 5.5 till alla element i vektor
#Svaret i ny vektor
arr6 = arr5+5.5

#Beräkna summan av alla element i en veckor
summan = np.sum(arr5)

#Beräkna produkten av två vektorer 
#Svaret i ny vektor
arr7 = arr5*arr6

#Info om en vektor
np.shape(arr2)

#Skapa en 3x3 matris
rad0 = [1,2,3]
rad1 = [4,5,6]
rad2 = [7,8,9]
mat1=  np.array(rad0,rad1,rad2)

#Skapa en 2-D vektor av en 1-D vektor
arr8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr9 = arr8.reshape(4, 3)

#Skapa transponatet till en matris
mat2 = np.transpose(mat1)

#Skapa lista av en 1-D vektor
Lista2 = list(arr5)
