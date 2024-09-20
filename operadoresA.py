print("Act.9 Clases V3")
print("Maldonado R. Valentina Mat: 22308051281253")
# Zona de class
class Operadores1253:
    # Zona de funciones 
    def suma1253(self,M,V):
        s1253 = M + V 
        print(f"La suma de {M} + {V} = {s1253}")
    def resta1253(self,A,L):
        r1253 = A - L
        print(f"La resta de {A} - {L} = {r1253}")
    def multiplicacion1253(self,D,E):
        m1253 = D * E
        print(f"La multiplicación de {D} x {E} = {m1253}")
    def division1253(self,O,N):
        d1253 = O / N
        print(f"La división de {O} ÷ {N} = {d1253}")
    def modulo1253(self,R,I):
        md1253 = R % I
        print(f"El módulo de {R} mod {I} = {md1253}")
    def exponente1253(self,Z,P):
        ex1253 = Z ** P
        print(f"El exponete de {Z} ^ {P} = {ex1253}")
    def cociente1253(self,Y,S):
        c1253 = Y // S
        print(f"El cociente de {Y} // {S} = {c1253}")


# Zona de creacion de objeto
operaVale = Operadores1253()

# Zona de uso de objeto
print("Función Suma (+)")
operaVale.suma1253(6,6)
print("Función Resta (-)")
operaVale.resta1253(100,46)
print("Función Multiplicación (x)")
operaVale.multiplicacion1253(7,5)
print("Función División (÷)")
operaVale.division1253(100,2)
print("Función Módulo (mod)")
operaVale.modulo1253(17,12)
print("Función Exponenete (^)")
operaVale.exponente1253(3,3)
print("Función Cociente (//)")
operaVale.cociente1253(10,5)