from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IDA_em(Base):
    __tablename__ = 'IDA_em'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    lingua_portuguesa = Column(Float)
    lingua_estrangeira = Column(Float)
    artes = Column(Float)
    matematica = Column(Float)
    fisica = Column(Float)
    quimica = Column(Float)
    biologia = Column(Float)
    astronomia = Column(Float)
    historia = Column(Float)
    geografia = Column(Float)
    sociologia = Column(Float)
    filosofia = Column(Float)
    educacao_fisica = Column(Float)
    data = Column(DateTime)

class IDA_emTable:
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
                    'lingua_estrangeira': row['lingua_estrangeira'],
                    'artes': row['artes'],
                    'matematica': row['matematica'],
                    'fisica': row['fisica'],
                    'quimica': row['quimica'],
                    'biologia': row['biologia'],
                    'astronomia': row['astronomia'],
                    'historia': row['historia'],
                    'geografia': row['geografia'],
                    'sociologia': row['sociologia'],
                    'filosofia': row['filosofia'],
                    'educacao_fisica': row['educacao_fisica'],
                    'data': row['data']
                }
                ida = IDA_em(**data)
                session.add(ida)
            session.commit()
            # print("Dados de IDA_em adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados de IDA_em: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela IDA.EnsinoMedio
    #     '''
    #     fundamental_table = IDA_emTable(self.engine)
    #     fundamental_table.create_table()
    #     df_fundamental_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "lingua_portuguesa": [8.5],
    #         "lingua_estrangeira": [8.5],
    #         "artes": [8.5],
    #         "matematica": [8.5],
    #         "fisica": [8.5],
    #         "quimica": [8.5],
    #         "biologia": [8.5],
    #         "astronomia": [8.5],
    #         "historia": [8.5],
    #         "geografia": [8.5],
    #         "sociologia": [8.5],
    #         "filosofia": [8.5],
    #         "educacao_fisica": [8.5],
    #         "data": [datetime.now()]
    #     })
    #     fundamental_table.add_data(df_fundamental_renomeado)
    #     print(f"Tabela 'IDA.EnsinoMedio' criada no banco de dados. Inseridos '{len(df_fundamental_renomeado)}' registros")