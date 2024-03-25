import streamlit as st

class QuestionariosAlf:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def collect_answers(self, tab, matricula):
        answers = {'Matrícula': matricula}
        
        if tab in answers:
            respostas_sessao = answers[tab]
            answers.update(respostas_sessao)

        if tab == 'Alfabetização':
            literacy_questions = [
                "A criança reconhece todas as letras do alfabeto?",
                "A criança consegue ler palavras simples e familiares?",
                "A criança consegue escrever palavras simples e familiares?",
                "A criança consegue segmentar palavras em sílabas?",
                "A criança lê de forma fluente, sem soletrar ou decodificar cada palavra?",
                "A criança consegue responder perguntas sobre o que leu?",
                "A criança conhece o significado das palavras que lê e escreve?",
                "A criança demonstra interesse pela leitura e pela escrita?",
                "A criança participa ativamente das aulas de alfabetização?",
                "A criança demonstra progresso ao longo do tempo em suas habilidades de leitura e escrita?"
            ]
            
            for i, question in enumerate(literacy_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"alf_{i}")
                answers[question] = answer
                
        elif tab == 'Fundamental':
            fundamental_questions = [
                "A criança consegue resolver problemas matemáticos simples envolvendo adição, subtração, multiplicação e divisão?",
                "Ela consegue interpretar e analisar textos de diferentes tipos, como contos, notícias e poemas?",
                "Ela formula perguntas e hipóteses sobre o mundo natural?",
                "Ela compreende a relação entre passado, presente e futuro?",
                "Ela compreende a relação entre o homem e o meio ambiente?",
                "A criança demonstra criatividade e expressividade nas diferentes formas de arte?",
                "Ela desenvolve suas habilidades motoras e coordenação corporal?",
                "Ela se comunica de forma eficaz com os outros?",
                "Ela reconhece e pronuncia palavras e frases simples em inglês?",
                "Ela utiliza a tecnologia para pesquisa, comunicação e aprendizagem?"
            ]
            
            for i, question in enumerate(fundamental_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"fund_{i}")
                answers[question] = answer
                
        elif tab == 'Fundamental 2':
            fundamental2_questions_questions = [
                "Domina os conceitos matemáticos básicos de frações, decimais e porcentagens?",
                "Resolve problemas matemáticos mais complexos envolvendo diferentes operações?",
                "Interpreta e analisa criticamente textos de diferentes gêneros literários?",
                "Demonstra interesse e conhecimento sobre diferentes áreas da ciência (física, química, biologia)?",
                "Desenvolve senso crítico para analisar diferentes interpretações da história?",
                "Demonstra conhecimento sobre os principais países e regiões do mundo?",
                "Participa de diferentes atividades esportivas com cooperação e respeito?",
                "Demonstra autoconhecimento, autoconfiança e resiliência?",
                "Demonstra interesse pela cultura dos países de língua inglesa?",
                "Produz conteúdo digital de forma ética e responsável?" 
            ]
            
            for i, question in enumerate(fundamental2_questions_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"fund2_{i}")
                answers[question] = answer

        elif tab == 'Ensino Médio':
            high_school_questions = [
                "Ele utiliza diferentes métodos e estratégias para resolver problemas matemáticos de forma eficiente?",
                "Ele utiliza linguagem matemática adequada e argumenta de forma lógica?",
                "Ele é capaz de analisar criticamente diferentes interpretações da história?",
                "O aluno compreende os principais processos de globalização e seus impactos na sociedade?",
                "Ele é capaz de formular e defender argumentos de forma lógica e fundamentada?",
                "Ele é capaz de analisar criticamente os problemas sociais e propor soluções?",
                "O aluno domina os principais conceitos da física e suas aplicações no mundo real?",
                "Ele é capaz de analisar criticamente os impactos da química na sociedade e no meio ambiente?",
                "O aluno domina os principais conceitos da biologia e as relações entre os seres vivos?",
                "Ele é capaz de se comunicar de forma eficaz em diferentes situações?"
            ]

            for i, question in enumerate(high_school_questions):
                answer = st.radio(question, options=["Sempre", "Frequentemente", "Às vezes", "Raramente", "Nunca"], key=f"em_{i}")
                answers[question] = answer

        return answers