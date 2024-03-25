import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

class DocentesTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir do arquivo CSV 'docentes.csv'.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Docentes'):
            print("A tabela 'Docentes' já existe no banco de dados.")
            return

        docentes = pd.read_csv('Data/docentes.csv', sep=';')

        columns = [
            Column('Medida', String),
            Column('Etapa_ensino', String),
            Column('Ano', Integer),
            Column('Docentes', Integer)
        ]

        metadata = MetaData()
        docentes_table = Table('Docentes', metadata, *columns)

        metadata.create_all(self.engine)

        session = Session(self.engine)

        data_list = docentes.to_dict(orient='records')
        for data_row in data_list:
            x = docentes_table.insert().values(data_row)
            session.execute(x)

        session.commit()
        session.close()
        print(f"Tabela 'Docentes' criada no banco de dados. Inseridos '{len(docentes)}' registros")
