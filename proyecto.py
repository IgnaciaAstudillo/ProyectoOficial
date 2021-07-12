archivo = open("C:\\Users\eddie\OneDrive\Documentos\Archivos.txt\CasosPorComuna.csv.txt", "r")

linea1 = archivo.readline() #lee primera linea
linea1 = linea1.strip()     #quita el salto de linea de la primera linea
linea1 = linea1.split(",")  #transforma cada elemento de primera linea separado por una coma, en un elemento de la lista

lineas = archivo.readlines() #lee cada linea y las almacena en una lista, cada elemento de la lista es una linea

regiones = []
regionescod = []
comunas = []
comunascod = []

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

print("----------------------------Regiones------------------------------")   
print(regiones, "\n")
print("-----------------------Códigos de Regiones------------------------")
print(regionescod, "\n")

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
------------------------------------------------------------------

""")

comuna = input("Ingrese la comuna que desea buscar: ")                          

while not ((comuna.lower() in comunas) or (comuna in comunascod)):              #verificar si la región está en la lista de regiones
    comuna = input("ERROR, ingrese una comuna válida: ")                        # o lista de códigos de regiones

if comuna.isnumeric():                                  #si se ingresó la comuna por código, cambiamos el código de la comuna por su nombre,
                                                        #esto es para que en el gráfica salga por nombre
    for indicecodigo in range (len(comunascod)):
        if comunascod[indicecodigo] == comuna:

            for indicecomuna in range (len(comunas)):
                if indicecodigo == indicecomuna:

                    comuna = comunas[indicecomuna]
                

fecha = input("Ingrese una fecha: ")                            

while not fecha in linea1:                                                      #verificar si la fecha está en la lista de fechas
    fecha = input("ERROR, ingrese una fecha válida: ")  


#####################################################################################################################
################################# BUSCAR CONTAGIADOS PARA UNA FECHA ESPECÍFICA ######################################
#####################################################################################################################

contagiadosdía = 0
TotalContagiadosDía = 0
GuardarRegión = ""


for linea in lineas:
    linea = linea.strip("\n")           #borramos el salto de linea      

    listalinea = linea.split(",")       #guardamos cada elemento de la linea en una lista

    for elemento in range (len(listalinea)): #se recorre cada elemento de la linea actual

        if listalinea[elemento].lower() == comuna.lower(): #si el elemento actual es igual a la comuna ingresada por el usuario
            
            GuardarComuna = listalinea[elemento]            # Almacenamos el nombre de la comuna en una variable

            for buscar in range (len(linea1)):              #ciclo for que empiece a recorrer todas los elementos(fechas) de la primera linea
                
                if linea1[buscar] == fecha:                 #si la fecha que ingreso el usuario coincide con alguna de la lista
                    
                    for contag in range (len(listalinea)):  #ciclo for que recorre nuevamente la linea en que se encuentra, ahora
                                                            #con el objetivo de buscar los contagiados
                        if contag == buscar:                    #si el indice del contagiado es igual al indice de la fecha en nuestra lista linea1
                            contagiadosdía = listalinea[contag]    #guardamos la cantidad de contagiados en nuestra variable del mismo nombre. 

            GuardarRegión = listalinea[elemento - elemento]

    for elemento in range (len(listalinea)):                #Este ciclo es para encontrar el total de contagiados de una fecha especifica de la región en 
                                                            #la que se encuentra la comuna que ingresó el usuario

        if listalinea[elemento] == GuardarRegión and listalinea[elemento + 2] == "Total":

            for buscar in range (len(linea1)):

                if linea1[buscar] == fecha:                 #si la fecha de la lista coincide con la que ingresó el usuario

                    for TotalContag in range (len(listalinea)):

                        if TotalContag == buscar:
                            TotalContagiadosDía = listalinea[TotalContag]
                            
if contagiadosdía == "":   #si el número de contagiados es vacío
    contagiadosdía = 0     #reemplazar por un 0

print("")
print("La cantidad de contagiados en la comuna de", comuna, "para la fecha", fecha, "es: ", contagiadosdía) #verificación de datos por pantalla
print("La cantidad de contagiados en la región de", GuardarRegión, "para la fecha", fecha, "es: ", TotalContagiadosDía)

##################################################################################################################
#######################    BUSCAR  MAYOR  Y  MENOR  DENSIDAD  DE  CONTAGIADOS  POR  FECHA  #######################
##################################################################################################################

fechas = []
MayorDensidad = 0           #definimos variables
MenorDensidad = 9000000     #en este caso pusimos 9 millones, debido a que la región con más habitantes en chile no supera esa cifra y de esta manera podemos cumplir la condición en la que lo utilizaremos.
RegionMayor = ""
RegionMenor = ""
densidad = 0
Población = 0
acumulados = 0
AcumuladosMayor = 0
AcumuladosMenor = 0


for dates in range (6, len(linea1)):        
    fechas.append(linea1[dates])

for linea in lineas:
    linea = linea.strip("\n")           #borramos el salto de linea      

    listalinea = linea.split(",")       #guardamos cada elemento de la linea en una lista

    for elemento in range (len(listalinea)): #se recorre cada elemento de la linea actual    
        
        if listalinea[elemento] == "Total":     #Esto es para encontrar el total de cada región
            #print(listalinea[elemento])
            acumulados = 0
            densidad = 0

            for casosact in range (6, len(listalinea)):             #ciclo for que suma todos los casos activos por día           
                #print(listalinea[casosact])
                acumulados = acumulados + float(listalinea[casosact])

            Población = float(listalinea[elemento - elemento + 4])
            densidad = acumulados / Población

            if densidad > MayorDensidad:            #si el número actual es superior al guardado en la variable densidad     
                MayorDensidad = densidad                #Almacenamos este número MAYOR
                RegionMayor = listalinea[elemento - elemento]  #Almacenamos el nombre de la región correspondiente a este total de densidad
                PoblacionMayor = float(listalinea[elemento - elemento + 4])      
                AcumuladosMayor = acumulados       

            if densidad < (MenorDensidad):       #si el número actual es inferior al guardado en la variable densidad //en la primera iteración la variable MenorDensidad vale 9000000 
                MenorDensidad = densidad              #Almacenamos este número MENOR
                RegionMenor = listalinea[elemento - elemento] 
                PoblaciónMenor = float(listalinea[elemento - elemento + 4])
                AcumuladosMenor = acumulados

print("")
print("La región de", RegionMayor, "cuanta con", PoblacionMayor, "habitantes y tiene", AcumuladosMayor, "casos activos acumulados.")
print("La región de", RegionMenor, "cuenta con", PoblaciónMenor, "habitantes y tiene", AcumuladosMenor, "casos activos acumulados.")

print("")                     
print("La mayor densidad de tasa de contagio es en la región de", RegionMayor, "y corresponde a: ", MayorDensidad)
print("La menor densidad de tasa de contagio es en la región de", RegionMenor, "y corresponde a: ", MenorDensidad)


import matplotlib.pyplot as plt

#contagiados por fecha de una comuna ingresada del usuario

contagiadosdía = float(contagiadosdía)
TotalContagiadosDía = float(TotalContagiadosDía)

x = [GuardarRegión, GuardarComuna]
y = [TotalContagiadosDía, contagiadosdía]

plt.title("region")
plt.title(fecha)
plt.bar(x, y)
plt.xlabel("Región v/s Comuna")
plt.ylabel("Casos Activos")
plt.show()

#Gráfico de Mayor densidad /// 
#Se muestra la densidad como los casos activos acumulados v/s la población no contagiada, la suma es la población total

PoblacionNoContagiada = PoblacionMayor - AcumuladosMayor

exp_vals = [PoblacionNoContagiada, AcumuladosMayor]
exp_labels = ["Población no contagiada", "Casos activos acumulados"]

plt.xlabel("MAYOR DENSIDAD DE TASA DE CONTAGIO")
plt.title(RegionMayor)
plt.pie(exp_vals, labels=exp_labels)
plt.show()

#Gráfico menor densidad

PoblacionNoContagiada2 = PoblaciónMenor - AcumuladosMenor

exp_vals2 = [PoblacionNoContagiada2, AcumuladosMenor]
exp_labels2 = ["Población no contagiada", "Casos activos acumulados"]

plt.xlabel("MENOR DENSIDAD DE TASA DE CONTAGIO")
plt.title(RegionMenor)
plt.pie(exp_vals2, labels=exp_labels2)
plt.show()

#Comparación Mayor y Menor tasa de contagio

plt.xlabel("Regiones")
plt.ylabel("Densidad de Tasa de contagio")
plt.title("Mayor y Menor densidad de tasa de contagio")

RegionesX = [RegionMayor, RegionMenor]
DensidadY = [MayorDensidad, MenorDensidad]

plt.bar(RegionesX, DensidadY)
plt.show()

