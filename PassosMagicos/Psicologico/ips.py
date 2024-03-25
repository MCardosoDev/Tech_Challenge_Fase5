from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IPS(Base):
    __tablename__ = 'IPS'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    bom_relacionamento_familiares = Column(String)
    amigos_com_quem_contar = Column(String)
    sente_bem_consigo_vida = Column(String)
    acredita_alcancar_objetivos = Column(String)
    acredita_aprendendo_progredindo_estudos = Column(String)
    tem_plano_alcancar_objetivos = Column(String)
    alimenta_saudavel_pratica_atividades_fisicas = Column(String)
    nao_pressionado_usar_drogas_bebidas_alcoolicas = Column(String)
    se_sente_seguro_casa_escola_comunidade = Column(String)
    sabe_buscar_ajuda_quando_precisa = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class IPSTable:
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
                geral = IPS(**row)
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
    #     Código para gerar a tabela IPS
    #     '''
    #     geral_table = IPSTable(self.engine)
    #     geral_table.create_table()
    #     df_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "bom_relacionamento_familiares": ["Sim"],
    #         "amigos_com_quem_contar": ["Não"],
    #         "sente_bem_consigo_vida": ["Sim"],
    #         "acredita_alcancar_objetivos": ["Não"],
    #         "acredita_aprendendo_progredindo_estudos": ["Sim"],
    #         "tem_plano_alcancar_objetivos": ["Não"],
    #         "alimenta_saudavel_pratica_atividades_fisicas": ["Sim"],
    #         "nao_pressionado_usar_drogas_bebidas_alcoolicas": ["Sim"],
    #         "se_sente_seguro_casa_escola_comunidade": ["Não"],
    #         "sabe_buscar_ajuda_quando_precisa": ["Sim"],
    #         "data": [datetime.now()],
    #         "pontuacao": [3],
    #         "nivel_risco": ["Alto Risco"]
    #     })
    #     geral_table.add_data(df_renomeado)
    #     print(f"Tabela 'IPS' criada no banco de dados. Inseridos '{len(df_renomeado)}' registros")