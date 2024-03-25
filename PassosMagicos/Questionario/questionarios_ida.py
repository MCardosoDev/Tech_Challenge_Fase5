import streamlit as st

class QuestionariosIDA:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IDA':
            literacy_questions = [
                "Língua Portuguesa",
                "Matemática",
                "Ciências",
                "Artes: Desenvolvimento da criatividade e da expressão artística",
                "Educação Física: Desenvolvimento das habilidades motoras, coordenação e lateralidade"
            ]
            
            col1, col2 = st.columns(2)
            for i, question in enumerate(literacy_questions):
                if i % 2 == 0:
                    with col1:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"alf_{question}")
                        answers[question] = answer
                else:
                    with col2:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"alf_{question}")
                        answers[question] = answer

        elif tab == 'IDA_f':
            fundamental_questions = [
                "Língua Portuguesa",
                "Matemática",
                "Ciências",
                "História",
                "Geografia",
                "Artes",
                "Educação Física",
                "Inglês"
            ]
            
            col1, col2 = st.columns(2)
            for i, question in enumerate(fundamental_questions):
                if i % 2 == 0:
                    with col1:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"f_{question}")
                        answers[question] = answer
                else:
                    with col2:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"f_{question}")
                        answers[question] = answer
                
        elif tab == 'IDA_f2':
            fundamental2_questions = [
                "Língua Portuguesa",
                "Matemática",
                "Ciências",
                "História",
                "Geografia",
                "Artes",
                "Educação Física",
                "Inglês"
            ]
            
            col1, col2 = st.columns(2)
            for i, question in enumerate(fundamental2_questions):
                if i % 2 == 0:
                    with col1:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"f2_{question}")
                        answers[question] = answer
                else:
                    with col2:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"f2_{question}")
                        answers[question] = answer

        elif tab == 'IDA_em':
            high_school_questions = [
                "Língua Portuguesa",
                "Língua Estrangeira",
                "Artes",
                "Matemática",
                "Física",
                "Química",
                "Biologia",
                "Astronomia",
                "História",
                "Geografia",
                "Sociologia",
                "Filosofia",
                "Educação Física"
            ]

            col1, col2 = st.columns(2)
            for i, question in enumerate(high_school_questions):
                if i % 2 == 0:
                    with col1:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"em_{question}")
                        answers[question] = answer
                else:
                    with col2:
                        answer = st.number_input(question, min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"em_{question}")
                        answers[question] = answer

        return answers