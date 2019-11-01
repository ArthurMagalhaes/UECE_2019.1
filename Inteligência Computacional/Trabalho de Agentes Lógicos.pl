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
centro(ccet). # ccet - Centro de Ciências Exatas e Tecnologia.
centro(ccbs). # ccbs - Centro de Ciências Biológicas e da Saúde.
centro(ccsa). # ccsa - Centro de Ciências Sociais Aplicadas.

#Subareas e disciplinas correlatas
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
subarea(genetica_molecular, biologia).
subarea(fitogeografia, biologia).
subarea(citologia, biologia).
subarea(morfologia_grupos_recentes, zootecnia).
subarea(ortodontia, odontologia).
subarea(periodontia, odontologia).
subarea(enfermagem_obstetrica, enfermagem).
subarea(direito_penal, direito).
subarea(historia_moderna, historia).
subarea(historia_medieval, historia).
subarea(logica, filosofia).
subarea(etica, filosofia).
subarea(literatura, letras).
subarea(linguas_indigenas, letras).
disciplina_subarea(d1, programacao, 4).
disciplina_subarea(d2, programacao, 4).
disciplina_subarea(d3, computacao_e_algoritmos, 4).
disciplina_subarea(d4, computacao_e_algoritmos, 4).
disciplina_subarea(d5, matematica,4).
disciplina_subarea(d6, fisica_e_eletricidade, 6).
disciplina_subarea(d7, pedagogia, 4).
disciplina_subarea(d8, mecanica, 4).
disciplina_subarea(d9, mecanica, 4).
disciplina_subarea(d10, termodinamica, 4).
disciplina_subarea(d11, eletromagnetismo, 4).
disciplina_subarea(d12, fisica_ondulatoria, 6).
disciplina_subarea(d13, calculo_diferencial_e_integral, 6).
disciplina_subarea(d14, geometria_analitica, 4).
disciplina_subarea(d15, fitogeografia, 4). 
disciplina_subarea(d16, fitogeografia, 4).
disciplina_subarea(d17, genetica_molecular, 6). 
disciplina_subarea(d18, direito_penal, 4). 
disciplina_subarea(d19, direito_penal, 6).
disciplina_subarea(d20, etica, 4).
disciplina_subarea(d21, ortodontia, 6).
disciplina_subarea(d22, literatura, 6).
disciplina_subarea(d23, linguas_indigenas, 4).
disciplina_subarea(d24, historia_moderna, 4).
disciplina_subarea(d25, historia_moderna, 4).
disciplina_subarea(d26, historia_medieval, 6).

# Cursos
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
curso_por_centro(ciencia_da_computacao, bacharelado, ccet). 
curso_por_centro(fisica, bacharelado, ccet).
curso_por_centro(fisica, licenciatura, ccet).
curso_por_centro(enfermagem, bacharelado, ccbs).  
curso_por_centro(biologia, licenciatura, ccbs). 
curso_por_centro(odontologia, bacharelado, ccbs). 
curso_por_centro(zootecnia, licenciatura, ccbs). 
curso_por_centro(direito, bacharelado, ccsa). 
curso_por_centro(filosofia, licenciatura, ccsa).
curso_por_centro(historia, licenciatura, ccsa).
curso_por_centro(letras, bacharelado, ccsa).

# Professores
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

# Estudantes
cursando(e1, ciencia_da_computacao, bacharelado).
cursando(e2, ciencia_da_computacao, bacharelado).
cursando(e3, ciencia_da_computacao, bacharelado).
cursando(e4, biologia, licenciatura).
cursando(e5, biologia, licenciatura).
cursando(e6, fisica, bacharelado).
cursando(e7, fisica, licenciatura).
cursando(e8, direito, bacharelado).
cursando(e9, direito, bacharelado).
cursando(e10, direito, bacharelado).
cursando(e11, letras, bacharelado).
cursando(e12, letras, bacharelado).
cursando(e13, filosofia, licenciatura).
cursando(e14, historia, licenciatura).
cursando(e15, historia, licenciatura).
matriculado_em(e1, d2).
matriculado_em(e1, d3).
matriculado_em(e1, d4).
matriculado_em(e1, d6).
matriculado_em(e2, d2).
matriculado_em(e2, d5).
matriculado_em(e2, d6).
matriculado_em(e3, d4).
matriculado_em(e4, d15).
matriculado_em(e4, d16).
matriculado_em(e5, d15).
matriculado_em(e6, d10).
matriculado_em(e6, d11).
matriculado_em(e7, d13).
matriculado_em(e7, d14).
matriculado_em(e8, d18).
matriculado_em(e8, d19).
matriculado_em(e9, d18).
matriculado_em(e9, d19).
matriculado_em(e10, d19).
matriculado_em(e11, d22).
matriculado_em(e11, d23).
matriculado_em(e12, d22).
matriculado_em(e12, d23).
matriculado_em(e13, d20).
matriculado_em(e14, d24).
matriculado_em(e14, d26).
matriculado_em(e15, d24).
matriculado_em(e15, d25).
matriculado_em(e15, d26).

