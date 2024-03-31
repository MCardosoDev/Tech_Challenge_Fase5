import pandas as pd
from datetime import datetime
from Fundamental.fundamental import FundamentalTable
from Infra.database import DatabaseConnection

class QuestionarioFundSalvo:
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

        mapper_fundamental = {
            "Matrícula": "matricula",
            "A criança consegue resolver problemas matemáticos simples envolvendo adição, subtração, multiplicação e divisão?": "resolve_problemas_matematicos",
            "Ela consegue interpretar e analisar textos de diferentes tipos, como contos, notícias e poemas?": "interpreta_textos",
            "Ela formula perguntas e hipóteses sobre o mundo natural?": "formula_perguntas_naturais",
            "Ela compreende a relação entre passado, presente e futuro?": "compreende_relacao_temporal",
            "Ela compreende a relação entre o homem e o meio ambiente?": "compreende_relacao_meio_ambiente",
            "A criança demonstra criatividade e expressividade nas diferentes formas de arte?": "demonstra_criatividade_arte",
            "Ela desenvolve suas habilidades motoras e coordenação corporal?": "desenvolve_habilidades_motoras",
            "Ela se comunica de forma eficaz com os outros?": "comunica_eficazmente",
            "Ela reconhece e pronuncia palavras e frases simples em inglês?": "reconhece_pronuncia_ingles",
            "Ela utiliza a tecnologia para pesquisa, comunicação e aprendizagem?": "utiliza_tecnologia"
        }

        df_fundamental = pd.DataFrame.from_dict(self.questionarios['Fundamental'], orient='index', columns=['Resposta_Fundamental']).T
        data_atual = datetime.now()
        df_fundamental['data'] = data_atual

        df_fundamental_renomeado = self.rename_columns(df_fundamental, mapper_fundamental)
        df_fundamental_renomeado['pontuacao'] = df_fundamental_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_fundamental_renomeado['nivel_risco'] = df_fundamental_renomeado['pontuacao'].apply(self.calcular_nivel_risco)

        fundamental_table = FundamentalTable(engine)
        fundamental_table.add_data(df_fundamental_renomeado)
    
        return True