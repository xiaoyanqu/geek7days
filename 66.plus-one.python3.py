class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        total = 1
        i = len(digits) - 1
        
        while i >= 0:
            total += digits[i] + carry
            carry, total = total // 10, total % 10
            digits[i] = total
            if not carry:
                break
            i -= 1
        
        if carry:
            return [1] + digits
        else:
            return digits
