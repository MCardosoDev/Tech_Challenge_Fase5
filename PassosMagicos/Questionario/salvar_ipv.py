import pandas as pd
from datetime import datetime
from Psicologico.ipv import IPVTable
from Infra.database import DatabaseConnection

class QuestionarioIPVSalvo:
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
            "Autoconhecimento: Você sabe identificar seus principais interesses, habilidades e paixões?": "sabe_identificar_interesses_habilidades_paixoes",
            "Autonomia e Responsabilidade: Você assume total responsabilidade pelo seu processo de aprendizado?": "assume_responsabilidade_processo_aprendizado",
            "Motivação e Engajamento: Você se sente entusiasmado e motivado com as atividades de aprendizagem?": "sente_entusiasmado_motivado_atividades_aprendizagem",
            "Experimentação e Adaptabilidade: Você já experimentou diferentes métodos de aprendizado para encontrar o que funciona melhor para você?": "experimentou_diferentes_metodos_aprendizado_encontrar_melhor",
            "Aprendizagem Ativa e Reflexiva: Você participa ativamente das aulas e busca compreender os conceitos por trás do que está aprendendo?": "participa_ativamente_aulas_busca_compreender_conceitos",
            "Resiliência e Persistência: Você aprende com seus erros e se esforça para superar as dificuldades com persistência?": "aprende_com_erros_esforca_superar_dificuldades_persistencia",
            "Planejamento e Metas: Você define metas claras e de longo prazo para sua trajetória educacional?": "define_metas_claras_longo_prazo_trajetoria_educacional",
            "Busca por Recursos e Apoio: Você busca ajuda de professores, colegas, mentores ou outros profissionais quando precisa?": "busca_ajuda_professores_colegas_mentores_profissionais",
            "Visão de Futuro e Propósito: Você consegue visualizar como a educação te ajudará a alcançar seus sonhos e objetivos de vida?": "visualiza_como_educacao_ajudara_alcancar_sonhos_objetivos_vida",
            "Aprendizagem Contínua: Você se considera um aprendiz constante, sempre buscando novas informações e habilidades?": "considera_aprendiz_constante_busca_novas_informacoes_habilidades"
        }
        
        df = pd.DataFrame.from_dict(self.questionarios['IPV'], orient='index', columns=['Resposta_IPV']).T
        
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_ipp)
        df_renomeado['pontuacao'] = df_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_renomeado['nivel_risco'] = df_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental_table = IPVTable(engine)
        fundamental_table.add_data(df_renomeado)

        return True
