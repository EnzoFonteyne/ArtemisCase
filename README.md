# ArtemisCase

## Desafio 1 - reconcile_accounts

# Reconciliação de transações com verificação de datas e transações duplicadas

Este projeto em Python implementa um sistema para reconciliar duas listas de transações financeiras, verificando se transações equivalentes estão presentes em ambas as listas, com tolerância de **±1 dia na data** da transação.

## 📋 Objetivo

O objetivo é identificar se cada transação está **presente** na outra lista com os mesmos dados (exceto a data) e se existe uma **data correspondente válida**, definida como a mesma data, um dia antes ou um dia depois. O código classifica cada transação como:

- `FOUND`: transação correspondente encontrada na outra lista (com data válida).
- `MISSING`: transação não encontrada ou sem data correspondente no intervalo aceitável.

## 🧰 Requisitos

Este script foi feito para rodar em **Python 3.7+**, utilizando **apenas bibliotecas padrão**, portanto não há necessidade de instalar dependências externas.

## 📁 Estrutura esperada dos arquivos

- Os arquivos `transaction1.csv` e `transaction2.csv` devem estar localizados na pasta `desafio1/`.
- Cada CSV deve conter um cabeçalho na primeira linha e os dados a partir da segunda.
- A estrutura das linhas deve ser: `data(yyyy-mm-dd),departamento,valor,beneficiário`
---

## Desafio 2 - Breast Cancer Wisconsin (Diagnostic) – Análise e Modelagem

## 📄 Estrutura do Notebook

1. **Exploração Inicial dos Dados**  
   - Carregamento do CSV e inspeção das dimensões, tipos e estatísticas básicas (`df.info()`, `df.describe()`).
   - Verificação de valores ausentes e limpeza preliminar.

2. **Análise Exploratória (EDA)**  
   - **Boxplots** de cada variável, separados por `target`, para avaliar distribuição e outliers.  
   - **Pairplot** (seaborn) para visualizar a relação bivariada entre features e separação de classes.  
   - **Heatmap** de correlações para identificar multicolinearidade.

3. **Modelagem – Regressão Linear (OLS)**  
   - Ajuste de modelo OLS com todas as 6 features.  
   - Interpretação de coeficientes, *p*-valores, R², condition number e diagnósticos de resíduos.

4. **Modelagem – Regressão Logística (GLM Binomial)**  
   - Ajuste via `statsmodels.GLM(..., family=Binomial(link=logit))`.  
   - Interpretação de coeficientes em **log-odds**, testes *z*, pseudo R² de Cox–Snell, AIC/BIC e deviance.

5. **Avaliação de Desempenho**  
   - Divisão treino/teste, predição e cálculo de **RMSE** e **acurácia** em ambos os modelos.  
   - Comparação entre:  
     - Regressão Linear completa vs. sem `mean_fractal_dimension`.  
     - Regressão Logística completa vs. reduzida (4 variáveis).  
   - Análise gráfica dos resíduos com **boxplots**.

6. **Conclusão**  
   - A regressão logística reduzida (usando apenas `mean_concave_points`, `mean_perimeter`, `worst_texture` e `worst_area`) obteve o melhor trade-off entre simplicidade, acurácia (~96,7 %) e estabilidade (AIC/BIC menores).  
---