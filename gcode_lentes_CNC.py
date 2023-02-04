import math
import numpy as np
import matplotlib.pyplot as plt
#Variables a introducir
r = 52.5 #Radius
#H = 4 #Height of lens
#DOC = 0.05 #Depth of cut
feedrate = 105 #speed of the machine
safezone = 22 #safe zone in X axis for the tool to rest
angle =19.46

x_array = np.array([])
y_array = np.array([])


with open('lenteV2.txt', 'w') as f:
    #Tells the machine to go to safezone at feedrate speeds
    f.write("G1 F" + str(feedrate) + " X" + str(safezone) + '\n')
    print("X    Y")
    for i in np.arange(0, np.pi/2, 0.1):
        x = r * math.sin(i)
        y = r * math.cos(i)
        #f.write("G0 " + "X" + str(safezone) + '\n') #go to safe zone again, come back to safe zone
        #f.write("G1 " + "Y-" + str(round(y,2)) + '\n') #go deeper onto the material
        #f.write("G1 " + "X" + str(round(x,2)) + '\n') #go brrr into the material
        x_array = np.append(x_array, [round(x, 2)])
        y_array = np.append(y_array, [round(y, 2)])
        #print("X: " + str(x) + "     " + "Y: " + str(y) )
        plt.plot(x_array, y_array)

#print("X    Y")
#for i in x_array:
#    print(i, end = ' ')
#for w in y_array:
#    print(w)


print("Numero de pasos: " +str(len(x_array)))
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#with open('lenteV2.txt', 'w') as f:
#    f.write("aguante boca")
