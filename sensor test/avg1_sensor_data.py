import sys, os

sensor_file = open("sensor.txt", "r")
avg_file = open("avg1.txt", "w")
avg_list = []
avg_size = 100

for x in range(0,avg_size):
        avg_list.append(0.0)
x = 0
for line in sensor_file:
        avg = 0.0
        avg_list[x % avg_size] = float(line)
        if x >= (avg_size - 1):
            for c in range(0, avg_size):
                avg += avg_list[c]
            avg = avg / avg_size
        else:
            for c in range(0, (x + 1)):
                avg += avg_list[x]
            avg = avg / (x + 1)
        x += 1
        avg_file.write(str(avg) + "\n")

print("All done")


