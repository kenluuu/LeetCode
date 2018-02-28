class Solution(object):
    def plusOne(self, digits):

        # brute force Solution
        if len(digits) == 0: return [1]
        last = len(digits)-1
        done = False
        while not done:
            if last == -1:
                digits.insert(0, 1)
                done = True
            elif digits[last] == 9:
                digits[last] = 0
                last -= 1
            else:
                digits[last] += 1
                done = True
        return digits

        #Turn digits to a integer and add 1
        str_digits = ""
        for digit in digits:
            str_digits += str(digit)
        int_digits = int(str_digits)
        int_digits += 1
        str_digits = str(int_digits)
        return [int(digit) for digit in str_digits]
