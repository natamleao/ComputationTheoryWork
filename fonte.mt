@Programa Fonte UFC

# Exemplo 01: incremento binário.
# Descrição: adiciona 1 a um número binário.
#
band 1011
init right
accept done

right, 1, right, 1, >
right, 0, right, 0, >
right, _, carry, _, <

carry, 1, carry, 0, <
carry, 0, done, 1, <
carry, _, done, 1, <

# Exemplo 02: binário divisível por 3.
# Descrição: verifica se um número binário é divisível por 3.
#
#band 1111
#band 10100
#band 111001
#band 10010
#init q0
#accept accept
#
#q0, 0, q0, 0, >
#q0, 1, q1, 1, >
#q0, _, accept, _, >
#
#q1, 1, q0, 1, >
#q1, 0, q2, 0, >
#
#q2, 0, q1, 0, >
#q2, 1, q2, 1, >

# Exemplo 03: divisível por 3 (base 10).
# Descrição: verifica se um número de base 10 é divisível por 3.
#
#band 42
#band 57
#band 1337
#band 5328
#band 7521
#band 314159265
#band 4728
#init q0
#accept accept
#
#q0, 0, q0, 0, >
#q0, 3, q0, 3, >
#q0, 6, q0, 6, >
#q0, 9, q0, 9, >
#q0, 1, q1, 1, >
#q0, 4, q1, 4, >
#q0, 7, q1, 7, >
#q0, 2, q2, 2, >
#q0, 5, q2, 5, >
#q0, 8, q2, 8, >
#q0, _, accept, _, >
#
#q1, 0, q1, 0, >
#q1, 3, q1, 3, >
#q1, 9, q1, 6, >
#q1, 9, q1, 9, >
#q1, 2, q0, 2, >
#q1, 5, q0, 5, >
#q1, 8, q0, 8, >
#q1, 1, q2, 1, >
#q1, 4, q2, 4, >
#q1, 7, q2, 7, >
#
#q2, 0, q2, 0, >
#q2, 3, q2, 3, >
#q2, 6, q2, 6, >
#q2, 9, q2, 9, >
#q2, 2, q1, 2, >
#q2, 5, q1, 5, >
#q2, 8, q1, 8, >
#q2, 1, q0, 1, >
#q2, 4, q0, 4, >
#q2, 7, q0, 7, >

# Exemplo 04: três comprimentos iguais.
# Descrição: decide a linguagem {aⁿbⁿcⁿ | n ≥ 1}, ou seja, aceita a seguido por b e depois c do mesmo comprimento.
#
#band aabc
#band aabcc
#band aabcbc
#band aabbcc
#init qA
#accept accept
#
#qA, B, scan, B, >
#qA, a, qB, A, >
#
#qB, a, qB, a, >
#qB, B, qB, B, >
#qB, b, qC, B, >
#
#qC, b, qC, b, >
#qC, C, qC, C, >
#qC, c, back, C, <
#
#back, a, back, a, <
#back, B, back, B, <
#back, b, back, b, <
#back, C, back, C, <
#back, A, qA, A, >
#
#scan, B, scan, B, >
#scan, C, scan, C, >
#scan, _, accept, _, >

# Exemplo 05: strings iguais.
# Descrição: decide a linguagem { w#w | w ∈ {0,1}* } (duas strings binárias iguais separadas por '#').
#
#band #
#band 1#10
#band 10#1
#band 10#10
#band 01001#01001
#init start
#accept accept
#
#start, 1, have1, _, >
#start, 0, have0, _, >
#start, #, check, #, >
#
#have0, 0, have0, 0, >
#have0, 1, have0, 1, >
#have0, #, match0, #, >
#
#match0, x, match0, x, >
#match0, 0, back, x, < 
#
#back, 0, back, 0, <
#back, 1, back, 1, <
#back, #, back, #, <
#back, x, back, x, <
#back, _, start, _, >
#
#match1, x, match1, x, >
#match1, 1, back, x, <
#
#have1, 0, have1, 0, >
#have1, 1, have1, 1, >
#have1, #, match1, #, >
#
#check, x, check, x, >
#check, _, accept, _, >

