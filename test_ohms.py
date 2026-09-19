from ohms_law import calc_resistance
result = calc_resistance(10, 8) 
 
print("Resistance =", result, "ohms")
assert calc_resistance(9, 0.03) == 300 
assert calc_resistance(24, 2) == 12

print(calc_resistance.__doc__)

