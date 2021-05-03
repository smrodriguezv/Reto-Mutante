import boto3
from boto3.dynamodb.conditions import Key

#Metodo que busca la cantidad de Registros de acuerdo a la descripción
def busquedaMutantes(descripcion):
    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table('RegistrosDna')
    respuesta = table.query(
        KeyConditionExpression=Key('Descripcion').eq(descripcion)
    )
    return respuesta


#Metodo que  devuelve un Json con las estadísticas de las verificaciones de ADN: {“count_mutant_dna”:40, “count_human_dna”:100: “ratio”:0.4}

def ratio_mutante():
    
    resultado=busquedaMutantes("HUMANO_MUTANTE")
    if resultado['ResponseMetadata']['HTTPStatusCode']!=200:
        respuesta= {
                'statusCode':resultado['ResponseMetadata']['HTTPStatusCode'],
                'descripción':"Error en la lectura de Base de Datos"
        }
        return respuesta
    cant_Mutantes=resultado["Count"]
    
    resultado=busquedaMutantes("HUMANO_NO_MUTANTE")
    if resultado['ResponseMetadata']['HTTPStatusCode']!=200:
        respuesta= {
                'statusCode':resultado['ResponseMetadata']['HTTPStatusCode'],
                'descripción':"Error en la lectura de Base de Datos"
        }
        return respuesta
    cant_No_Mutantes=resultado["Count"]
    
    cantHumanos=   cant_Mutantes +  cant_No_Mutantes
    ratio=0;
    if cant_Mutantes>0:
        ratio= (cant_Mutantes/cantHumanos)*100
    respuesta= {
                'statusCode':200,
                'count_mutant_dna':cant_Mutantes,
                'count_human_dna':cantHumanos,
                'ratio':ratio
    }
    return respuesta