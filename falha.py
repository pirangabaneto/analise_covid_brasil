"""
1) Fazer um programa que receba uma data e gere um relatorio que contenha as seguintes
informacoes:
1. Data - A data escolhida -> OK
2. Estado - A sigla do Estado -> OK
3. casosAcumulado - A quantidade de casos acumulados do estado
4. obitosAcumulado - A quantidade de obitos acumulados do estado
5. percPopCasos - O percentual de casos referentes ao total da populacao por estado
6. casoAnterior - O numero de casos do dia anterior a data utilizada do estado
7. obitoAnterior - O numero de obitos anteriores a data utilizada do estado
8. percCaso - Percentual de aumento de casos em relacao ao dia anterior
9. percObito - Percentual de aumento de obitos em relacao ao dia anterior
10. novosCasos - Quantidade de novos casos
11. novosObitos - Quantidade de novos obitos




# 1. Data - A data escolhida
def p1(data):
    return "A data escolhida foi: " + data

# 2. Estado - A sigla do Estado
def p2(base):
    return base['estado'].unique()


# 3. casosAcumulado - A quantidade de casos acumulados do estado
def p3(estados, base, data):
    valoresCA = []
    for i in estados:
        valoresCA.append((base.loc[(base['estado'] == i) & (base['data'] == data)]['casosAcumulado']).sum())
        #valoresCA.append(base.loc[base['data'] == data, 'casosAcumulado'].sum())
        #valoresCA.append(base.loc[(base['estado'] == i), 'casosAcumulado'].sum())
    return dict((key, value) for (key, value) in zip(estados, valoresCA))


#4. obitosAcumulado - A quantidade de obitos acumulados do estado
def p4(estados, base, data):
    valoresOA = []
    for i in estados:
        valoresOA.append(base.loc[(base['estado'] == i) & (base['data'] == data), 'obitosAcumulado'].sum())

    return valoresOA
    #return dict((key, value) for (key, value) in zip(estados, valoresOA))


def q1(data):
    # ler a base
    #base = lerArquivo('HIST_PAINEL_COVIDBR_02fev2021-v2.csv')
    base = lerArquivo('HIST_PAINEL_COVIDBR_02fev2021.csv')
    #base = lerArquivo('teste.csv')
    base = base[base['estado'].notna()]
    # 1. Data - A data escolhida
    # tem que vir como string
    # data_escolhida = datetime.strptime(data, "%Y-%m-%d").date()
    #data_escolhida = p1(data)

    # 2. Estado - A sigla do Estado
    estados = p2(base)
    #print(estados)

    # 3. casosAcumulado - A quantidade de casos acumulados do estado
    #casosAcumulados = p3(estados,base,data)
    #print casosAcumulados
    #print casosAcumulados
    #valoresCA.append(base.loc[(base['estado'] == i) & (base['data'] == data) & (base['casosAcumulado'] != 0), 'casosAcumulado'].
    parte = base.loc[(base['data'].eq('2021-02-01') & -(base['estado'].eq('BA')))]
    print(parte['data'])
    #print (base.loc[base['data'] == data, 'casosAcumulado'].sum())
    #valoresCA = []
    #for i in estados:

     #   valoresCA.append(base.loc[(base['estado'] == i) & (base['data'] == data), 'casosAcumulado'].sum())

    #casosAcumulados = dict((key, value) for (key, value) in zip(estados, valoresCA))
    #casosAcumulados = p3(estados,base, data)
    #print "casos acumulados:"
    #print casosAcumulados
"""
"""
    #4. obitosAcumulado - A quantidade de obitos acumulados do estado
    #valoresOA = []
    #for i in estados:
    #    valoresOA.append(base.loc[(base['estado'] == i) & (base['data'] == data), 'obitosAcumulado'].sum())

    #obtosAcumulados = dict((key, value) for (key, value) in zip(estados, valoresOA))
    obtosAcumulados = p4(estados,base, data)
    #print "obtos acumulados:"
    #print obtosAcumulados

    # 5. percPopCasos - O percentual de casos referentes ao total da populacao por estado
    #popEstados = lerArquivo('populacao_estado _resumido.csv')
    popEstados = {"AC": 894470,# }
"AL": 3351543,
"AP":  861773,
"AM":4207714, 
"BA": 14930634, 
"CE": 9187103,
"DF": 3055149,
"ES": 4064052,
"GO": 7113540,
"MA":7114598,
"MT": 3526220,
"MS": 2809394,
"MG":21292666,
"PA":11516840,
"PB":4039277,
"PR":11516840,
"PE":9616621,
"PI":3281480,
"RJ":6747815,
"RN":3534165,
"RS":11422973,
"RO":1796460,
"RR":631181,
"SC":7252502,
"SP":46289333,
"SE":2318822,
"TO": 1590248,
                  }
    percPopCasos = []
    for i in estados:

        #if popEstados[estados].size != 0:
        #print
        percPopCasos.append(
                (casosAcumulados.get(i) * 100.0) /
                #5
                popEstados.get(str(i))
                #(popEstados.loc[(popEstados['estado'].str.strip() == i), 'populacao'])#.values[0]#.astype(int)#.values[0]
                # pegando a populacao de cada estado
            )
    percPopCasos = dict((key, value) for (key, value) in zip(estados, percPopCasos))
    #print(percPopCasos)

    # 6. casoAnterior - O numero de casos do dia anterior a data utilizada do estado
    valoresCAn = []
    dataAnterior = str((datetime.strptime(data, "%Y-%m-%d") - timedelta(days=1)).date())

    for i in estados:
        valoresCAn.append(base.loc[(base['estado'] == i) & (base['data'] == dataAnterior), 'casosAcumulado'].sum())

    casosAnteriores = dict((key, value) for (key, value) in zip(estados, valoresCAn))
    #print "casos anteriores:"
    #print casosAnteriores

    # 7. obitoAnterior - O numero de obitos anteriores a data utilizada do estado
    valoresOAn = []
    for i in estados:
        valoresOAn.append(base.loc[(base['estado'] == i) & (base['data'] == dataAnterior), 'obitosAcumulado'].sum())

    obtosAnteriores = dict((key, value) for (key, value) in zip(estados, valoresOAn))
    #print "obtos anteriores:"
    #print obtosAnteriores

    # 8. percCaso - Percentual de aumento de casos em relacao ao dia anterior
    valoresAC = []
    for i in estados:
        if casosAnteriores.get(i) != 0:
            valoresAC.append(
                ((casosAcumulados.get(i) - casosAnteriores.get(i)) / float(casosAnteriores.get(i))) * 100
            )
        # percCaso.append(base.loc[(base['estado'] == i) & (base['data'] == dataAnterior), 'obitosAcumulado'].sum())
        percCaso = dict((key, value) for (key, value) in zip(estados, valoresAC))
    #print percCaso

    #9. percObito - Percentual de aumento de obitos em relacao ao dia anterior
    valoresAO = []
    for i in estados:
        if(obtosAnteriores.get(i) != 0):
            valoresAO.append(
                # casosAcumulados.get(i) - 10
                ((obtosAcumulados.get(i) - obtosAnteriores.get(i)) / float(obtosAnteriores.get(i))) * 100
            )
        percObito = dict((key, value) for (key, value) in zip(estados, valoresAO))
    #print percObito

    #10. novosCasos - Quantidade de novos casos
    valoresNC = []
    for i in estados:
        valoresNC.append(base.loc[(base['estado'] == i) & (base['data'] == data), 'casosNovos'].sum())

    novosCasos = dict((key, value) for (key, value) in zip(estados, valoresNC))
    #print "novos casos:"
    #print novosCasos

    #11. novosObitos - Quantidade de novos obitos
    valoresNO = []
    for i in estados:
        valoresNO.append(base.loc[(base['estado'] == i) & (base['data'] == data), 'obitosNovos'].sum())

    novosObitos = dict((key, value) for (key, value) in zip(estados, valoresNO))
    #print "novos obtos:"
    #print novosObitos

# print casosAcumulados



base = lerArquivo('HIST_PAINEL_COVIDBR_02fev2021-v2.csv')
#a = (base.loc[(base['estado'] == 'AC') & (base['data'] == (datetime.strptime("2021-02-01", "%Y-%m-%d"))), 'casosAcumulado'].sum())

(base['data'])
#base.info()
"""
"""

q1('2021-02-01')
"""