with open(r'aoc_2019_01_input.txt', 'r') as f:
    masses = [int(v) for v in f.read().strip().split('\n')]

def fuel_calc(mass):
    return ((mass//3)-2)

base_fuel = sum([fuel_calc(mass) for mass in masses])

print("Part One: ", base_fuel)

def fuel_mass_correction(mass):
    add_fuel_mass = max(fuel_calc(mass), 0)
    if add_fuel_mass == 0: return 0
    return add_fuel_mass + fuel_mass_correction(add_fuel_mass)

corrected_fuel_mass = sum([fuel_mass_correction(mass) for mass in masses])

print("Part Two: ", corrected_fuel_mass)