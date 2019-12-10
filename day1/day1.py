# Part 1
# Puzzle input
data = [103842, 72629,  121232, 120959, 94285,  85852,  78876,  93545,  136775,
        111893, 112863, 61947,  52671,  122769, 90995,  106037, 106618, 144212,
        125766, 56163,  125865, 87828,  117596, 118778, 131537, 131498, 81583,
        111443, 139184, 101980, 114117, 76003,  99157,  93721,  106494, 66654,
        73954,  85815,  139358, 78163,  144753, 58928,  137799, 75580,  115861,
        131718, 145985, 61232,  139664, 123931, 101512, 107532, 119323, 54937,
        82412,  149218, 98531,  122318, 138890, 59125,  111176, 97205,  52214,
        84531,  115983, 69976,  125186, 142852, 66808,  81689,  62885,  126094,
        86092,  59981,  54868,  142381, 92384,  121232, 96994,  93489,  141201,
        108497, 64092,  101991, 137907, 63230,  55724,  126888, 70665,  111235,
        123493, 148071, 147590, 113936, 57270,  127204, 144599, 56041,  62105,
        124342]


def fuel_required(mass):
    return mass//3-2


def fuel_for_modules(modules):
    total = 0
    for module in modules:
        total += fuel_required(module)
    return total


print("Solution Part 1:")
print(fuel_for_modules(data))

# Part 2


def fuel_for_fuel(fuel_modules):
    fuel = fuel_required(fuel_modules)
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_for_fuel(fuel)


def total_fuel(modules):
    total = 0
    for module in modules:
        fuel_m = fuel_required(module)
        total += fuel_m + fuel_for_fuel(fuel_m)
    return total


print("Solution Part 2:")
print(total_fuel(data))
