import streamlit as st

class QuestionariosIPV:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IPV':
            social_vulnerability_questions = [
                "Autoconhecimento: Você sabe identificar seus principais interesses, habilidades e paixões?",
                "Autonomia e Responsabilidade: Você assume total responsabilidade pelo seu processo de aprendizado?",
                "Motivação e Engajamento: Você se sente entusiasmado e motivado com as atividades de aprendizagem?",
                "Experimentação e Adaptabilidade: Você já experimentou diferentes métodos de aprendizado para encontrar o que funciona melhor para você?",
                "Aprendizagem Ativa e Reflexiva: Você participa ativamente das aulas e busca compreender os conceitos por trás do que está aprendendo?",
                "Resiliência e Persistência: Você aprende com seus erros e se esforça para superar as dificuldades com persistência?",
                "Planejamento e Metas: Você define metas claras e de longo prazo para sua trajetória educacional?",
                "Busca por Recursos e Apoio: Você busca ajuda de professores, colegas, mentores ou outros profissionais quando precisa?",
                "Visão de Futuro e Propósito: Você consegue visualizar como a educação te ajudará a alcançar seus sonhos e objetivos de vida?",
                "Aprendizagem Contínua: Você se considera um aprendiz constante, sempre buscando novas informações e habilidades?"
            ]
            
            for i, question in enumerate(social_vulnerability_questions):
                answer = st.radio(question, options=["Sim", "Não"], key=f"soc_{i}")
                answers[question] = answer

        return answers