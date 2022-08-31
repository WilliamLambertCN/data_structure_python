def gcd(m,n):
    if m<n:
        m,n=n,m
    
    while m%n!=0:
        rest = m%n
        m = n
        n= rest

    return n
        

class Fraction:
# the methods go here
    
    def __init__(self, numerator, denominator):
        self.num=numerator
        self.den=denominator

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        temp = gcd(newden,newnum)
        newnum = newnum//temp
        newden = newden//temp
        return Fraction(newnum,newden)
    
    def __sub__(self):
        pass

    def __eq__(self,other):
        return self.num*other.den==self.den*other.num

    def __eq__(self,other):
        return self.num*other.den!=self.den*other.num

    def __lt__(self,other):
        pass

    def __le__(self,other):
        pass

    def __gt__(self,other):
        pass

    def __ge__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __pow__(self,other):
        pass

    def __truediv__(self,other):
        pass

    def __floordiv__(self,other):
        pass

    def __mod__(self,other):
        pass
        
##f1 =Fraction(1,4)
##f2=Fraction(1,2)
##f3=f1+f2
##print(f3)

