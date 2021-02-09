# alteracoes no documento original:
# das linhas 34989 a 35614 apaguei a infomacao MANAUS que ficava na coluna G pois nao seguia o modelo de colunas proposto

from datetime import datetime, timedelta
import pandas as pd
from fpdf import FPDF
import csv
import operator
from itertools import product


def lerArquivo(nome):
    csv_file = nome
    # data = pd.read_csv(csv_file, sep=',', low_memory=False)
    return pd.read_csv(csv_file, sep=',', low_memory=False)
    # print(data.info())


# 1. Data - A data escolhida
def p1(data):
    with open(base + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return "A data escolhida foi: " + data


# 2. Estado - A sigla do Estado
def p2(nome):
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        estados = []
        primeiro = True
        for i in base:
            if not primeiro:
                if not i[1] in estados:
                    # print "nao ta"
                    estados.append(i[1])
            else:
                primeiro = False
        return estados
        # print i[1] in estados


base = 'HIST_PAINEL_COVIDBR_02fev2021'
estados = p2(base)


# 2. Estado - Os nomes das cidades
def pc(nome):
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        cidades = []
        primeiro = True
        for i in base:
            if not primeiro:
                if not i[2] in cidades:
                    # print "nao ta"
                    cidades.append(i[1])
            else:
                primeiro = False
        return cidades


# cidades = pc(base)

# 3. casosAcumulado - A quantidade de casos acumulados do estado
def p3(lista_estados, nome, data):
    result = dict.fromkeys(lista_estados, 0)
    usadas = []
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        estadosCorretos = ['DF', 'PR', 'RS', 'GO', 'MT', 'MS', 'SC', 'SP']
        for linha in base:
            if (linha[7] == data):
                if not linha[2] in usadas or (linha[2] == "" and linha[1] in estadosCorretos):
                    result[linha[1]] = result[linha[1]] + int(linha[10])
                    usadas.append(linha[2])
        return result


# casosAcumulado = p3(estados,'HIST_PAINEL_COVIDBR_02fev2021','2021-02-02')
# print(casosAcumulado)
# print(sum(a.values()))


# 4. obitosAcumulado - A quantidade de obitos acumulados do estado
def p4(lista_estados, nome, data):
    result = dict.fromkeys(lista_estados, 0)
    usadas = []
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        estadosCorretos = ['DF', 'PR', 'RS', 'GO', 'MT', 'MS', 'SC', 'SP']
        for linha in base:
            if (linha[7] == data):
                if not linha[2] in usadas or (linha[2] == "" and linha[1] in estadosCorretos):
                    result[linha[1]] = result[linha[1]] + int(linha[12])
                    usadas.append(linha[2])
        return result


# obitosAcumulado = p4(estados,'HIST_PAINEL_COVIDBR_02fev2021','2021-02-02')
# print(obitosAcumulado)
# print(sum(a.values()))


# 5. percPopCasos - O percentual de casos referentes ao total da populacao por estado
popEstados = {"AC": 894470,
                  "AL": 3351543,
                  "AP": 861773,
                  "AM": 4207714,
                  "BA": 14930634,
                  "CE": 9187103,
                  "DF": 3055149,
                  "ES": 4064052,
                  "GO": 7113540,
                  "MA": 7114598,
                  "MT": 3526220,
                  "MS": 2809394,
                  "MG": 21292666,
                  "PA": 11516840,
                  "PB": 4039277,
                  "PR": 11516840,
                  "PE": 9616621,
                  "PI": 3281480,
                  "RJ": 6747815,
                  "RN": 3534165,
                  "RS": 11422973,
                  "RO": 1796460,
                  "RR": 631181,
                  "SC": 7252502,
                  "SP": 46289333,
                  "SE": 2318822,
                  "TO": 1590248,
                  }
def p5(casosAcumulados):

    percPopCasos = []
    for i in estados:
        percPopCasos.append(
            (casosAcumulados.get(i) * 100.0) /
            popEstados.get(str(i))
            # pegando a populacao de cada estado
        )
    return dict((key, value) for (key, value) in zip(estados, percPopCasos))


# percPopCasos = p5(casosAcumulado)
# print(percPopCasos)
# print(sum(a.values()))


# 6. casoAnterior - O numero de casos do dia anterior a data utilizada do estado
def p6(data):
    data_anterior = str((datetime.strptime(data, "%Y-%m-%d") - timedelta(days=1)).date())
    return p3(estados, 'HIST_PAINEL_COVIDBR_02fev2021', data_anterior)


# casoAnterior = p6('2021-02-02')
# print casoAnterior


# 7. obitoAnterior - O numero de obitos anteriores a data utilizada do estado
def p7(data):
    data_anterior = str((datetime.strptime(data, "%Y-%m-%d") - timedelta(days=1)).date())
    return p4(estados, 'HIST_PAINEL_COVIDBR_02fev2021', data_anterior)


# obitoAnterior = p7('2021-02-02')
# print obitoAnterior


# 8. percCaso - Percentual de aumento de casos em relacao ao dia anterior
def p8(casosAnteriores, casosAcumulados):
    valoresAC = []
    for i in estados:
        valoresAC.append(
            (casosAcumulados[i] - casosAnteriores[i]) / float(casosAnteriores[i]) * 100
        )
    return dict((key, value) for (key, value) in zip(estados, valoresAC))


# percCaso = p8(casoAnterior, casosAcumulado)
# print percCaso

# 9. percObito - Percentual de aumento de obitos em relacao ao dia anterior
def p9():
    valoresOC = []
    for i in estados:
        valoresOC.append(
            (obitosAcumulado[i] - obitoAnterior[i]) / float(obitoAnterior[i]) * 100
        )
    return dict((key, value) for (key, value) in zip(estados, valoresOC))


# percObito = p9()
# print percObito


# 10. novosCasos - Quantidade de novos casos
def p10(lista_estados, nome, data):
    result = dict.fromkeys(lista_estados, 0)
    usadas = []
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        estadosCorretos = ['DF', 'PR', 'RS', 'GO', 'MT', 'MS', 'SC', 'SP']
        for linha in base:
            if (linha[7] == data):
                if not linha[2] in usadas or (linha[2] == "" and linha[1] in estadosCorretos):
                    result[linha[1]] = result[linha[1]] + int(linha[11])
                    usadas.append(linha[2])
        return result


# novosCasos = p10(estados,'HIST_PAINEL_COVIDBR_02fev2021','2021-02-02')
# print(novosCasos)

# 11. novosObitos - Quantidade de novos obitos
def p11(lista_estados, nome, data):
    result = dict.fromkeys(lista_estados, 0)
    usadas = []
    with open(nome + '.csv') as csv_file:
        base = csv.reader(csv_file, delimiter=',')
        estadosCorretos = ['DF', 'PR', 'RS', 'GO', 'MT', 'MS', 'SC', 'SP']
        for linha in base:
            if (linha[7] == data):
                if not linha[2] in usadas or (linha[2] == "" and linha[1] in estadosCorretos):
                    result[linha[1]] = result[linha[1]] + int(linha[13])
                    usadas.append(linha[2])
        return result


def p12(obitosAcumulado):
    percPopObitos = []
    for i in estados:
        percPopObitos.append(
            (obitosAcumulado.get(i) * 100.0) /
            popEstados.get(str(i))
            # pegando a populacao de cada estado
        )
    return dict((key, value) for (key, value) in zip(estados, percPopObitos))


def gerar_pdf(data):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF(orientation='L')
    # pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 10

    # Text height is the same as current font size
    th = 2 * pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    pdf.cell(epw, 0.0, 'Dados relativos ao dia ' + data, align='C')
    pdf.ln(th)

    header_completo = ['Estado', 'Total de Casos', 'Total de Obitos', '% por Populacao', 'Casos dia Anterior',
                       'Obitos dia Anterior', '% de Aumento de casos', '% de Aumento de obitos', 'Novos Casos',
                       'Novos Obitos']
    header = ['ES', 'TC', 'TO', '%PO', 'CDA', 'ODA', '%AC', '%AO', 'NC', 'NO']

    # legenda:
    pdf.cell(epw, 0.0, 'Legenda:', align='L')
    pdf.ln(th)

    for i in range(len(header)):
        pdf.cell(0.3 * epw, th, header[i] + ' ->  ' + header_completo[i], border=1, align='L')
        pdf.ln(th)
    pdf.ln(3 * th)

    # header:
    primeiro = True
    for titulo in header:
        pdf.cell(col_width, th, titulo, border=1)
    primeiro = True
    pdf.ln(th)

    # body
    for estado in sorted(estados):
        pdf.cell(col_width, th, estado, border=1)
        pdf.cell(col_width, th, str(casosAcumulado[estado]), border=1)
        pdf.cell(col_width, th, str(obitosAcumulado[estado]), border=1)
        pdf.cell(col_width, th, "{:.6f}".format(percPopCasos[estado]), border=1)
        pdf.cell(col_width, th, str(casoAnterior[estado]), border=1)
        pdf.cell(col_width, th, str(obitoAnterior[estado]), border=1)
        pdf.cell(col_width, th, "{:.6f}".format(percPopCasos[estado]), border=1)
        pdf.cell(col_width, th, "{:.6f}".format(percPopCasos[estado]), border=1)
        pdf.cell(col_width, th, str(novosCasos[estado]), border=1)
        pdf.cell(col_width, th, str(novosObitos[estado]), border=1)

        pdf.ln(th)
    pdf.ln(th)

    col_width = epw / 2
    # total de casos e obitos:
    pdf.cell(col_width, th, 'Total Casos', border=1)
    pdf.cell(col_width, th, str(sum(casosAcumulado.values())), border=1)
    pdf.ln(th)

    pdf.cell(col_width, th, 'Total Obitos', border=1)
    pdf.cell(col_width, th, str(sum(obitosAcumulado.values())), border=1)
    pdf.ln(th)

    pdf.output("relatorio-geral-"+data+".pdf")


#estados pelo numero de casos
def gerar_pdf_numero_casos(data):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Text height is the same as current font size
    th = 2 * pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    pdf.cell(epw, 0.0, 'Dados relativos ao dia ' + data, align='C')
    pdf.ln(th)

    pdf.cell(epw, 0.0, 'Estados/Numero de casos ordenado do maior para o menor', align='C')
    pdf.ln(th)

    dict_ordenado = casosAcumulado
    # body
    while len(dict_ordenado) != 0:
        maior_estado = next(iter(dict_ordenado))
        for estado in dict_ordenado:
            if dict_ordenado[estado] > dict_ordenado[maior_estado]:
                maior_estado = estado

        pdf.cell(col_width, th, maior_estado, border=1)
        pdf.cell(col_width, th, str(dict_ordenado[maior_estado]), border=1)
        del dict_ordenado[maior_estado]

        pdf.ln(th)
    pdf.ln(th)

    pdf.output("relatorio-num-casos-"+data+".pdf")


#estados pelo numero de obitos
def gerar_pdf_numero_obitos(data):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Text height is the same as current font size
    th = 2 * pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    pdf.cell(epw, 0.0, 'Dados relativos ao dia ' + data, align='C')
    pdf.ln(th)

    pdf.cell(epw, 0.0, 'Estados/Numero de obitos ordenado do maior para o menor', align='C')
    pdf.ln(th)

    dict_ordenado = obitosAcumulado
    # body
    while len(dict_ordenado) != 0:
        maior_estado = next(iter(dict_ordenado))
        for estado in dict_ordenado:
            if dict_ordenado[estado] > dict_ordenado[maior_estado]:
                maior_estado = estado

        pdf.cell(col_width, th, maior_estado, border=1)
        pdf.cell(col_width, th, str(dict_ordenado[maior_estado]), border=1)
        del dict_ordenado[maior_estado]

        pdf.ln(th)
    pdf.ln(th)
    pdf.output("relatorio-num-obitos-"+data+".pdf")


#numero total de casos em relacao a populacao do estado.
def gerar_pdf_numero_casos_pop(data):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Text height is the same as current font size
    th = 2 * pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    pdf.cell(epw, 0.0, 'Dados relativos ao dia ' + data, align='C')
    pdf.ln(th)

    pdf.cell(epw, 0.0, 'Numero total de casos em relacao a populacao do estado', align='C')
    pdf.ln(th)

    dict_ordenado = percPopCasos
    # body
    while len(dict_ordenado) != 0:
        maior_estado = next(iter(dict_ordenado))
        for estado in dict_ordenado:
            if dict_ordenado[estado] > dict_ordenado[maior_estado]:
                maior_estado = estado

        pdf.cell(col_width, th, maior_estado, border=1)
        pdf.cell(col_width, th, str(dict_ordenado[maior_estado]), border=1)
        del dict_ordenado[maior_estado]

        pdf.ln(th)
    pdf.ln(th)
    pdf.output("relatorio-num-casos-pop-"+data+".pdf")


#numero total de obitos em relacao a populacao do estado.
def gerar_pdf_numero_obitos_pop(data):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Text height is the same as current font size
    th = 2 * pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    pdf.cell(epw, 0.0, 'Dados relativos ao dia ' + data, align='C')
    pdf.ln(th)

    pdf.cell(epw, 0.0, 'Numero total de obitos em relacao a populacao do estado.', align='C')
    pdf.ln(th)

    dict_ordenado = percPopObitos
    # body
    while len(dict_ordenado) != 0:
        maior_estado = next(iter(dict_ordenado))
        for estado in dict_ordenado:
            if dict_ordenado[estado] > dict_ordenado[maior_estado]:
                maior_estado = estado

        pdf.cell(col_width, th, maior_estado, border=1)
        pdf.cell(col_width, th, str(dict_ordenado[maior_estado]), border=1)
        del dict_ordenado[maior_estado]

        pdf.ln(th)
    pdf.ln(th)
    pdf.output("relatorio-num-obitos-pop-"+data+".pdf")



data = raw_input("Data (aaaa-mm-dd): ")
casosAcumulado = p3(estados, base, data)

obitosAcumulado = p4(estados, base, data)
percPopCasos = p5(casosAcumulado)
percPopObitos = p12(obitosAcumulado) #relacao num de obitos - populacao do estado
casoAnterior = p6(data)
obitoAnterior = p7(data)
percCaso = p8(casoAnterior, casosAcumulado)
percObito = p9()
novosCasos = p10(estados, base, data)
novosObitos = p11(estados, base, data)
gerar_pdf(data)

# 2) A partir dos dados gere um relatorio que ordene os estados pelo numero de casos e outro
# relatorio pelo numero de obitos gerando um ranking dos estados em relacao ao numero total de
# casos e obitos.

gerar_pdf_numero_casos(data)
gerar_pdf_numero_obitos(data)


#3)Agora gere dois relatorios do ranking dos estados que represente o numero total de casos e
#obitos em relacao a populacao do estado.

gerar_pdf_numero_casos_pop(data)
gerar_pdf_numero_obitos_pop(data)

#4) Feito o ranking dos itens 2 e 3, quais analises podem ser feitas?

#numero de obitos de cada estado no periodo marco-2020 a janeiro-2021:
datas_analise = ['2020-03-30','2020-04-30','2020-05-30','2020-06-30','2020-07-30','2020-08-30','2020-09-30','2020-10-30',
                 '2020-11-30','2020-12-30','2021-01-30']

def casosAcumuladosRange():
    res = []
    for i in datas_analise:
        res.append(p3(estados, base, i))

    #escrevendo o csv
    with open('casos-acumulados-range.csv', 'wb') as file:
        writer = csv.writer(file)

        # escrevendo o header:
        header = estados[:]
        header.insert(0, 'data')

        writer.writerow(header)

        # escrevendo os valores a baixo da linah correspondente
        cont = 0
        for data in res:
            linha = []
            linha.append(datas_analise[cont])
            for estado in estados:
                linha.append(data[estado])
            writer.writerow(linha)
            cont = cont + 1
        # writer.writerow([1, "Linus Torvalds", "Linux Kernel"])


def obitosAcumuladosRange():
    res = []
    for i in datas_analise:
        res.append(p4(estados, base, i))

    #escrevendo o csv
    with open('obitos-acumulados-range.csv', 'wb') as file:
        writer = csv.writer(file)

        # escrevendo o header:
        header = estados[:]
        header.insert(0, 'data')

        writer.writerow(header)

        # escrevendo os valores a baixo da linah correspondente
        cont = 0
        for data in res:
            linha = []
            linha.append(datas_analise[cont])
            for estado in estados:
                linha.append(data[estado])
            writer.writerow(linha)
            cont = cont + 1
        # writer.writerow([1, "Linus Torvalds", "Linux Kernel"])


def perCasosAcumuladosRange():
    res = []
    for i in datas_analise:
        res.append(p5(p3(estados, base, i)))

    #escrevendo o csv
    with open('per-casos-acumulados-range.csv', 'wb') as file:
        writer = csv.writer(file)

        # escrevendo o header:
        header = estados[:]
        header.insert(0, 'data')

        writer.writerow(header)

        # escrevendo os valores a baixo da linah correspondente
        cont = 0
        for data in res:
            linha = []
            linha.append(datas_analise[cont])
            for estado in estados:
                linha.append(data[estado])
            writer.writerow(linha)
            cont = cont + 1
        # writer.writerow([1, "Linus Torvalds", "Linux Kernel"])

#casosAcumuladosRange()
#obitosAcumuladosRange()
#perCasosAcumuladosRange()