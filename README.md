# Reto-Mutante
#desarrollado por Sandra Rodriguez, Cel: 3118271812, Para Mercado Libre

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

**Aclaraciones previas a la implementación
1. para el desarrollo de la solución, y para seguir buenas practicas se cambia el alcance de la función de identificar mutante, donde se solicita regresar True si es Mutante, y False si no lo es. se modifica
a regresar una estructura tipo json, donde se indique el estado, esto indica adicional al saber si es mutante o no, si la estructura es correcta o existe algun inconveniente en el almacenado de la base de datos. 
2. En el API rest de mutante se indica que debe regresar 403 si no es mutante, este error HTTPS es para indicar que no se autenticó, lo cual no obedece a la razon real del rechazo y puede confundir al que lo consume, 
por ello se define que la respuesta 200 indica si el ADN es valido, y si es mutante o no es una descripción que se puede entregar en el cuerpo del mensaje, como in ID de respuesta. y en cuanto al fallo de estructura 
se regresa un mensaje 400, que indica que el mensaje se encuentra erroneo. adicional se incluye el mensaje HTTP que regrese el consumo a la base de datos. 
3. En cuanto a la logica de identificar si es mutante o no, y teniendo presente que el ADN puede ser NxN, podriamos tener de 8x8, lo que puede causar que en un mismo subregistro, se encuentre dos secuencias, aun siendo 
   seguidas. de acuerdo a ello se defini que es valido tener dos secuencias en el mismo subregistro de la siguiente manera:

               Mutante

  A  T  G  C  G  A  A  T  G  C  G  A                
  C  A  G  T  G  C  C |A||G| T  G  C                   
  T  T  A  T  T  T  C |A||G| T  G  C                  
  A  G  A  C  G  G  A |A||G| C  G  C                  
  G  C  G  T  C  A  C |A||G| T  G  C                 
  T  C  A  C  T  G  C  A |G| T  G  C                  
  A  T  G  C  G  A  A  T |G| C  G  A                
  C  A  G  T  G  C  C |A||G| T  G  C                   
  T  T  A  T  T  T  A |A||G| T  G  C                  
  A  G  A  C  G  G  C |A| G  G  G  C                  
  G  C  G  T  C  A  C |A| G  T  G  C                 
  T  C  A  C  T  G  C  A  G  T  G  C     
  
4. Como la definición es que si se encuentran mas de dos secuencias es un humano mutante, y para optimizar el funcionamiento, se define que la funcionalidad al momento de contabilizar 2 secuencia, detenga la busqueda y
 retorne la validación de HUMANO_MUTANTE.
5. Se incluye como validación adicional, las oblicuas no solo de izquierda a derecha si no de derecha a izquierda.  
6. Se tiene un dilema en el tipo de metodo de validación de ser Mutante, porque se indica que debe ser POST, e inicialmente se solicita que regrese una validación por lo que no correspondería, sin embargo como se debe almacenar 
	el ADN entonces si sería valido.  de acuerdo a ello se mantiene el tipo de método. 
7. se incluye en la respuesta de la consulta del ratio el estatus Code, que identifica si la consulta a la base de datos es exitosa o no. 

8. Se procede a contruir el aplicativo con los siguientes pasos:
8.1.	Se aclara la funcionalidad requerida
8.2.    Se planifica la contrucción de la solución
	8.2.1 	Se define arquitectura de la solución (adjunto en el siguiente link)
	8.2.2	Se contruyen pruebas unitarias	
	8.2.3   H.U.1. Se construye funcionalidad Mutante criterios de aceptación ya mencionados., se incluyen pruebas Unitarias. 
	8.2.4   H.U.2. Se contruye API_REST en AWS de validación Mutante, se configura arquitectura en Nube. se realizan pruebas de PostMan, subir a repositorio GitHub
	8.2.5   H.U.3. Se contruye Configuración Base de datos en AWS y se desarrolla almacenado de información.  se realizan pruebas de PostMan,  subir a repositorio GitHub
	8.2.6   H.U.4. Se contruye API_REST en AWS de ratio, se configura arquitectura en Nube. se realizan pruebas de PostMan,  subir a repositorio GitHub
	8.2.7   Se finaliza documentación y se hace entrega del proyecto 



*******************************A continuación se describe el proceso de la aplicación y como implementarla bajo el siguiente menú:

1. ******Funcionalidad que identifica Humano y lo almacena *******
2. ******Funcionalidad que regresa el ratio del ADN *******
3. ******Cómo ejecutar el programa**********************



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
	Contiene un metodo principal AlmacenDna(dna,result), que almacena en base de datos Dynamodb de AWS, para ello fuen necesario configurarlo y crear una tabla llamada 'RegistrosDna', donde tiene dos llaves cuya
	llave de partición es la descripción (Cadena) que es igual a 'descripción' y la llave de ordenación es el ADN (Cadena) que es igual al 'adn', en la descripción se almacena si es mutante(HUMANO_MUTANTE)o si 
	no lo ES (HUMANO_NO_MUTANTE).
	Si el ADN ya se encuentra registrado, solo actualiza el registro, no se crean dos registros con el mismo ADN. 
	
	
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
	de datos Dynamodb de AWS cuya tabla es 'RegistrosDna', los ADN y el calculo del ratio. éste metodo regresa el siguiente cuerpo:
	{
		'statusCode':200
		'count_mutant_dna':Cantidad de mutantes,
		'count_human_dna':Cantidad de registros almacenados
		'ratio':el ratio de mutantes VS humanos registrados
	}
	o, si existe fallo en base de datos:
	{
		'statusCode': XXX ->Error que regresa el consumo a la base de datos
		'descripción': 'Falla en la lectura de Base de datos',
	}

