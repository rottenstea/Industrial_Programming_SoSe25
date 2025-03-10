import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u

import seaborn as sns

sns.set_style("darkgrid")

a = np.arange(10)

b = np.random.randint(1,90, size = len(a)) * u.deg

sns.scatterplot(x = a,y = b)

plt.show()