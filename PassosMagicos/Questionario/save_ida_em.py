import pandas as pd
from datetime import datetime
from Materias.ida_em import IDA_emTable
from Infra.database import DatabaseConnection

class QuestionarioIDA_emSalvo:
    def __init__(self, questionarios):
        self.questionarios = questionarios

    def rename_columns(self, df, mapper):
        return df.rename(columns=mapper)

    def save(self):
        db_connection = DatabaseConnection('passos_magicos')
        engine = db_connection.get_engine()

        mapper_materias = {
            "Matrícula": "matricula",
            "Língua Portuguesa": "lingua_portuguesa",
            "Língua Estrangeira": "lingua_estrangeira",
            "Artes": "artes",
            "Matemática": "matematica",
            "Física": "fisica",
            "Química": "quimica",
            "Biologia": "biologia",
            "Astronomia": "astronomia",
            "História": "historia",
            "Geografia": "geografia",
            "Sociologia": "sociologia",
            "Filosofia": "filosofia",
            "Educação Física": "educacao_fisica"
        }

        df_em = pd.DataFrame.from_dict(self.questionarios, orient='index').T
        data_atual = datetime.now()
        df_em['data'] = data_atual

        em_renomeado = self.rename_columns(df_em, mapper_materias)

        em_table = IDA_emTable(engine)
        em_table.add_data(em_renomeado)

        return True
