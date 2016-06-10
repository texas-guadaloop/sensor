import sys, os
import random
import math

#files of output
acc_file = open("acc.txt","w")
vel_file = open("vel.txt", "w")
pos_file = open("pos.txt", "w")
#sensor_noise_file = open("noise.txt", "w")
range_file = open("range.txt", "w")
#sensor_file = open("sensor.txt", "w")
# max acceleration
Amax_g = 2.0
Amax_std = Amax_g * 9.80665
#test range in seconds
seconds_range = 30
milliseconds_range = seconds_range * 1000
#acceleration phase
acc_seconds_range = 5
acc_milli_range = acc_seconds_range * 1000
acc_milli_begin = 0
acc_milli_end = acc_milli_begin + acc_milli_range
acc_tau_seconds = .5
acc_tau_milli = acc_tau_seconds * 1000
#coasting phase
coasting_seconds_range = 20
coasting_milli_range = coasting_seconds_range * 1000
coasting_milli_begin = acc_milli_end 
coasting_milli_end = coasting_milli_begin + coasting_milli_range
coasting_tau_seconds = 0.01
coasting_tau_milli = coasting_tau_seconds * 1000
#deceleration phase
dcc_seconds_range = 5
dcc_milli_range = dcc_seconds_range * 1000
dcc_milli_begin = coasting_milli_end
dcc_milli_end = dcc_milli_begin + dcc_milli_range
dcc_tau_seconds = .5
dcc_tau_milli = dcc_tau_seconds * 1000

x0 = 0
v0 = 0
#acc phase
for t in range(acc_milli_begin, acc_milli_end):
    exponent = math.exp(-t/acc_tau_milli)
    acc = 1 - exponent
    acc = acc * Amax_std
    t_s = t * 1.0 * 0.001
    pos = Amax_std * ((t_s*t_s * 0.5) + (-1.0*acc_tau_seconds*acc_tau_seconds*exponent) + (-1.0*acc_tau_seconds*t_s) + (acc_tau_seconds * acc_tau_seconds))
    vel = Amax_std * (t_s + acc_tau_seconds*exponent - acc_tau_seconds)
    range_file.write(str(t) + "\n")
    acc_file.write(str(acc) + "\n")
    vel_file.write(str(vel) + "\n")
    pos_file.write(str(pos) + "\n")
x0 = pos
v0 = vel

#coasting phase
for t in range(coasting_milli_begin, coasting_milli_end):
    t0 = t - coasting_milli_begin
    t_s = t0 * 1.0 * 0.001
    exponent = math.exp(-t0/coasting_tau_milli)
    pos = Amax_std * ((coasting_tau_seconds*coasting_tau_seconds*exponent) + (coasting_tau_seconds*t_s) + (1.0 * coasting_tau_seconds * coasting_tau_seconds)) + (t_s * v0) + x0
    vel = Amax_std * (-1.0 * coasting_tau_seconds*exponent + coasting_tau_seconds) + v0
    acc = exponent * Amax_std
    range_file.write(str(t) + "\n")
    acc_file.write(str(acc) + "\n")
    vel_file.write(str(vel) + "\n")
    pos_file.write(str(pos) + "\n")
x0 = pos
v0 = vel

#dcc phase
for t in range(dcc_milli_begin, dcc_milli_end):
    t0 = t - dcc_milli_begin
    t_s = t0 * 1.0 * 0.001
    exponent = math.exp(-t0/dcc_tau_milli)
    acc = 1 - exponent
    acc = acc * Amax_std * -1
    pos = -Amax_std * ((t_s*t_s * 0.5) + (-1.0*dcc_tau_seconds*dcc_tau_seconds*exponent) + (-1.0*dcc_tau_seconds*t_s) + (dcc_tau_seconds * dcc_tau_seconds)) + (v0 * t_s) + x0
    vel = -Amax_std * (t_s + dcc_tau_seconds*exponent - dcc_tau_seconds) + v0
    range_file.write(str(t) + "\n")
    acc_file.write(str(acc) + "\n")
    vel_file.write(str(vel) + "\n")
    pos_file.write(str(pos) + "\n")

print("All done")
