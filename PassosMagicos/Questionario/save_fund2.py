import pandas as pd
from datetime import datetime
from Fundamental_2.fundamental_2 import Fundamental2Table
from Infra.database import DatabaseConnection

class QuestionarioFund2Salvo:
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

        mapper_fundamental_2 = {
            "Matrícula": "matricula",
            "Domina os conceitos matemáticos básicos de frações, decimais e porcentagens?": "domina_conceitos_matematicos",
            "Resolve problemas matemáticos mais complexos envolvendo diferentes operações?": "resolve_problemas_complexos",
            "Interpreta e analisa criticamente textos de diferentes gêneros literários?": "interpreta_textos_criticamente",
            "Demonstra interesse e conhecimento sobre diferentes áreas da ciência (física, química, biologia)?": "interesse_conhecimento_ciencias",
            "Desenvolve senso crítico para analisar diferentes interpretações da história?": "desenvolve_senso_critico_historia",
            "Demonstra conhecimento sobre os principais países e regiões do mundo?": "conhecimento_paises_regioes",
            "Participa de diferentes atividades esportivas com cooperação e respeito?": "participa_atividades_esportivas",
            "Demonstra autoconhecimento, autoconfiança e resiliência?": "autoconhecimento_autoconfianca_resiliencia",
            "Demonstra interesse pela cultura dos países de língua inglesa?": "interesse_cultura_inglesa",
            "Produz conteúdo digital de forma ética e responsável?": "produz_conteudo_digital_etico_responsavel"
        }

        df_fundamental2 = pd.DataFrame.from_dict(self.questionarios['Fundamental 2'], orient='index', columns=['Resposta_Fundamental2']).T
        data_atual = datetime.now()
        df_fundamental2['data'] = data_atual

        df_fundamental2_renomeado = self.rename_columns(df_fundamental2, mapper_fundamental_2)
        df_fundamental2_renomeado['pontuacao'] = df_fundamental2_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_fundamental2_renomeado['nivel_risco'] = df_fundamental2_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental2_table = Fundamental2Table(engine)
        fundamental2_table.add_data(df_fundamental2_renomeado)

        return True