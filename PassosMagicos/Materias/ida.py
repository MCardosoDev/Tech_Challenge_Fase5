from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IDA(Base):
    __tablename__ = 'IDA'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    lingua_portuguesa = Column(Float)
    matematica = Column(Float)
    ciencias = Column(Float)
    artes = Column(Float)
    educacao_fisica = Column(Float)
    data = Column(DateTime)

class IDATable:
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
                    'artes': row['artes'],
                    'educacao_fisica': row['educacao_fisica'],
                    'data': row['data']
                }
                ida = IDA(**data)
                session.add(ida)
            session.commit()
            # print("Dados de IDA adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados de IDA: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela IDA.Alfabetizacao
    #     '''
    #     alfabetizacao_table = IDATable(self.engine)
    #     alfabetizacao_table.create_table()
    #     df_alfabetizacao_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "lingua_portuguesa": [8.5],
    #         "matematica": [7.0],
    #         "ciencias": [9.2],
    #         "artes": [6.8],
    #         "educacao_fisica": [8.0],
    #         "data": [datetime.now()]
    #     })
    #     alfabetizacao_table.add_data(df_alfabetizacao_renomeado)
    #     print(f"Tabela 'IDA.Alfabetizacao' criada no banco de dados. Inseridos '{len(df_alfabetizacao_renomeado)}' registros")