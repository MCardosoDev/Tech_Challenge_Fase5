import pandas as pd
from datetime import datetime
from Geral.iaa import IAATable
from Infra.database import DatabaseConnection

class QuestionarioIAASalvo:
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

        mapper_geral = {
            "Matrícula": "matricula",
            "Ele faz perguntas e busca tirar dúvidas quando necessário?": "faz_perguntas_tira_duvidas",
            "Você busca feedback e utiliza-o para aprimorar seu aprendizado?": "busca_feedback_utiliza_aprimorar_aprendizado",
            "Você reconhece seus pontos fortes e áreas de desenvolvimento?": "reconhece_pontos_fortes_areas_desenvolvimento",
            "Você se sente satisfeito com seu progresso e desenvolvimento?": "sente_satisfeito_progresso_desenvolvimento",
            "Você acredita que está aprendendo e se tornando mais capaz?": "acredita_aprendendo_tornando_mais_capaz",
            "Você reconhece a importância da educação para seu futuro?": "reconhece_importancia_educacao_para_futuro",
            "Você se sente motivado a continuar aprendendo e se desafiando?": "sente_motivado_continuar_aprendendo_desafiando",
            "Você organiza e gerencia seu tempo de forma eficiente?": "organiza_gerencia_tempo_forma_eficiente",
            "Você busca se conectar com outros alunos e profissionais da área?": "busca_conectar_outros_alunos_profissionais",
            "Você têm iniciativa e autonomia em seus estudos?": "tem_iniciativa_autonomia_estudos"
        }

        df = pd.DataFrame.from_dict(self.questionarios['IAA'], orient='index', columns=['Resposta_IAA']).T
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_geral)
        df_renomeado['pontuacao'] = df_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_renomeado['nivel_risco'] = df_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental_table = IAATable(engine)
        fundamental_table.add_data(df_renomeado)

        return df_renomeado, True