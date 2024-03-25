import pandas as pd
from datetime import datetime
from Alfabetizacao.alfabetizacao import AlfabetizacaoTable
from Infra.database import DatabaseConnection

class QuestionarioAlfSalvo:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def rename_columns(self, df, mapper):
        return df.rename(columns=mapper)

    def calcular_pontuacao(self, row):
        self.pontuacao = 0
        for answer in row.values:
            if answer == "Raramente":
                self.pontuacao += 1
            elif answer == "Às vezes":
                self.pontuacao += 2
            elif answer == "Frequentemente":
                self.pontuacao += 3
            elif answer == "Sempre":
                self.pontuacao += 4
        return self.pontuacao
    
    def calcular_nivel_risco(self, pontuacao):
        if pontuacao >= 0 and pontuacao <= 10:
            return "Muito Elevado"
        elif pontuacao >= 11 and pontuacao <= 20:
            return "Elevado"
        elif pontuacao >= 21 and pontuacao <= 30:
            return "Moderado"
        elif pontuacao >= 31 and pontuacao <= 40:
            return "Baixo"
        else:
            return "Valor de pontuação inválido"

    def save(self):
        db_connection = DatabaseConnection('passos_magicos')
        engine = db_connection.get_engine()

        mapper_alfabetizacao = {
            "Matrícula": "matricula",
            "A criança reconhece todas as letras do alfabeto?": "reconhece_letras",
            "A criança consegue ler palavras simples e familiares?": "ler_palavras_simples",
            "A criança consegue escrever palavras simples e familiares?": "escrever_palavras_simples",
            "A criança consegue segmentar palavras em sílabas?": "segmentar_palavras",
            "A criança lê de forma fluente, sem soletrar ou decodificar cada palavra?": "ler_fluente",
            "A criança consegue responder perguntas sobre o que leu?": "responder_perguntas_leitura",
            "A criança conhece o significado das palavras que lê e escreve?": "conhece_significado_palavras",
            "A criança demonstra interesse pela leitura e pela escrita?": "demonstra_interesse",
            "A criança participa ativamente das aulas de alfabetização?": "participa_ativamente",
            "A criança demonstra progresso ao longo do tempo em suas habilidades de leitura e escrita?": "progresso_habilidades"
        }

        df_alfabetizacao = pd.DataFrame.from_dict(self.questionarios['Alfabetização'], orient='index', columns=['Resposta_Alfabetizacao']).T
        data_atual = datetime.now()
        df_alfabetizacao['data'] = data_atual

        df_alfabetizacao_renomeado = self.rename_columns(df_alfabetizacao, mapper_alfabetizacao)
        df_alfabetizacao_renomeado['pontuacao'] = df_alfabetizacao_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_alfabetizacao_renomeado['nivel_risco'] = df_alfabetizacao_renomeado['pontuacao'].apply(self.calcular_nivel_risco)

        alfabetizacao_table = AlfabetizacaoTable(engine)
        alfabetizacao_table.add_data(df_alfabetizacao_renomeado)

        return df_alfabetizacao_renomeado, True
