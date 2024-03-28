import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,30])
y = np.array([40,50,60])

plt.plot(x,y)
plt.show()

#Markers
x1 = np.array([10,20])
y1 = np.array([40,45])

plt.plot(x1,y1,'o')
plt.show()