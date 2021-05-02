import boto3
from boto3.dynamodb.conditions import Key

import utilsejes
'''
Metodo que almacena registro de Humano (DNA) en base de datos Dynomodb, cuya llave de partición es la descripción (Cadena) y la llave de ordenación es el ADN (Cadena), en la descripción se almacena si es mutante(HUMANO_MUTANTE)
o si no lo ES (HUMANO_NO_MUTANTE); y en el ADN se almacena el ADN del Humano. 
'''

def AlmacenDna(dna,result):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    tabla = dynamodb.Table('RegistrosDna')
    
    #Se toma en un solo registro el ADN, se toma como base el horizontal. 
    dnaRegistro=utilsejes.ejeHorizontal(dna)
    respuesta = tabla.put_item(
       Item={
            'Descripcion':result['descripcion'],
            'ADN': dnaRegistro
            }
    )
    return respuesta


