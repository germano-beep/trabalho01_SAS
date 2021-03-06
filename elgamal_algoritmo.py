# biblibote para gerar número aleatórios
import random
from math import pow
import time

a = random.randint(2, 10)

# Gerando grandes números aleatórios 
def gcd(a, b):
	if a < b:
		return gcd(b, a)
	elif a % b == 0:
		return b;
	else:
		return gcd(b, a % b)

#Gerando chave
def gen_key(q):

	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

# Exponenciação modular
def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c

# Criptografia assimétrica
def encrypt(msg, q, h, g):

	en_msg = []

	k = gen_key(q)# chave privada que será enviada
	s = power(h, k, q)
	p = power(g, k, q)
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])

	print("g^k usada : ", p)
	print("g^ak usada : ", s)
	print("\n")
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

def decrypt(en_msg, p, key, q):

	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
		
	return dr_msg

def main():
    msg = input("\nEscreva uma mensagem a ser criptografada: ")
    print(F"Mensagem original: {msg}\n")

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)# Recebendo a chave privada
    h = power(g, key, q)
    print("g usada : ", g)
    print("g^a usada : ", h)

    inicio = time.time()
    en_msg, p = encrypt(msg, q, h, g)
    fim = time.time()

    print("Mensagem Criptografada:", en_msg)
    print("Tempo para criptografar:", fim-inicio)
    print("\n")

    inicio = None
    fim = None

    inicio = time.time()
    dr_msg = decrypt(en_msg, p, key, q)
    fim = time.time()

    dmsg = ''.join(dr_msg)
    print("Menssagem descriptografada :", dmsg)
    print("Tempo para descriptografar:", fim-inicio)

if __name__ == '__main__':
    main()