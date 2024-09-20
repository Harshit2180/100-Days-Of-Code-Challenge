# Question Link
# https://leetcode.com/problems/integer-to-roman/descriptio

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: 'M',
                900: 'CM',
                500: 'D',
                400: 'CD',
                100: 'C',
                90: 'XC',
                50: 'L',
                40: 'XL',
                10: 'X',
                9: 'IX',
                5: 'V',
                4: 'IV',
                1: 'I'
                }

        res = ''

        for base, symb in roman.items():
            res += symb * (num // base)
            num %= base
        else:
            return res


"""
I began by defining a dictionary to map Roman numeral values to their corresponding symbols, covering all necessary bases from 1000 down to 1. I initialized an empty string res to build the resulting Roman numeral representation. Then, I iterated through the dictionary, which contains pairs of base values and their symbols. For each base value, I calculated how many times it can fit into the given number by performing integer division. I added the appropriate number of symbols to the result string. After that, I updated the number using the modulus operator to get the remainder, allowing me to proceed to the next smaller base. Finally, once all bases had been processed, I returned the constructed Roman numeral string, which represents the original number.
"""
