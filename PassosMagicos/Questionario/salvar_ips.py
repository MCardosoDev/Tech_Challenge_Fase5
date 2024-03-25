import pandas as pd
from datetime import datetime
from Psicologico.ips import IPSTable
from Infra.database import DatabaseConnection

class QuestionarioIPSSalvo:
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

        mapper_ips = {
            "Matrícula": "matricula",
            "Ambiente Familiar: Você tem um bom relacionamento com seus familiares?": "bom_relacionamento_familiares",
            "Vida Social: Você tem amigos com quem você pode contar?": "amigos_com_quem_contar",
            "Saúde Mental: Você se sente bem consigo mesmo e com sua vida?": "sente_bem_consigo_vida",
            "Autoestima: Você acredita que é capaz de alcançar seus objetivos?": "acredita_alcancar_objetivos",
            "Desempenho Escolar: Você acredita que está aprendendo e progredindo em seus estudos?": "acredita_aprendendo_progredindo_estudos",
            "Planos para o Futuro: Você tem um plano para alcançar seus objetivos?": "tem_plano_alcancar_objetivos",
            "Hábitos de Vida: Você se alimenta de forma saudável e pratica atividades físicas regularmente?": "alimenta_saudavel_pratica_atividades_fisicas",
            "Uso de Substâncias: Você não se sente pressionado a usar drogas ou bebidas alcoólicas?": "nao_pressionado_usar_drogas_bebidas_alcoolicas",
            "Violência: Você se sente seguro em casa, na escola e na comunidade?": "se_sente_seguro_casa_escola_comunidade",
            "Rede de Apoio: Você sabe como buscar ajuda quando precisa?": "sabe_buscar_ajuda_quando_precisa"
        }

        df = pd.DataFrame.from_dict(self.questionarios['IPS'], orient='index', columns=['Resposta_IPS']).T
        
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_ips)
        df_renomeado['pontuacao'] = df_renomeado.apply(self.calcular_pontuacao, axis=1)
        df_renomeado['nivel_risco'] = df_renomeado['pontuacao'].apply(self.calcular_nivel_risco)
        
        fundamental_table = IPSTable(engine)
        fundamental_table.add_data(df_renomeado)

        return df_renomeado, True
