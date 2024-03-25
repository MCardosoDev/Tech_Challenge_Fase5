import streamlit as st

class QuestionariosIEG:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IEG':
            general_questions = [
                "O aluno demonstra interesse e entusiasmo durante as aulas?",
                "Ele participa ativamente das discussões e atividades propostas?",
                "Ele faz perguntas e busca tirar dúvidas quando necessário?",
                "Ele demonstra iniciativa em contribuir com a turma?",
                "O aluno consegue acompanhar as explicações e responder às perguntas com clareza?",
                "Ele demonstra compreensão dos conceitos e conteúdos abordados?",
                "Ele consegue aplicar o conhecimento adquirido em diferentes situações?",
                "Ele identifica suas dificuldades e busca formas de superá-las?",
                "O aluno demonstra progresso em relação ao seu nível inicial de conhecimento?",
                "Ele se esforça para melhorar suas habilidades e desempenho?"
            ]
            
            for i, question in enumerate(general_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"ger_{i}")
                answers[question] = answer

        return answers