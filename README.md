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
