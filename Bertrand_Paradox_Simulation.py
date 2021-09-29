# Bertrand Paradox Simulation
# Congyang Xie
# CX2257

import math
import random


# Solution B
# create a class of random points within a given circle
class RandPointInCircle:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # Use polar coordinates to represent a point
        alpha = random.random() * 2 * math.pi
        r = random.random() ** 0.5 * self.radius

        x = self.x_center + r * math.cos(alpha)
        y = self.y_center + r * math.sin(alpha)

        return x, y


# declare 2 int for counting the points int the circle and the inscribed circle
points = 0
inscribedP = 0

for i in range(0, 1000000):

    # randomly generate point within circle O(0, 0), r = 2
    point = RandPointInCircle(2.0, 0.0, 0.0).randPoint()
    points += 1

    # if the the point is within circle O(0, 0), r = 1, then add it to the inscribed circle set
    if math.sqrt(point[0] ** 2 + point[1] ** 2) < 1:
        inscribedP += 1

# calculate the percentage of randomly generated points fall in the inscribed circle
pct1 = inscribedP / points
print("The probability is" + ' ' + str(pct1))


# the straight solution

# create a class of the random point on a given circle
class RandPointOnCircle:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # Use polar coordinates to represent a point
        alpha = random.random() * 2 * math.pi
        r = self.radius

        x = self.x_center + r * math.cos(alpha)
        y = self.y_center + r * math.sin(alpha)

        return x, y


chords = 0
longChords = 0

for i in range(0, 1000000):

    # randomly generate chord on circle O(0, 0), r = 2
    point1 = RandPointOnCircle(2.0, 0.0, 0.0).randPoint()
    point2 = RandPointOnCircle(2.0, 0.0, 0.0).randPoint()
    chords += 1

    # calculate the the distance between the 2 points, which is the length of the chord
    distance = math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))
    if distance > math.sqrt(3) * 2.0:
        longChords += 1

# calculate the percentage of randomly generated chords that are longer than the side length
# of the inscribed triangle
pct2 = longChords / chords
print("The probability is" + ' ' + str(pct2))
