from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import random
from Alfabetizacao.alfabetizacao import AlfabetizacaoTable
from Fundamental.fundamental import FundamentalTable
from Fundamental_2.fundamental_2 import Fundamental2Table
from EnsinoMedio.ensino_medio import EnsinoMedioTable
from Geral.ieg import IEGTable
from Geral.iaa import IAATable
from Psicologico.ipp import IPPTable
from Psicologico.ips import IPSTable
from Psicologico.ipv import IPVTable
from Materias.ida import IDATable
from Materias.ida_f import IDA_fTable
from Materias.ida_f2 import IDA_f2Table
from Materias.ida_em import IDA_emTable

Base = declarative_base()

class CadastroAluno(Base):
    __tablename__ = 'CadastroAlunos'
    ID = Column(Integer, primary_key=True)
    Matricula = Column(String)
    Nome = Column(String)
    Sobrenome = Column(String)
    Data_de_Nascimento = Column(Date)
    Serie = Column(String)
    Sexo = Column(String)
    Ingresso = Column(Date)
    Evasao = Column(String)
    Data_da_Conclusao = Column(String)
    Bolsista_ou_Escola_Publica = Column(String)
    Instituicao_Onde_Estuda = Column(String)
    Endereco = Column(String)
    Telefone = Column(String)

