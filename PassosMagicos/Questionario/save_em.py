import pandas as pd
from datetime import datetime
from EnsinoMedio.ensino_medio import EnsinoMedioTable
from Infra.database import DatabaseConnection

class QuestionarioEMSalvo:
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

        mapper_ensino_medio = {
            "Matrícula": "matricula",
            "Ele utiliza diferentes métodos e estratégias para resolver problemas matemáticos de forma eficiente?": "utiliza_metodos_matematicos",
            "Ele utiliza linguagem matemática adequada e argumenta de forma lógica?": "utiliza_linguagem_matematica",
            "Ele é capaz de analisar criticamente diferentes interpretações da história?": "analisa_criticamente_interpretacoes_historia",
            "O aluno compreende os principais processos de globalização e seus impactos na sociedade?": "compreende_globalizacao_impactos",
            "Ele é capaz de formular e defender argumentos de forma lógica e fundamentada?": "formula_defende_argumentos",
            "Ele é capaz de analisar criticamente os problemas sociais e propor soluções?": "analisa_criticamente_problemas_sociais",
            "O aluno domina os principais conceitos da física e suas aplicações no mundo real?": "domina_conceitos_fisica",
            "Ele é capaz de analisar criticamente os impactos da química na sociedade e no meio ambiente?": "analisa_criticamente_impactos_quimica",
            "O aluno domina os principais conceitos da biologia e as relações entre os seres vivos?": "domina_conceitos_biologia",
            "Ele é capaz de se comunicar de forma eficaz em diferentes situações?": "comunica_eficazmente_diferentes_situacoes"
        }

        df_ensino_medio = pd.DataFrame.from_dict(self.questionarios['Ensino Médio'], orient='index', columns=['Resposta_Ensino_Medio']).T
        data_atual = datetime.now()
        df_ensino_medio['data'] = data_atual

        df_ensino_medio_renomeado = self.rename_columns(df_ensino_medio, mapper_ensino_medio)
        df_ensino_medio_renomeado['pontuacao'] = df_ensino_medio_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_ensino_medio_renomeado['nivel_risco'] = df_ensino_medio_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        ensino_medio_table = EnsinoMedioTable(engine)
        ensino_medio_table.add_data(df_ensino_medio_renomeado)

        return df_ensino_medio_renomeado, True