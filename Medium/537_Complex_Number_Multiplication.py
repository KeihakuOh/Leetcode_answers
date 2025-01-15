class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = self.parse_complex(num1)
        real2, imaginary2 = self.parse_complex(num2)
        real = real1 * real2 - imaginary1 * imaginary2
        imaginary = real1 * imaginary2 + imaginary1 * real2
        return f"{real}+{imaginary}i"
    
    def parse_complex(self, num: str):
        real, imaginary = num.split('+')
        return int(real), int(imaginary[:-1])