import pandas as pd
from datetime import datetime
from CadastroAlunos.cadastro_alunos import CadastroAlunosTable
from Infra.database import DatabaseConnection

class CadastroAlunoSalvo:
    def __init__(self, df):
        self.questionario = df
    
    def save(self):
        db_connection = DatabaseConnection('passos_magicos')
        engine = db_connection.get_engine()

        cadastro_alunos_table = CadastroAlunosTable(engine)
        cadastro_alunos_table.create_table()
        cadastro_alunos_table.add_data(self.questionario)

        return True
