# Exercitiu 5 a

def exp_prim(n, p):         # man gibt die Funktion exp_prim zwei Parameter n und p
    exp = 0                 # exp bekommt als Wert 0

    while n % p == 0:       # wir uberprufen ob n durch p ohne rest teilbar ist
        exp += 1            # dass bedeutet dass p ein Primfaktor von n ist
        n //= p             # nachher wird der exp erhoht und n durch p geteilt

    return exp              # wir returnieren die exp, dieses Reihe wird uns zeigen wie oft p in der Primfaktorzerlegung der n ist

# Beispiel
n = 40
p = 2
exp = exp_prim(n, p)
print(f"Der Exponent von {p} in der Primfaktorzerlegung von {n} ist: {exp}")


# 5 b


def main():
    exp_prim(n, p)