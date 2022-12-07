import random
import matplotlib.pyplot as plt
import numpy

amount_rows = 200


def create_random_dice_data():
    dice_numbers = [[random.randint(1, 6) for i in range(2)] for j in range(amount_rows)]
    return dice_numbers


def create_z_data(xy_data):
    i = 1
    counter = 0
    dice1 = 1
    dice2 = 1
    z_data = []
    while i <= 6:
        for j in range(1, 7):
            z_data.append(0)
            for item in xy_data:
                if item[0] == dice1 and item[1] == dice2:
                    z_data[counter] += 1
            counter += 1
            dice2 += 1

        dice1 += 1
        dice2 = 1
        i += 1

    return z_data


fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

matrix = create_random_dice_data()
x = [i for i in range(1, 7) for _ in range(6)]
y = [i for _ in range(6) for i in range(1, 7)]
z = [0 for i in range(36)]  # z coordinates of each bar
dx = [0.3 for i in range(36)]  # Width of each bar
dy = dx  # Depth of each bar
dz = create_z_data(matrix)       # Height of each bar


ax.bar3d(x, y, z, dx, dy, dz, shade=True)
ax.set_title('Shaded')

fig.show()

print("average: ", numpy.average(dz))
print("max: ", numpy.max(dz))
print("min: ", numpy.min(dz))
