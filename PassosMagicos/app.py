from sqlglot import column
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.subplots as sp
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from sqlalchemy import create_engine, text
from Questionario.salvar_ips import QuestionarioIPSSalvo
from Questionario.salvar_ipp import QuestionarioIPPSalvo
from Questionario.salvar_ipv import QuestionarioIPVSalvo
from Questionario.save_alf import QuestionarioAlfSalvo
from Questionario.save_fund import QuestionarioFundSalvo
from Questionario.save_fund2 import QuestionarioFund2Salvo
from Questionario.save_ida_f2 import QuestionarioIDA_f2Salvo
from Questionario.save_ida_em import QuestionarioIDA_emSalvo
from Questionario.save_em import QuestionarioEMSalvo
from Questionario.save_ieg import QuestionarioIEGSalvo
from Questionario.save_iaa import QuestionarioIAASalvo
from Questionario.save_ida import QuestionarioIDASalvo
from Questionario.save_ida_f import QuestionarioIDA_fSalvo
from Questionario.questionarios_ips import QuestionariosIPS
from Questionario.questionarios_ipp import QuestionariosIPP
from Questionario.questionarios_ipv import QuestionariosIPV
from Questionario.questionarios_f import QuestionariosAlf
from Questionario.quetionarios_ieg import QuestionariosIEG
from Questionario.questionarios_iaa import QuestionariosIAA
from Questionario.questionarios_ida import QuestionariosIDA
from Questionario.salvar_cadastro import CadastroAlunoSalvo

engine = create_engine(f'sqlite:///Data/passos_magicos.db', echo=False)

def sql(query):
    with engine.connect() as conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall()
    return pd.DataFrame(dados,columns=consulta.keys())

def get_aluno():
    query = '''
        SELECT Matricula, Nome, Sobrenome FROM CadastroAlunos
    '''
    alunos = sql(query)
    alunos['Nome_Completo'] = alunos['Nome'] + ' ' + alunos['Sobrenome']

    return alunos

def panelIAN():
    tab1, tab2, tab3, tab4 = st.tabs([
                                        'Alfabetização',
                                        'Fundamental 1',
                                        'Fundamental 2',
                                        'Ensino Médio'
                                    ])

    with tab1:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='2')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_alf' not in globals():
                answers_alf = {}

            if answers_alf == {}:
                answers_alf = {tab: {} for tab in ['Alfabetização']}

            questionario_alf = QuestionariosAlf(answers_alf)
            
            answers_alf['Alfabetização'] = questionario_alf.collect_answers('Alfabetização', matricula_selected)

            if st.button('Salvar Questionário', key='s1'):
                    questionario_salvo = QuestionarioAlfSalvo(answers_alf)
                    result = questionario_salvo.save()
                    if result:
                        answers_alf.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
            
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)
    
    with tab2:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='3')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_f' not in globals():
                answers_f = {}

            if answers_f == {}:
                answers_f = {tab: {} for tab in ['Fundamental']}

            questionario_f = QuestionariosAlf(answers_f)

            answers_f['Fundamental'] = questionario_f.collect_answers('Fundamental', matricula_selected)
            
            if st.button('Salvar Questionário', key='s2'):
                    questionario_salvo = QuestionarioFundSalvo(answers_f)
                    result = questionario_salvo.save()

                    if result:
                        answers_f.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

    with tab3:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='4')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_f2' not in globals():
                answers_f2 = {}

            if answers_f2 == {}:
                answers_f2 = {tab: {} for tab in ['Fundamental 2']}

            questionario_f2 = QuestionariosAlf(answers_f2)

            answers_f2['Fundamental 2'] = questionario_f2.collect_answers('Fundamental 2', matricula_selected)
            
            if st.button('Salvar Questionário', key='s3'):
                    questionario_salvo = QuestionarioFund2Salvo(answers_f2)
                    result = questionario_salvo.save()
                    if result:
                        answers_f2.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

    with tab4:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='5')
        
        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_em' not in globals():
                answers_em = {}

            if answers_em == {}:
                answers_em = {tab: {} for tab in ['Ensino Médio']}

            questionario_em = QuestionariosAlf(answers_em)

            answers_em['Ensino Médio'] = questionario_em.collect_answers('Ensino Médio', matricula_selected)

            if st.button('Salvar Questionário', key='s4'):
                    questionario_salvo = QuestionarioEMSalvo(answers_em)
                    result = questionario_salvo.save()
                    if result:
                        answers_em.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIEG():
    alunos_df = get_aluno()
    selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='6')

    if selected_aluno:
        matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

        if 'answers_g' not in globals():
            answers_g = {}

        if answers_g == {}:
            answers_g = 'IEG'

        questionario_g = QuestionariosIEG(answers_g)

        st.markdown("""
                    #### IEG - Indicadores de Engajamento
                    """)
        answers_g = questionario_g.collect_answers('IEG', matricula_selected)

        if st.button('Salvar Questionário', key='s5'):
                questionario_salvo = QuestionarioIEGSalvo(answers_g)
                result = questionario_salvo.save()
                if result:
                    answers_g.clear()
                    st.success("Questionário salvo com sucesso!")
        else:
            st.info("Por favor, preencha todos os questionários antes de salvar.")
    
    hide_st_style = '''
        <style>
            footer {visibility: hidden;}
            div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
        </style>
    '''
    st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIAA():
    alunos_df = get_aluno()
    selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='7')

    if selected_aluno:
        matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

        if 'answers_iaa' not in globals():
            answers_iaa = {}

        if answers_iaa == {}:
            answers_iaa = {tab: {} for tab in ['IAA']}

        questionario_iaa = QuestionariosIAA(answers_iaa)

        st.markdown("""
                    #### IAA - Indicador de AutoAvaliação
                    """)
        answers_iaa['IAA'] = questionario_iaa.collect_answers('IAA', matricula_selected)

        if st.button('Salvar Questionário', key='s5'):
                questionario_salvo = QuestionarioIAASalvo(answers_iaa)
                result = questionario_salvo.save()
                if result:
                    answers_iaa.clear()
                    st.success("Questionário salvo com sucesso!")
        else:
            st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIPP():
    alunos_df = get_aluno()
    selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='8')

    if selected_aluno:
        matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

        if 'answers_ipp' not in globals():
            answers_ipp = {}

        if answers_ipp == {}:
            answers_ipp = {tab: {} for tab in ['IPP']}

        questionario_ipp = QuestionariosIPP(answers_ipp)

        st.markdown("""
                    #### IPP - Indicadores Psicopedagógicos
                    A avaliação de ansiedade e depressão em crianças é fundamental para o processo de aprendizagem por diversos motivos.
                    Impacto no desempenho escolar
                    """)
        answers_ipp['IPP'] = questionario_ipp.collect_answers('IPP', matricula_selected)

        if st.button('Salvar Questionário', key='s6'):
                questionario_salvo = QuestionarioIPPSalvo(answers_ipp)
                result = questionario_salvo.save()
                if result:
                    answers_ipp.clear()
                    st.success("Questionário salvo com sucesso!")
        else:
            st.info("Por favor, preencha todos os questionários antes de salvar.")

        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIPS():
    alunos_df = get_aluno()
    selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='9')

    if selected_aluno:
        matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

        if 'answers_ips' not in globals():
            answers_ips = {}

        if answers_ips == {}:
            answers_ips = {tab: {} for tab in ['IPS']}

        questionario_ips = QuestionariosIPS(answers_ips)

        st.markdown("""
                    #### IPS - Indicador Psicossocial
                    A avaliação de ansiedade e depressão em crianças é fundamental para o processo de aprendizagem por diversos motivos.
                    Impacto no desempenho escolar
                    """)
        answers_ips['IPS'] = questionario_ips.collect_answers('IPS', matricula_selected)

        if st.button('Salvar Questionário', key='s7'):
                questionario_salvo = QuestionarioIPSSalvo(answers_ips)
                result = questionario_salvo.save()
                if result:
                    answers_ips.clear()
                    st.success("Questionário salvo com sucesso!")
        else:
            st.info("Por favor, preencha todos os questionários antes de salvar.")

        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIPV():
    alunos_df = get_aluno()
    selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='10')

    if selected_aluno:
        matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

        if 'answers_ipv' not in globals():
            answers_ipv = {}

        if answers_ipv == {}:
            answers_ipv = {tab: {} for tab in ['IPV']}

        questionario_ipv = QuestionariosIPV(answers_ipv)

        st.markdown("""
                    #### IPV - Indicadores do Ponto de Virada
                    A avaliação de ansiedade e depressão em crianças é fundamental para o processo de aprendizagem por diversos motivos.
                    Impacto no desempenho escolar
                    """)
        answers_ipv['IPV'] = questionario_ipv.collect_answers('IPV', matricula_selected)

        if st.button('Salvar Questionário', key='s7'):
                questionario_salvo = QuestionarioIPVSalvo(answers_ipv)
                result = questionario_salvo.save()
                if result:
                    answers_ipv.clear()
                    st.success("Questionário salvo com sucesso!")
        else:
            st.info("Por favor, preencha todos os questionários antes de salvar.")
    
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelIDA():
    tab1, tab2, tab3, tab4 = st.tabs([
                                        'Alfabetização',
                                        'Fundamental 1',
                                        'Fundamental 2',
                                        'Ensino Médio'
                                    ])
    with tab1:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='ida')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_ida' not in globals():
                answers_ida = {}

            if answers_ida == {}:
                answers_ida = 'IDA'

            questionario_ida = QuestionariosIDA(answers_ida)
            
            answers_ida = questionario_ida.collect_answers('IDA', matricula_selected)

            if st.button('Salvar Questionário', key='s11'):
                    questionario_salvo = QuestionarioIDASalvo(answers_ida)
                    result = questionario_salvo.save()
                    if result:
                        answers_ida.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
            
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)
    
    with tab2:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='3')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_ida_f' not in globals():
                answers_ida_f = {}

            if answers_ida_f == {}:
                answers_ida_f = 'IDA_f'

            questionario_ida_f = QuestionariosIDA(answers_ida_f)

            answers_ida_f = questionario_ida_f.collect_answers('IDA_f', matricula_selected)
            
            if st.button('Salvar Questionário', key='s12'):
                    questionario_salvo = QuestionarioIDA_fSalvo(answers_ida_f)
                    result = questionario_salvo.save()

                    if result:
                        answers_ida_f.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)
    
    with tab3:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='4')

        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_ida_f2' not in globals():
                answers_ida_f2 = {}

            if answers_ida_f2 == {}:
                answers_ida_f2 = 'IDA_f2'

            questionario_ida_f2 = QuestionariosIDA(answers_ida_f2)

            answers_ida_f2 = questionario_ida_f2.collect_answers('IDA_f2', matricula_selected)
            
            if st.button('Salvar Questionário', key='s13'):
                    questionario_salvo = QuestionarioIDA_f2Salvo(answers_ida_f2)
                    result = questionario_salvo.save()
                    if result:
                        answers_ida_f2.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)
    
    with tab4:
        alunos_df = get_aluno()
        selected_aluno = st.selectbox("Selecione o aluno:", alunos_df['Nome_Completo'], key='5')
        
        if selected_aluno:
            matricula_selected = alunos_df.loc[alunos_df['Nome_Completo'] == selected_aluno, 'Matricula'].values[0]

            if 'answers_ida_em' not in globals():
                answers_ida_em = {}

            if answers_ida_em == {}:
                answers_ida_em = 'IDA_f_em'

            questionario_ida_em = QuestionariosIDA(answers_ida_em)

            answers_ida_em = questionario_ida_em.collect_answers('IDA_em', matricula_selected)

            if st.button('Salvar Questionário', key='s14'):
                    questionario_salvo = QuestionarioIDA_emSalvo(answers_ida_em)
                    result = questionario_salvo.save()
                    if result:
                        answers_ida_em.clear()
                        st.success("Questionário salvo com sucesso!")
            else:
                st.info("Por favor, preencha todos os questionários antes de salvar.")
        
        hide_st_style = '''
            <style>
                footer {visibility: hidden;}
                div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
        '''
        st.markdown(hide_st_style, unsafe_allow_html=True)

