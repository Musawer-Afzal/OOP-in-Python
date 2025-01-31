# Computation class
# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method
# Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.
# Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.
# Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.
# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.


class Computation:

    def __inti__(self):
        pass

    def Factorial(self, n):
        return (1 if n == 0 else n * self.Factorial(n - 1))
    
    def naturalSum(self, n):
        sums = sum([i for i in range(1, n + 1)])
        return sums
    
    def testPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def testPrims(self, n, m):
        smaller = min(n,m)
        for i in range(2, smaller + 1):
            if n % i == 0 and m % i == 0:
                return False
        return True

    def tableMult(self, n):
        for i in range(1, 11):
            print(f"{n} * {i} == ", n * i )
        print("Single Table Multiplication End")

    def allTableMult(self):
        for i in range(1, 10):
            for j in range(1, 11):
                print(f"{i} * {j} == ", i * j)

    
    def listDiv(self, n):
        Ldiv = [i for i in range(1, n + 1) if n % i == 0]
        print(Ldiv)

    def listDicPrim(self, n):
        Ldiv = [i for i in range(1, n + 1) if n % i == 0]
        primes = []

        for i in Ldiv:
            if i < 2:
                continue
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return primes
            


newComputation = Computation()
print(newComputation.Factorial(5))
print(newComputation.naturalSum(23))
print(newComputation.testPrime(11))
print(newComputation.testPrims(14,25))
newComputation.tableMult(5)
newComputation.allTableMult()
newComputation.listDiv(30)
print(newComputation.listDicPrim(35))