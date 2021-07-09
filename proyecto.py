#buscar regiones, regiones cod, comunas, comunas cod.

archivo = open("C:\\Users\eddie\OneDrive\Documentos\Archivos.txt\CasosActivosPorComuna.csv", "r")

lineas = archivo.readlines() #lee cada linea y las almacena en una lista, cada elemento de la lista es una linea
#print(lineas)
regiones = []
regionescod = []
comunas = []
comunascod = []

#ciclo que recorre cada elemento de la lista lineas
for linea in lineas:
    linea = linea.strip()                #borramos el salto de linea      
    #print(linea)                        #imprimimos la linea
    listalinea = linea.split(",")        #encerramos la linea en una lista
    #print(listalinea)                   #imprimimos la lista que corresponde a toda una linea con sus elementos separados

    for elemento in range(len(listalinea)):     #ciclo for que recorre el largo de la listalinea que contiene todos los elementos de una linea

        if elemento == 0 and listalinea[elemento].lower() not in regiones:          #si el indice es igual a 0, o sea, si reconoce el primer elemento de la lista
            regiones.append(listalinea[elemento].lower())                           #añadir a la lista regiones
        
        if elemento == 1 and listalinea[elemento] not in regionescod:       #si el indice es igual a 1
          regionescod.append(listalinea[elemento])                          #añadir a lista de código de regiones
        
        if elemento == 2:                                                   #si el indice es igual a 2
            comunas.append(listalinea[elemento].lower())                            #añadir a lista de comunas
        
        if elemento == 3:                                                   #si el indice es igual a 3
            comunascod.append(listalinea[elemento])                         #añadir a lista de código de regiones
        
print(regiones, "\n")
print(regionescod, "\n")
print(comunas, "\n")
print(comunascod, "\n")

archivo.close()

#desplegar regiones

print("----------------------------Bienvenido----------------------------")

region = input("""------------------------------------------------------------------

15. Región de Arica y Parinacota
01. Región de Tarapacá
02. Región de Antofagasta
03. Región de Atacama
04. Región de Coquimbo
05. Región de Valparaíso
13. Región de Metropolitana
06. Región del Libertador general Bernardo O'Higgins
07. Región de Maule
16. Región de Ñuble
08. Región de BioBio
09. Región de La Araucanía
14. Región de Los Rios
10. Región de Los Lagos
11. Región de Aysen
12. Región de Magallanes y la Antartica

------------------------------------------------------------------

Ingrese por nombre o por código la región que desea buscar: 
""")

while not ((region.lower() in regiones) or (region in regionescod)):            #verificar si la región está en la lista de regiones
    region = input("ERROR, ingrese región nuevamente: ")                        # o lista de códigos de regiones

print("")

comuna = input("Ingrese la comuna que desea buscar: ")                          

while not ((comuna.lower() in comunas) or (comuna in comunascod)):              #verificar si la región está en la lista de regiones
    comuna = input("ERROR, ingrese comuna nuevamene: ")                         # o lista de códigos de regiones

#comentarios hola a todos ajdhakjdhakdahd

'''
archivo = open("C:\\Users\eddie\OneDrive\Documentos\Archivos.txt\CasosPorComuna.csv", "r")

linea1 = archivo.readline() #lee primera linea
linea1 = linea1.strip()     #quita el salto de linea de la primera linea
linea1 = linea1.split(",")  #transforma cada elemento de primera linea separado por una coma, en un elemento de la lista


lineas = archivo.readlines() #lee cada linea y las almacena en una lista, cada elemento de la lista es una linea
#print(lineas)

comuna = input("ingrese la comuna que desea buscar: ")
fecha = input("ingrese una fecha: ")
contagiados = 0
print(linea1)

#ciclo que recorre cada elemento de la lista lineas
for linea in lineas:
    linea = linea.strip("\n")           #borramos el salto de linea      
                                        #imprimimos la linea

    listalinea = linea.split(",")       #guardamos cada elemento de la linea en una lista
    print(listalinea)                   #imprimimos la lista que corresponde a toda una linea con sus elementos separados

    for elemento in range (len(listalinea)): #se recorre cada elemento de la linea actual

        if listalinea[elemento].lower() == comuna.lower(): #si el elemento actual es igual a la comuna ingresada por el usuario
            print(listalinea[elemento])                    #imprimir comuna

##################################################

            for buscar in range (len(linea1)):              #ciclo for que empiece a recorrer todas los elementos(fechas) de la primera linea
                
                if linea1[buscar] == fecha:                 #si la fecha que ingreso el usuario coincide con alguna de la lista
                    
                    for contag in range (len(listalinea)):
                        
                        if contag == buscar:
                            #print("")
                            #print(listalinea[contag])
                            #print("")

                            contagiados = listalinea[contag]
                            
if contagiados == "":
    contagiados = 0

print("La cantidad de contagiados en la comuna de", comuna, "para la fecha", fecha, "es: ", contagiados)
'''
