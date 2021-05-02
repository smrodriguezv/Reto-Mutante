
#Se definen variables de constantes
SEC_PERMITIDA= ("AAAA","CCCC","GGGG","TTTT") #Representa las secuencias que identifica las posibilidad de ser Mutante.
TOTAL_EJES = 4 #Representa la cantidad de Ejes, horizontal, vertical, oblicuo derecha->Izquierda, y oblicuo izquierda->Derecha.
SEC_VALIDA = 2 #Representa la cantidad minima de secuencias validas.
LONG_SEC=4      #Represente la longitud de la secuencia, en este caso es 4 porque cada secuencia debe ser de 4 caracteres.


#definición de funciones que captura la información de ADN por ejes y busca secuencias permitidas  

#metodo que captura la información de ADN del eje Horizontal
def ejeHorizontal(dna):
    strHorizontal = ""
    for i in range(len(dna)):
        strHorizontal += (dna[i] + ",")
    return strHorizontal

#metodo que captura la información de ADN del eje Vertical
def ejeVertical(dna):
    strVertical = ""
    for i in range(len(dna)):
        for j in range (len(dna)):
            strVertical += dna[j][i]
        strVertical += ","
    return strVertical

#metodo que captura la información de ADN del eje Oblicuo Izquierda a Derecha
def ejeOblicuoIz(dna):
    strOblicuoIz = ""
    lenDna=(len(dna)-1)
    for j in range((LONG_SEC-1),len(dna)):
        strOblicuoIzA=""
        strOblicuoIzB=""
        for i in range (j+1):
            strOblicuoIzA += dna[lenDna-(j-i)][(i)]
            if j!=(lenDna):
                strOblicuoIzB += dna[i][lenDna-(j-i)]
        strOblicuoIz += (strOblicuoIzA +"," + strOblicuoIzB + ",")
    return strOblicuoIz

#metodo que captura la información de ADN del eje Oblicuo Derecha a Izquierda
def ejeOblicuoDe(dna):
    strOblicuoDe = ""
    lenDna=(len(dna)-1)
    for j in range((LONG_SEC-1),len(dna)):
        strOblicuoDeA=""
        strOblicuoDeB=""
        for i in range (j+1):
            strOblicuoDeA += dna[i][(j-i)]
            if j!=(lenDna):
                strOblicuoDeB += dna[lenDna-(j-i)][lenDna-i]
        strOblicuoDe += (strOblicuoDeA +"," + strOblicuoDeB + ",")
    return strOblicuoDe


switchEje = {
    0: ejeHorizontal,
    1: ejeVertical,
    2: ejeOblicuoIz,
    3: ejeOblicuoDe,
}


#metodo que busca secuencias que definen a un Hombre Mutante
def BuscaSecuencia (dnaEje):
    cantSec=0
    for i in range(len(SEC_PERMITIDA)):
        encuentro=dnaEje.find(SEC_PERMITIDA[i],0,(len(dnaEje)-1))
        while (encuentro>=0):
            cantSec +=1;
            encuentro=dnaEje.find(SEC_PERMITIDA[i],(encuentro+len(SEC_PERMITIDA[i])),(len(dnaEje)-1))
            if cantSec >= SEC_VALIDA:
                return cantSec
        if cantSec >= SEC_VALIDA:
            return cantSec
    return cantSec
    