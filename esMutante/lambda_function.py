import json
import EsMutante
import AlmacenaDna


#Metodo que recibe el consumo del API, hace llamado de validación de ser Humano y si es mutante o no, adicional almacena los registros de DNA con la descripción si es Mutante o no. 
#regresa 4 tipos de respuesta, 1. Fallo de estructura, 2. Si es Mutante 3.Si no es mutante y 4 Que exista algun inconveniente en el momento de almacenar el DNA.

def lambda_handler(event, context):
   
    dna=event['dna'] 
    result=EsMutante.isMutant(dna)
    if result['statusCode']==200:
        respons = AlmacenaDna.AlmacenDna(dna,result)
        if respons['ResponseMetadata']['HTTPStatusCode']!=200:
            return {
                'statusCode': respons['ResponseMetadata']['HTTPStatusCode'],
                'descripción': result['descripcion']
                'descripción1': "No se almacenó la información"
            }   
    return result
    
