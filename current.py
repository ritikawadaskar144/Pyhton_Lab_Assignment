V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohm): "))

I = V / R

print("Current:", I, "Amperes")

if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
