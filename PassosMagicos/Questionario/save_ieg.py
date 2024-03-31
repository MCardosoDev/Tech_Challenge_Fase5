import pandas as pd
from datetime import datetime
from Geral.ieg import IEGTable
from Infra.database import DatabaseConnection

class QuestionarioIEGSalvo:
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

        mapper_ieg = {
            "Matrícula": "matricula",
            "O aluno demonstra interesse e entusiasmo durante as aulas?": "interesse_entusiasmo_aulas",
            "Ele participa ativamente das discussões e atividades propostas?": "participa_ativamente_discussoes_atividades",
            "Ele faz perguntas e busca tirar dúvidas quando necessário?": "faz_perguntas_busca_tirar_duvidas",
            "Ele demonstra iniciativa em contribuir com a turma?": "iniciativa_contribuir_turma",
            "O aluno consegue acompanhar as explicações e responder às perguntas com clareza?": "acompanha_explicacoes_responde_clareza",
            "Ele demonstra compreensão dos conceitos e conteúdos abordados?": "compreensao_conceitos_conteudos",
            "Ele consegue aplicar o conhecimento adquirido em diferentes situações?": "aplicar_conhecimento_diferentes_situacoes",
            "Ele identifica suas dificuldades e busca formas de superá-las?": "identifica_dificuldades_busca_superar",
            "O aluno demonstra progresso em relação ao seu nível inicial de conhecimento?": "progresso_relacao_nivel_inicial",
            "Ele se esforça para melhorar suas habilidades e desempenho?": "esforca_melhorar_habilidades_desempenho"
        }
        df = pd.DataFrame.from_dict(self.questionarios, orient='index').T
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_ieg)
        df_renomeado['pontuacao'] = df_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_renomeado['nivel_risco'] = df_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental_table = IEGTable(engine)
        fundamental_table.add_data(df_renomeado)

        return True