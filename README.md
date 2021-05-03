# Reto-Mutante

Se crea funcionalidad que identifica si un Humano es Mutante o no, adicional se crea funcionalidad para regresar el Ratio de la cantida de Mutantes VS Humanos registrados
La funcionalidad se encuentra desarrollada en Python y se expondra en Nube AWS.


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

Nivel 2:
Crear una API REST, hostear esa API en un cloud computing libre (Google App Engine, Amazon AWS, etc), crear el servicio “/mutant/”
en donde se pueda detectar si un humano es mutante enviando la secuencia de ADN mediante un HTTP POST con un Json el cual tenga el
siguiente formato
POST → /mutant/
{
	“dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}

Nivel 3:

Anexar una base de datos, la cual guarde los ADN’s verificados con la API.
Solo 1 registro por ADN.
Exponer un servicio extra “/stats” que devuelva un Json con las estadísticas de las
verificaciones de ADN: {“count_mutant_dna”:40, “count_human_dna”:100: “ratio”:0.4}
**************************************************************************************

							A continuación se describe el proceso de la aplicación y como implementarla bajo el siguiente menú:

1. ******Funcionalidad que identifica Humano y lo almacena *******
2. ******Funcionalidad que regresa el ratio del ADN *******
3. ******Cómo ejecutar el programa**********************
4. ******Cómo consumir las APIs**********************



1. ******Funcionalidad que identifica Humano y lo almacena *******

Se crean 6 archivos python que consta de 4 funcionales y otros 2 para realizar pruebas unitarias y de escritorio.

*****Archivos Funcionales
1.1 Lambda_function.py
	Es la que recibe el consumo de api rest POST /mutant ejemplo : {"dna":["ATGCGAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TAATGG"]}, y luego hace llamado a la función de identificar
	si es mutante o no: EsMutante.isMutant(dna) que se encuentra en archivo es Mutante. De recibir correctametne  y sin ecepción por estructura, se llama al metodo de almacenar el ADN y su 
	estado: AlmacenaDna.AlmacenDna(dna,result), que se encuentra en archivo AlmacenaDna. fianalmente regresa el estado de la solicitud bajo el siguiente body
		{
			'statusCode': 'respuesta HTTPS',  -> esta puede ser 400-si existe un error de estructura o 200 si la estructura es correcta o el estado que regrese el almacenado de la base de datos. 
			'descripción': 'descripcón del estado´' ->en caso de ser 400 permite 3 estados  error de longitud de registros, debe ser NxN, y error en los caracteres si son diferentes a A,C,G,T, en caso de ser 200
													se regresa si es Mutante o no es Mutante, en caso de tener fallo en el registro en Base de datos se regresa error que no se pudo almacenar.
		}

1.2. EsMutante.py
	Contiene el metodo principal de isMutant(dna), quien recibe el DNA, valida su estructura (que cumpla NxN->validaEstruct(dna) y que cumpla letras ->validaLetras(dna)); una vez validada su estructura, 
	genera la busqueda de dos o mas secuencias permitidas con el método  metodoSecuencia.BuscaSecuencia(dnaEje) que se encuentra en archivo metodoSecuencia.py, aqui se recorre la estructura del ADN para buscar
	secuencias permitidas "AAAA" "CCCC" "GGGG" "TTTT".
	Finalmente regresa el estado del proceso bajo el siguiente body:
		{
			'statusCode': 'respuesta HTTPS',  -> esta puede ser 400-si existe un error de estructura o 200 si la estructura es correcta 
			'descripción': 'descripcón del estado´' ->en caso de ser 400 permite 3 estados  error de longitud de registros, debe ser NxN, y error en los caracteres si son diferentes a A,C,G,T, en caso de ser 200
													se regresa si es Mutante o no es Mutante.
		}										
	
1.3. metodoSecuencia.py
	Contiene metodo principal BuscaSecuencia(dna), quien se encarga de buscar la secuencias en los diferentes ejes(llamando funciones para obtenerlos), de acuerdo a ello las funciones para obtener los ejes son 
	-para obtener los horizontales ->ejeHorizontal(adn)- regresa toda la información del eje
	-para obtener los verticales-> ejeVertical(dna) -regresa toda la información del eje
	-para obtener los oblicuas de izquierda a derecha -> ejeOblicuoIz(dna)- regresa toda la información del eje
	-para obtener los oblicuas de derecha a izquierda -> ejeOblicuoDe(dna)-regresa toda la información del eje
	la respuesta del metodo principal regresa la cantidad de secuencias encontradas, >1 significa que es Mutante.
	
