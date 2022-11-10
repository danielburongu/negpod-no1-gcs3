#!/usr/bin/python3
class py_solution:
    def roman_to_integer(self, s):
        rom_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        int_value = 0
        for i in range(len(s)):
            if i > 0 and rom_value[s[i]] > rom_value[s[i - 1]]:
                int_value += rom_value[s[i]] - 2 * rom_value[s[i - 1]]
            else:
                int_value += rom_value[s[i]]
        return int_value

print(py_solution().roman_to_integer('III'))
print(py_solution().roman_to_integer('LVIII'))
print(py_solution().roman_to_integer('MCMXCIV'))
print(py_solution().roman_to_integer('XCIX'))
print(py_solution().roman_to_integer('MDCCCL'))
