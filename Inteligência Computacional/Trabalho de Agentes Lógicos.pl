#Regras
ministrada_por(X, Y):- ministra(Y, X).
subarea_por_professor(X, Y):- disciplina_subarea(W, X), ministra(Y, W).
professor_por_centro(X, Y):- lotado_em(X, W, Z), curso_por_centro(W, Z, Y), centro(Y).
disciplina_por_centro(X, Y):- disciplina_curso(X, W, Z), curso_por_centro(W, Z, Y), centro(Y).
professor_mc(P):- ministra(P, D), disciplina_curso(D, C1, M1), disciplina_curso(D, C2, M2), (C1\==M1;C2\==M2).

#Base de dados
cet(matematica).
cet(probabilidade_e_estatistica).
cet(ciencia_da_computacao).
cet(fisica).
centro(ccet).
centro(ccbs).
centro(ccsa).
subarea(programacao, ciencia_da_computacao).
subarea(computacao_e_algoritmos, ciencia_da_computacao).
subarea(arquitetura_de_computadores, ciencia_da_computacao).
subarea(matematica, ciencia_da_computacao).
subarea(fisica_e_eletricidade, ciencia_da_computacao).
subarea(pedagogia, ciencia_da_computacao).
subarea(mecanica, fisica).
subarea(termodinamica, ciencia_da_computacao).
subarea(eletromagnetismo, fisica).
subarea(fisica_ondulatoria, fisica).
subarea(calculo_diferencial_e_integral, fisica).
subarea(geometria_analitica, fisica).
disciplina_subarea(d1, programacao).
disciplina_subarea(d2, programacao).
disciplina_subarea(d3, computacao_e_algoritmos).
disciplina_subarea(d4, computacao_e_algoritmos).
disciplina_subarea(d5, matematica).
disciplina_subarea(d6, fisica_e_eletricidade).
disciplina_subarea(d7, pedagogia).
disciplina_subarea(d8, mecanica).
disciplina_subarea(d9, mecanica).
disciplina_subarea(d10, termodinamica).
disciplina_subarea(d11, eletromagnetismo).
disciplina_subarea(d12, fisica_ondulatoria).
disciplina_subarea(d13, calculo_diferencial_e_integral).
disciplina_subarea(d14, geometria_analitica).
disciplina_curso(d1, bacharelado, ciencia_da_computacao).
disciplina_curso(d2, bacharelado, ciencia_da_computacao).
disciplina_curso(d3, bacharelado, ciencia_da_computacao).
disciplina_curso(d4, bacharelado, ciencia_da_computacao).
disciplina_curso(d5, bacharelado, ciencia_da_computacao).
disciplina_curso(d6, bacharelado, ciencia_da_computacao).
disciplina_curso(d8, bacharelado, fisica).
disciplina_curso(d9, bacharelado, fisica).
disciplina_curso(d10, bacharelado, fisica).
disciplina_curso(d11, bacharelado, fisica).
disciplina_curso(d12, licenciatura, fisica).
disciplina_curso(d13, licenciatura, fisica).
disciplina_curso(d14, licenciatura, fisica).
curso_por_centro(ciencia_da_computacao, bacharelado, ccet). # ccet - Centro de Ciências Exatas e Tecnologia
curso_por_centro(fisica, bacharelado, ccet).
curso_por_centro(fisica, licenciatura, ccet).
curso_por_centro(enfermagem, bacharelado, ccbs). # ccbs - Centro de Ciências Biológicas e da Saúde.
curso_por_centro(veterinária, bacharelado, ccbs). 
curso_por_centro(biologia, licenciatura, ccbs). 
curso_por_centro(odontologia, bacharelado, ccbs). 
curso_por_centro(zootecnia, licenciatura, ccbs). 
curso_por_centro(direito, bacharelado, ccsa). # ccsa - Centro de Ciências Sociais Aplicadas
curso_por_centro(filosofia, licenciatura, ccsa).
curso_por_centro(história, licenciatura, ccsa).
curso_por_centro(letras, bacharelado, ccsa).
lotado_em(p1, ciencia_da_computacao, bacharelado).
lotado_em(p2, ciencia_da_computacao, bacharelado).
lotado_em(p3, ciencia_da_computacao, bacharelado).
lotado_em(p4, fisica, bacharelado).
lotado_em(p5, fisica, bacharelado).
lotado_em(p6, fisica, bacharelado).
lotado_em(p7, fisica, licenciatura).
lotado_em(p8, fisica, licenciatura).
lotado_em(p9, fisica, licenciatura).
ministra(p1, d1).
ministra(p1, d2).
ministra(p1, d3).
ministra(p1, d11).
ministra(p2 , d4).
ministra(p2 , d5).
ministra(p3 , d6).
ministra(p3 , d7).
ministra(p4 , d8).
ministra(p4 , d13).
ministra(p5 , d9).
ministra(p6 , d10).
ministra(p6 , d11).
ministra(p8 , d12).
ministra(p8 , d13).
ministra(p9 , d8).
ministra(p9 , d14).


