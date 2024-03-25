from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IDA_f(Base):
    __tablename__ = 'IDA_f'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    lingua_portuguesa = Column(Float)
    matematica = Column(Float)
    ciencias = Column(Float)
    historia = Column(Float)
    geografia = Column(Float)
    artes = Column(Float)
    educacao_fisica = Column(Float)
    ingles = Column(Float)
    data = Column(DateTime)

class IDA_fTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_data(self, df):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            for _, row in df.iterrows():
                data = {
                    'matricula': row['matricula'],
                    'lingua_portuguesa': row['lingua_portuguesa'],
                    'matematica': row['matematica'],
                    'ciencias': row['ciencias'],
                    'historia': row['historia'],
                    'geografia': row['geografia'],
                    'artes': row['artes'],
                    'educacao_fisica': row['educacao_fisica'],
                    'ingles': row['ingles'],
                    'data': row['data']
                }
                ida = IDA_f(**data)
                session.add(ida)
            session.commit()
            # print("Dados de IDA_f adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados de IDA_f: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela IDA.Fundamental
    #     '''
    #     fundamental_table = IDA_fTable(self.engine)
    #     fundamental_table.create_table()
    #     df_fundamental_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "lingua_portuguesa": [8.5],
    #         "matematica": [7.0],
    #         "ciencias": [9.2],
    #         "historia": [8.5],
    #         "geografia": [8.5],
    #         "artes": [6.8],
    #         "educacao_fisica": [8.0],
    #         "ingles": [8.5],
    #         "data": [datetime.now()]
    #     })
    #     fundamental_table.add_data(df_fundamental_renomeado)
    #     print(f"Tabela 'IDA.Fundamental' criada no banco de dados. Inseridos '{len(df_fundamental_renomeado)}' registros")