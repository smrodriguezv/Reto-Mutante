#Se realzian pruebas Unitarias de la solución

import unittest
import EsMutante


class TestEsMutante(unittest.TestCase):
    #Caso1. no cumple NxN en el Primer registro y es mayor
    def test_esMutante_NoCumple_NxN_1(self):
        self.assertEqual(EsMutante.isMutant(("ATGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATGG")),EsMutante.NO_CUMPLE_NxN)

    #Caso2. no cumple NxN en el Primer registro y es menor
    def test_esMutante_NoCumple_NxN_2(self):
        self.assertEqual(EsMutante.isMutant(("GCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATGG")),EsMutante.NO_CUMPLE_NxN)
    #Caso3. no cumple NxN en el ultimo registro y es mayor
    def test_esMutante_NoCumple_NxN_3(self):
        self.assertEqual(EsMutante.isMutant(("TGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATGGG")),EsMutante.NO_CUMPLE_NxN)
    #Caso4. no cumple NxN en el Primer registro y es menor
    def test_esMutante_NoCumple_NxN_4(self):
        self.assertEqual(EsMutante.isMutant(("TGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATG")),EsMutante.NO_CUMPLE_NxN)
    #Caso5. no cumple NxN todos los registros tienen tamaño diferente
    def test_esMutante_NoCumple_NxN_5(self):
        self.assertEqual(EsMutante.isMutant(("TTGCGAA","TGC","ATGT","GAAGG","CCCCTA","G")),EsMutante.NO_CUMPLE_NxN)
    #Caso6. no cumple NxN en contiene menos registros que la longitud
    def test_esMutante_NoCumple_NxN_6(self):
        self.assertEqual(EsMutante.isMutant(("TGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATGG","TAATGG")),EsMutante.NO_CUMPLE_NxN)
    #Caso7. no cumple NxN en el Primer registro y es menor
    def test_esMutante_NoCumple_NxN_7(self):
        self.assertEqual(EsMutante.isMutant(("TGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA")),EsMutante.NO_CUMPLE_NxN)
   
   #Caso8. no cumple con la condición de letras A,C,T,G tiene caracter diferente en el primer registro
    def test_esMutante_NO_CUMPLE_LETRAS_1(self):
        self.assertEqual(EsMutante.isMutant(("1GCGAAA","CAGTGCA","TTATGTA","AGAAGGA","CCCCTAA","TAATGGA","TAATGGA")),EsMutante.NO_CUMPLE_LETRAS)
    #Caso9. no cumple con la condición de letras A,C,T,G tiene caracter diferente en el ultimo registro
    def test_esMutante_NO_CUMPLE_LETRAS_2(self):
        self.assertEqual(EsMutante.isMutant(("TGCGAAA","CAGTGCA","TTATGTA","AGAAGGA","CCCCTAA","TAATGGA","TAATGGj")),EsMutante.NO_CUMPLE_LETRAS)
    #Caso10. no cumple con la condición de letras A,C,T,G tiene caracter diferentes en todos los registros
    def test_esMutante_NO_CUMPLE_LETRAS_3(self):
        self.assertEqual(EsMutante.isMutant(("1GCGAAA","eAGTGCA","ETATGTA","AGAdGGA","CCCVTAA","TAAGGAF","TAATGGj")),EsMutante.NO_CUMPLE_LETRAS)
        
    #Caso11. Humano no Mutante coincide secuencia los ultimpos del primer registro con los primeros del segundo registro de manera Horizontal
    def test_esMutante_HUMANO_NO_MUTANTE_1(self):
        self.assertEqual(EsMutante.isMutant(("ATGCAA","AAGTGG","GGATTT","TTAAGG","ACCCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)
    #Caso12. Humano no Mutante coincide secuencia los ultimpos del primer registro con los primeros del segundo registro de manera vertical
    def test_esMutante_HUMANO_NO_MUTANTE_2(self):
        self.assertEqual(EsMutante.isMutant(("AAGCTT","AAGTGG","GGATTT","TTAAGG","ACCCTA","AAATGG")),EsMutante.HUMANO_NO_MUTANTE)   
    #Caso13. Humano no Mutante coincide secuencia de 3 caracteres de manera Horizontal
    def test_esMutante_HUMANO_NO_MUTANTE_3(self):
        self.assertEqual(EsMutante.isMutant(("AAAGAA","AAGTGG","GGATTT","AGAAGG","CTCCTA","TAATTT")),EsMutante.HUMANO_NO_MUTANTE)
    #Caso14. Humano no Mutante coincide secuencia de 3 caracteres de manera Vertical
    def test_esMutante_HUMANO_NO_MUTANTE_4(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTGG","AGATTT","CGAAGG","ACCCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)     
    #Caso15. Humano no Mutante coincide secuencia de 3 caracteres de manera oblicua
    def test_esMutante_HUMANO_NO_MUTANTE_5(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTGG","GGACTT","AGAAGG","ACCCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)
    #Caso16. Humano no Mutante coincide 1 sola secuencia de manera horizontal
    def test_esMutante_HUMANO_NO_MUTANTE_6(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTGG","GGACTT","AGACGG","CCCCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)    
    #Caso17. Humano no Mutante coincide 1 sola secuencia de manera Vertical
    def test_esMutante_HUMANO_NO_MUTANTE_7(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTGG","AGACTT","AGACGG","AACCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)    
    #Caso18. Humano no Mutante coincide 1 sola secuencia de manera Oblicua de izquierda a derecha
    def test_esMutante_HUMANO_NO_MUTANTE_8(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTGG","AGACTT","CGAAGG","AACCTA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)    
    #Caso19. Humano no Mutante coincide 1 sola secuencia de manera Oblicua de derecha  a izquierda
    def test_esMutante_HUMANO_NO_MUTANTE_9(self):
        self.assertEqual(EsMutante.isMutant(("ATGGAA","AAGTAG","AGAATT","CGAGGG","AACCGA","TAATGG")),EsMutante.HUMANO_NO_MUTANTE)              
 
    #Caso20. Humano  Mutante coincide 2 secuencias una horizontal (primer registro AAAA) y otra vertical (segundo registro CCCC)
    def test_esMutante_HUMANO_MUTANTE_1(self):
        self.assertEqual(EsMutante.isMutant(("AAAACC","ACGTAG","ACAATT","CCAGGG","TCCCGA","TAATGG")),EsMutante.HUMANO_MUTANTE)
    #Caso21. Humano  Mutante coincide 2 secuencias una horizontal (primer registro AAAA) y otra vertical (ultimo registro AAAA)
    def test_esMutante_HUMANO_MUTANTE_2(self):
        self.assertEqual(EsMutante.isMutant(("AAAACC","AAGTAG","ACAATA","CCAGGA","TCCCGA","TAATGA")),EsMutante.HUMANO_MUTANTE)           
    #Caso22. Humano  Mutante coincide 2 secuencias una horizontal (primer registro AAAA) y otra horizontal (ultimo registro AAAA)
    def test_esMutante_HUMANO_MUTANTE_4(self):
        self.assertEqual(EsMutante.isMutant(("AAAACC","AAGTAG","ACAATA","CCAGGA","TCCCGC","TAAAAA")),EsMutante.HUMANO_MUTANTE)           
    #Caso23. Humano  Mutante coincide 2 secuencias una horizontal (primer registro AAAA) y otra horizontal (ultimo registro TTTT)
    def test_esMutante_HUMANO_MUTANTE_5(self):
        self.assertEqual(EsMutante.isMutant(("AAAACC","AAGTAG","ACAATA","CCAGGA","TCCCGC","TATTTT")),EsMutante.HUMANO_MUTANTE)           
    #Caso24. Humano  Mutante coincide 2 secuencias una horizontal en un mismo registro "AAAA" "AAAAA" Criterio de aceptación definido
    def test_esMutante_HUMANO_MUTANTE_6(self):
        self.assertEqual(EsMutante.isMutant(("AAAAAAAA","ACTGACTG","GTCGCTAA","ACTGACTG","GTCACTAA","ACTGACTG","GTCGATAA","ACTGCCTG")),EsMutante.HUMANO_MUTANTE)           
    #Caso25. Humano  Mutante coincide 2 secuencias una horizontal en un mismo registro "GGGG" "AAAAA" Criterio de aceptación definido
    def test_esMutante_HUMANO_MUTANTE_7(self):
        self.assertEqual(EsMutante.isMutant(("GGGGAAAA","ACTGACTG","GTCGCTAA","ACTGACTG","GTCACTAA","ACTGACTG","GTCGATAA","ACTGCCTG")),EsMutante.HUMANO_MUTANTE)           
    #Caso26. Humano  Mutante coincide 2 secuencias una horizontal (primer registro TTTT) y otra horizontal (ultimo registro AAAA)
    def test_esMutante_HUMANO_MUTANTE_8(self):
        self.assertEqual(EsMutante.isMutant(("TTTTACCG","ACTGACTG","GTCGCTAA","ACTGACTG","GTCACTAA","ACTGACTG","GTCGATAA","ACTGAAAA")),EsMutante.HUMANO_MUTANTE)                                                               
    #Caso27. Humano  Mutante coincide 2 secuencias vertical (primer registro CCCC) y otra horizontal (ultimo registro GGGG)
    def test_esMutante_HUMANO_MUTANTE_9(self):
         self.assertEqual(EsMutante.isMutant(("CAACCC","CAGTAG","CCAATG","CCAGGG","TGGCGG","TAACAG")),EsMutante.HUMANO_MUTANTE)   
    #Caso28. Humano  Mutante coincide 2 secuencias una horizontal (primer registro CCCC) y otra Oblicua de izquierda a derecha (TTTT)
    def test_esMutante_HUMANO_MUTANTE_10(self):
         self.assertEqual(EsMutante.isMutant(("CCCCAG","CTGTAG","CCTATG","ACATGC","TGGCTG","TAACAT")),EsMutante.HUMANO_MUTANTE)            
    #Caso29. Humano  Mutante coincide 2 secuencias una Vertical (primer registro AAAA) y otra Oblicua de izquierda a derecha (CCCC)
    def test_esMutante_HUMANO_MUTANTE_11(self):
         self.assertEqual(EsMutante.isMutant(("ACCCAG","ATGCAG","ACTACG","ACATGC","TGGCGG","TAACAT")),EsMutante.HUMANO_MUTANTE)   
    #Caso29. Humano  Mutante coincide 2 secuencias una Oblicuo de Izquierda a derecha (primer registro CCCC) y otra Oblicua de derecha a izquierda (TTTT)
    def test_esMutante_HUMANO_MUTANTE_12(self):
         self.assertEqual(EsMutante.isMutant(("CGCCAT","ACGCTG","ACCTCG","ACTCGA","TGGCGG","TAACAT")),EsMutante.HUMANO_MUTANTE)   
    #Caso30. Humano  Mutante coincide 2 secuencias una horizontal(ultimo regoistro registro GGGG) y otra Oblicua de derecha a izquierda (GGGG)
    def test_esMutante_HUMANO_MUTANTE_12(self):
         self.assertEqual(EsMutante.isMutant(("CGCCAT","AGGCCG","ACCTCG","ACTCGA","TGAGGG","TAGGGG")),EsMutante.HUMANO_MUTANTE)   
    
   
if __name__=='__main__':
    unittest.main()
    #main()