# Exemplo 06: palíndromo.
# Descrição: aceita palíndromos compostos pelos símbolos 'a' e 'b'.
#
#band a
#band ab
#band bb
#band babab
#band abba
#init start
#accept accept
#
#start, _, accept, _, >
#start, b, haveB, _, >
#start, a, haveA, _, >
#
#haveA, a, haveA, a, >
#haveA, b, haveA, b, >
#haveA, _, matchA, _, <
#
#matchA, _, accept, _, >
#matchA, a, back, _, <
#matchA, b, reject, b, >
#
#back, a, back, a, <
#back, b, back, b, <
#back, _, start, _, >
#
#matchB, a, reject, a, >
#matchB, b, back, _, <
#matchB, _, accept, _, >
#
#haveB, _, matchB, _, <
#haveB, a, haveB, a, >
#haveB, b, haveB, b, >

# Exemplo 07: potências de dois.
# Descrição: corresponde a cadeias de 0s cujo comprimento é uma potência de dois.
#
#band 0
#band 000
#band 00000000
#band 0000
#band 00000
#init zero
#accept accept
#
#zero, 0, one, _, >
#zero, _, reject, _, >
#
#one, x, one, x, >
#one, 0, even, x, >
#one, _, accept, _, >
#
#back, _, one, _, >
#back, 0, back, 0, <
#back, x, back, x, <
#
#even, _, back, _, <
#even, x, even, x, >
#even, 0, odd, 0, >
#
#odd, 0, even, x, >
#odd, x, odd, x, >
#odd, _, reject, _, >

# Exemplo 08: comprimentos multiplicados.
# Descrição: decide a linguagem { a^(i)b^(j)c^(k) | i*j = k e i,j,k ≥ 1 }.
# (a's seguidos por b's e depois c's.) onde o número de a's multiplicado pelo número de b's é igual ao número de c's
#
#band abbbcccccc
#band abc
#band b
#band aabcbc
#band aabcc
#band aabbbbcccccccc
#band abbbccccc
#band aabbbcccccc
#init start
#accept accept
#
#start, a, aplus, a, >
#
#aplus, a, aplus, a, >
#aplus, b, bplus, b, >
#
#bplus, b, bplus, b, >
#bplus, c, cplus, c, >
#
#cplus, c, cplus, c, >
#cplus, _, left, _, <
#
#left, a, left, a, <
#left, b, left, b, <
#left, c, left, c, <
#left, _, eachA, _, >
#
#eachA, b, scan, b, >
#eachA, a, eachB, _, >
#
#eachB, a, eachB, a, >
#eachB, C, nextA, C, <
#eachB, b, markC, B, >
#
#markC, b, markC, b, >
#markC, C, markC, C, >
#markC, c, nextB, C, <
#
#nextB, b, nextB, b, <
#nextB, C, nextB, C, <
#nextB, B, eachB, B, >
#
#nextA, a, nextA, a, <
#nextA, B, nextA, b, <
#nextA, _, eachA, _, >
#
#scan, b, scan, b, >
#scan, C, scan, C, >
#scan, _, accept, _, >

# Exemplo 09: adição binária.
# Descrição: adiciona dois números binários juntos.
# Formato: dada a entrada a+b, em que a e b são números binários, deixa c b na fita, onde c = a + b.
#
#band 11+1
#init right
#accept done
#
#right, 0, right, 0, >
#right, 1, right, 1, >
#right, +, right, +, >
#right, _, read, _, <
#
#read, +, rewrite, _, <
#read, 1, have1, c, <
#read, 0, have0, c, <
#
#rewrite, 0, rewrite, 0, <
#rewrite, 1, rewrite, 1, <
#rewrite, l, rewrite, 1, <
#rewrite, O, rewrite, 0, <
#rewrite, _, done, _, >
#
#have1, 0, have1, 0, <
#have1, 1, have1, 1, <
#have1, +, add1, +, <
#
#add1, O, add1, O, <
#add1, l, add1, l, <
#add1, 1, carry, O, <
#add1, 0, back1, l, >
#add1, _, back1, l, >
#
#carry, 1, carry, 0, <
#carry, 0, back1, 1, >
#carry, _, back1, 1, >
#
#back1, 0, back1, 0, >
#back1, 1, back1, 1, >
#back1, O, back1, O, >
#back1, l, back1, l, >
#back1, +, back1, +, >
#back1, c, read, 1, <
#
#have0, 0, have0, 0, <
#have0, 1, have0, 1, <
#have0, +, add0, +, <
#
#add0, O, add0, O, <
#add0, l, add0, l, <
#add0, 1, back0, l, >
#add0, 0, back0, O, >
#add0, _, back0, O, >
#
#back0, c, read, 0, <
#back0, 0, back0, 0, >
#back0, 1, back0, 1, >
#back0, O, back0, O, >
#back0, l, back0, l, >
#back0, +, back0, +, >

