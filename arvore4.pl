% Definindo os progenitores e seus filhos
progenitor(samira, pedro).
progenitor(vincenzo, pedro).
progenitor(tiago, samira).
progenitor(tiago, guilherme).
progenitor(marcela, samira).
progenitor(marcela, guilherme).
progenitor(guilherme, joao).
progenitor(pietra, joao).
progenitor(luiz, tiago).
progenitor(nathalia, tiago).
progenitor(vinicius, marcela).
progenitor(paula, marcela).

% Definindo o sexo masculino
sexo(vincenzo, masculino).
sexo(pedro, masculino).
sexo(guilherme, masculino).
sexo(joao, masculino).
sexo(tiago, masculino).
sexo(luiz, masculino).
sexo(vinicius, masculino).

% Definindo o sexo feminino
sexo(samira, feminino).
sexo(pietra, feminino).
sexo(marcela, feminino).
sexo(nathalia, feminino).
sexo(paula, feminino).

% Algoritmo para identificar a irmã.
irma(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y,sexo(X, feminino).
% Algoritmo para identificar o irmão.
irmao(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y,sexo(X,masculino).
% Algoritmo para identificar o avô.
vô(X,Y):-progenitor(X,A),progenitor(Y,A),sexo(X,masculino).
% Algoritmo para identificar a avó.
vó(X,Y):-progenitor(X,A),progenitor(Y,A),sexo(X,feminino).
% Algoritmo para identificar a mãe.
mae(X,Y):-progenitor(X,Y),sexo(X,feminino).
% Algoritmo para identificar o pai.
pai(X,Y):-progenitor(X,Y),sexo(X,masculino).
% Algoritmo para identificar o tio.
tio(X,Y):-irmao(X,A),progenitor(A,Y).
% Algoritmo para identificar a tia.
tia(X,Y):-irma(X,A),progenitor(A,Y).
% Algoritmo para identificar os primos(independente do sexo).
primo(X,Y):-progenitor(A,X),progenitor(A,Y),(irmao(X,Y);irma(X,Y)),X\==Y.
% Algoritmo para identificar os filhos(independente do sexo).
filho(X,Y) :-progenitor(Y, X).
