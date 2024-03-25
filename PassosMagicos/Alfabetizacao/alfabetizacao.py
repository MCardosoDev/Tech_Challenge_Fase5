from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class Alfabetizacao(Base):
    __tablename__ = 'Alfabetizacao'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    reconhece_letras = Column(String)
    ler_palavras_simples = Column(String)
    escrever_palavras_simples = Column(String)
    segmentar_palavras = Column(String)
    ler_fluente = Column(String)
    responder_perguntas_leitura = Column(String)
    conhece_significado_palavras = Column(String)
    demonstra_interesse = Column(String)
    participa_ativamente = Column(String)
    progresso_habilidades = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class AlfabetizacaoTable:
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
                alfabetizacao = Alfabetizacao(**row)
                session.add(alfabetizacao)
            session.commit()
            # print("Dados adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela Alfabetizacao
    #     '''
    #     alfabetizacao_table = AlfabetizacaoTable(self.engine)
    #     alfabetizacao_table.create_table()
    #     df_alfabetizacao_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "reconhece_letras": ["Nunca"],
    #         "ler_palavras_simples": ["Raramente"],
    #         "escrever_palavras_simples": ["Sempre"],
    #         "segmentar_palavras": ["Sempre"],
    #         "ler_fluente": ["Frequentemente"],
    #         "responder_perguntas_leitura": ["Frequentemente"],
    #         "conhece_significado_palavras": ["Às vezes"],
    #         "demonstra_interesse": ["Frequentemente"],
    #         "participa_ativamente": ["Às vezes"],
    #         "progresso_habilidades": ["Às vezes"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     alfabetizacao_table.add_data(df_alfabetizacao_renomeado)
    #     print(f"Tabela 'Alfabetizacao' criada no banco de dados. Inseridos '{len(df_alfabetizacao_renomeado)}' registros")
