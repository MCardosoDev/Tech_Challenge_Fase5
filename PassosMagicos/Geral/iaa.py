from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IAA(Base):
    __tablename__ = 'IAA'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    faz_perguntas_tira_duvidas = Column(String)
    busca_feedback_utiliza_aprimorar_aprendizado = Column(String)
    reconhece_pontos_fortes_areas_desenvolvimento = Column(String)
    sente_satisfeito_progresso_desenvolvimento = Column(String)
    acredita_aprendendo_tornando_mais_capaz = Column(String)
    reconhece_importancia_educacao_para_futuro = Column(String)
    sente_motivado_continuar_aprendendo_desafiando = Column(String)
    organiza_gerencia_tempo_forma_eficiente = Column(String)
    busca_conectar_outros_alunos_profissionais = Column(String)
    tem_iniciativa_autonomia_estudos = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class IAATable:
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
                geral = IAA(**row)
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
    #     Código para gerar a tabela IAA
    #     '''
    #     geral_table = IAATable(self.engine)
    #     geral_table.create_table()
    #     df_geral_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "faz_perguntas_tira_duvidas": ["Nunca"],
    #         "busca_feedback_utiliza_aprimorar_aprendizado": ["Sempre"],
    #         "reconhece_pontos_fortes_areas_desenvolvimento": ["Nunca"],
    #         "sente_satisfeito_progresso_desenvolvimento": ["Raramente"],
    #         "acredita_aprendendo_tornando_mais_capaz": ["Raramente"],
    #         "reconhece_importancia_educacao_para_futuro": ["Às vezes"],
    #         "sente_motivado_continuar_aprendendo_desafiando": ["Sempre"],
    #         "organiza_gerencia_tempo_forma_eficiente": ["Às vezes"],
    #         "busca_conectar_outros_alunos_profissionais": ["Frequentemente"],
    #         "tem_iniciativa_autonomia_estudos": ["Frequentemente"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     geral_table.add_data(df_geral_renomeado)
    #     print(f"Tabela 'IAA' criada no banco de dados. Inseridos '{len(df_geral_renomeado)}' registros")