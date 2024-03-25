import streamlit as st

class QuestionariosIPS:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'IPS':
            ips = [
                "Ambiente Familiar: Você tem um bom relacionamento com seus familiares?",
                "Vida Social: Você tem amigos com quem você pode contar?",
                "Saúde Mental: Você se sente bem consigo mesmo e com sua vida?",
                "Autoestima: Você acredita que é capaz de alcançar seus objetivos?",
                "Desempenho Escolar: Você acredita que está aprendendo e progredindo em seus estudos?",
                "Planos para o Futuro: Você tem um plano para alcançar seus objetivos?",
                "Hábitos de Vida: Você se alimenta de forma saudável e pratica atividades físicas regularmente?",
                "Uso de Substâncias: Você não se sente pressionado a usar drogas ou bebidas alcoólicas?",
                "Violência: Você se sente seguro em casa, na escola e na comunidade?",
                "Rede de Apoio: Você sabe como buscar ajuda quando precisa?"
            ]
            
            for i, question in enumerate(ips):
                answer = st.radio(question, options=["Sim", "Não"], key=f"soc_{i}")
                answers[question] = answer

        return answers