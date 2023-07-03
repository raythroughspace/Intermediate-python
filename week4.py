class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        elif denom <0: #only numerator can be negative
            num = -num
            denom = -denom
            
        gcd = 1
        for div in range(1, max(abs(num), denom) + 1):
            if (num % div ==0 and denom % div==0):
                gcd = div
        self.num = num//gcd
        self.denom = denom//gcd
    
    def __str__(self):
        """str(Fraction) -> str
        returns the string representation of Fraction"""
        return f"{self.num}/{self.denom}"
    
    def __float__(self):
        """float(Fraction) -> float
        returns the float representation equal to Fraction"""
        return self.num/self.denom
    
    def __add__(self, other):
        """self + other -> Fraction
        returns a Fraction that is the sum of self and other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        return Fraction(a*d + b*c, b*d)
    
    def __sub__(self, other):
        """self + other -> Fraction
        returns a Fraction that is the subtraction of self and other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        return Fraction(a*d - b*c, b*d)
    
    def __mul__(self, other):
        """self * other -> Fraction
        returns a Fraction that is the multiplication of self and other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        return Fraction(a*c, b*d)
    
    def __truediv__(self, other):
        """self / other -> Fraction
        returns a Fraction that is the division of self with other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        return Fraction(a*d, b*c)
    
    def __eq__(self, other):
        """self == other -> bool
        returns True if self equals other as fractions, False otherwise"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        return a==c and b==d


# examples
p = Fraction(1,17)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False