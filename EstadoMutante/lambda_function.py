import json
import EstadoDNA


#Metodo que recibe el consumo del API GET, hace llamado a metodo que devuelve un Json con las estadísticas de las verificaciones de ADN: {“count_mutant_dna”:40, “count_human_dna”:100: “ratio”:0.4}

def lambda_handler(event, context):

    respuesta=EstadoDNA.ratio_mutante()
    return respuesta