import math

for angle in range(0, 346, 15):
    radians = math.radians(angle)
    sin = round(math.sin(radians), 4)
    cos = round(math.cos(radians), 4)
    print(f"{angle}={sin} {cos}")
    