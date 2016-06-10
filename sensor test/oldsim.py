import sys, os
import random
import math

#files of output
acc_file = open("acc.txt","w")
sensor_noise_file = open("noise.txt", "w")
range_file = open("range.txt", "w")
sensor_file = open("sensor.txt", "w")
#alpha: constant that defines how quickly we reach our max acceleration
alpha = 1.0/100.0
#c: max acceleration
c = 2.0
#env noise not totally sure bout this
env_snr = 100.0
inv_env_snr = 1.0/env_snr
env_noise_range = c * inv_env_snr
#b: constant that determines how to scale the noise from the change in movement
b = 100.0
#test range in seconds
seconds_range = 30
milliseconds_range = seconds_range * 1000




for x in range(0, milliseconds_range):
        exponent = (alpha*x - (c * c)) * -1
        denom = 1.0 + math.exp(exponent)
        acc_profile = c / denom
        acc_file.write(str(acc_profile) + "\n")

        exponent = (c*c) - alpha * x
        numer = c * alpha * math.exp(exponent)
        denom = math.exp(exponent) + 1
        denom = denom * denom
        dx_acc_profile = numer/denom

        noise_from_acc = b * dx_acc_profile
        noise_from_acc = noise_from_acc / 2
        noise_from_acc = random.uniform(-noise_from_acc, noise_from_acc)
        sensor_noise_file.write(str(noise_from_acc) + "\n")
        
        noise_env = env_noise_range / 2
        noise_env = random.uniform(-noise_env, noise_env)

        total_noise = noise_from_acc + noise_env
        simulated_sensor_data = total_noise + acc_profile
        sensor_file.write(str(simulated_sensor_data) + "\n")
        range_file.write(str(x) + "\n")

print("All done")
