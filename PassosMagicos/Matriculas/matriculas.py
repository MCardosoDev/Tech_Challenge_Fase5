import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

class MatriculasTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir dos dados do arquivo 'matriculas.csv'.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Matriculas'):
            print("A tabela 'Matriculas' já existe no banco de dados.")
            return

        matriculas = pd.read_csv('Data/matriculas.csv', sep=';')

        columns = [
            Column('Matriculas', Integer),
            Column('Localizacao', String),
            Column('Categoria', Integer),
            Column('Etapa_ensino_superior', String),
            Column('Etapa_ensino', String),
            Column('Ano', Integer)
        ]

        metadata = MetaData()
        matriculas_table = Table('Matriculas', metadata, *columns)

        metadata.create_all(self.engine)

        session = Session(self.engine)

        data_list = matriculas.to_dict(orient='records')
        for data_row in data_list:
            x = matriculas_table.insert().values(data_row)
            session.execute(x)

        session.commit()
        session.close()
        print(f"Tabela 'Matriculas' criada no banco de dados. Inseridos '{len(matriculas)}' registros")

