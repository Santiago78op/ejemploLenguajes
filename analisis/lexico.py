class Analisisis_Lexico():
    
    
    #DIC['PARTIDOS'] = { PALABRA: TABLA, CADENA: "REAL MADRID", JORNADA:300}
    def entrada(self,msg):
        cadena = ''
        if msg == 'PARTIDOS':
            cadena = 'Goooool'
            return cadena
        elif msg == 'TABLA':
            gol = 1
            cadena = f'el resultado del partido es {gol}'
            cadena = 'Viva el futball'
            return cadena
            #cadena = ''
            #if JORNADA in csv:
            #else:
                #cadena = 'No encontre el dato en el csv revisa el archivo.
                #return cadena