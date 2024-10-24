matricula = ["2422976", "2422970", "2422983", "2422977", "2422993"]
lastNumbersForMatricula = list(map(lambda item: int(item[-1]), matricula)) # separa o numero final das matriculas

#Calcula o N a partir das matriculas
def calcN(list):
    acc = 0
    for i in range(len(lastNumbersForMatricula)):
      acc += list[i]
    return (acc+10)/10

#
def derivada_numerica(f, x, h = 0.0001):
  return (f(x + h) - f(x - h)) / (2 * h)

# 
def newton_raphson(n_velo,fun, val0, tol = 1e-8, maxIter = 100):
    for _ in range(maxIter):
      f = lambda t: fun(t) - n_velo
      valueF = f(val0) 
      valueFDerivada = derivada_numerica(f, val0)

      val = val0 - (valueF/valueFDerivada)

      if(abs(val - val0) <= tol):
        return val
      
      val0 = val  


# funcao da velocidade
V = lambda x: -0.0000005181382 * x ** 8 + 0.0000615620817 * x ** 7 - 0.0030378878339 * x ** 6 + 0.0806132093984 * x ** 5 - 1.2432080780626 * x ** 4 + 11.213134252073 * x ** 3 - 56.1414827095908 * x ** 2 + 134.6598926750734 * x - 98.1605150163588

# velocidade N 
N = calcN(lastNumbersForMatricula)


# for i in range(0, 29): 
print(newton_raphson(N, V, 1))