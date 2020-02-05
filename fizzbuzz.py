# driver / piloto
FIZZ = 'Fizz'
BUZZ = 'Buzz'
NUMERO_FIZZ = 3
NUMERO_BUZZ = 5

class Kata:
	def esDivisible(self,numero,divisor):
		return True if numero%divisor==0 else False
	def contiene(self,pajar,aguja):
		return True if str(pajar).find(str(aguja))>0 else False
	def esFizz(self,numero):
		return self.esDivisible(numero,NUMERO_FIZZ) or self.contiene(numero,NUMERO_FIZZ)
	def esBuzz(self,numero):
		return self.esDivisible(numero,NUMERO_BUZZ) or self.contiene(numero,NUMERO_BUZZ)
	def esFizzBuzz(self,numero):
		return self.contiene(numero,NUMERO_FIZZ) and self.esDivisible(numero,NUMERO_BUZZ)
	def fizzbuzz(self,numero):
		if self.esFizzBuzz(numero):
			return FIZZ+BUZZ		
		if self.esFizz(numero):
			return FIZZ
		if self.esBuzz(numero):
			return BUZZ
		return numero

# moq

if __name__ == "__main__":



	kata=Kata()

	for i in range(100):
		print(i+1,kata.fizzbuzz(i+1))

'''
print(1,fizzbuzz(1)==1)
print(3,fizzbuzz(3)=='Fizz')
print(5,fizzbuzz(5)=='Buzz')
'''

#k = Kata;
#print(Kata.fizzbuzz(15))


# corner case (los casos raros)
# happy patch (los casos sencillos)

# especificaciones incompletas


