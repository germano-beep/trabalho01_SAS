# biblibote para gerar número aleatórios
import random
import time

# função utilizada para encontrar o maximo divisor comum, utilizado para
# escolher um número entre 1 < e < φ(x)
def mdc(num1, num2):
    while(num2 != 0):
        resto = num1 % num2
        num1 = num2
        num2 = resto
    return num1


# função utilizada para criar chave pública, nela será encontrado um número 
# aletório entre um e o tociente em que o mdc dele e o tociente seja 1
def create_public_key(tociente):
    while True:
        e = random.randrange(2, tociente)
        if(mdc(tociente, e) == 1):
            return e


def create_private_key(tociente, e):
    d = 0
    while((d*e) % tociente != 1):
        d += 1
    return d


def create_encrypted_message(message, e, n):
    encrypted_message = ""
    for letter in message:
        # função ord() recebe uma letra como parâmetro e retorna o código ASCII dela
        # ** potência
        key = (ord(letter) ** e) % n
        #  chr() recebe código ASCII e é retornado a letra.
        encrypted_message += chr(key)
    return encrypted_message


def create_decrypted_message(message, n, d):
    decrypted_message = ""
    for letter in message:
        key = (ord(letter) ** d) % n
        decrypted_message += chr(key)
    return decrypted_message


def execute_rsa():
    message = input("\nEscreva uma mensagem a ser criptografada: ")
    p = int(input("Escolha um número primo: "))
    q = int(input("Escolha outro número primo: "))
    n = p * q
    tociente = (p - 1) * (q - 1)

    print("\n")

    # número co-primo com o tociente de n
    e = create_public_key(tociente)
    d = create_private_key(tociente, e)

    print(f"Chave publica: ({e}, {n})")
    print(f"Chave privada: ({d}, {n}) \n")

    inicio = time.time()
    message = create_encrypted_message(message, e, n)
    fim = time.time()
    print(f"Mensagem Criptografada: {message}")
    print(f"Tempo para criptografar: {fim-inicio}\n")
    
    inicio = None
    fim = None


    

    inicio = time.time()
    message = create_decrypted_message(message, n, d)
    fim = time.time()

    print(f"Mensagem Descriptografada: {message}")
    print(f"Tempo para descriptografar: {fim-inicio}")


execute_rsa()
