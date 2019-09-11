#Regras
pai(X,Y):- masculino(X), progenitor(X,Y).
mae(X,Y):- feminino(X), progenitor(X,Y).
filho(X,Y):- masculino(X), progenitor(Y,X).
filha(X,Y):- feminino(X), progenitor(Y,X).
irmao(X,Y):- masculino(X), pai(Z, X), pai(Z, Y), X\==Y.
irmao(X,Y):- masculino(X), mae(Z, X), mae(Z, Y), X\==Y.
irma(X,Y):- feminino(X), pai(Z, X), pai(Z, Y), X\==Y.
irma(X,Y):- feminino(X), mae(Z, X), mae(Z, Y), X\==Y.
avo(X,Y):- progenitor(X,Z), progenitor(Z,Y).
tio(X,Y):- irmao(X,Z), progenitor(Z,Y).
tia(X,Y):- irma(X,Z), progenitor(Z,Y).
primo(X,Y):- masculino(X), progenitor(W,X), progenitor(Z,Y), irmao(W,Z), X\==Y.
primo(X,Y):- masculino(X), progenitor(W,X), progenitor(Z,Y), irma(W,Z), X\==Y.
prima(X,Y):- feminino(X), progenitor(W,X), progenitor(Z,Y), irmao(W,Z), X\==Y.
prima(X,Y):- feminino(X), progenitor(W,X), progenitor(Z,Y), irma(W,Z), X\==Y.
descendente(X,Y):- progenitor(Y,X).
descendente(X,Y):- descendente(X,Z), progenitor(Y,Z).

#Base de dados
masculino(jos�).
feminino(maria).
masculino(jo�o).
feminino(ana).
feminino(helena).
feminino(joana).
masculino(m�rio).
masculino(carlos).

progenitor(jos�, jo�o).
progenitor(jos�, ana).
progenitor(maria, jo�o).
progenitor(maria, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(jo�o, m�rio).
progenitor(helena, carlos).
progenitor(m�rio, carlos).