from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import pandas as pd
from datetime import datetime

Base = declarative_base()

class IEG(Base):
    __tablename__ = 'IEG'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    interesse_entusiasmo_aulas = Column(String)
    participa_ativamente_discussoes_atividades = Column(String)
    faz_perguntas_busca_tirar_duvidas = Column(String)
    iniciativa_contribuir_turma = Column(String)
    acompanha_explicacoes_responde_clareza = Column(String)
    compreensao_conceitos_conteudos = Column(String)
    aplicar_conhecimento_diferentes_situacoes = Column(String)
    identifica_dificuldades_busca_superar = Column(String)
    progresso_relacao_nivel_inicial = Column(String)
    esforca_melhorar_habilidades_desempenho = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class IEGTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def add_data(self, df):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        data = df.to_dict(orient='records')
        print(data)
        try:
            for row in data:
                geral = IEG(**row)
                session.add(geral)
            session.commit()
            print("Dados adicionados com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar dados: {e}")
            session.rollback()
        finally:
            session.close()

    # def initTableAlf(self):
    #     '''
    #     Código para gerar a tabela IEG
    #     '''
    #     geral_table = IEGTable(self.engine)
    #     geral_table.create_table()
    #     df_geral_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "interesse_entusiasmo_aulas": ["Nunca"],
    #         "participa_ativamente_discussoes_atividades": ["Às vezes"],
    #         "faz_perguntas_busca_tirar_duvidas": ["Nunca"],
    #         "iniciativa_contribuir_turma": ["Às vezes"],
    #         "acompanha_explicacoes_responde_clareza": ["Frequentemente"],
    #         "compreensao_conceitos_conteudos": ["Frequentemente"],
    #         "aplicar_conhecimento_diferentes_situacoes": ["Nunca"],
    #         "identifica_dificuldades_busca_superar": ["Raramente"],
    #         "progresso_relacao_nivel_inicial": ["Às vezes"],
    #         "esforca_melhorar_habilidades_desempenho": ["Raramente"],
    #         "data": [datetime.now()],
    #         "pontuacao": [10],
    #         "nivel_risco": ["Muito Elevado"]
    #     })
    #     geral_table.add_data(df_geral_renomeado)
    #     print(f"Tabela 'IEG' criada no banco de dados. Inseridos '{len(df_geral_renomeado)}' registros")