# Exemplo 10: multiplicação unária.
# Descrição: multiplica dois números unários separados por um '*'. Aqui, '||*|||' significa 2 vezes 3.
#
#band ||*|||
#
#init eachA
#accept done
#
#eachA, *, skip, *, >
#eachA, |, toB, _, >
#
#skip, |, skip, |, >
#skip, _, done, _, >
#
#nextA, _, eachA, |, >
#nextA, |, nextA, |, <
#nextA, *, nextA, *, <
#
#toB, |, toB, |, >
#toB, *, eachB, *, >
#
#nextB, _, eachB, |, >
#nextB, |, nextB, |, <
#
#eachB, |, sep, _, >
#eachB, _, nextA, _, <
#
#sepL, _, nextB, _, <
#sepL, |, sepL, |, <
#
#sep, _, add, _, >
#sep, |, sep, |, >
#
#add, |, add, |, >
#add, _, sepL, |, <

# Exemplo 11: multiplicação binária.
# Descrição: multiplica dois números binários.
#
#band 11*101
#init start
#accept done
#
#start, 0, _init, 0, <
#start, 1, _init, 1, <
#
#_init, _, right, +, >
#
#right, 0, right, 0, >
#right, 1, right, 1, >
#right, *, right, *, >
#right, _, readB, _, <
#
#shift1, 1, shift1, 1, >
#shift1, 0, shift0, 1, >
#shift1, _, right, 1, >
#
#shift, 1, shift1, *, >
#shift, _, tidy, _, <
#shift, 0, shift0, *, >
#
#tidy, 0, tidy, _, <
#tidy, 1, tidy, _, <
#tidy, +, done, _, <
#
#shift0, _, right, 0, >
#shift0, 1, shift1, 0, >
#shift0, 0, shift0, 0, >
#
#addA, 0, addA, 0, <
#addA, 1, addA, 1, <
#addA, *, read, *, <
#
#readB, 1, addA, _, <
#readB, 0, doubleL, _, <
#
#doubleL, *, shift, 0, >
#doubleL, 0, doubleL, 0, <
#doubleL, 1, doubleL, 1, <
#
#rewrite, _, double, _, >
#rewrite, O, rewrite, 0, <
#rewrite, l, rewrite, 1, <
#rewrite, 0, rewrite, 0, <
#rewrite, 1, rewrite, 1, <
#
#double, *, shift, 0, >
#double, 0, double, 0, >
#double, 1, double, 1, >
#double, +, double, +, >
#
#back0, 0, back0, 0, >
#back0, 1, back0, 1, >
#back0, O, back0, O, >
#back0, l, back0, l, >
#back0, +, back0, +, >
#back0, c, read, 0, <
#
#read, +, rewrite, +, <
#read, 1, have1, c, <
#read, 0, have0, c, <
#
#back1, c, read, 1, <
#back1, 0, back1, 0, >
#back1, 1, back1, 1, >
#back1, O, back1, O, >
#back1, l, back1, l, >
#back1, +, back1, +, >
#
#carry, 1, carry, 0, <
#carry, 0, back1, 1, >
#carry, _, back1, 1, >
#
#add0, O, add0, O, <
#add0, l, add0, l, <
#add0, 1, back0, l, >
#add0, 0, back0, O, >
#add0, _, back0, O, >
#
#have0, +, add0, +, <
#have0, 0, have0, 0, <
#have0, 1, have0, 1, <
#
#have1, +, add1, +, <
#have1, 0, have1, 0, <
#have1, 1, have1, 1, <
#
#add1, 0, back1, l, >
#add1, _, back1, l, >
#add1, 1, carry, O, <
#add1, O, add1, O, <
#add1, l, add1, l, <