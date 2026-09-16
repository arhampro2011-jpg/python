blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

import matplotlib.pyplot as plt 
import numpy as np 

x=[blood_sugar_men,blood_sugar_women]
color=['g','r']
bins=[80,100,125,150]

plt.hist(x,color=color, bins=bins, orientation='horizontal')
plt.show()