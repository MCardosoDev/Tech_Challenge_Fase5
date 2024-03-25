import pandas as pd
from sqlalchemy import inspect, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

class EscolasTable:
    def __init__(self, engine):
        self.engine = engine

    def create_table(self):
        """
        Cria uma tabela no banco de dados a partir dos dados do arquivo 'escolas.csv'.

        Returns:
            None
        """
        assert self.engine, "A conexão com o banco de dados não foi criada corretamente."

        inspector = inspect(self.engine)

        if inspector.has_table('Escolas'):
            print("A tabela 'Escolas' já existe no banco de dados.")
            return

        escolas = pd.read_csv('Data/escolas.csv', sep=';')

        columns = [
            Column('Escolas', String),
            Column('Localizacao', String),
            Column('Categoria', Integer),
            Column('Etapa_ensino_superior', String),
            Column('Etapa_ensino', String),
            Column('Ano', Integer)
        ]

        metadata = MetaData()
        escolas_table = Table('Escolas', metadata, *columns)

        metadata.create_all(self.engine)

        session = Session(self.engine)

        data_list = escolas.to_dict(orient='records')
        for data_row in data_list:
            x = escolas_table.insert().values(data_row)
            session.execute(x)

        session.commit()
        session.close()
        print(f"Tabela 'Escolas' criada no banco de dados. Inseridos '{len(escolas)}' registros")
