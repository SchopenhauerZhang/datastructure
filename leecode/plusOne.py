class Solution:
    def plusOne(self, digits: list()) -> list():
        digits = list(str(int(''.join([str(x) for x in digits]))+1))

        return [int(x) for x in digits]
#print(Solution().plusOne([1,2,3]))

    def _plusOne(self, digits: list()) -> list():
        for i in range(len(digits)-1,-1,-1):
            k = digits[i]
            k+=1
            l = k%10
            digits[i] = l
            c = k//10
            if c == 0:
                return digits
        if digits[0] == 0:
            return [1]+digits