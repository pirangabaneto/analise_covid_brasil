# analise_covid_brasil

Orientações:

. Versão do Python: 2.7

. Arquivo principal: projeto_tres.py

. Formato de input (data): aaaa-mm-dd

Obs.:

. Foi necessário realizar um pré-processamento na base original:

      . Havia linhas da base cuja coluna de "cidade" estava omissa;
      
      . Havia linhas da base cuja coluna "data" contia a sigla do estado;
      
      . Havia linhas duplicadas.
  
. A implementação foi feita, originalmente, utilizando as bibliotecas Numpy e Pandas - checar documento "falha.py" - porém, devido a inconsistência da base,
outra implementação foi necessária, culminando no documento "projeto_tres_py"

Conclusões:

      . Checar gráficos: https://datastudio.google.com/reporting/62609957-572c-4a16-8253-0a4bda8dcf88

<details>
  <summary>Análise da distribuição do número de casos (págs 2 - 6):</summary>
  
  1. Podemos visualizar que os estados com maior número de casos confirmados então entre os estados mais populosos da região (págs 1 - 5);
  2. De forma equivalente, tais estados estão entre os mais populosos de todo o país (pág 6).
</details>


<details>
  <summary>Análise da distribuição do número de óbtios (págs 8 - 13):</summary>
  
  1. Podemos visualizar que os estados com maior número de óbtios confirmados então entre os estados mais populosos da região (págs 8 - 13);
  2. De forma equivalente, tais estados estão entre os mais populosos de todo o país (pág 14).
</details>


<details>
  <summary>Relação: Número de Casos VS Número de Óbitos:</summary>
  
  1. Podemos observar que, não necessariamente, o estado com maior número de casos, por região (GO, SC, PA, BA, SP) detém o maior número de óbitos (GO, RS, PA, CE, SP);
  2. Dado o ponto anteror, temos que, a letalidade do vírus varia entre os estados;
</details>
