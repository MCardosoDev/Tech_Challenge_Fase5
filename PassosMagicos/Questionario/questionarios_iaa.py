import streamlit as st

class QuestionariosIAA:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IAA':
            general_questions = [
                "Ele faz perguntas e busca tirar dúvidas quando necessário?",
                "Você busca feedback e utiliza-o para aprimorar seu aprendizado?",
                "Você reconhece seus pontos fortes e áreas de desenvolvimento?",
                "Você se sente satisfeito com seu progresso e desenvolvimento?",
                "Você acredita que está aprendendo e se tornando mais capaz?",
                "Você reconhece a importância da educação para seu futuro?",
                "Você se sente motivado a continuar aprendendo e se desafiando?",
                "Você organiza e gerencia seu tempo de forma eficiente?",
                "Você busca se conectar com outros alunos e profissionais da área?",
                "Você têm iniciativa e autonomia em seus estudos?"
            ]
            
            for i, question in enumerate(general_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"ger_{i}")
                answers[question] = answer

        return answers