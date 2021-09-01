datos_file=open("Calificaciones.txt","r")
datos=[]

while True:
    datos_read=datos_file.readline()
    if len(datos_read)==0:
      break
    datos_convertido=datos_read.replace(" ","")
    datos_convertido=datos_read.replace("\n","")
    datos_div=datos_convertido.split(",")
    datos.append(datos_div)


def promedio(datos):
  suma=0
  for i in range(len(datos)):
    venta=float(datos[i][1])
    suma+=venta
  return suma/(len(datos))


def mejor_promedio(datos):
  lista=[]
  for i in range(len(datos)):
    lista.append(float(datos[i][1]))
  for i in range(len(datos)):
    if (int(datos[i][1]))==(max(lista)):
      maxi=(datos[i])
      return maxi


def reprobados(datos):
  lista=[]
  reprobados=[]
  for i in range(len(datos)):
    lista.append(float(datos[i][1]))
  for i in range(len(datos)):
    if (int(datos[i][1]))<70:
      reprobados.append(datos[i])
  return reprobados


opcion=int(input())

if opcion==1:
  print(round(promedio(datos),2))
elif opcion==2:
  print(mejor_promedio(datos)[0]+mejor_promedio(datos)[1])
elif opcion==3:
  print(reprobados(datos)[0][0]+reprobados(datos)[0][1]+"\n"+reprobados(datos)[1][0]+" "+reprobados(datos)[1][1]+"\n"+reprobados(datos)[2][0]+reprobados(datos)[2][1]+"\n"+reprobados(datos)[3][0]+reprobados(datos)[3][1])