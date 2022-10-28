cpf = input('Informe seu CPF:')
cpf_ = list(cpf)
cpf_1 = cpf_.copy()
cpf_2 = cpf_.copy()
cpf_1.remove(cpf_1[-2])
cpf_1.remove(cpf_1[-1])
cpf_2.remove(cpf_[-1])
cpf_copy1 = cpf_.copy()
cpf_copy = [eval(i) for i in cpf_copy1]
i = 10
j = 11
l2 = []
l0 = []
for x in range(len(cpf_1)):
  a = int(cpf_[x])*i
  i = i - 1
  l0.append(a)
soma = sum(l0)
digit1 = int(cpf_copy[-2])
digit2 = (cpf_copy[-1])
resto = soma%11
if resto == 0 or resto == 1:
  digitverificador1 = 0
else:
  digitverificador1 = (11 - resto) 
for y in range(len(cpf_2)):
  b = int(cpf_[y])*j
  j = j - 1
  l2.append(b)
add = sum(l2)
rest = add%11
if rest == 0 or rest == 1:
  digitverificador2 = 0
else:
  digitverificador2 = (11 - rest) 
if digit1 == digitverificador1 and digit2 == digitverificador2:
  a = 1 == 1
else:
  a = 1 == 2
e1 = ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul', 'Tocantins']
e2 = ['Amazonas', 'Pará', 'Roraima', 'Amapá', 'Acre', 'Rondônia']
e4 = ['Paraíba', 'Pernambuco', 'Alagoas', 'Rio Grande do Norte']
e0 = ['Rio Grande do Sul', 'Minas Gerais', 'São Paulo']
e6 = ['Rio de Janeiro', 'Espírito Santo']
e3 = ['Ceará', 'Maranhão', 'Piauí']
e7 = ['Paraná', 'Santa Catarina']
e5 = ['Bahia', 'Sergipe']
if (cpf_copy[-3]) == 0:
  local = e0[0]
elif (cpf_copy[-3]) == 1:
  local = e1
elif (cpf_copy[-3]) == 2:
  local = e2
elif (cpf_copy[-3]) == 3:
  local = e3
elif (cpf_copy[-3]) == 4:
  local = e4
elif (cpf_copy[-3]) == 5:
  local = e5
elif (cpf_copy[-3]) == 6:
  local = e0[1]
elif (cpf_copy[-3]) == 7:
  local = e6
elif (cpf_copy[-3]) == 8:
  local = e0[2]
elif (cpf_copy[-3]) == 9:
  local = e7
if a and (local == e1 or local == e2 or local == e3 or local == e4 or local == e5 or local == e6 or local == e7):
  print('CPF Válido e foi emitido em: ', ' ou '.join(local), '!')
elif local == e0[0]:
  print('CPF Válido e foi emitido em: ', e0[0], '!')
elif local == e0[1]:
  print('CPF Válido e foi emitido em: ', e0[1], '!')
elif local == e0[2]:
  print('CPF Válido e foi emitido em: ', e0[2], '!')
else:
  print('CPF inválido! Verifique os números informados!')
