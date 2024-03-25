#%%
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class EnsinoMedio(Base):
    __tablename__ = 'EnsinoMedio'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    utiliza_metodos_matematicos = Column(String)
    utiliza_linguagem_matematica = Column(String)
    analisa_criticamente_interpretacoes_historia = Column(String)
    compreende_globalizacao_impactos = Column(String)
    formula_defende_argumentos = Column(String)
    analisa_criticamente_problemas_sociais = Column(String)
    domina_conceitos_fisica = Column(String)
    analisa_criticamente_impactos_quimica = Column(String)
    domina_conceitos_biologia = Column(String)
    comunica_eficazmente_diferentes_situacoes = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class EnsinoMedioTable:
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
                ensino_medio = EnsinoMedio(**row)
                session.add(ensino_medio)
            session.commit()
            # print("Dados adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela EnsinoMedio
    #     '''
    #     ensino_medio_table = EnsinoMedioTable(self.engine)
    #     ensino_medio_table.create_table()
    #     df_ensino_medio_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "utiliza_metodos_matematicos": ["Nunca"],
    #         "utiliza_linguagem_matematica": ["Às vezes"],
    #         "analisa_criticamente_interpretacoes_historia": ["Às vezes"],
    #         "compreende_globalizacao_impactos": ["Nunca"],
    #         "formula_defende_argumentos": ["Raramente"],
    #         "analisa_criticamente_problemas_sociais": ["Sempre"],
    #         "domina_conceitos_fisica": ["Frequentemente"],
    #         "analisa_criticamente_impactos_quimica": ["Raramente"],
    #         "domina_conceitos_biologia": ["Sempre"],
    #         "comunica_eficazmente_diferentes_situacoes": ["Nunca"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     ensino_medio_table.add_data(df_ensino_medio_renomeado)
    #     print(f"Tabela 'EnsinoMedio' criada no banco de dados. Inseridos '{len(df_ensino_medio_renomeado)}' registros")
