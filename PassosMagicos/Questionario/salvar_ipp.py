import pandas as pd
from datetime import datetime
from Psicologico.ipp import IPPTable
from Infra.database import DatabaseConnection

class QuestionarioIPPSalvo:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def rename_columns(self, df, mapper):
        return df.rename(columns=mapper)

    def calcular_pontuacao(self, row):
        pontuacao = 0
        for answer in row.values:
            if answer == "Sim":
                pontuacao += 1
            elif answer == "Não":
                pontuacao += 0
        return pontuacao

    def calcular_nivel_risco(self, pontuacao):
        if pontuacao >= 0 and pontuacao <= 3:
            return "Alto Risco"
        elif pontuacao >= 4 and pontuacao <= 7:
            return "Moderado Risco"
        elif pontuacao >= 8 and pontuacao <= 10:
            return "Baixo Risco"
        else:
            return "Valor de pontuação inválido"
    
    def save(self):
        db_connection = DatabaseConnection('passos_magicos')
        engine = db_connection.get_engine()

        mapper_ipp = {
            "Matrícula": "matricula",
            "Aprendizagem: Ele participa ativamente das aulas e responde às perguntas com clareza?": "participa_ativamente_responde_perguntas_clareza",
            "Comportamento: Ele se relaciona com os colegas de forma respeitosa e cooperativa?": "relaciona_respeitosamente_cooperativamente_colegas",
            "Comunicação: Ele apresenta dificuldades na comunicação oral ou escrita?": "dificuldades_comunicacao_oral_escrita",
            "Habilidades Motoras: Ele demonstra coordenação motora e destreza nas atividades?": "demonstra_coordenacao_destreza_atividades",
            "Desenvolvimento Social: Ele demonstra empatia e respeito pelos outros?": "demonstra_empatia_respeito_outros",
            "Autoestima: Ele reconhece seus pontos fortes e áreas de desenvolvimento?": "reconhece_pontos_fortes_areas_desenvolvimento",
            "Funções Cognitivas: Ele consegue se concentrar nas tarefas, lembrar de informações e resolver problemas?": "consegue_concentrar_tarefas_lembrar_informacoes_resolver_problemas",
            "Habilidades Acadêmicas: O aluno lê, escreve e faz cálculos matemáticos com fluência e compreensão?": "habilidades_academicas_leitura_escrita_calculos_fluencia_compreensao",
            "Saúde Emocional: O aluno se sente feliz e seguro na escola e em casa?": "saude_emocional_aluno_feliz_seguro_escola_casa",
            "Condições Socioeconômicas: O aluno tem acesso a recursos materiais e sociais adequados para seu desenvolvimento?": "acesso_recursos_socioeconomicos_adequados_desenvolvimento"
        }

        df = pd.DataFrame.from_dict(self.questionarios['IPP'], orient='index', columns=['Resposta_IPP']).T
        
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_ipp)
        df_renomeado['pontuacao'] = df_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_renomeado['nivel_risco'] = df_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental_table = IPPTable(engine)
        fundamental_table.add_data(df_renomeado)

        return df_renomeado, True
