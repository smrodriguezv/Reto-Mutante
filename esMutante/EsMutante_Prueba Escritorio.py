'''
´----------------------------------------Define si un Humano es mutante ---------------------------------------
Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras
En donde recibirás como parámetro un array de Strings que representan cada fila de una tabla de (NxN) con la secuencia del ADN. 
Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.
      No-Mutante                            Mutante
  A  T  G  C  G  A                    |A| T  G  C |G| A
  C  A  G  T  G  C                     C |A| G  T |G| C
  T  T  A  T  T  T                     T  T |A| T |G| T
  A  G  A  C  G  G                     A  G  A |A||G| G
  G  C  G  T  C  A                    |C||C||C||C| T  A
  T  C  A  C  T  G                     T  C  A  C  T  G
Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical.
'''

import EsMutante


#Casos de prueba
#Mutante 6X6 en eje x, y, y Oblicuo derecha
#dna=("ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG")
#No Mutante 6x6 no tiene ninguna secuencia
#dna=("ATGCGA","CAGTGC","TTATGT","AGAAGG","ACCCTA","TCACTG")
#No Mutante 7x7 solo tiene 1 secuencia
#dna=("TTGCGAA","CAGTGCC","TTATGTA","AGAAGGC","ACCCTAA","TCACTGC","TCACTGC")
# Mutante 7x7 2 secuencias
#dna=("ATGCGAA","CAGTGCC","TTATGTA","AGAAGGC","ACCCTAA","TCACTGC","TCACTGC")
#2 en el mismo eje 12x12
#dna=("ATGCGAATGCGA","CAGTGCCAGTGC","TTATGTTTATGT","AGAAGGAGAAGG","ACCCTAACCCTA","TCACTGTCACTG","ATGCGAATGCGA","CAGTGCCAGTGC","TTATGTTTATGT","AGAAGGAGAAGG","ACCCTAACCCTA","TCACTGTCACTG")
#diferentes letras Error de estructura
#dna=("1TGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG")
#diferentes letras Error de estructura
dna=("AAAAA","AAAAA","AAAAA","AAAAA","AAAAA")
#diferentes tamaño Error de estructura
#dna=("ATGCGA2","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATG")#diferente tamaño
x = EsMutante.isMutant(dna)
print (x)

    
    
#"ATGCGAA"
#"CAGTGCC"
#"TTATGTA"
#"AGAAGGC"
#"ACCCTAA"
#"TCACTGC"
#"TCACTGC"