class CadastroAlunosTable:
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
                cadastro_aluno = CadastroAluno(**row)
                session.add(cadastro_aluno)
            session.commit()
            print("Dados de cadastro adicionados com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar dados de cadastro: {e}")
            session.rollback()
        finally:
            session.close()

    def initTableAlf(self, num_rows=200):
        '''
        Código para gerar a tabela CadastroAlunos
        '''
        start_date = pd.to_datetime("2019-01-01")
        end_date = pd.to_datetime("2024-01-01")

        cadastro_aluno_table = CadastroAlunosTable(self.engine)
        cadastro_aluno_table.create_table()
        cadastro_aluno = pd.DataFrame({
            'Matricula': [f'M{i:06d}' for i in range(1, num_rows + 1)],
            'Nome': [self.generate_first_name() for _ in range(num_rows)],
            'Sobrenome': [self.generate_last_name() for _ in range(num_rows)],
            'Data_de_Nascimento': [self.generate_birth_date() for _ in range(num_rows)],
            'Serie': np.random.choice(['1ª série', '2ª série', '3ª série'], size=num_rows),
            'Sexo': np.random.choice(['Masculino', 'Feminino'], size=num_rows),
            'Ingresso': pd.to_datetime(np.random.randint(pd.Timestamp('2019-01-01').value / 10 ** 9,
                                                          pd.Timestamp('2023-01-01').value / 10 ** 9,
                                                          size=num_rows), unit='s').date,
            'Evasao': np.random.choice([None, pd.to_datetime('2022-01-01')], size=num_rows).astype(str),
            'Data_da_Conclusao': np.random.choice([None] + pd.to_datetime(
                np.random.randint(pd.Timestamp('2020-01-01').value / 10 ** 9,
                                  pd.Timestamp('2023-01-01').value / 10 ** 9,
                                  size=num_rows), unit='s').tolist(), size=num_rows).astype(str),
            'Bolsista_ou_Escola_Publica': np.random.choice(['Bolsista', 'Escola pública'], size=num_rows),
            'Instituicao_Onde_Estuda': np.random.choice(['Centro', 'Filipinho', 'Cipó', 'Granjinha'], size=num_rows),
            'Endereco': [self.generate_address() for _ in range(num_rows)],
            'Telefone': [self.generate_phone_number() for _ in range(num_rows)]
        })
        
        cadastro_aluno_table.add_data(cadastro_aluno)
        print(f"Tabela 'CadastroAlunos' criada no banco de dados. Inseridos '{num_rows}' registros")

        alfabetizacao_table = AlfabetizacaoTable(self.engine)
        alfabetizacao_table.create_table()
        fundamental_table = FundamentalTable(self.engine)
        fundamental_table.create_table()
        fundamental2_table = Fundamental2Table(self.engine)
        fundamental2_table.create_table()
        ensino_medio_table = EnsinoMedioTable(self.engine)
        ensino_medio_table.create_table()
        ida_alfabetizacao_table = IDATable(self.engine)
        ida_alfabetizacao_table.create_table()
        ida_fundamental_table = IDA_fTable(self.engine)
        ida_fundamental_table.create_table()
        ida_fundamental2_table = IDA_f2Table(self.engine)
        ida_fundamental2_table.create_table()
        ida_ensino_medio_table = IDA_emTable(self.engine)
        ida_ensino_medio_table.create_table()
        ieg_table = IEGTable(self.engine)
        ieg_table.create_table()
        iaa_table = IAATable(self.engine)
        iaa_table.create_table()
        ipp_table = IPPTable(self.engine)
        ipp_table.create_table()
        ips_table = IPSTable(self.engine)
        ips_table.create_table()
        ipv_table = IPVTable(self.engine)
        ipv_table.create_table()

        fake_records_alfabetizacao = []
        fake_records_fundamental = []
        fake_records_fundamental2 = []
        fake_records_ensino_medio = []
        fake_records_ida_alfabetizacao = []
        fake_records_ida_fundamental = []
        fake_records_ida_fundamental2 = []
        fake_records_ida_ensino_medio = []
        fake_records_ieg = []
        fake_records_iaa = []
        fake_records_ipp = []
        fake_records_ips = []
        fake_records_ipv = []

        for index, aluno in cadastro_aluno.iterrows():
            for i in range(100):
                respostas_alfabetizacao = {
                    "matricula": aluno['Matricula'],
                    "reconhece_letras": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "ler_palavras_simples": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "escrever_palavras_simples": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "segmentar_palavras": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "ler_fluente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "responder_perguntas_leitura": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "conhece_significado_palavras": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "demonstra_interesse": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "participa_ativamente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "progresso_habilidades": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }
                
                pontuacao = self.calcular_pontuacao(respostas_alfabetizacao)
                nivel_risco = self.calcular_nivel_risco(pontuacao)

                respostas_alfabetizacao["pontuacao"] = pontuacao
                respostas_alfabetizacao["nivel_risco"] = nivel_risco

                fake_records_alfabetizacao.append(respostas_alfabetizacao)

            for i in range(100):
                respostas_fundamental = {
                    "matricula": aluno['Matricula'],
                    "resolve_problemas_matematicos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "interpreta_textos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "formula_perguntas_naturais": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "compreende_relacao_temporal": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "compreende_relacao_meio_ambiente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "demonstra_criatividade_arte": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "desenvolve_habilidades_motoras": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "comunica_eficazmente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "reconhece_pronuncia_ingles": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "utiliza_tecnologia": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao1 = self.calcular_pontuacao(respostas_fundamental)
                nivel_risco1 = self.calcular_nivel_risco(pontuacao1)

                respostas_fundamental["pontuacao"] = pontuacao1
                respostas_fundamental["nivel_risco"] = nivel_risco1

                fake_records_fundamental.append(respostas_fundamental)
            
            for i in range(100):
                respostas_fundamental2 = {
                    "matricula": aluno['Matricula'],
                    "domina_conceitos_matematicos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "resolve_problemas_complexos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "interpreta_textos_criticamente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "interesse_conhecimento_ciencias": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "desenvolve_senso_critico_historia": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "conhecimento_paises_regioes": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "participa_atividades_esportivas": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "autoconhecimento_autoconfianca_resiliencia": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "interesse_cultura_inglesa": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "produz_conteudo_digital_etico_responsavel": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao2 = self.calcular_pontuacao(respostas_fundamental2)
                nivel_risco2 = self.calcular_nivel_risco(pontuacao2)

                respostas_fundamental2["pontuacao"] = pontuacao2
                respostas_fundamental2["nivel_risco"] = nivel_risco2

                fake_records_fundamental2.append(respostas_fundamental2)
                
            for i in range(100):
                respostas_ensino_medio = {
                    "matricula": aluno['Matricula'],
                    "utiliza_metodos_matematicos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "utiliza_linguagem_matematica": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "analisa_criticamente_interpretacoes_historia": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "compreende_globalizacao_impactos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "formula_defende_argumentos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "analisa_criticamente_problemas_sociais": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "domina_conceitos_fisica": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "analisa_criticamente_impactos_quimica": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "domina_conceitos_biologia": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "comunica_eficazmente_diferentes_situacoes": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao3 = self.calcular_pontuacao(respostas_ensino_medio)
                nivel_risco3 = self.calcular_nivel_risco(pontuacao3)

                respostas_ensino_medio["pontuacao"] = pontuacao3
                respostas_ensino_medio["nivel_risco"] = nivel_risco3

                fake_records_ensino_medio.append(respostas_ensino_medio)
                
            for i in range(50):
                respostas_ida_alfabetizacao = {
                    "matricula": aluno['Matricula'],
                    "lingua_portuguesa": round(np.random.uniform(0, 10), 2),
                    "matematica": round(np.random.uniform(0, 10), 2),
                    "ciencias": round(np.random.uniform(0, 10), 2),
                    "artes": round(np.random.uniform(0, 10), 2),
                    "educacao_fisica": round(np.random.uniform(0, 10), 2),
                    "data": self.generate_random_date(start_date, end_date)
                }
                
                fake_records_ida_alfabetizacao.append(respostas_ida_alfabetizacao)

            for i in range(50):
                respostas_ida_fundamental = {
                    "matricula": aluno['Matricula'],
                    "lingua_portuguesa": round(np.random.uniform(0, 10), 2),
                    "matematica": round(np.random.uniform(0, 10), 2),
                    "ciencias": round(np.random.uniform(0, 10), 2),
                    "historia": round(np.random.uniform(0, 10), 2),
                    "geografia": round(np.random.uniform(0, 10), 2),
                    "artes": round(np.random.uniform(0, 10), 2),
                    "educacao_fisica": round(np.random.uniform(0, 10), 2),
                    "ingles": round(np.random.uniform(0, 10), 2),
                    "data": self.generate_random_date(start_date, end_date)
                }

                fake_records_ida_fundamental.append(respostas_ida_fundamental)

            for i in range(50):
                respostas_ida_fundamental2 = {
                    "matricula": aluno['Matricula'],
                    "lingua_portuguesa": round(np.random.uniform(0, 10), 2),
                    "matematica": round(np.random.uniform(0, 10), 2),
                    "ciencias": round(np.random.uniform(0, 10), 2),
                    "historia": round(np.random.uniform(0, 10), 2),
                    "geografia": round(np.random.uniform(0, 10), 2),
                    "artes": round(np.random.uniform(0, 10), 2),
                    "educacao_fisica": round(np.random.uniform(0, 10), 2),
                    "ingles": round(np.random.uniform(0, 10), 2),
                    "data": self.generate_random_date(start_date, end_date)
                }

                fake_records_ida_fundamental2.append(respostas_ida_fundamental2)

            for i in range(50):
                respostas_ida_ensino_medio = {
                    "matricula": aluno['Matricula'],
                    "lingua_portuguesa": round(np.random.uniform(0, 10), 2),
                    "lingua_estrangeira": round(np.random.uniform(0, 10), 2),
                    "artes": round(np.random.uniform(0, 10), 2),
                    "matematica": round(np.random.uniform(0, 10), 2),
                    "fisica": round(np.random.uniform(0, 10), 2),
                    "quimica": round(np.random.uniform(0, 10), 2),
                    "biologia": round(np.random.uniform(0, 10), 2),
                    "astronomia": round(np.random.uniform(0, 10), 2),
                    "historia": round(np.random.uniform(0, 10), 2),
                    "geografia": round(np.random.uniform(0, 10), 2),
                    "sociologia": round(np.random.uniform(0, 10), 2),
                    "filosofia": round(np.random.uniform(0, 10), 2),
                    "educacao_fisica": round(np.random.uniform(0, 10), 2),
                    "data": self.generate_random_date(start_date, end_date)
                }

                fake_records_ida_ensino_medio.append(respostas_ida_ensino_medio)

            for i in range(100):
                respostas_ieg = {
                    "matricula": aluno['Matricula'],
                    "interesse_entusiasmo_aulas": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "participa_ativamente_discussoes_atividades": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "faz_perguntas_busca_tirar_duvidas": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "iniciativa_contribuir_turma": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "acompanha_explicacoes_responde_clareza": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "compreensao_conceitos_conteudos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "aplicar_conhecimento_diferentes_situacoes": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "identifica_dificuldades_busca_superar": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "progresso_relacao_nivel_inicial": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "esforca_melhorar_habilidades_desempenho": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao8 = self.calcular_pontuacao(respostas_ieg)
                nivel_risco8 = self.calcular_nivel_risco(pontuacao8)

                respostas_ieg["pontuacao"] = pontuacao8
                respostas_ieg["nivel_risco"] = nivel_risco8

                fake_records_ieg.append(respostas_ieg)
                
            for i in range(100):
                respostas_iaa = {
                    "matricula": aluno['Matricula'],
                    "faz_perguntas_tira_duvidas": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "busca_feedback_utiliza_aprimorar_aprendizado": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "reconhece_pontos_fortes_areas_desenvolvimento": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "sente_satisfeito_progresso_desenvolvimento": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "acredita_aprendendo_tornando_mais_capaz": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "reconhece_importancia_educacao_para_futuro": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "sente_motivado_continuar_aprendendo_desafiando": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "organiza_gerencia_tempo_forma_eficiente": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "busca_conectar_outros_alunos_profissionais": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "tem_iniciativa_autonomia_estudos": np.random.choice(["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"]),
                    "data": self.generate_random_date(start_date, end_date)
                }
    
                pontuacao9 = self.calcular_pontuacao(respostas_iaa)
                nivel_risco9 = self.calcular_nivel_risco(pontuacao9)

                respostas_iaa["pontuacao"] = pontuacao9
                respostas_iaa["nivel_risco"] = nivel_risco9

                fake_records_iaa.append(respostas_iaa)
            
            for i in range(100):
                respostas_ipp = {
                    "matricula": aluno['Matricula'],
                    "participa_ativamente_responde_perguntas_clareza": np.random.choice(["Sim", "Não"]),
                    "relaciona_respeitosamente_cooperativamente_colegas": np.random.choice(["Sim", "Não"]),
                    "dificuldades_comunicacao_oral_escrita": np.random.choice(["Sim", "Não"]),
                    "demonstra_coordenacao_destreza_atividades": np.random.choice(["Sim", "Não"]),
                    "demonstra_empatia_respeito_outros": np.random.choice(["Sim", "Não"]),
                    "reconhece_pontos_fortes_areas_desenvolvimento": np.random.choice(["Sim", "Não"]),
                    "consegue_concentrar_tarefas_lembrar_informacoes_resolver_problemas": np.random.choice(["Sim", "Não"]),
                    "habilidades_academicas_leitura_escrita_calculos_fluencia_compreensao": np.random.choice(["Sim", "Não"]),
                    "saude_emocional_aluno_feliz_seguro_escola_casa": np.random.choice(["Sim", "Não"]),
                    "acesso_recursos_socioeconomicos_adequados_desenvolvimento": np.random.choice(["Sim", "Não"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao10 = self.calcular_pontuacao_sim_nao(respostas_ipp)
                nivel_risco10 = self.calcular_nivel_risco_sim_nao(pontuacao10)

                respostas_ipp["pontuacao"] = pontuacao10
                respostas_ipp["nivel_risco"] = nivel_risco10

                fake_records_ipp.append(respostas_ipp)

            for i in range(100):
                respostas_ips = {
                    "matricula": aluno['Matricula'],
                    "bom_relacionamento_familiares": np.random.choice(["Sim", "Não"]),
                    "amigos_com_quem_contar": np.random.choice(["Sim", "Não"]),
                    "sente_bem_consigo_vida": np.random.choice(["Sim", "Não"]),
                    "acredita_alcancar_objetivos": np.random.choice(["Sim", "Não"]),
                    "acredita_aprendendo_progredindo_estudos": np.random.choice(["Sim", "Não"]),
                    "tem_plano_alcancar_objetivos": np.random.choice(["Sim", "Não"]),
                    "alimenta_saudavel_pratica_atividades_fisicas": np.random.choice(["Sim", "Não"]),
                    "nao_pressionado_usar_drogas_bebidas_alcoolicas": np.random.choice(["Sim", "Não"]),
                    "se_sente_seguro_casa_escola_comunidade": np.random.choice(["Sim", "Não"]),
                    "sabe_buscar_ajuda_quando_precisa": np.random.choice(["Sim", "Não"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao11 = self.calcular_pontuacao_sim_nao(respostas_ips)
                nivel_risco11 = self.calcular_nivel_risco_sim_nao(pontuacao11)

                respostas_ips["pontuacao"] = pontuacao11
                respostas_ips["nivel_risco"] = nivel_risco11

                fake_records_ips.append(respostas_ips)

            for i in range(100):
                respostas_ipv = {
                    "matricula": aluno['Matricula'],
                    "sabe_identificar_interesses_habilidades_paixoes": np.random.choice(["Sim", "Não"]),
                    "assume_responsabilidade_processo_aprendizado": np.random.choice(["Sim", "Não"]),
                    "sente_entusiasmado_motivado_atividades_aprendizagem": np.random.choice(["Sim", "Não"]),
                    "experimentou_diferentes_metodos_aprendizado_encontrar_melhor": np.random.choice(["Sim", "Não"]),
                    "participa_ativamente_aulas_busca_compreender_conceitos": np.random.choice(["Sim", "Não"]),
                    "aprende_com_erros_esforca_superar_dificuldades_persistencia": np.random.choice(["Sim", "Não"]),
                    "define_metas_claras_longo_prazo_trajetoria_educacional": np.random.choice(["Sim", "Não"]),
                    "busca_ajuda_professores_colegas_mentores_profissionais": np.random.choice(["Sim", "Não"]),
                    "visualiza_como_educacao_ajudara_alcancar_sonhos_objetivos_vida": np.random.choice(["Sim", "Não"]),
                    "considera_aprendiz_constante_busca_novas_informacoes_habilidades": np.random.choice(["Sim", "Não"]),
                    "data": self.generate_random_date(start_date, end_date)
                }

                pontuacao12 = self.calcular_pontuacao_sim_nao(respostas_ipv)
                nivel_risco12 = self.calcular_nivel_risco_sim_nao(pontuacao12)

                respostas_ipv["pontuacao"] = pontuacao12
                respostas_ipv["nivel_risco"] = nivel_risco12

                fake_records_ipv.append(respostas_ipv)
        
        alfabetizacao_table.add_data(pd.DataFrame(fake_records_alfabetizacao))
        fundamental_table.add_data(pd.DataFrame(fake_records_fundamental))
        fundamental2_table.add_data(pd.DataFrame(fake_records_fundamental2))
        ensino_medio_table.add_data(pd.DataFrame(fake_records_ensino_medio))
        ida_alfabetizacao_table.add_data(pd.DataFrame(fake_records_ida_alfabetizacao))
        ida_fundamental_table.add_data(pd.DataFrame(fake_records_ida_fundamental))
        ida_fundamental2_table.add_data(pd.DataFrame(fake_records_ida_fundamental2))
        ida_ensino_medio_table.add_data(pd.DataFrame(fake_records_ida_ensino_medio))
        ieg_table.add_data(pd.DataFrame(fake_records_ieg))
        iaa_table.add_data(pd.DataFrame(fake_records_iaa))
        ipp_table.add_data(pd.DataFrame(fake_records_ipp))
        ips_table.add_data(pd.DataFrame(fake_records_ips))
        ipv_table.add_data(pd.DataFrame(fake_records_ipv))
        
        print(f"Tabela 'Alfabetizacao' criada no banco de dados. Inseridos '{len(fake_records_alfabetizacao)}' registros")
        print(f"Tabela 'IPV' criada no banco de dados. Inseridos '{len(fake_records_ipv)}' registros")
        print(f"Tabela 'IPS' criada no banco de dados. Inseridos '{len(fake_records_ips)}' registros")
        print(f"Tabela 'IPP' criada no banco de dados. Inseridos '{len(fake_records_ipp)}' registros")
        print(f"Tabela 'IDA.Alfabetizacao' criada no banco de dados. Inseridos '{len(fake_records_ida_alfabetizacao)}' registros")
        print(f"Tabela 'Alfabetizacao' criada no banco de dados. Inseridos '{len(fake_records_alfabetizacao)}' registros")
        print(f"Tabela 'Fundamental' criada no banco de dados. Inseridos '{len(fake_records_fundamental)}' registros")
        print(f"Tabela 'Fundamental2' criada no banco de dados. Inseridos '{len(fake_records_fundamental2)}' registros")
        print(f"Tabela 'Ensino Medio' criada no banco de dados. Inseridos '{len(fake_records_ensino_medio)}' registros")
        print(f"Tabela 'IDA.Funfamental' criada no banco de dados. Inseridos '{len(fake_records_ida_fundamental)}' registros")
        print(f"Tabela 'IDA.Funfamental2' criada no banco de dados. Inseridos '{len(fake_records_ida_fundamental2)}' registros")
        print(f"Tabela 'IDA.EnsinoMedio' criada no banco de dados. Inseridos '{len(fake_records_ida_ensino_medio)}' registros")
        print(f"Tabela 'IEG' criada no banco de dados. Inseridos '{len(fake_records_ieg)}' registros")
        print(f"Tabela 'IAA' criada no banco de dados. Inseridos '{len(fake_records_iaa)}' registros")

    def calcular_pontuacao(self, respostas):
        pontuacao = 0
        for answer in respostas.values():
            if answer == "Raramente":
                pontuacao += 1
            elif answer == "Às vezes":
                pontuacao += 2
            elif answer == "Frequentemente":
                pontuacao += 3
            elif answer == "Sempre":
                pontuacao += 4
        return pontuacao
    
    def calcular_nivel_risco(self, pontuacao):
        if pontuacao >= 0 and pontuacao <= 10:
            return "Muito Elevado"
        elif pontuacao >= 11 and pontuacao <= 20:
            return "Elevado"
        elif pontuacao >= 21 and pontuacao <= 30:
            return "Moderado"
        elif pontuacao >= 31 and pontuacao <= 40:
            return "Baixo"
        else:
            return "Valor de pontuação inválido"
    
    def calcular_pontuacao_sim_nao(self, respostas):
        pontuacao = 0
        for answer in respostas.values():
            if answer == "Sim":
                pontuacao += 1
            elif answer == "Não":
                pontuacao += 0
        return pontuacao

    def calcular_nivel_risco_sim_nao(self, pontuacao):
        if pontuacao >= 0 and pontuacao <= 3:
            return "Alto Risco"
        elif pontuacao >= 4 and pontuacao <= 7:
            return "Moderado Risco"
        elif pontuacao >= 8 and pontuacao <= 10:
            return "Baixo Risco"
        else:
            return "Valor de pontuação inválido"

    def generate_random_date(self, start, end):
        return pd.to_datetime(np.random.randint(start.value, end.value))

    def generate_first_name(self):
        first_names = ['Maria', 'José', 'Ana', 'João', 'Luiz', 'Fernanda', 'Carlos', 'Mariana', 'Pedro', 'Amanda']
        return np.random.choice(first_names)

    def generate_last_name(self):
        last_names = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Lima', 'Almeida', 'Ferreira', 'Costa',
                      'Rodrigues']
        return np.random.choice(last_names)

    def generate_address(self):
        streets = ['Rua A', 'Rua B', 'Rua C', 'Rua D', 'Rua E', 'Rua F', 'Rua G', 'Rua H', 'Rua I', 'Rua J']
        return np.random.choice(streets) + ', Embu-Guaçu, São Paulo'

    def generate_phone_number(self):
        return f'({np.random.randint(10, 99)}) 9{np.random.randint(1000, 9999)}-{np.random.randint(1000, 9999)}'

    def generate_birth_date(self):
        today = datetime.today()
        start_date = today - timedelta(days=365 * 18)
        end_date = today - timedelta(days=365 * 10)
        return np.random.choice(pd.date_range(start_date, end_date).date)