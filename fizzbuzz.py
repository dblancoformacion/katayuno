# driver / piloto
FIZZ = 'Fizz'
BUZZ = 'Buzz'
NUMERO_FIZZ = 3
NUMERO_BUZZ = 5

class Kata:
	def esDivisible(numero,divisor):
		#if
		return True
	def contiene():
		return True
	def esFizz():
		return True
	def esBuzz():
		return True
	def esFizzBuzz():
		return True
	def fizzbuzz(numero):
		resultado = ''
		if numero%NUMERO_FIZZ==0:
			resultado+=FIZZ
		if numero%NUMERO_BUZZ==0:
			resultado+=BUZZ
		if resultado=='':
			resultado=numero
		#str(numero).find(3)
		return resultado

# moq

if __name__ == "__main__":



	for i in range(100):
		print(i+1,Kata.fizzbuzz(i+1))
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


