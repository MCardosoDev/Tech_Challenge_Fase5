import streamlit as st

class QuestionariosIPP:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IPP':
            ipp = [
                "Aprendizagem: Ele participa ativamente das aulas e responde às perguntas com clareza?",
                "Comportamento: Ele se relaciona com os colegas de forma respeitosa e cooperativa?",
                "Comunicação: Ele apresenta dificuldades na comunicação oral ou escrita?",
                "Habilidades Motoras: Ele demonstra coordenação motora e destreza nas atividades?",
                "Desenvolvimento Social: Ele demonstra empatia e respeito pelos outros?",
                "Autoestima: Ele reconhece seus pontos fortes e áreas de desenvolvimento?",
                "Funções Cognitivas: Ele consegue se concentrar nas tarefas, lembrar de informações e resolver problemas?",
                "Habilidades Acadêmicas: O aluno lê, escreve e faz cálculos matemáticos com fluência e compreensão?",
                "Saúde Emocional: O aluno se sente feliz e seguro na escola e em casa?",
                "Condições Socioeconômicas: O aluno tem acesso a recursos materiais e sociais adequados para seu desenvolvimento?"
            ]
            
            for i, question in enumerate(ipp):
                answer = st.radio(question, options=["Sim", "Não"], key=f"soc_{i}")
                answers[question] = answer

        return answers