def panelDash():
    style = {'width': '100%'}
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
                                                        'IAN',
                                                        'IDA',
                                                        'IEG',
                                                        'IAA',
                                                        'IPS',
                                                        'IPP',
                                                        'IPV',
                                                        'Alunos'
                                                    ])
    with tab1:
        st.markdown("### IAN - Indicadores de adequação de nível", unsafe_allow_html=True)
        st.markdown("#### Alfabetização", unsafe_allow_html=True)
        df_alf = sql("select * from Alfabetizacao")
        alunos_df = get_aluno()

        df_alf['data'] = pd.to_datetime(df_alf['data'])
        df_alf['data'] = df_alf['data'].dt.date
        df_alf.sort_values(by='data', inplace=True)

        min_date = df_alf['data'].min()
        max_date = df_alf['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default
            )

        df_filtered = df_alf[(df_alf['data'] >= start_date) & (df_alf['data'] <= end_date)]
        
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='alf')

        if aluno == 'Todos':
            df_filtered = df_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_filtered = df_filtered[df_filtered['matricula'] == matricula]

        df_sum = df_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_sum = df_sum.sort_values(by='data')

        fig = px.line(df_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig, style = style, use_container_width=True)

        df_seas = df_alf.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_seas.set_index('data', inplace=True)

        results = seasonal_decompose(df_seas['pontuacao'], period=180)
        rolling_avg = df_seas['pontuacao'].rolling(window=30).mean()

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_seas.index, y=results.seasonal, mode='lines', name='Sazonalidade'))
        fig2.add_trace(go.Scatter(x=df_seas.index, y=rolling_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig2.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig2, style=style, use_container_width=True)

        recent_data = df_filtered[df_filtered['data'] == df_filtered['data'].max()]
        mapper_alfabetizacao = {
            "reconhece_letras": "A criança reconhece todas as letras do alfabeto?",
            "ler_palavras_simples": "A criança consegue ler palavras simples e familiares?",
            "escrever_palavras_simples": "A criança consegue escrever palavras simples e familiares?",
            "segmentar_palavras": "A criança consegue segmentar palavras em sílabas?",
            "ler_fluente": "A criança lê de forma fluente, sem soletrar ou decodificar cada palavra?",
            "responder_perguntas_leitura": "A criança consegue responder perguntas sobre o que leu?",
            "conhece_significado_palavras": "A criança conhece o significado das palavras que lê e escreve?",
            "demonstra_interesse": "A criança demonstra interesse pela leitura e pela escrita?",
            "participa_ativamente": "A criança participa ativamente das aulas de alfabetização?",
            "progresso_habilidades": "A criança demonstra progresso ao longo do tempo em suas habilidades de leitura e escrita?"
        }

        fig3 = go.Figure()

        for pergunta in recent_data.columns[2:11]:
            pergunta_mapeada = mapper_alfabetizacao[pergunta]
            contagem_respostas = recent_data[pergunta].value_counts()
            fig3.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig3.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig3, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco = recent_data['nivel_risco'].value_counts()

            fig_risco = go.Figure(go.Bar(x=contagem_risco.index, y=contagem_risco.values))

            fig_risco.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco, style=style, use_container_width=True)
        with col2:
            contagem_risco_g = df_filtered['nivel_risco'].value_counts()

            fig_risco_g = go.Figure(go.Bar(x=contagem_risco_g.index, y=contagem_risco_g.values))

            fig_risco_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_g, style=style, use_container_width=True)

        # st.dataframe(recent_data)
        st.markdown('***')
        st.markdown("#### Fundamental 1", unsafe_allow_html=True)
        df_fund = sql("select * from Fundamental")

        df_fund['data'] = pd.to_datetime(df_fund['data'])
        df_fund['data'] = df_fund['data'].dt.date
        df_fund.sort_values(by='data', inplace=True)

        df_fund_filtered = df_fund[(df_fund['data'] >= start_date) & (df_fund['data'] <= end_date)]

        if aluno == 'Todos':
            df_fund_filtered = df_fund_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_fund_filtered = df_fund_filtered[df_fund_filtered['matricula'] == matricula]

        df_fund_sum = df_fund_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_fund_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_fund_sum = df_fund_sum.sort_values(by='data')

        fig_fund = px.line(df_fund_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_fund.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_fund, style = style, use_container_width=True)

        df_fund_seas = df_fund.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_fund_seas.set_index('data', inplace=True)

        results_fund = seasonal_decompose(df_fund_seas['pontuacao'], period=180)
        rolling_fund_avg = df_fund_seas['pontuacao'].rolling(window=30).mean()

        fig_fund2 = go.Figure()
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=results_fund.seasonal, mode='lines', name='Sazonalidade'))
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=rolling_fund_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_fund2.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_fund2, style=style, use_container_width=True)

        recent_data = df_fund_filtered[df_fund_filtered['data'] == df_fund_filtered['data'].max()]

        mapper_fundamental = {
            "resolve_problemas_matematicos": "A criança consegue resolver problemas matemáticos simples envolvendo adição, subtração, multiplicação e divisão?",
            "interpreta_textos": "Ela consegue interpretar e analisar textos de diferentes tipos, como contos, notícias e poemas?",
            "formula_perguntas_naturais": "Ela formula perguntas e hipóteses sobre o mundo natural?",
            "compreende_relacao_temporal": "Ela compreende a relação entre passado, presente e futuro?",
            "compreende_relacao_meio_ambiente": "Ela compreende a relação entre o homem e o meio ambiente?",
            "demonstra_criatividade_arte": "A criança demonstra criatividade e expressividade nas diferentes formas de arte?",
            "desenvolve_habilidades_motoras": "Ela desenvolve suas habilidades motoras e coordenação corporal?",
            "comunica_eficazmente": "Ela se comunica de forma eficaz com os outros?",
            "reconhece_pronuncia_ingles": "Ela reconhece e pronuncia palavras e frases simples em inglês?"
        }

        fig3fund = go.Figure()

        for pergunta in recent_data.columns[2:11]:
            pergunta_mapeada = mapper_fundamental[pergunta]
            contagem_respostas = recent_data[pergunta].value_counts()
            fig3fund.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig3fund.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig3fund, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco = recent_data['nivel_risco'].value_counts()

            fig_risco = go.Figure(go.Bar(x=contagem_risco.index, y=contagem_risco.values))

            fig_risco.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco, style=style, use_container_width=True)
        with col2:
            contagem_risco_g = df_fund_filtered['nivel_risco'].value_counts()

            fig_risco_g = go.Figure(go.Bar(x=contagem_risco_g.index, y=contagem_risco_g.values))

            fig_risco_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_g, style=style, use_container_width=True)

        # st.dataframe(recent_data)
        
        st.markdown('***')
        st.markdown("#### Fundamental 2", unsafe_allow_html=True)
        df_fund2 = sql("select * from Fundamental2")

        df_fund2['data'] = pd.to_datetime(df_fund2['data'])
        df_fund2['data'] = df_fund2['data'].dt.date
        df_fund2.sort_values(by='data', inplace=True)

        df_fund2_filtered = df_fund2[(df_fund2['data'] >= start_date) & (df_fund2['data'] <= end_date)]

        if aluno == 'Todos':
            df_fund2_filtered = df_fund2_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_fund2_filtered = df_fund2_filtered[df_fund2_filtered['matricula'] == matricula]
    
        df_fund2_sum = df_fund2_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_fund2_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_fund2_sum = df_fund2_sum.sort_values(by='data')

        fig_fund2 = px.line(df_fund2_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_fund2.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_fund2, style = style, use_container_width=True)

        df_fund2_seas = df_fund2.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_fund2_seas.set_index('data', inplace=True)

        results_fund = seasonal_decompose(df_fund2_seas['pontuacao'], period=180)
        rolling_fund_avg = df_fund2_seas['pontuacao'].rolling(window=30).mean()

        fig_fund2 = go.Figure()
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=results_fund.seasonal, mode='lines', name='Sazonalidade'))
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=rolling_fund_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_fund2.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_fund2, style=style, use_container_width=True)

        recent_data = df_fund2_filtered[df_fund2_filtered['data'] == df_fund2_filtered['data'].max()]

        mapper_fundamental2 = {
            "domina_conceitos_matematicos": "Domina os conceitos matemáticos básicos de frações, decimais e porcentagens?",
            "resolve_problemas_complexos": "Resolve problemas matemáticos mais complexos envolvendo diferentes operações?",
            "interpreta_textos_criticamente": "Interpreta e analisa criticamente textos de diferentes gêneros literários?",
            "interesse_conhecimento_ciencias": "Demonstra interesse e conhecimento sobre diferentes áreas da ciência (física, química, biologia)?",
            "desenvolve_senso_critico_historia": "Desenvolve senso crítico para analisar diferentes interpretações da história?",
            "conhecimento_paises_regioes": "Demonstra conhecimento sobre os principais países e regiões do mundo?",
            "participa_atividades_esportivas": "Participa de diferentes atividades esportivas com cooperação e respeito?",
            "autoconhecimento_autoconfianca_resiliencia": "Demonstra autoconhecimento, autoconfiança e resiliência?",
            "interesse_cultura_inglesa": "Demonstra interesse pela cultura dos países de língua inglesa?",
            "produz_conteudo_digital_etico_responsavel": "Produz conteúdo digital de forma ética e responsável?"
        }

        fig3fund = go.Figure()

        for pergunta in recent_data.columns[2:11]:
            pergunta_mapeada = mapper_fundamental2[pergunta]
            contagem_respostas = recent_data[pergunta].value_counts()
            fig3fund.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig3fund.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig3fund, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco = recent_data['nivel_risco'].value_counts()

            fig_risco = go.Figure(go.Bar(x=contagem_risco.index, y=contagem_risco.values))

            fig_risco.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco, style=style, use_container_width=True)
        with col2:
            contagem_risco_g = df_fund2_filtered['nivel_risco'].value_counts()

            fig_risco_g = go.Figure(go.Bar(x=contagem_risco_g.index, y=contagem_risco_g.values))

            fig_risco_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_g, style=style, use_container_width=True)
        
        # st.dataframe(df_fund2)

        st.markdown('***')
        st.markdown("#### Ensino Médio", unsafe_allow_html=True)
        df_em = sql("select * from EnsinoMedio")

        df_em['data'] = pd.to_datetime(df_em['data'])
        df_em['data'] = df_em['data'].dt.date
        df_em.sort_values(by='data', inplace=True)

        df_em_filtered = df_em[(df_em['data'] >= start_date) & (df_em['data'] <= end_date)]

        if aluno == 'Todos':
            df_em_filtered = df_em_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_em_filtered = df_em_filtered[df_em_filtered['matricula'] == matricula]

        df_em_sum = df_em_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_em_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_em_sum = df_em_sum.sort_values(by='data')

        fig_fund2 = px.line(df_em_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_fund2.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_fund2, style = style, use_container_width=True)

        df_em_seas = df_em.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_em_seas.set_index('data', inplace=True)

        results_fund = seasonal_decompose(df_em_seas['pontuacao'], period=180)
        rolling_fund_avg = df_em_seas['pontuacao'].rolling(window=30).mean()

        fig_fund2 = go.Figure()
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=results_fund.seasonal, mode='lines', name='Sazonalidade'))
        fig_fund2.add_trace(go.Scatter(x=df_fund_seas.index, y=rolling_fund_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_fund2.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_fund2, style=style, use_container_width=True)

        recent_data = df_em_filtered[df_em_filtered['data'] == df_em_filtered['data'].max()]

        mapper_ensino_medio = {
            "utiliza_metodos_matematicos": "Ele utiliza diferentes métodos e estratégias para resolver problemas matemáticos de forma eficiente?",
            "utiliza_linguagem_matematica": "Ele utiliza linguagem matemática adequada e argumenta de forma lógica?",
            "analisa_criticamente_interpretacoes_historia": "Ele é capaz de analisar criticamente diferentes interpretações da história?",
            "compreende_globalizacao_impactos": "O aluno compreende os principais processos de globalização e seus impactos na sociedade?",
            "formula_defende_argumentos": "Ele é capaz de formular e defender argumentos de forma lógica e fundamentada?",
            "analisa_criticamente_problemas_sociais": "Ele é capaz de analisar criticamente os problemas sociais e propor soluções?",
            "domina_conceitos_fisica": "O aluno domina os principais conceitos da física e suas aplicações no mundo real?",
            "analisa_criticamente_impactos_quimica": "Ele é capaz de analisar criticamente os impactos da química na sociedade e no meio ambiente?",
            "domina_conceitos_biologia": "O aluno domina os principais conceitos da biologia e as relações entre os seres vivos?",
            "comunica_eficazmente_diferentes_situacoes": "Ele é capaz de se comunicar de forma eficaz em diferentes situações?"
        }

        fig3fund = go.Figure()

        for pergunta in recent_data.columns[2:11]:
            pergunta_mapeada = mapper_ensino_medio[pergunta]
            contagem_respostas = recent_data[pergunta].value_counts()
            fig3fund.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig3fund.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig3fund, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco = recent_data['nivel_risco'].value_counts()

            fig_risco = go.Figure(go.Bar(x=contagem_risco.index, y=contagem_risco.values))

            fig_risco.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco, style=style, use_container_width=True)
        with col2:
            contagem_risco_g = df_em_filtered['nivel_risco'].value_counts()

            fig_risco_g = go.Figure(go.Bar(x=contagem_risco_g.index, y=contagem_risco_g.values))

            fig_risco_g.update_layout(
                title='Contagem de Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_g, style=style, use_container_width=True)

        # st.dataframe(df_em)

    with tab2:
        st.markdown("### IDA - Indicador de Desenvolvimento Acadêmico", unsafe_allow_html=True)
        st.markdown("#### Alfabetização", unsafe_allow_html=True)

        df_ida_a = sql("select * from IDA")
        alunos_df = get_aluno()
        df_ida_a['data'] = pd.to_datetime(df_ida_a['data']).dt.date

        min_date = df_ida_a['data'].min()
        max_date = df_ida_a['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início",
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start2.1'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and2.1'
            )

        df_ida_a_filtered = df_ida_a[(df_ida_a['data'] >= start_date) & (df_ida_a['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='ida_a')

        if aluno == 'Todos':
            df_ida_a_filtered = df_ida_a_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ida_a_filtered = df_ida_a_filtered[df_ida_a_filtered['matricula'] == matricula]

        cols_pontuacao = df_ida_a_filtered.columns[2:-1]
        df_ida_a_filtered['media'] = df_ida_a_filtered[cols_pontuacao].mean(axis=1)

        df_media_por_data = df_ida_a_filtered.groupby('data')['media'].mean().reset_index()

        fig_ida_a = px.line(df_media_por_data, x='data', y='media', title='Curva de Evolução do Aluno')
        fig_ida_a.update_xaxes(title='Data')
        fig_ida_a.update_yaxes(title='Média de Pontuação')

        st.plotly_chart(fig_ida_a, style = style, use_container_width=True)

        mapper_materias = {
            "lingua_portuguesa": "Língua Portuguesa",
            "matematica": "Matemática",
            "ciencias": "Ciências",
            "artes": "Artes",
            "educacao_fisica": "Educação Física"
        }
        
        df_pontuacoes = df_ida_a_filtered.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_pontuacoes['data'] = df_ida_a_filtered['data']
        df_media_por_materia = df_pontuacoes.groupby('data').mean().reset_index()

        recent_ida_a_data = df_ida_a_filtered[df_ida_a_filtered['data'] == df_ida_a_filtered['data'].max()]
        df_pontuacoes_g = recent_ida_a_data.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_pontuacoes_g['data'] = recent_ida_a_data['data']
        df_media_por_materia_g = df_pontuacoes_g.groupby('data').mean().reset_index()

        df_melted = df_media_por_materia.melt(id_vars=['data'], var_name='Matéria', value_name='Média')

        fig_ida_a1 = px.line(
            df_melted,
            x='data',
            y='Média',
            color='Matéria', 
            title='Evolução do Desempenho do Aluno por Matéria',
            labels={'data': 'Data', 'Média': 'Média de Pontuação', 'Matéria': 'Matéria'}
        )

        fig_ida_a1.update_traces(mode='lines+markers')

        st.plotly_chart(fig_ida_a1, style = style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            fig_ida_a2 = go.Figure()

            for materia in df_media_por_materia.columns[1:]:
                fig_ida_a2.add_trace(go.Bar(x=[materia], y=[df_media_por_materia[materia].mean()], name=materia))

            fig_ida_a2.update_layout(
                title='Média por Matéria no Último Registro',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_a2, style=style, use_container_width=True)

        with col2:
            fig_ida_a3 = go.Figure()

            for materia in df_media_por_materia_g.columns[1:]:
                fig_ida_a3.add_trace(go.Bar(x=[materia], y=[df_media_por_materia_g[materia].mean()], name=materia))

            fig_ida_a3.update_layout(
                title='Média Geral por Matéria',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_a3, style=style, use_container_width=True)
        
        df_ida_a['media'] = df_ida_a[cols_pontuacao].mean(axis=1)
        df_ida_a = df_ida_a.groupby('data')['media'].mean().reset_index()
        df_ida_a.set_index('data', inplace=True)

        results = seasonal_decompose(df_ida_a['media'], period=180)
        rolling_avg = df_ida_a['media'].rolling(window=30).mean()

        fig_ida_a4 = go.Figure()
        fig_ida_a4.add_trace(go.Scatter(x=df_ida_a.index, y=results.seasonal, mode='lines', name='Sazonalidade'))
        fig_ida_a4.add_trace(go.Scatter(x=df_ida_a.index, y=rolling_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_ida_a4.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')

        st.plotly_chart(fig_ida_a4, style=style, use_container_width=True)

        # st.dataframe(df_ida_a_filtered)
        st.markdown('***')
        st.markdown("#### Fundamental 1", unsafe_allow_html=True)
        df_ida_f = sql("select * from IDA_f")
        df_ida_f['data'] = pd.to_datetime(df_ida_f['data']).dt.date

        df_ida_f_filtered = df_ida_f[(df_ida_f['data'] >= start_date) & (df_ida_f['data'] <= end_date)]

        if aluno == 'Todos':
            df_ida_f_filtered = df_ida_f_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ida_f_filtered = df_ida_f_filtered[df_ida_f_filtered['matricula'] == matricula]

        cols_pontuacao = df_ida_f_filtered.columns[2:-1]
        df_ida_f_filtered['media'] = df_ida_f_filtered[cols_pontuacao].mean(axis=1)

        df_media_por_data = df_ida_f_filtered.groupby('data')['media'].mean().reset_index()

        fig_ida_f = px.line(df_media_por_data, x='data', y='media', title='Curva de Evolução do Aluno')
        fig_ida_f.update_xaxes(title='Data')
        fig_ida_f.update_yaxes(title='Média de Pontuação')

        st.plotly_chart(fig_ida_f, style = style, use_container_width=True)

        mapper_materias = {
            "lingua_portuguesa": "Língua Portuguesa",
            "matematica": "Matemática",
            "ciencias": "Ciências",
            "historia": "História",
            "geografia": "Geografia",
            "artes": "Artes",
            "educacao_fisica": "Educação Física",
            "ingles": "Inglês"
        }
        
        df_ida_f_pontuacoes = df_ida_f_filtered.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_f_pontuacoes['data'] = df_ida_f_filtered['data']
        df_ida_f_media_por_materia = df_ida_f_pontuacoes.groupby('data').mean().reset_index()

        recent_ida_f_data = df_ida_f_filtered[df_ida_f_filtered['data'] == df_ida_f_filtered['data'].max()]
        df_ida_f_pontuacoes_g = recent_ida_f_data.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_f_pontuacoes_g['data'] = recent_ida_f_data['data']
        df_ida_f_media_por_materia_g = df_ida_f_pontuacoes_g.groupby('data').mean().reset_index()

        df_ida_f_melted = df_ida_f_media_por_materia.melt(id_vars=['data'], var_name='Matéria', value_name='Média')

        fig_ida_f1 = px.line(
            df_ida_f_melted,
            x='data',
            y='Média',
            color='Matéria', 
            title='Evolução do Desempenho do Aluno por Matéria',
            labels={'data': 'Data', 'Média': 'Média de Pontuação', 'Matéria': 'Matéria'}
        )

        fig_ida_f1.update_traces(mode='lines+markers')

        st.plotly_chart(fig_ida_f1, style = style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            fig_ida_f2 = go.Figure()

            for materia in df_ida_f_media_por_materia.columns[1:]:
                fig_ida_f2.add_trace(go.Bar(x=[materia], y=[df_ida_f_media_por_materia[materia].mean()], name=materia))

            fig_ida_f2.update_layout(
                title='Média por Matéria no Último Registro',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_f2, style=style, use_container_width=True)

        with col2:
            fig_ida_f3 = go.Figure()

            for materia in df_ida_f_media_por_materia_g.columns[1:]:
                fig_ida_f3.add_trace(go.Bar(x=[materia], y=[df_ida_f_media_por_materia_g[materia].mean()], name=materia))

            fig_ida_f3.update_layout(
                title='Média Geral por Matéria',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_f3, style=style, use_container_width=True)
        
        df_ida_f['media'] = df_ida_f[cols_pontuacao].mean(axis=1)
        df_ida_f = df_ida_f.groupby('data')['media'].mean().reset_index()
        df_ida_f.set_index('data', inplace=True)

        results_ida_f = seasonal_decompose(df_ida_f['media'], period=180)
        rolling_avg_ida_f = df_ida_f['media'].rolling(window=30).mean()

        fig_ida_f4 = go.Figure()
        fig_ida_f4.add_trace(go.Scatter(x=df_ida_f.index, y=results_ida_f.seasonal, mode='lines', name='Sazonalidade'))
        fig_ida_f4.add_trace(go.Scatter(x=df_ida_f.index, y=rolling_avg_ida_f, mode='lines', name='Média Móvel (30 dias)'))
        fig_ida_f4.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')

        st.plotly_chart(fig_ida_f4, style=style, use_container_width=True)

        # st.dataframe(df_ida_f_filtered)

        st.markdown('***')
        st.markdown("#### Fundamental 2", unsafe_allow_html=True)
        df_ida_f2 =sql("select * from IDA_f2")
        df_ida_f2['data'] = pd.to_datetime(df_ida_f2['data']).dt.date

        df_ida_f2_filtered = df_ida_f2[(df_ida_f2['data'] >= start_date) & (df_ida_f2['data'] <= end_date)]

        if aluno == 'Todos':
            df_ida_f2_filtered = df_ida_f2_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ida_f2_filtered = df_ida_f2_filtered[df_ida_f2_filtered['matricula'] == matricula]

        cols_pontuacao = df_ida_f2_filtered.columns[2:-1]
        df_ida_f2_filtered['media'] = df_ida_f2_filtered[cols_pontuacao].mean(axis=1)

        df_media_por_data = df_ida_f2_filtered.groupby('data')['media'].mean().reset_index()

        fig_ida_f2 = px.line(df_media_por_data, x='data', y='media', title='Curva de Evolução do Aluno')
        fig_ida_f2.update_xaxes(title='Data')
        fig_ida_f2.update_yaxes(title='Média de Pontuação')

        st.plotly_chart(fig_ida_f2, style = style, use_container_width=True)

        mapper_materias = {
            "lingua_portuguesa": "Língua Portuguesa",
            "matematica": "Matemática",
            "ciencias": "Ciências",
            "historia": "História",
            "geografia": "Geografia",
            "artes": "Artes",
            "educacao_fisica": "Educação Física",
            "ingles": "Inglês"
        }
        
        df_ida_f2_pontuacoes = df_ida_f2_filtered.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_f2_pontuacoes['data'] = df_ida_f2_filtered['data']
        df_ida_f2_media_por_materia = df_ida_f2_pontuacoes.groupby('data').mean().reset_index()

        recent_ida_f2_data = df_ida_f2_filtered[df_ida_f2_filtered['data'] == df_ida_f2_filtered['data'].max()]
        df_ida_f2_pontuacoes_g = recent_ida_f2_data.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_f2_pontuacoes_g['data'] = recent_ida_f2_data['data']
        df_ida_f2_media_por_materia_g = df_ida_f2_pontuacoes_g.groupby('data').mean().reset_index()

        df_ida_f2_melted = df_ida_f2_media_por_materia.melt(id_vars=['data'], var_name='Matéria', value_name='Média')

        fig_ida_f21 = px.line(
            df_ida_f2_melted,
            x='data',
            y='Média',
            color='Matéria', 
            title='Evolução do Desempenho do Aluno por Matéria',
            labels={'data': 'Data', 'Média': 'Média de Pontuação', 'Matéria': 'Matéria'}
        )

        fig_ida_f21.update_traces(mode='lines+markers')

        st.plotly_chart(fig_ida_f21, style = style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            fig_ida_f22 = go.Figure()

            for materia in df_ida_f2_media_por_materia.columns[1:]:
                fig_ida_f22.add_trace(go.Bar(x=[materia], y=[df_ida_f2_media_por_materia[materia].mean()], name=materia))

            fig_ida_f22.update_layout(
                title='Média por Matéria no Último Registro',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_f22, style=style, use_container_width=True)

        with col2:
            fig_ida_f23 = go.Figure()

            for materia in df_ida_f2_media_por_materia_g.columns[1:]:
                fig_ida_f23.add_trace(go.Bar(x=[materia], y=[df_ida_f2_media_por_materia_g[materia].mean()], name=materia))

            fig_ida_f23.update_layout(
                title='Média Geral por Matéria',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_f23, style=style, use_container_width=True)
        
        df_ida_f2['media'] = df_ida_f2[cols_pontuacao].mean(axis=1)
        df_ida_f2 = df_ida_f2.groupby('data')['media'].mean().reset_index()
        df_ida_f2.set_index('data', inplace=True)

        results_ida_f2 = seasonal_decompose(df_ida_f2['media'], period=180)
        rolling_avg_ida_f2 = df_ida_f2['media'].rolling(window=30).mean()

        fig_ida_f24 = go.Figure()
        fig_ida_f24.add_trace(go.Scatter(x=df_ida_f2.index, y=results_ida_f2.seasonal, mode='lines', name='Sazonalidade'))
        fig_ida_f24.add_trace(go.Scatter(x=df_ida_f2.index, y=rolling_avg_ida_f2, mode='lines', name='Média Móvel (30 dias)'))
        fig_ida_f24.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')

        st.plotly_chart(fig_ida_f24, style=style, use_container_width=True)

        # st.dataframe(df_ida_f2)
        
        st.markdown('***')
        st.markdown("#### Ensino Médio", unsafe_allow_html=True)
        df_ida_em = sql("select * from IDA_em")
        df_ida_em['data'] = pd.to_datetime(df_ida_em['data']).dt.date

        df_ida_em_filtered = df_ida_em[(df_ida_em['data'] >= start_date) & (df_ida_em['data'] <= end_date)]

        if aluno == 'Todos':
            df_ida_em_filtered = df_ida_em_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ida_em_filtered = df_ida_em_filtered[df_ida_em_filtered['matricula'] == matricula]

        cols_pontuacao = df_ida_em_filtered.columns[2:-1]
        df_ida_em_filtered['media'] = df_ida_em_filtered[cols_pontuacao].mean(axis=1)

        df_media_por_data = df_ida_em_filtered.groupby('data')['media'].mean().reset_index()

        fig_ida_em = px.line(df_media_por_data, x='data', y='media', title='Curva de Evolução do Aluno')
        fig_ida_em.update_xaxes(title='Data')
        fig_ida_em.update_yaxes(title='Média de Pontuação')

        st.plotly_chart(fig_ida_em, style = style, use_container_width=True)

        mapper_materias = {
            "lingua_portuguesa": "Língua Portuguesa",
            "lingua_estrangeira": "Língua Estrangeira",
            "artes": "Artes",
            "matematica": "Matemática",
            "fisica": "Física",
            "quimica": "Química",
            "biologia": "Biologia",
            "astronomia": "Astronomia",
            "historia": "História",
            "geografia": "Geografia",
            "sociologia": "Sociologia",
            "filosofia": "Filosofia",
            "educacao_fisica": "Educação Física"
        }
        
        df_ida_em_pontuacoes = df_ida_em_filtered.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_em_pontuacoes['data'] = df_ida_em_filtered['data']
        df_ida_em_media_por_materia = df_ida_em_pontuacoes.groupby('data').mean().reset_index()

        recent_ida_em_data = df_ida_em_filtered[df_ida_em_filtered['data'] == df_ida_em_filtered['data'].max()]
        df_ida_em_pontuacoes_g = recent_ida_em_data.iloc[:, 2:-1].rename(columns=mapper_materias)
        df_ida_em_pontuacoes_g['data'] = recent_ida_em_data['data']
        df_ida_em_media_por_materia_g = df_ida_em_pontuacoes_g.groupby('data').mean().reset_index()

        df_ida_em_melted = df_ida_em_media_por_materia.melt(id_vars=['data'], var_name='Matéria', value_name='Média')

        fig_ida_em1 = px.line(
            df_ida_em_melted,
            x='data',
            y='Média',
            color='Matéria', 
            title='Evolução do Desempenho do Aluno por Matéria',
            labels={'data': 'Data', 'Média': 'Média de Pontuação', 'Matéria': 'Matéria'}
        )

        fig_ida_em1.update_traces(mode='lines+markers')

        st.plotly_chart(fig_ida_em1, style = style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            fig_ida_em2 = go.Figure()

            for materia in df_ida_em_media_por_materia.columns[1:]:
                fig_ida_em2.add_trace(go.Bar(x=[materia], y=[df_ida_em_media_por_materia[materia].mean()], name=materia))

            fig_ida_em2.update_layout(
                title='Média por Matéria no Último Registro',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_em2, style=style, use_container_width=True)

        with col2:
            fig_ida_em3 = go.Figure()

            for materia in df_ida_em_media_por_materia_g.columns[1:]:
                fig_ida_em3.add_trace(go.Bar(x=[materia], y=[df_ida_em_media_por_materia_g[materia].mean()], name=materia))

            fig_ida_em3.update_layout(
                title='Média Geral por Matéria',
                xaxis_title='Matéria', 
                yaxis_title='Média',
                yaxis=dict(range=[0, 10])
            )
            
            st.plotly_chart(fig_ida_em3, style=style, use_container_width=True)
        
        df_ida_em['media'] = df_ida_em[cols_pontuacao].mean(axis=1)
        df_ida_em = df_ida_em.groupby('data')['media'].mean().reset_index()
        df_ida_em.set_index('data', inplace=True)

        results_ida_em = seasonal_decompose(df_ida_em['media'], period=180)
        rolling_avg_ida_em = df_ida_em['media'].rolling(window=30).mean()

        fig_ida_em4 = go.Figure()
        fig_ida_em4.add_trace(go.Scatter(x=df_ida_em.index, y=results_ida_em.seasonal, mode='lines', name='Sazonalidade'))
        fig_ida_em4.add_trace(go.Scatter(x=df_ida_em.index, y=rolling_avg_ida_em, mode='lines', name='Média Móvel (30 dias)'))
        fig_ida_em4.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')

        st.plotly_chart(fig_ida_em4, style=style, use_container_width=True)

        # st.dataframe(df_ida_em)

    with tab3:
        df_ieg = sql("select * from IEG")
        alunos_df = get_aluno()
        st.markdown("### IEG - Indicadores de Engajamento", unsafe_allow_html=True)

        df_ieg['data'] = pd.to_datetime(df_ieg['data'])
        df_ieg['data'] = df_ieg['data'].dt.date
        df_ieg.sort_values(by='data', inplace=True)

        min_date = df_ieg['data'].min()
        max_date = df_ieg['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start3'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and3'
            )

        df_ieg_filtered = df_ieg[(df_ieg['data'] >= start_date) & (df_ieg['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='ieg')

        if aluno == 'Todos':
            df_ieg_filtered = df_ieg_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ieg_filtered = df_ieg_filtered[df_ieg_filtered['matricula'] == matricula]

        df_ieg_sum = df_ieg_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ieg_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_ieg_sum = df_ieg_sum.sort_values(by='data')

        fig_ieg = px.line(df_ieg_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_ieg.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_ieg, style = style, use_container_width=True)

        df_ieg_seas = df_ieg.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ieg_seas.set_index('data', inplace=True)

        results_ieg = seasonal_decompose(df_ieg_seas['pontuacao'], period=180)
        rolling_ieg_avg = df_ieg_seas['pontuacao'].rolling(window=30).mean()

        fig_ieg1 = go.Figure()

        fig_ieg1.add_trace(go.Scatter(x=df_ieg_seas.index, y=results_ieg.seasonal, mode='lines', name='Sazonalidade'))
        fig_ieg1.add_trace(go.Scatter(x=df_ieg_seas.index, y=rolling_ieg_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_ieg1.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_ieg1, style=style, use_container_width=True)

        recent_ieg_data = df_ieg_filtered[df_ieg_filtered['data'] == df_ieg_filtered['data'].max()]

        mapper_ieg = {
            "interesse_entusiasmo_aulas": "O aluno demonstra interesse e entusiasmo durante as aulas?",
            "participa_ativamente_discussoes_atividades": "Ele participa ativamente das discussões e atividades propostas?",
            "faz_perguntas_busca_tirar_duvidas": "Ele faz perguntas e busca tirar dúvidas quando necessário?",
            "iniciativa_contribuir_turma": "Ele demonstra iniciativa em contribuir com a turma?",
            "acompanha_explicacoes_responde_clareza": "O aluno consegue acompanhar as explicações e responder às perguntas com clareza?",
            "compreensao_conceitos_conteudos": "Ele demonstra compreensão dos conceitos e conteúdos abordados?",
            "aplicar_conhecimento_diferentes_situacoes": "Ele consegue aplicar o conhecimento adquirido em diferentes situações?",
            "identifica_dificuldades_busca_superar": "Ele identifica suas dificuldades e busca formas de superá-las?",
            "progresso_relacao_nivel_inicial": "Ele demonstra progresso em relação ao seu nível inicial de conhecimento?",
            "esforca_melhorar_habilidades_desempenho": "Ele se esforça para melhorar suas habilidades e desempenho?"
        }

        fig_ieg2 = go.Figure()
        
        for pergunta in recent_ieg_data.columns[2:11]:
            pergunta_mapeada = mapper_ieg[pergunta]
            contagem_respostas = recent_ieg_data[pergunta].value_counts()
            fig_ieg2.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig_ieg2.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig_ieg2, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco_ieg = recent_ieg_data['nivel_risco'].value_counts()

            fig_risco_ieg = go.Figure(go.Bar(x=contagem_risco_ieg.index, y=contagem_risco_ieg.values))

            fig_risco_ieg.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ieg, style=style, use_container_width=True)
        with col2:
            contagem_risco_ieg_g = df_ieg_filtered['nivel_risco'].value_counts()

            fig_risco_ieg_g = go.Figure(go.Bar(x=contagem_risco_ieg_g.index, y=contagem_risco_ieg_g.values))

            fig_risco_ieg_g.update_layout(
                title='Contagem de Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ieg_g, style=style, use_container_width=True)

        # st.dataframe(recent_ieg_data)

    with tab4:
        df_iaa = sql("select * from IAA")
        alunos_df = get_aluno()
        st.markdown("### IAA - Indicador de AutoAvaliação", unsafe_allow_html=True)

        df_iaa['data'] = pd.to_datetime(df_iaa['data'])
        df_iaa['data'] = df_iaa['data'].dt.date
        df_iaa.sort_values(by='data', inplace=True)

        min_date = df_iaa['data'].min()
        max_date = df_iaa['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start4'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and4'
            )

        df_iaa_filtered = df_iaa[(df_iaa['data'] >= start_date) & (df_iaa['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='iaa')

        if aluno == 'Todos':
            df_iaa_filtered = df_iaa_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_iaa_filtered = df_iaa_filtered[df_iaa_filtered['matricula'] == matricula]

        df_iaa_sum = df_iaa_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_iaa_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_iaa_sum = df_iaa_sum.sort_values(by='data')

        fig_iaa = px.line(df_iaa_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_iaa.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_iaa, style = style, use_container_width=True)

        df_iaa_seas = df_iaa.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_iaa_seas.set_index('data', inplace=True)

        results_iaa = seasonal_decompose(df_iaa_seas['pontuacao'], period=180)
        rolling_iaa_avg = df_iaa_seas['pontuacao'].rolling(window=30).mean()

        fig_iaa1 = go.Figure()

        fig_iaa1.add_trace(go.Scatter(x=df_iaa_seas.index, y=results_iaa.seasonal, mode='lines', name='Sazonalidade'))
        fig_iaa1.add_trace(go.Scatter(x=df_iaa_seas.index, y=rolling_iaa_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_iaa1.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_iaa1, style=style, use_container_width=True)

        recent_iaa_data = df_iaa_filtered[df_iaa_filtered['data'] == df_iaa_filtered['data'].max()]

        mapper_iaa = {
            "faz_perguntas_tira_duvidas": "Ele faz perguntas e busca tirar dúvidas quando necessário?",
            "busca_feedback_utiliza_aprimorar_aprendizado": "Você busca feedback e utiliza-o para aprimorar seu aprendizado?",
            "reconhece_pontos_fortes_areas_desenvolvimento": "Você reconhece seus pontos fortes e áreas de desenvolvimento?",
            "sente_satisfeito_progresso_desenvolvimento": "Você se sente satisfeito com seu progresso e desenvolvimento?",
            "acredita_aprendendo_tornando_mais_capaz": "Você acredita que está aprendendo e se tornando mais capaz?",
            "reconhece_importancia_educacao_para_futuro": "Você reconhece a importância da educação para seu futuro?",
            "sente_motivado_continuar_aprendendo_desafiando": "Você se sente motivado a continuar aprendendo e se desafiando?",
            "organiza_gerencia_tempo_forma_eficiente": "Você organiza e gerencia seu tempo de forma eficiente?",
            "busca_conectar_outros_alunos_profissionais": "Você busca se conectar com outros alunos e profissionais da área?",
            "tem_iniciativa_autonomia_estudos": "Você têm iniciativa e autonomia em seus estudos?"
        }

        fig_iaa2 = go.Figure()
        
        for pergunta in recent_iaa_data.columns[2:11]:
            pergunta_mapeada = mapper_iaa[pergunta]
            contagem_respostas = recent_iaa_data[pergunta].value_counts()
            fig_iaa2.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig_iaa2.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig_iaa2, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco_iaa = recent_iaa_data['nivel_risco'].value_counts()

            fig_risco_iaa = go.Figure(go.Bar(x=contagem_risco_iaa.index, y=contagem_risco_iaa.values))

            fig_risco_iaa.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_iaa, style=style, use_container_width=True)
        with col2:
            contagem_risco_iaa_g = df_iaa_filtered['nivel_risco'].value_counts()

            fig_risco_iaa_g = go.Figure(go.Bar(x=contagem_risco_iaa_g.index, y=contagem_risco_iaa_g.values))

            fig_risco_iaa_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_iaa_g, style=style, use_container_width=True)

        # st.dataframe(recent_iaa_data)

    with tab5:
        df_ips = sql("select * from IPS")
        alunos_df = get_aluno()
        st.markdown("### IPS - Indicador Psicossocial", unsafe_allow_html=True)

        df_ips['data'] = pd.to_datetime(df_ips['data'])
        df_ips['data'] = df_ips['data'].dt.date
        df_ips.sort_values(by='data', inplace=True)

        min_date = df_ips['data'].min()
        max_date = df_ips['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start5'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and5'
            )

        df_ips_filtered = df_ips[(df_ips['data'] >= start_date) & (df_ips['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='ips')

        if aluno == 'Todos':
            df_ips_filtered = df_ips_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ips_filtered = df_ips_filtered[df_ips_filtered['matricula'] == matricula]

        df_ips_sum = df_ips_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ips_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_ips_sum = df_ips_sum.sort_values(by='data')

        fig_ips = px.line(df_ips_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_ips.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_ips, style = style, use_container_width=True)

        df_ips_seas = df_ips.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ips_seas.set_index('data', inplace=True)

        results_ips = seasonal_decompose(df_ips_seas['pontuacao'], period=180)
        rolling_ips_avg = df_ips_seas['pontuacao'].rolling(window=30).mean()

        fig_ips1 = go.Figure()

        fig_ips1.add_trace(go.Scatter(x=df_ips_seas.index, y=results_ips.seasonal, mode='lines', name='Sazonalidade'))
        fig_ips1.add_trace(go.Scatter(x=df_ips_seas.index, y=rolling_ips_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_ips1.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_ips1, style=style, use_container_width=True)

        recent_ips_data = df_ips_filtered[df_ips_filtered['data'] == df_ips_filtered['data'].max()]

        mapper_ips = {
                "bom_relacionamento_familiares": "Ambiente Familiar: Você tem um bom relacionamento com seus familiares?",
                "amigos_com_quem_contar": "Vida Social: Você tem amigos com quem você pode contar?",
                "sente_bem_consigo_vida": "Saúde Mental: Você se sente bem consigo mesmo e com sua vida?",
                "acredita_alcancar_objetivos": "Autoestima: Você acredita que é capaz de alcançar seus objetivos?",
                "acredita_aprendendo_progredindo_estudos": "Desempenho Escolar: Você acredita que está aprendendo e progredindo em seus estudos?",
                "tem_plano_alcancar_objetivos": "Planos para o Futuro: Você tem um plano para alcançar seus objetivos?",
                "alimenta_saudavel_pratica_atividades_fisicas": "Hábitos de Vida: Você se alimenta de forma saudável e pratica atividades físicas regularmente?",
                "nao_pressionado_usar_drogas_bebidas_alcoolicas": "Uso de Substâncias: Você não se sente pressionado a usar drogas ou bebidas alcoólicas?",
                "se_sente_seguro_casa_escola_comunidade": "Violência: Você se sente seguro em casa, na escola e na comunidade?",
                "sabe_buscar_ajuda_quando_precisa": "Rede de Apoio: Você sabe como buscar ajuda quando precisa?"
            }

        fig_ips2 = go.Figure()
        
        for pergunta in recent_ips_data.columns[2:11]:
            pergunta_mapeada = mapper_ips[pergunta]
            contagem_respostas = recent_ips_data[pergunta].value_counts()
            fig_ips2.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig_ips2.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig_ips2, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco_ips = recent_ips_data['nivel_risco'].value_counts()

            fig_risco_ips = go.Figure(go.Bar(x=contagem_risco_ips.index, y=contagem_risco_ips.values))

            fig_risco_ips.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ips, style=style, use_container_width=True)
        with col2:
            contagem_risco_ips_g = df_ips_filtered['nivel_risco'].value_counts()

            fig_risco_ips_g = go.Figure(go.Bar(x=contagem_risco_ips_g.index, y=contagem_risco_ips_g.values))

            fig_risco_ips_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ips_g, style=style, use_container_width=True)

        # st.dataframe(recent_ips_data)

    with tab6:
        df_ipp = sql("select * from IPP")
        alunos_df = get_aluno()
        st.markdown("### IPP - Indicadores Psicopedagógicos", unsafe_allow_html=True)

        df_ipp['data'] = pd.to_datetime(df_ipp['data'])
        df_ipp['data'] = df_ipp['data'].dt.date
        df_ipp.sort_values(by='data', inplace=True)

        min_date = df_ipp['data'].min()
        max_date = df_ipp['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start6'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and6'
            )

        df_ipp_filtered = df_ipp[(df_ipp['data'] >= start_date) & (df_ipp['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='ipp')

        if aluno == 'Todos':
            df_ipp_filtered = df_ipp_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ipp_filtered = df_ipp_filtered[df_ipp_filtered['matricula'] == matricula]

        df_ipp_sum = df_ipp_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ipp_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_ipp_sum = df_ipp_sum.sort_values(by='data')

        fig_ipp = px.line(df_ipp_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_ipp.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_ipp, style = style, use_container_width=True)

        df_ipp_seas = df_ipp.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ipp_seas.set_index('data', inplace=True)

        results_ipp = seasonal_decompose(df_ipp_seas['pontuacao'], period=180)
        rolling_ipp_avg = df_ipp_seas['pontuacao'].rolling(window=30).mean()

        fig_ipp1 = go.Figure()

        fig_ipp1.add_trace(go.Scatter(x=df_ipp_seas.index, y=results_ipp.seasonal, mode='lines', name='Sazonalidade'))
        fig_ipp1.add_trace(go.Scatter(x=df_ipp_seas.index, y=rolling_ipp_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_ipp1.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_ipp1, style=style, use_container_width=True)

        recent_ipp_data = df_ipp_filtered[df_ipp_filtered['data'] == df_ipp_filtered['data'].max()]

        mapper_ipp = {
            "participa_ativamente_responde_perguntas_clareza": "Aprendizagem: Ele participa ativamente das aulas e responde às perguntas com clareza?",
            "relaciona_respeitosamente_cooperativamente_colegas": "Comportamento: Ele se relaciona com os colegas de forma respeitosa e cooperativa?",
            "dificuldades_comunicacao_oral_escrita": "Comunicação: Ele apresenta dificuldades na comunicação oral ou escrita?",
            "demonstra_coordenacao_destreza_atividades": "Habilidades Motoras: Ele demonstra coordenação motora e destreza nas atividades?",
            "demonstra_empatia_respeito_outros": "Desenvolvimento Social: Ele demonstra empatia e respeito pelos outros?",
            "reconhece_pontos_fortes_areas_desenvolvimento": "Autoestima: Ele reconhece seus pontos fortes e áreas de desenvolvimento?",
            "consegue_concentrar_tarefas_lembrar_informacoes_resolver_problemas": "Funções Cognitivas: Ele consegue se concentrar nas tarefas, lembrar de informações e resolver problemas?",
            "habilidades_academicas_leitura_escrita_calculos_fluencia_compreensao": "Habilidades Acadêmicas: O aluno lê, escreve e faz cálculos matemáticos com fluência e compreensão?",
            "saude_emocional_aluno_feliz_seguro_escola_casa": "Saúde Emocional: O aluno se sente feliz e seguro na escola e em casa?",
            "acesso_recursos_socioeconomicos_adequados_desenvolvimento": "Condições Socioeconômicas: O aluno tem acesso a recursos materiais e sociais adequados para seu desenvolvimento?"
        }

        fig_ipp2 = go.Figure()
        
        for pergunta in recent_ipp_data.columns[2:11]:
            pergunta_mapeada = mapper_ipp[pergunta]
            contagem_respostas = recent_ipp_data[pergunta].value_counts()
            fig_ipp2.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig_ipp2.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig_ipp2, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco_ipp = recent_ipp_data['nivel_risco'].value_counts()

            fig_risco_ipp = go.Figure(go.Bar(x=contagem_risco_ipp.index, y=contagem_risco_ipp.values))

            fig_risco_ipp.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ipp, style=style, use_container_width=True)
        with col2:
            contagem_risco_ipp_g = df_ipp_filtered['nivel_risco'].value_counts()

            fig_risco_ipp_g = go.Figure(go.Bar(x=contagem_risco_ipp_g.index, y=contagem_risco_ipp_g.values))

            fig_risco_ipp_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ipp_g, style=style, use_container_width=True)

        # st.dataframe(df_ipp)

    with tab7:
        st.markdown("### IPV - Indicadores do Ponto de Virada", unsafe_allow_html=True)

        df_ipv = sql("select * from IPV")
        alunos_df = get_aluno()
        df_ipv['data'] = pd.to_datetime(df_ipv['data'])
        df_ipv['data'] = df_ipv['data'].dt.date
        df_ipv.sort_values(by='data', inplace=True)

        min_date = df_ipv['data'].min()
        max_date = df_ipv['data'].max()
        data_atual = datetime.now().date()
        data_inicio_default = max(min_date, (pd.Timestamp(data_atual) - pd.DateOffset(months=6)).date())
        data_fim_default = max_date

        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input(
                "Selecione a data de início", 
                min_value=min_date,
                max_value=max_date,
                value=data_inicio_default,
                key='start7'
            )

        with col2:
            end_date = st.date_input(
                "Selecione a data de fim", 
                min_value=min_date,
                max_value=max_date,
                value=data_fim_default,
                key='and7'
            )

        df_ipv_filtered = df_ipv[(df_ipv['data'] >= start_date) & (df_ipv['data'] <= end_date)]
        alunos_list = ['Todos'] + alunos_df['Nome_Completo'].tolist()
        aluno = st.selectbox("Selecione o aluno:", alunos_list, key='ipv')

        if aluno == 'Todos':
            df_ipv_filtered = df_ipv_filtered.copy()
        else:
            matricula = alunos_df.loc[alunos_df['Nome_Completo'] == aluno, 'Matricula'].values[0]  
            df_ipv_filtered = df_ipv_filtered[df_ipv_filtered['matricula'] == matricula]

        df_ipv_sum = df_ipv_filtered.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ipv_sum.rename(columns={'nivel_risco': 'Contagem'}, inplace=True)
        df_ipv_sum = df_ipv_sum.sort_values(by='data')

        fig_ipv = px.line(df_ipv_sum, x='data', y='pontuacao', title='Evolução do Índice ao Longo do Tempo')
        fig_ipv.update_layout(xaxis_title='Data', yaxis_title='Pontuação Total')
        st.plotly_chart(fig_ipv, style = style, use_container_width=True)

        df_ipv_seas = df_ipv.groupby('data').agg({'pontuacao': 'sum'}).reset_index()
        df_ipv_seas.set_index('data', inplace=True)

        results_ipv = seasonal_decompose(df_ipv_seas['pontuacao'], period=180)
        rolling_ipv_avg = df_ipv_seas['pontuacao'].rolling(window=30).mean()

        fig_ipv1 = go.Figure()

        fig_ipv1.add_trace(go.Scatter(x=df_ipv_seas.index, y=results_ipv.seasonal, mode='lines', name='Sazonalidade'))
        fig_ipv1.add_trace(go.Scatter(x=df_ipv_seas.index, y=rolling_ipv_avg, mode='lines', name='Média Móvel (30 dias)'))
        fig_ipv1.update_layout(title='Sazonalidade e Média Móvel', xaxis_title='Data', yaxis_title='Valor')
        st.plotly_chart(fig_ipv1, style=style, use_container_width=True)

        recent_ipv_data = df_ipv_filtered[df_ipv_filtered['data'] == df_ipv_filtered['data'].max()]

        mapper_ipv = {
            "sabe_identificar_interesses_habilidades_paixoes": "Autoconhecimento: Você sabe identificar seus principais interesses, habilidades e paixões?",
            "assume_responsabilidade_processo_aprendizado": "Autonomia e Responsabilidade: Você assume total responsabilidade pelo seu processo de aprendizado?",
            "sente_entusiasmado_motivado_atividades_aprendizagem": "Motivação e Engajamento: Você se sente entusiasmado e motivado com as atividades de aprendizagem?",
            "experimentou_diferentes_metodos_aprendizado_encontrar_melhor": "Experimentação e Adaptabilidade: Você já experimentou diferentes métodos de aprendizado para encontrar o que funciona melhor para você?",
            "participa_ativamente_aulas_busca_compreender_conceitos": "Aprendizagem Ativa e Reflexiva: Você participa ativamente das aulas e busca compreender os conceitos por trás do que está aprendendo?",
            "aprende_com_erros_esforca_superar_dificuldades_persistencia": "Resiliência e Persistência: Você aprende com seus erros e se esforça para superar as dificuldades com persistência?",
            "define_metas_claras_longo_prazo_trajetoria_educacional": "Planejamento e Metas: Você define metas claras e de longo prazo para sua trajetória educacional?",
            "busca_ajuda_professores_colegas_mentores_profissionais": "Busca por Recursos e Apoio: Você busca ajuda de professores, colegas, mentores ou outros profissionais quando precisa?",
            "visualiza_como_educacao_ajudara_alcancar_sonhos_objetivos_vida": "Visão de Futuro e Propósito: Você consegue visualizar como a educação te ajudará a alcançar seus sonhos e objetivos de vida?",
            "considera_aprendiz_constante_busca_novas_informacoes_habilidades": "Aprendizagem Contínua: Você se considera um aprendiz constante, sempre buscando novas informações e habilidades?"
        }

        fig_ipv2 = go.Figure()
        
        for pergunta in recent_ipv_data.columns[2:11]:
            pergunta_mapeada = mapper_ipv[pergunta]
            contagem_respostas = recent_ipv_data[pergunta].value_counts()
            fig_ipv2.add_trace(go.Bar(x=contagem_respostas.index, y=contagem_respostas.values, name=pergunta_mapeada))

        fig_ipv2.update_layout(
            barmode='group', 
            title='Respostas nas Últimas Avaliações',
            xaxis_title='Resposta', 
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig_ipv2, style=style, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_risco_ipv = recent_ipv_data['nivel_risco'].value_counts()

            fig_risco_ipv = go.Figure(go.Bar(x=contagem_risco_ipv.index, y=contagem_risco_ipv.values))

            fig_risco_ipv.update_layout(
                title='Risco nas Últimas Avaliações',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ipv, style=style, use_container_width=True)
        with col2:
            contagem_risco_ipv_g = df_ipv_filtered['nivel_risco'].value_counts()

            fig_risco_ipv_g = go.Figure(go.Bar(x=contagem_risco_ipv_g.index, y=contagem_risco_ipv_g.values))

            fig_risco_ipv_g.update_layout(
                title='Risco Geral',
                xaxis_title='Risco', 
                yaxis_title='Contagem'
            )
            
            st.plotly_chart(fig_risco_ipv_g, style=style, use_container_width=True)
        # st.dataframe(df_ipv)
            
    with tab8:
        st.markdown('#### Dados de Cadastro INDE')
        df_cadastro = sql("select * from CadastroAlunos")

        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_sexo = df_cadastro['Sexo'].value_counts()
            fig_c = go.Figure(data=[go.Pie(
                labels=contagem_sexo.index, 
                values=contagem_sexo.values, 
                hole=.5,
                textinfo='percent+value', 
                hoverinfo='percent+value'
            )])

            fig_c.update_layout(
                title='Estudantes por Gênero',
                title_y=0.90
            )

            st.plotly_chart(fig_c, style=style, use_container_width=True)

        with col2:
            today = pd.Timestamp.now()
            df_cadastro['Data_de_Nascimento'] = pd.to_datetime(df_cadastro['Data_de_Nascimento'])

            today = pd.Timestamp.now()
            df_cadastro['Idade'] = (today - df_cadastro['Data_de_Nascimento']).dt.days // 365

            fig_c1 = px.histogram(
                df_cadastro, x='Idade', color='Sexo', 
                title='Distribuição por Sexo e Idade',
                labels={'Idade': 'Idade (anos)', 'count': 'Contagem', 'Sexo': 'Sexo'}
            )

            fig_c1.update_traces(marker=dict(line=dict(width=0.5)))
            st.plotly_chart(fig_c1, use_container_width=True)
        
        st.markdown('***')
        col1, col2 = st.columns([1, 1])
        with col1:
            contagem_sexo = df_cadastro['Bolsista_ou_Escola_Publica'].value_counts()
            fig_c2 = go.Figure(data=[go.Pie(
                labels=contagem_sexo.index, 
                values=contagem_sexo.values,
                hole=.5, 
                textinfo='percent+value', 
                hoverinfo='percent+value')]
            )
            fig_c2.update_layout(
                title='Vinculo',
                title_y=0.90
            )

            st.plotly_chart(fig_c2, style=style, use_container_width=True)
            
        with col2:
            contagem_instituicao = df_cadastro['Instituicao_Onde_Estuda'].value_counts()
            
            fig_c3 = go.Figure(data=[go.Pie(
                labels=contagem_instituicao.index, 
                values=contagem_instituicao.values,
                hole=.5, 
                textinfo='percent+value', 
                hoverinfo='percent+value')]
            )
            fig_c3.update_layout(
                title='Distribuição por Instituição de Ensino',
                title_y=0.90
            )

            st.plotly_chart(fig_c3, style=style, use_container_width=True)

        st.markdown('***')
        st.markdown('#### IDNE Fases 0˜4 e Fase 8')
        col1, col2 = st.columns([1, 1])
        with col1:
            soma_alf = df_alf['pontuacao'].mean()
            soma_em = df_em['pontuacao'].mean()
            soma_fund = df_fund['pontuacao'].mean()
            soma_fund2 = df_fund2['pontuacao'].mean()
            resultado_ian = (soma_alf + soma_em + soma_fund + soma_fund2) * 0.1

            soma_ida_a = df_ida_a['media'].mean()
            soma_ida_f = df_ida_f['media'].mean()
            soma_ida_f2 = df_ida_f2['media'].mean()
            soma_ida_em = df_ida_em['media'].mean()
            resultado_ida = (soma_ida_a + soma_ida_f + soma_ida_f2 + soma_ida_em) * 0.2

            soma_ieg = df_ieg['pontuacao'].mean()
            resultado_ieg = soma_ieg * 0.2

            soma_iaa = df_iaa['pontuacao'].mean()
            resultado_iaa = soma_iaa * 0.1

            soma_ips = df_ips['pontuacao'].mean()
            resultado_ips = soma_ips * 0.1

            soma_ipp = df_ipp['pontuacao'].mean()
            resultado_ipp = soma_ipp * 0.1

            soma_ipv = df_ipv['pontuacao'].mean()
            resultado_ipv = soma_ipv * 0.2

            idne = {
                'Fase': ['IAN', 'EDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV'],
                'Resultado': [resultado_ian, resultado_ida, resultado_ieg, resultado_iaa, resultado_ips, resultado_ipp, resultado_ipv]
            }
            df_idne = pd.DataFrame(idne)

            fig_c4 = go.Figure(data=[go.Pie(
                labels=df_idne['Fase'], 
                values=df_idne['Resultado'],
                hole=.5, 
                title=f"INDE Geral  {df_idne['Resultado'].mean().round(2)}",
                textinfo='percent', 
                hoverinfo='percent')]
            )

            st.plotly_chart(fig_c4, style=style, use_container_width=True)
            
        with col2:
            soma_alf = df_alf['pontuacao'].mean()
            soma_em = df_em['pontuacao'].mean()
            soma_fund = df_fund['pontuacao'].mean()
            soma_fund2 = df_fund2['pontuacao'].mean()
            resultado_ian = (soma_alf + soma_em + soma_fund + soma_fund2) * 0.1

            soma_ida_a = df_ida_a['media'].mean()
            soma_ida_f = df_ida_f['media'].mean()
            soma_ida_f2 = df_ida_f2['media'].mean()
            soma_ida_em = df_ida_em['media'].mean()
            resultado_ida = (soma_ida_a + soma_ida_f + soma_ida_f2 + soma_ida_em) * 0.4

            soma_ieg = df_ieg['pontuacao'].mean()
            resultado_ieg = soma_ieg * 0.2

            soma_iaa = df_iaa['pontuacao'].mean()
            resultado_iaa = soma_iaa * 0.1

            soma_ips = df_ips['pontuacao'].mean()
            resultado_ips = soma_ips * 0.2

            idne = {
                'Fase': ['IAN', 'EDA', 'IEG', 'IAA', 'IPS'],
                'Resultado': [resultado_ian, resultado_ida, resultado_ieg, resultado_iaa, resultado_ips ]
            }

            df_idne = pd.DataFrame(idne)
            
            fig_c5 = go.Figure(data=[go.Pie(
                labels=df_idne['Fase'], 
                values=df_idne['Resultado'],
                hole=.5, 
                title=f"INDE Geral  {df_idne['Resultado'].mean().round(2)}",
                textinfo='percent',
                hoverinfo='percent')]
            )

            st.plotly_chart(fig_c5, style=style, use_container_width=True)

def painelCadastro():
    st.markdown('#### Cadastro de Alunos')
    matricula_n = sql("SELECT MAX(Matricula) matricula FROM CadastroAlunos")

    matricula_atual = int(matricula_n.iloc[0, 0][1:])
    nova_matricula = f"M{matricula_atual + 1:06d}" 
    matricula = nova_matricula

    col1, col2 = st.columns([1, 1])
    with col1:
        nome = st.text_input('Nome')
    with col2:
        sobrenome = st.text_input('Sobrenome')

    col3, col4 = st.columns([1, 1])
    with col3:
        data_nascimento = st.date_input('Data de Nascimento')
    with col4:
        serie = st.text_input('Série')

    col5, col6 = st.columns([1, 1])
    with col5:
        sexo = st.radio('Sexo', ('Masculino', 'Feminino'))
    with col6:
        ingresso = st.date_input('Data de Ingresso')

    col7, col8 = st.columns([1, 1])
    with col7:
        evasao = st.date_input('Evasão', None)
    with col8:
        data_conclusao = st.date_input('Data da Conclusão', None)

    col9, col10 = st.columns([1, 1])
    with col9:
        bolsista_ou_escola_publica = st.selectbox('Bolsista ou Escola Pública', ['Bolsista', 'Escola pública'])
    with col10:
        instituicao_onde_estuda = st.selectbox('Instituição Onde Estuda', ['Centro', 'Filipinho', 'Cipó', 'Granjinha'])

    col11, col12 = st.columns([1, 1])
    with col11:
        endereco = st.text_input('Endereço')
    with col12:
        telefone = st.text_input('Telefone')

    if st.button('Cadastrar', key='cadastroaluno'):
        df_cadastro = criar_df_cadastro(matricula, nome, sobrenome, data_nascimento, serie, sexo, ingresso, 
                                         evasao, data_conclusao, bolsista_ou_escola_publica, 
                                         instituicao_onde_estuda, endereco, telefone)


        questionario_salvo = CadastroAlunoSalvo(df_cadastro)
        result = questionario_salvo.save()
        if result:
            del df_cadastro
            st.success('Cadastro realizado com sucesso!')

def criar_df_cadastro(matricula, nome, sobrenome, data_nascimento, serie, sexo, ingresso, evasao, 
                      data_conclusao, bolsista_ou_escola_publica, instituicao_onde_estuda, 
                      endereco, telefone):
    data = {
        'Matricula': [matricula],
        'Nome': [nome],
        'Sobrenome': [sobrenome],
        'Data_de_Nascimento': [data_nascimento],
        'Serie': [serie],
        'Sexo': [sexo],
        'Ingresso': [ingresso],
        'Evasao': [evasao],
        'Data_da_Conclusao': [data_conclusao],
        'Bolsista_ou_Escola_Publica': [bolsista_ou_escola_publica],
        'Instituicao_Onde_Estuda': [instituicao_onde_estuda],
        'Endereco': [endereco],
        'Telefone': [telefone]
    }
    df = pd.DataFrame(data)
    return df


def main():
    st.set_page_config(page_title='Passos Mágicos', page_icon=':bar_chart:', layout='wide')
    # logo_url = 'https://github.com/MCardosoDev/Tech_Challenge_Fase5/raw/main/PassosMagicos/logo.png'
    logo_url = './Images/Logo.png'
    st.sidebar.image(logo_url, width=250)
    view = st.sidebar.radio(
            'Painéis',
            (
                'INDE',
                'Avaliações 📝',
                'Analises 📈'
            )
        )
    
    if view == 'INDE':
        st.markdown("#### METODOLOGIA")
        st.markdown("##### A organização atende crianças e jovens de 6 a 18 anos, em comunidades de baixa renda em Embu - Guaçu, SP. ")
        st.image('./Images/image.png')
        st.markdown("***")
        st.markdown("##### Índice de Desenvolvimento Educacional")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("PEGAGÓCIGO: 1")
        with col2:
            st.markdown("""
                IAN - Indicador de Adequação de Nível


                IDA - Indicador de Desempenho Acadêmico


                IEG - Indicador de Engajamento
            """)
        st.markdown("***")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("PSICOSSOCIAL: 2")
        with col2:
            st.markdown("""
                IAA - indicador de Autoavaliação

                IPS - Indicador Psicossocial
            """)
        st.markdown("***")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("PSICOPEDAGÓCIGO: 3")
        with col2:
            st.markdown("""
                IPP - Indicador PsicoPedagógico

                IPV - Indicador de Ponto de virada
            """)
        st.markdown("***")
        st.markdown("##### Ponderação Dos Indicaroes no INDE")
        st.image('./Images/inde.png')

    elif view == 'Avaliações 📝':
        def display_panel(user_menu):
            if user_menu == 'IAN':
                with st.spinner("Carregando questionários..."):
                    panelIAN()
            elif user_menu == 'IEG':
                with st.spinner("Carregando questionários..."):
                    panelIEG()
            elif user_menu == 'IAA':
                with st.spinner("Carregando questionários..."):
                    panelIAA()
            elif user_menu == 'IDA':
                with st.spinner("Carregando questionários..."):
                    panelIDA()
            elif user_menu == 'IPP':
                with st.spinner("Carregando questionários..."):
                    panelIPP()
            elif user_menu == 'IPS':
                with st.spinner("Carregando questionários..."):
                    panelIPS()
            elif user_menu == 'IPV':
                with st.spinner("Carregando questionários..."):
                    panelIPV()
            elif user_menu == 'dash':
                with st.spinner("Carregando o Painel de Acompanhamento..."):
                    panelDash()
            elif user_menu == 'cadastro':
                with st.spinner("Carregando o Painel de Acompanhamento..."):
                    painelCadastro()

        session_state = st.session_state
        if 'user_menu' not in session_state:
            session_state.user_menu = 'Home'

        if session_state.user_menu == 'Home':          
            st.markdown(
                f"""
                <style>
                .top-bar {{
                    background-color: transparent;
                    padding: 10px;
                    border-radius: 0 0 10px 10px;
                    margin-bottom: 20px;
                }}
                .top-bar h1 {{
                    color: #0c51a1;
                    text-align: center;
                    font-size: 50px;
                }}
                </style>
                <div class="top-bar">
                    <h1>Analytics</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("Bem-vindo ao Analytics, a solução para análise em todos os aspectos da Passos Mágicos.")
            st.write("Abaixo estão os Questionarios dos Indicadores.")
            st.write("----")
            
            col, col0 = st.columns([1, 2])
            with col:
                if st.button("Cadastro Novos Alunos 📝", key='Cadastro', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'cadastro'
                    st.rerun()
            st.markdown('***')

            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.write("Indicadores de Adequação de Nível")
                if st.button("IAN 📝", key='IAN', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IAN'
                    st.rerun()

            with col2:
                st.write("Indicadores de Engajamento")
                if st.button("IEG 📝", key='IEG', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IEG'
                    st.rerun()
            
            with col3:
                st.write("Indicador de AutoAvaliação")
                if st.button("IAA 📝", key='IAA', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IAA'
                    st.rerun()
            st.markdown('***')

            col7, col8 = st.columns([1, 2])
            with col7:
                st.write("Indicador de Desenvolvimento Acadêmico")
                if st.button("IDA 📝", key='IDA', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IDA'
                    st.rerun()
            st.markdown('***')

            col4, col5, col6 = st.columns([1, 1, 1])
            with col4:
                st.write("Indicadores Psicopedagógicos")
                if st.button("IPP 📝", key='IPP', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IPP'
                    st.rerun()
            
            with col5:
                st.write("Indicador Psicossocial")
                if st.button("IPS 📝", key='IPS', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IPS'
                    st.rerun()
            
            with col6:
                st.write("Indicadores do Ponto de Virada")
                if st.button("IPV 📝", key='IPV', help="Acesse os questionários da plataforma", use_container_width=True):
                    session_state.user_menu = 'IPV'
                    st.rerun()
        
        if st.sidebar.button("Menu Principal"):
            session_state.user_menu = 'Home'
            display_panel(session_state.user_menu)
            st.rerun()

        display_panel(session_state.user_menu)
        st.sidebar.divider()           

    elif view == 'Analises 📈':
        with st.spinner("Carregando o Painel de Acompanhamento..."):
            panelDash()

if __name__ == "__main__":
    main()