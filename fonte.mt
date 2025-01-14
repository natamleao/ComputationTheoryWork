# @Programa Fonte UFC
# coloca x e y na palavra
band 101001
init qp
accept qf

qp, 1, qp, x, >
qp, 0, qi, y, >
qi, 1, qi, x, >
qi, 0, qp, y, >
qp, _, qf, _, <

# Substituir os caracteres de uma palavra por x
# band 11101
# init q0
# accept qf

# q0, 1, q0, x, >
# q0, 0, q0, x, >
# q0, _, qf, _, <

# Verificar se é um binário múltiplo de 3
# band 110
# init q0
# accept q0

# q0, 0, q0, 0, >
# q0, 1, q1, 1, >
# q1, 0, q2, 0, >
# q1, 1, q0, 1, >
# q2, 0, q1, 0, >
# q2, 1, q2, 1, >