archivo = open("C:\\Users\eddie\OneDrive\Documentos\Archivos.txt\CasosPorComuna.csv.txt", "r")

linea1 = archivo.readline() #lee primera linea
linea1 = linea1.strip()     #quita el salto de linea de la primera linea
linea1 = linea1.split(",")  #transforma cada elemento de primera linea separado por una coma, en un elemento de la lista

lineas = archivo.readlines() #lee cada linea y las almacena en una lista, cada elemento de la lista es una linea

regiones = []           
regionescod = []        #Listas donde se almacenarán#
comunas = []             #comunas y códigos de comunas#
comunascod = []         #para posterior verificación#

#ciclo que recorre cada elemento de la lista lineas
for linea in lineas:
    linea = linea.strip("\n")            #borramos el salto de linea      
    listalinea = linea.split(",")        #encerramos la linea en una lista

    for elemento in range(len(listalinea)):     #ciclo for que recorre el largo de la listalinea que contiene todos los elementos de una linea

        if elemento == 0 and listalinea[elemento].lower() not in regiones:          #si el indice es igual a 0, o sea, si reconoce el primer elemento de la lista
            regiones.append(listalinea[elemento].lower())                           #añadir a la lista regiones
        
        if elemento == 1 and listalinea[elemento] not in regionescod:               #si el indice es igual a 1
          regionescod.append(listalinea[elemento])                                  #añadir a lista de código de regiones
        
        if elemento == 2:                                                           #si el indice es igual a 2
            comunas.append(listalinea[elemento].lower())                            #añadir a lista de comunas
        
        if elemento == 3:                                                           #si el indice es igual a 3
            comunascod.append(listalinea[elemento])                                 #añadir a lista de código de regiones
        
#print(regiones, "\n")          
#print(regionescod, "\n")   
#print(comunas, "\n")           
#print(comunascod, "\n")    

archivo.close()

#desplegar regiones

print("----------------------------Bienvenido----------------------------")

print("""------------------------------------------------------------------

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

""")

comuna = input("Ingrese la comuna que desea buscar: ")                          

while not ((comuna.lower() in comunas) or (comuna in comunascod)):              #verificar si la región está en la lista de regiones
    comuna = input("ERROR, ingrese una comuna válida: ")                        # o lista de códigos de regiones

fecha = input("Ingrese una fecha: ")                            

while not fecha in linea1:                                                      #verificar si la fecha está en la lista de fechas
    fecha = input("ERROR, ingrese una fecha válida: ")                         

contagiados = 0

for linea in lineas:
    linea = linea.strip("\n")           #borramos el salto de linea      

    listalinea = linea.split(",")       #guardamos cada elemento de la linea en una lista

    for elemento in range (len(listalinea)): #se recorre cada elemento de la linea actual

        if listalinea[elemento].lower() == comuna.lower(): #si el elemento actual es igual a la comuna ingresada por el usuario
            #print(listalinea[elemento])                    #imprimir comuna

##############################################################################################################################################################3

            for buscar in range (len(linea1)):              #ciclo for que empiece a recorrer todas los elementos(fechas) de la primera linea
                
                if linea1[buscar] == fecha:                 #si la fecha que ingreso el usuario coincide con alguna de la lista
                    
                    for contag in range (len(listalinea)):  #ciclo for que recorre nuevamente la linea en que se encuentra, ahora
                                                            #con el objetivo de buscar los contagiados
                        if contag == buscar:                    #si el indice del contagiado es igual al indice de la fecha en nuestra lista linea1
                            contagiados = listalinea[contag]    #guardamos la cantidad de contagiados en nuestra variable del mismo nombre.   
                            
if contagiados == "":   #si el número de contagiados es vacío
    contagiados = 0     #reemplazar por un 0

print("La cantidad de casos activos en la comuna de", comuna.upper(), "para la fecha", fecha, "es: ", contagiados) #verificación de datos por pantalla
