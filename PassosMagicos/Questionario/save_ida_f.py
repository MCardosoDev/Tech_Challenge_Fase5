import pandas as pd
from datetime import datetime
from Materias.ida_f import IDA_fTable
from Infra.database import DatabaseConnection

class QuestionarioIDA_fSalvo:
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
            "Matemática": "matematica",
            "Ciências": "ciencias",
            "História": "historia",
            "Geografia": "geografia",
            "Artes": "artes",
            "Educação Física": "educacao_fisica",
            "Inglês": "ingles"
        }

        df = pd.DataFrame.from_dict(self.questionarios, orient='index').T
        data_atual = datetime.now()
        df['data'] = data_atual

        df_renomeado = self.rename_columns(df, mapper_materias)

        df_table = IDA_fTable(engine)
        df_table.add_data(df_renomeado)

        return True
