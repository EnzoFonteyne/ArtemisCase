import csv
from pathlib import Path
from pprint import pprint
from collections import defaultdict
from datetime import datetime
from typing import Optional

def build_transactions(transactions: list) -> defaultdict:
    """
    Cria um defaultdict que mapeia chaves (dados de transação sem data) para listas de datas.
    """
    index = defaultdict(list) # índice para armazenar datas por chave

    for row in transactions:
        key = tuple(row[1:])  # ignora a data
        date = row[0] # data da transação
        index[key].append(date) # adiciona a data no índice para a chave correspondente

    return index

def parse_date(date_str: str) -> datetime:
    """Converte string no formato YYYY-MM-DD para datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d")

def find_closest_valid_date(base_date: datetime, candidate_dates: list) -> Optional[str]:
    """
    Dada uma data base, encontra a menor data em candidate_dates que esteja no intervalo de ±1 dia.
    Retorna a menor data válida (como string) ou None.
    """
    valid_dates = [] # Lista para armazenar datas válidas dentro do intervalo
    for d in candidate_dates: 
        d_dt = parse_date(d) # Converte a string de data para datetime
        if abs((d_dt - base_date).days) <= 1: # Verifica se a diferença é de no máximo 1 dia
            valid_dates.append(d_dt) # adiciona a data válida à lista
    return min(valid_dates).strftime("%Y-%m-%d") if valid_dates else None

def check_transaction_exists(transaction1: list, index2: defaultdict) -> list:
    """
    Verifica se a transação existe na lista 2 'index2.keys()' e se a data está dentro do intervalo de ±1 dia.
    Retorna uma lista com as transações reconciliadas, adicionando 'FOUND' ou 'MISSING' conforme necessário.
    """
    reconciled1 = []

    set2 = index2.keys()  # Converte o índice para um set de chaves para busca rápida

    for rows in transaction1:
        data_base = parse_date(rows[0]) # Converte a data da transação para datetime
        dados = tuple(rows[1:]) # Ignora a data para a verificação inicial

        if dados not in set2: # Se a chave não existe no set2, marca como 'MISSING'
            reconciled1.append(rows + ['MISSING'])
            continue
        
        # Se a chave existe, verifica se há uma data válida dentro do intervalo de ±1 dia
        closest = find_closest_valid_date(data_base, index2[dados])

        if closest: # Se encontrou uma data válida, marca como 'FOUND'
            reconciled1.append(rows + ['FOUND'])
            index2[dados].remove(closest)  # Remove a data encontrada para evitar duplicatas
        else: # Se não encontrou, marca como 'MISSING'
            reconciled1.append(rows + ['MISSING'])

    return reconciled1 

def reconcile_accounts(transaction1: list, transaction2: list) -> tuple:
    """
    Verifica se as transações existem em ambas as listas ou não, retorna uma cópia de cada uma das listas com uma coluna adicional 
    indicando se a transação existe na outra lista ou não.
    """
    
    # Chama a função para construir os sets e índices para ambas as listas de transações
    index1 = build_transactions(transaction1)
    index2 = build_transactions(transaction2)

    reconciled1 = check_transaction_exists(transaction1,index2)
    reconciled2 = check_transaction_exists(transaction2,index1)

    return reconciled1, reconciled2


if __name__ == "__main__":
    transactions1 = list(csv.reader(Path('desafio1/transaction1.csv').open()))[1:]  # Skip header
    transactions2 = list(csv.reader(Path('desafio1/transaction2.csv').open()))[1:]  # Skip header

    reconciled1, reconciled2 = reconcile_accounts(transactions1, transactions2)

    print("Transações da lista 1 reconciliadas:")
    pprint(reconciled1)

    print("\nTransações da lista 2 reconciliadas:")
    pprint(reconciled2)