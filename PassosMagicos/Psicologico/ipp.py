from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IPP(Base):
    __tablename__ = 'IPP'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    participa_ativamente_responde_perguntas_clareza = Column(String)
    relaciona_respeitosamente_cooperativamente_colegas = Column(String)
    dificuldades_comunicacao_oral_escrita = Column(String)
    demonstra_coordenacao_destreza_atividades = Column(String)
    demonstra_empatia_respeito_outros = Column(String)
    reconhece_pontos_fortes_areas_desenvolvimento = Column(String)
    consegue_concentrar_tarefas_lembrar_informacoes_resolver_problemas = Column(String)
    habilidades_academicas_leitura_escrita_calculos_fluencia_compreensao = Column(String)
    saude_emocional_aluno_feliz_seguro_escola_casa = Column(String)
    acesso_recursos_socioeconomicos_adequados_desenvolvimento = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class IPPTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_data(self, df):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        data = df.to_dict(orient='records')

        try:
            for row in data:
                geral = IPP(**row)
                session.add(geral)
            session.commit()
            # print("Dados adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela IPP
    #     '''
    #     geral_table = IPPTable(self.engine)
    #     geral_table.create_table()
    #     df_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "participa_ativamente_responde_perguntas_clareza": ["Sim"],
    #         "relaciona_respeitosamente_cooperativamente_colegas": ["Não"],
    #         "dificuldades_comunicacao_oral_escrita": ["Sim"],
    #         "demonstra_coordenacao_destreza_atividades": ["Não"],
    #         "demonstra_empatia_respeito_outros": ["Sim"],
    #         "reconhece_pontos_fortes_areas_desenvolvimento": ["Não"],
    #         "consegue_concentrar_tarefas_lembrar_informacoes_resolver_problemas": ["Sim"],
    #         "habilidades_academicas_leitura_escrita_calculos_fluencia_compreensao": ["Não"],
    #         "saude_emocional_aluno_feliz_seguro_escola_casa": ["Sim"],
    #         "acesso_recursos_socioeconomicos_adequados_desenvolvimento": ["Não"],
    #         "data": [datetime.now()],
    #         "pontuacao": [3],
    #         "nivel_risco": ["Alto Risco"]
    #     })
    #     geral_table.add_data(df_renomeado)
    #     print(f"Tabela 'IPP' criada no banco de dados. Inseridos '{len(df_renomeado)}' registros")