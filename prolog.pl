%fatos ou verdades
nasceuEm("Alexsander","Uruguaiana").
nasceuEm("Liliane","Uruguaiana").
nasceuEm("Evando","Santiago").
nasceuEm("Adriel","Porto Alegre").
nasceuEm("Adrian","Joao Pessoa").
nasceuEm("Ada","Uruguaiana").
nasceuEm("Nercila","Santiago").
nasceuEm("Euclides","Uruguaiana").
%regra recursiva de sobrecarga
nasceuEm(Pessoa, Lugar):- 
    nasceuEm(Pessoa, I),
    estaEm(I, Lugar).

localizadoEm("Uruguaiana","RS").
localizadoEm("Pejuçara","RS").
localizadoEm("Cruz Alta","RS").
localizadoEm("Santa Maria","RS").
localizadoEm("Porto Alegre","RS").
localizadoEm("RS","Brasil").
localizadoEm("SC","Brasil").
localizadoEm("Montreal","Quebec").
localizadoEm("Quebec","Canada").
localizadoEm("Santiago", "RS").
localizadoEm("Uruguaiana", "RS").


%regra recursiva
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, OutroLugar).
estaEm(Lugar, OutroLugar) :-
    localizadoEm(Lugar, I),
    estaEm(I, OutroLugar).

progenitor("Ada","Liliane").
progenitor("Nercila","Evando").
progenitor("Euclides","Liliane").
progenitor("Evando","Alexsander").
progenitor("Evando","Adrian").
progenitor("Evando","Adriel").
progenitor("Liliane","Alexsander").
progenitor("Liliane","Adrian").
progenitor("Liliane","Adriel").

avo(Avo, Neta) :-
    progenitor(Avo, Pai),
    progenitor(Pai, Neta).

irmao(I1, I2) :-
    progenitor(Pai,I1),
    progenitor(Pai,I2),
    I1 \= I2.

tio(Tio,Sobrinho) :-
    irmao(Tio,Pai),
    progenitor(Pai,Sobrinho).