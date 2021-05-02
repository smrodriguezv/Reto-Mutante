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

import metodoSecuencia


#Se definen variables de resupuesta de llamado de metodo isMutant

NO_CUMPLE_NxN={'statusCode':400,
                'descripcion': "NO_CUMPLE_NXN"
}
NO_CUMPLE_LETRAS={'statusCode':400,
                'descripcion': "NO_CUMPLE_LETRAS"
}

ESTRUCTURA_VALIDA={'statusCode':200,
                'descripcion': "ESTRUCTURA_VALIDA"
}

HUMANO_NO_MUTANTE={'statusCode':200,
                'descripcion': "HUMANO_NO_MUTANTE"
}
HUMANO_MUTANTE={'statusCode':200,
                'descripcion': "HUMANO_MUTANTE"
}


#metodo para validar que la estructura del adn cumpla con la condición de NxN
def validaTablaNxN(dna):
    for i in range(len(dna)):
        if len(dna[i]) != len(dna):
            return False
    return True


#metodos para validar que la estructura del adn cumpla con la condición de solo letras A,T,C,G
def Correcto():
    return True

def Error():
    return False
    
switch_Letra = {
    'A': Correcto,
    'T': Correcto,
    'C': Correcto,
    'G': Correcto,
}
    
def validaLetras(dna):
    for i in range(len(dna)):
        for y in range(len(dna)):
            if switch_Letra.get(dna[i][y],Error)()==False:
                return False
    return True


#metodo que valida los diferentes criterios de aceptación en estructura, en éste caso solo se valida que la estructura del ADN sea NxN y las letras deben ser A,C,G,T
def validaEstruct(dna):
    if validaTablaNxN(dna) == False:
        return NO_CUMPLE_NxN
    if validaLetras(dna) == False:
        return NO_CUMPLE_LETRAS
    return ESTRUCTURA_VALIDA   
        
#Metodo que define si un humano es mutante o no, hace llamdo a validar si la estructura es correcta y luego hace llamado a identifiar si el humano es mutante.
#Regresa 3 tipos de respuesta 1.si la estructura es correcta, 2. si es Mutante y 3 si no es Mutante. 
def isMutant(dna):
    respuesta = validaEstruct(dna)
    if respuesta!=ESTRUCTURA_VALIDA:
        return respuesta
    secuencias=0
    for i in range(metodoSecuencia.TOTAL_EJES):
        dnaEje = metodoSecuencia.switchEje.get(i)(dna)
        secuencias+=metodoSecuencia.BuscaSecuencia(dnaEje)
        if secuencias >= metodoSecuencia.SEC_VALIDA:
            return HUMANO_MUTANTE
    return HUMANO_NO_MUTANTE
    
