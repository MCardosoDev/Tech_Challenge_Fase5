from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class Fundamental(Base):
    __tablename__ = 'Fundamental'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    resolve_problemas_matematicos = Column(String)
    interpreta_textos = Column(String)
    formula_perguntas_naturais = Column(String)
    compreende_relacao_temporal = Column(String)
    compreende_relacao_meio_ambiente = Column(String)
    demonstra_criatividade_arte = Column(String)
    desenvolve_habilidades_motoras = Column(String)
    comunica_eficazmente = Column(String)
    reconhece_pronuncia_ingles = Column(String)
    utiliza_tecnologia = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class FundamentalTable:
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
                fundamental = Fundamental(**row)
                session.add(fundamental)
            session.commit()
            # print("Dados adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela Fundamental
    #     '''
    #     fundamental_table = FundamentalTable(self.engine)
    #     fundamental_table.create_table()
    #     df_fundamental_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "resolve_problemas_matematicos": ["Sempre"],
    #         "interpreta_textos": ["Nunca"],
    #         "formula_perguntas_naturais": ["Frequentemente"],
    #         "compreende_relacao_temporal": ["Sempre"],
    #         "compreende_relacao_meio_ambiente": ["Nunca"],
    #         "demonstra_criatividade_arte": ["Frequentemente"],
    #         "desenvolve_habilidades_motoras": ["Raramente"],
    #         "comunica_eficazmente": ["Raramente"],
    #         "reconhece_pronuncia_ingles": ["Às vezes"],
    #         "utiliza_tecnologia": ["Raramente"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     fundamental_table.add_data(df_fundamental_renomeado)
    #     print(f"Tabela 'Fundamental' criada no banco de dados. Inseridos '{len(df_fundamental_renomeado)}' registros")