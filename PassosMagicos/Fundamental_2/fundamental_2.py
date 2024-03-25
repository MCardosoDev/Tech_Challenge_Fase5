from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class Fundamental2(Base):
    __tablename__ = 'Fundamental2'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    domina_conceitos_matematicos = Column(String)
    resolve_problemas_complexos = Column(String)
    interpreta_textos_criticamente = Column(String)
    interesse_conhecimento_ciencias = Column(String)
    desenvolve_senso_critico_historia = Column(String)
    conhecimento_paises_regioes = Column(String)
    participa_atividades_esportivas = Column(String)
    autoconhecimento_autoconfianca_resiliencia = Column(String)
    interesse_cultura_inglesa = Column(String)
    produz_conteudo_digital_etico_responsavel = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class Fundamental2Table:
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
                fundamental_2 = Fundamental2(**row)
                session.add(fundamental_2)
            session.commit()
            # print("Dados adicionados com sucesso.")
        except Exception as e:
            # print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela Fundamental2
    #     '''
    #     fundamental_2_table = Fundamental2Table(self.engine)
    #     fundamental_2_table.create_table()
    #     df_fundamental_2_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "domina_conceitos_matematicos": ["Nunca"],
    #         "resolve_problemas_complexos": ["Às vezes"],
    #         "interpreta_textos_criticamente": ["Nunca"],
    #         "interesse_conhecimento_ciencias": ["Às vezes"],
    #         "desenvolve_senso_critico_historia": ["Sempre"],
    #         "conhecimento_paises_regioes": ["Sempre"],
    #         "participa_atividades_esportivas": ["Frequentemente"],
    #         "autoconhecimento_autoconfianca_resiliencia": ["Raramente"],
    #         "interesse_cultura_inglesa": ["Frequentemente"],
    #         "produz_conteudo_digital_etico_responsavel": ["Raramente"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     fundamental_2_table.add_data(df_fundamental_2_renomeado)
    #     print(f"Tabela 'fundamental_2' criada no banco de dados. Inseridos '{len(df_fundamental_2_renomeado)}' registros")