2.2 EstadoDNA.py
	Contiene metodo principal de realizar consulta de base de datos y regresar el ratio -> ratio_mutante(), esta realiza la busqueda en base de datos de Dynamodb en AWS, cuya tabla es RegistrosDna, realiza
	primero la busqueda de registros cuya descripcion (llave de partición)='HUMANO_MUTANTE' ->busquedaMutantes(descripcion), De ella valida si fue correcta la lectura, y cuantos mutantes existen,
	luego realiza el mismo proceso para conocer el resultade cuantos Humanos no mutante son (llave de partición)='HUMANO_NO_MUTANTE', de ello genera el calculo del ratio y regresa la siguiente estructura:
	{
		'statusCode':200
		'count_mutant_dna':Cantidad de mutantes,
		'count_human_dna':Cantidad de registros almacenados
		'ratio':el ratio de mutantes VS humanos registrados
	}
	o, si existe fallo en base de datos:
	{
		'statusCode': XXX ->Error que regresa el consumo a la base de datos
		'descripción': 'Falla en la lectura de Base de datos',
	}
	


3. ******Cómo ejecutar el programa**********************

3.1. Arquitectura:

El aplicativo fue creado en lenguaje python, y sus funciones fueron subidas a AWS, donde se definió como arquitectura un Apigateway llamado Registro_Mutante donde se crearon dos metodos(/Mutant POST, y /Mutant/stats GET), 
estos metodos se asociaron a dos lambda cada una asociada a cada metodo, con el objetivo que puedan trabajar de manera independiente: lambda 1:'Es_Mutante' asociada al metodo /Mutante POS que valida el DNA y lo almacena,
Lambda 2:'EstadoMutante' asociada al metodo /Mutant/stats que valida el ratio de mutantes VS ADN almacenados.  Adicional se conectó una base de datos Dynamodb para almacenar los registros y consultarlos, ambas lambda 
tienen un perfil de rol que le permite acceder a la base de datos de manera full (esto para el ejercicio)., esta base de datos solo tiene una tabla llamada 'RegistrosDna' donde tiene dos llaves cuya	llave de partición 
es la descripción (Cadena) que es igual al estado si es mutante o no, u la otra llave de ordenación es el ADN (Cadena).
las URL generada para los metodos y consumo de API rest son:

/Mutant POST Invocar URL: https://ygl6wmaey3.execute-api.us-east-2.amazonaws.com/Test/mutant

body ejemplo (tener presente las condiciones relacionadas al comienzo del documento): 
	{	
        "dna":["AAAAAA","AAAAA","AAAAA","AAAAA","AAAAC"]
    }
response
{
			'statusCode': 'respuesta HTTPS',  -> esta puede ser 400-si existe un error de estructura o 200 si la estructura es correcta o el estado que regrese el almacenado de la base de datos. 
			'descripción': 'descripcón del estado´' ->en caso de ser 400 permite 3 estados  error de longitud de registros, debe ser NxN, y error en los caracteres si son diferentes a A,C,G,T, en caso de ser 200
													se regresa si es Mutante o no es Mutante, en caso de tener fallo en el registro en Base de datos se regresa error que no se pudo almacenar.
}
/Mutant/stats GET Invocar URL: Invocar URL: https://ygl6wmaey3.execute-api.us-east-2.amazonaws.com/Test/mutant/stats

sin body
response
{
		'statusCode':200
		'count_mutant_dna':Cantidad de mutantes,
		'count_human_dna':Cantidad de registros almacenados
		'ratio':el ratio de mutantes VS humanos registrados
	}
o, si existe fallo en base de datos:
{
	'statusCode': XXX ->Error que regresa el consumo a la base de datos
	'descripción': 'Falla en la lectura de Base de datos',
}

3.2. Actualización de funcionalidad de lambda Es_Mutante

	De la carpeta esMutante se debe tomar solo los archivos: Lambda_function.py, EsMutante.py, metodoSecuencia.py y AlmacenaDna.py, estos deben ser asociados a la funcionalidad en Lambda, solo tener presente el acceso a 
	la base de datos, si se definió con el mismo nombre 'RegistrosDna' y las mismas llaves, no es necesario modificar el codigo, adicional es importante ver la zona donde se configura en AWS, la zona donde se encuentra la 
	base de datos es region_name="us-east-2", si esta se modifica, debe reemplzarse en las funciones que se tengan asociadas. 
	Una vez actualziado las funcionalidades y haber configurado la arquitectura mencionada, ya se podría realziar la solicitud a travez de PostMan.
	
3.2. Actualización de funcionalidad de lambda EstadoMutante

	3.2.1. De la carpeta EstadoMutante se debe tomar solo los archivos: Lambda_function.py, y EstadoDNA.py, estos deben ser asociados a la funcionalidad en Lambda, solo tener presente el acceso a 
	la base de datos, si se definió con el mismo nombre 'RegistrosDna' y las mismas llaves, no es necesario modificar el codigo, adicional es importante ver la zona donde se configura en AWS, la zona donde se encuentra la 
	base de datos es region_name="us-east-2", si esta se modifica, debe reemplzarse en las funciones que se tengan asociadas. 
	Una vez actualziado las funcionalidades y haber configurado la arquitectura mencionada, ya se podría realziar la solicitud a travez de PostMan.
	
La información de código fuente y arquitectura se encuentran en el siguiente link