1.4. AlmacenaDna.py
	Contiene un metodo principal AlmacenDna(dna,result), que almacena en base de datos Dynamondb de AWS, para ello fuen necesario configurarlo y crear una tabla llamada 'RegistrosDna', donde tiene dos llaves cuya
	llave de partición es la descripción (Cadena) que es igual a 'descripción' y la llave de ordenación es el ADN (Cadena) que es igual al 'adn', en la descripción se almacena si es mutante(HUMANO_MUTANTE)o si 
	no lo ES (HUMANO_NO_MUTANTE)
	
	
*****Archivos no Funcionales de Test

1.5. EsMutante_Prueba.py
	Se creó este archivo para realizar las primeras pruebas de la funcionalidad de validar si es mutante o no un Humano. basicamente declara una variable de dna y llama al metodo isMutant(dna) e imprime el 
	resultado en consola. 

1.6. test_Unitarias.py
	Se creó este archivo para realizar pruebas unitarias, donde se exponen 30 casos especiales para poder realizar tadas las posibles validaciones de la esctructura del ADN y si es mutante o no. 
	a correr el ser de pruebas con el comando pytest se valida que todas cumplen con el proposito:
	USUARIO@LAPTOP-0Q54MQCM MINGW64 ~/Documents/GitHub/Reto Mutante/Reto-Mutante/esMutante (main)
		$ pytest
		============================= test session starts =============================
		platform win32 -- Python 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
		rootdir: C:\Users\USUARIO\Documents\GitHub\Reto Mutante\Reto-Mutante\esMutante
		plugins: cov-2.11.1
		collected 31 items

		test_Unitarias.py ...............................                        [100%]

		============================= 31 passed in 0.07s ==============================
	Adicional se realiza proceso de Covertura de codigo sobre la ejecución de las pruebas la cual tubó un resultado del 99%:
			$ coverage report -m
		Name                 Stmts   Miss  Cover   Missing
		--------------------------------------------------
		EsMutante.py            39      0   100%
		metodoSecuencia.py      53      1    98%   75
		test_Unitarias.py       67      0   100%
		--------------------------------------------------
		TOTAL                  159      1    99%
		

2. ****Funcionalidad que regresa el ratio del ADN****

Se crean 2 archivos python que consta de la funcionalidad para consultar el ratio de los ADN almacenados, para este caso no se contemplaron pruebas unitarias

2.1 lambda_function.py
	Es la que recibe el consumo de api rest GET /stats sin cuerpo, y luego hace llamado a la función de EstadoDNA.ratio_mutante() que se encuentra en archivo EstadoDNA quien realzia la busqueda en base 
	de datos dynamondb de AWS cuya tabla es 'RegistrosDna', los ADN y el calculo del ratio. éste metodo regresa el siguiente cuerpo:
	{
		'statusCode':200
		'count_mutant_dna':Cantidad de mutantes,
		'count_human_dna':Cantidad de registros almacenados
		'ratio':el ratio de mutantes VS humanos registrados
	}
	o
	{
		'statusCode': XXX ->Error que regresa el consumo a la base de datos
		'descripción': 'Falla en la lectura de Base de datos',
	}
	De recibir correctametne  y sin ecepción por estructura,
	se llama al metodo de almacenar el ADN y su estado: AlmacenaDna.AlmacenDna(dna,result), que se encuentra en archivo AlmacenaDna. fianalmente regresa el estado de la solicitud bajo el siguiente body
	{
		'statusCode': 'respuesta HTTPS',  -> esta puede ser 400-si existe un error de estructura o 200 si la estructura es correcta o el estado que regrese el almacenado de la base de datos. 
		'descripción': 'descripcón del estado´' ->en caso de ser 400 permite 3 estados  error de longitud de registros, debe ser NxN, y error en los caracteres si son diferentes a A,C,G,T, en caso de ser 200
												se regresa si es Mutante o no es Mutante, en caso de tener fallo en el registro en Base de datos se regresa error que no se pudo almacenar.
	}


******Funcionalidad que regresa *******