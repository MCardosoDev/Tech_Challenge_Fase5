from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

Base = declarative_base()

class IPV(Base):
    __tablename__ = 'IPV'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    sabe_identificar_interesses_habilidades_paixoes = Column(String)
    assume_responsabilidade_processo_aprendizado = Column(String)
    sente_entusiasmado_motivado_atividades_aprendizagem = Column(String)
    experimentou_diferentes_metodos_aprendizado_encontrar_melhor = Column(String)
    participa_ativamente_aulas_busca_compreender_conceitos = Column(String)
    aprende_com_erros_esforca_superar_dificuldades_persistencia = Column(String)
    define_metas_claras_longo_prazo_trajetoria_educacional = Column(String)
    busca_ajuda_professores_colegas_mentores_profissionais = Column(String)
    visualiza_como_educacao_ajudara_alcancar_sonhos_objetivos_vida = Column(String)
    considera_aprendiz_constante_busca_novas_informacoes_habilidades = Column(String)
    data = Column(DateTime)
    pontuacao = Column(Integer)
    nivel_risco = Column(String)

class IPVTable:
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
                geral = IPV(**row)
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
    #     Código para gerar a tabela IPV
    #     '''
    #     geral_table = IPVTable(self.engine)
    #     geral_table.create_table()
    #     df_renomeado = pd.DataFrame({
    #         "matricula": ["M000000"],
    #         "sabe_identificar_interesses_habilidades_paixoes": ["Não"],
    #         "assume_responsabilidade_processo_aprendizado": ["Sim"],
    #         "sente_entusiasmado_motivado_atividades_aprendizagem": ["Não"],
    #         "experimentou_diferentes_metodos_aprendizado_encontrar_melhor": ["Sim"],
    #         "participa_ativamente_aulas_busca_compreender_conceitos": ["Não"],
    #         "aprende_com_erros_esforca_superar_dificuldades_persistencia": ["Sim"],
    #         "define_metas_claras_longo_prazo_trajetoria_educacional": ["Não"],
    #         "busca_ajuda_professores_colegas_mentores_profissionais": ["Sim"],
    #         "visualiza_como_educacao_ajudara_alcancar_sonhos_objetivos_vida": ["Não"],
    #         "considera_aprendiz_constante_busca_novas_informacoes_habilidades": ["Sim"],
    #         "data": [datetime.now()],
    #         "pontuacao": [3],
    #         "nivel_risco": ["Alto Risco"]
    #     })
    #     geral_table.add_data(df_renomeado)
    #     print(f"Tabela 'IPV' criada no banco de dados. Inseridos '{len(df_renomeado)}' registros")