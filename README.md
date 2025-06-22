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

## Desafio 3 - Consultas SQL

O notebook (`desafio3.ipynb`) contém a solução para o **Desafio 3** de SQL, aplicando consultas a um banco de dados SQLite chamado `Loja.sqlite` e exibindo os resultados em `pandas`.

---

## Pré-requisitos

- Python 3.x  
- Bibliotecas:
  - `sqlite3` (já incluída no Python)
  - `pandas`  
- O arquivo `Loja.sqlite` deve estar na mesma pasta do notebook.

---

## Estrutura do Notebook

1. ## Setup  
   - Importa as bibliotecas `sqlite3` e `pandas`.  
   - Abre conexão com o banco `Loja.sqlite`.

2. ## Consulta 1  
   - **Objetivo:** Listar todos os clientes (mesmo aqueles sem pedidos) junto com seus pedidos.  
   - **SQL:**  
     ```sql
     SELECT c.Nome, p.PedidoID, p.DataPedido, p.ValorTotal
       FROM Clientes AS c
  LEFT JOIN Pedidos   AS p ON c.ClienteID = p.ClienteID;
     ```
   - O resultado é carregado em um DataFrame `df_consulta1` com colunas:
     - `Nome Cliente`  
     - `PedidoID`  
     - `Data Pedido`  
     - `Valor Total`

3. ## Consulta 2  
   - **Objetivo:** Para cada cliente que fez pedidos, contar quantos pedidos e somar o valor total.  
   - **SQL:**  
     ```sql
     SELECT c.Nome,
            COUNT(p.PedidoID)    AS QuantidadePedidos,
            SUM(p.ValorTotal)    AS ValorTotal
       FROM Clientes AS c
  INNER JOIN Pedidos   AS p ON c.ClienteID = p.ClienteID
   GROUP BY c.ClienteID;
     ```
   - Carrega o resultado em `df_consulta2` com colunas:
     - `Nome Cliente`  
     - `QuantidadePedidos`  
     - `Valor Total`

4. ## Consulta 3  
   - **Objetivo:** Listar todos os pedidos que **ainda não** têm registro de pagamento.  
   - **SQL:**  
     ```sql
     SELECT p.PedidoID, p.DataPedido, p.ValorTotal
       FROM Pedidos AS p
      WHERE p.PedidoID NOT IN (
          SELECT PedidoID FROM Pagamentos
      );
     ```
   - Resultado em `df_consulta3` com colunas:
     - `PedidoID`  
     - `Data Pedido`  
     - `Valor Total`

---
