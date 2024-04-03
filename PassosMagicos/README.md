## Passos Mágicos Analytics: Transformando a Avaliação do INDE

A **Passos Mágicos Analytics** apresenta um MVP que visa facilitar a maneira como lidamos com a avaliação dos alunos através do INDE. Este sistema permite o cadastro detalhado dos alunos e a captação de todos os questionários que compõem a avaliação, oferecendo uma análise abrangente e personalizada.

Os questionários incluem uma variedade de aspectos educacionais e psicossociais, cobrindo desde os Indicadores de Adequação de Nível (IAN) até os Indicadores do Ponto de Virada (IPV). Cada questionário é composto por 10 questões cuidadosamente elaboradas para fornecer insights significativos sobre o desenvolvimento e o engajamento dos alunos.

A análise fornecida pelo Passos Mágicos Analytics não se limita apenas a uma visão geral, mas também permite filtrar os resultados por aluno. Isso possibilita um entendimento mais profundo do histórico de avaliação de cada indivíduo, identificando padrões, tendências e áreas de melhoria específicas.

Uma das características mais poderosas desta solução é a análise da sazonalidade, utilizando médias móveis para identificar períodos de piora e melhora em relação aos questionários. Essa abordagem permite uma compreensão mais refinada das tendências ao longo do tempo e ajuda a destacar áreas críticas que necessitam de intervenção.

Além disso, o Passos Mágicos Analytics oferece a possibilidade de adicionar facilmente dados externos, como dados da prefeitura, para comparar o impacto que a Passos Mágicos realiza. Isso permite uma avaliação mais abrangente e uma compreensão mais profunda do contexto em que os alunos estão inseridos.

Outro aspecto é a capacidade de adicionar e alternar questionários ou dados para possíveis inteligências artificiais. Essa funcionalidade visa automatizar a avaliação e predizer informações úteis para melhor atender o aluno, permitindo uma abordagem mais proativa e personalizada.

Em resumo, o MVP desenvolvido pelo Grupo 101 para a Passos Mágicos oferece uma visão abrangente e personalizada da avaliação do INDE, capacitando educadores e profissionais de apoio a tomar decisões informadas e direcionadas para o sucesso educacional e emocional de cada aluno.

***

Para podermos realizar o desafio, desenvolver e realizar testes foram necessários dados gerados artificialmente e em volume adequado, assim criando o banco in-memory com SQLite para facilitar a contração do MVP.

Então para rodar o MVP precisa-se:
- instalar as bibliotecas necessárias do arquivo ***requirements.txt***
- gerar os dados fictícios com o ***python3 criar_banco.py***
- e ***streamlit*** run app.py para rodar o mvp

todos no diretório raiz.

