import os
# A lista da matricula de voces
matricula = [2422976, 2422970, 2422983, 2422977, 2422993]
lastNumbersForMatricula = list(map(lambda item: item%10, matricula)) # separa o numero final das matriculas

#Calcula o N a partir das matriculas
def calcN(list):
    acc = 0
    for i in range(len(lastNumbersForMatricula)):
      acc += list[i]
    return (acc+10)/10

# Calcula a derivada pelo metodo numerico
def derivada_numerica(f, x, h = 0.0001):
  return (f(x + h) - f(x - h)) / (2 * h)

# calcula 
def newton_raphson(n_velo,fun, val0, tol = 1e-8, maxIter = 100):
    for _ in range(maxIter):
      f = lambda t: fun(t) - n_velo
      valueF = f(val0) 
      valueFDerivada = derivada_numerica(f, val0)

      val = val0 - (valueF/valueFDerivada)

      if(abs(val - val0) <= tol):
        return val
      
      val0 = val  

def handle_newton_raphson(velocity_n, fun, initial_value, max_value):
  list_num_right = set()
  list_num_left = set()
  for i in range(initial_value, max_value): 
    root = newton_raphson(velocity_n, fun, i)
    value = fun(root)
    if(value > N):
      list_num_right.add(root)
    elif(value < N):
      list_num_left.add(root)
    
  return [list_num_right, list_num_left]



# funcao da velocidade - tua funcao Velocidade
V = lambda x: -0.0000005181382 * x ** 8 + 0.0000615620817 * x ** 7 - 0.0030378878339 * x ** 6 + 0.0806132093984 * x ** 5 - 1.2432080780626 * x ** 4 + 11.213134252073 * x ** 3 - 56.1414827095908 * x ** 2 + 134.6598926750734 * x - 98.1605150163588

# velocidade N 
N = calcN(lastNumbersForMatricula)

list_right, list_left = handle_newton_raphson(N, V, 0, 30)
  
list_left_ordered = sorted(list_left)
list_right_ordered = sorted(list_right)

loop = True
while(loop):
  print(f"\nQual o instante em que o personagem atinge {N}m/s")
  print("\nEscolha uma das opcoes: ")
  print("-- 0 para raizes aproximados pela Esquerda")
  print("-- 1 para raizes aproximados pela Direita")
  print("-- 2 Sair\n")
  option = int(input())
    

  if(option == 0):
    os.system("clear")
    for i in list_left_ordered:
      print(f"{i} -> {V(i)}")
  
  if(option == 1):
    os.system("clear") 
    for i in list_right_ordered:
      print(f"{i} -> {V(i)}")

  if(option == 2):
    os.system("clear") 
    loop = False




