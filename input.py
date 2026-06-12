print ("\nSimulando a LatinChat")
print ("=====================")

print ("\nSala de Chat > De 30 a 40 años")
print ("------------------------------\n")

print ('Ana: ¿Cómo se llama usted?: ' )
nombre = input('Yo: ')
print ('Ana: Hola', nombre, ', encantada de conocerte :3')

print ('Ana: ¿Qué edad tiene usted?: ')
edad = input('Yo: ')
print ('Usted tiene', edad, ', y yo ya no digo mi edad xD')

print ('Ana: ¿Tiene WebCam?, ingrese "si" o "no", por favor!: ')
tiene_WebCam = input('Yo: ')

if tiene_WebCam in ('s', 'S', 'si', 'Si', 'SI'):
	print ("Ponga la WebCam para verla :-D")
elif tiene_WebCam in ('n', 'no', 'No', 'NO'):
	print ("Lastima por usted :'( Adiós")
