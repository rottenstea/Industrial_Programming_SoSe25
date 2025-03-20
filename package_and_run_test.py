import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set_style("darkgrid")


def make_scatterplot(x: np.array, y: np.array, fig_obj: plt.figure = None, ax_loc: int = 0):
    if fig_obj:

        f = fig_obj
        axes = f.get_axes()
        ax = axes[ax_loc]

    else:

        f, ax = plt.subplots(1, 1, figsize=(5, 5))

    sns.scatterplot(x=x, y=y, ax=ax, label="data")

    return f


# data
a = np.arange(100)
b = np.random.randint(1, 90, size=len(a))

# Option 1: No figure is passed to the function
# --------
fig1 = make_scatterplot(a, b)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Option 1: Function generates a scatterplot (x,y)")
fig1.show()

# Option 2: Figure object is passed beforehand
# ---------
fig2 = plt.figure(figsize=(5, 3))
plt.title("Option 2: Take a plt.figure() object and adds the scatterplot (x,y)")

# plotting some lines
plt.plot(a, 5 * np.sin(3 * a + 5), label='sin(x)', c="darkorange")
plt.axhline(y=np.mean(b), color='darkgray', linestyle='--', label='mean(y)')

# Call function while passing the figure object
fig2_scatter = make_scatterplot(x=a, y=b, fig_obj=fig2)

# add some labeling and the legend
plt.legend(loc="upper right", ncol=3)
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-5, 105)

fig2_scatter.show()
