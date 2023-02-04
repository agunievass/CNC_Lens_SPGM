import math
import numpy as np
#Variables a introducir
#Es MUY importante que los valores esten bien calculados; revisar el RADIO y H y L, deben coincidir como en el solidworks
#Si los resultados no te dan coherentes al ejecutar el programa, revisar estos parametros iniciales.
r = 39 #Radius of curvature of the lens
H = 3 #Height of the lens (thickness if you want)
L = 15 #Lenght of triangle formed (wideness of the lens)
DOF = 0.1 #Depth Of Cut
Z = 25 #Safe zone in X for the tool to stand by
feedrate = 120

with open('lenteV1.txt', 'w') as f: #Open the file in order to write the GCODE to it
    f.write("G1 "+ "F"+ str(feedrate) +" "+ "X" + str(Z)) #go to safe position
    f.write('\n')
    for i in range(int(H/DOF)):
        pasada = round(i*DOF, 1) #Profundidad de pasada
        longitud_pasada = np.sqrt(r**2-(r-(H-pasada))**2) #longitud de la pasada
        print("Distancia:", round(abs(L-longitud_pasada), 2), "   ", round(pasada, 2)) #imprimo el valor; solo para demostracion
        f.write("G1 "+ "Y-" + str(round(pasada,2))) #Go on Y direction (depth of pass)
        f.write('\n')
        f.write("G1 " + "X" + str(round(abs(L-longitud_pasada), 2))) #Go on X direction (shape of lens)
        f.write('\n')
        f.write("G0 X"+ str(Z))
        f.write('\n')
print("Number of operations: "+ str(round(H/DOF)))

#with open('lenteV1.txt', 'w') as f:
#    f.write("aguante boca")
