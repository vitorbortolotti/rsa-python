# Início do script

def calc_mdc(x, y): 
   while(y): 
       x, y = y, x % y 
  
   return x 


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Define os dois números primos p e q
p = 7723212143
print("p: {}".format(p))
q = 3078472921
print("q: {}".format(q))

# Executa a multiplicação e calcula o valor do número rsa n
n = p * q
print("n: {}".format(n))

# Calcula o valor de phi
phi = (p-1)*(q-1)
print("phi(n): {}".format(phi))

# Chave de encriptação e
e = 53
print("e: {} (Chave de encriptação)".format(e))

# Verificando que phi e e são primos entre si
mdc = calc_mdc(phi, e)
print("mdc(phi, e): {}".format(mdc))

# Chave de desencriptação
d = modinv(e, phi)
print("d: {} (Chave de desencriptação)".format(d))

# Mensagem original (cartão de credito)
m = 411111111111111
print("Mensagem original: {}".format(m))

# Mensagem encriptada
a = pow(m, e, n)
print("Mensagem encriptada: {}".format(a))

# Mensagem desencripitada
r = pow(a, d, n)
print("Mensagem desencripitada: {}".format(r))