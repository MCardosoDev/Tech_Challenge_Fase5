from Infra.database import DatabaseConnection
from CadastroAlunos.cadastro_alunos import CadastroAlunosTable
from Docentes.docentes import DocentesTable
from Escolas.escolas import EscolasTable
from Matriculas.matriculas import MatriculasTable
from Alfabetizacao.alfabetizacao import AlfabetizacaoTable
from Fundamental.fundamental import FundamentalTable
from Fundamental_2.fundamental_2 import Fundamental2Table
from EnsinoMedio.ensino_medio import EnsinoMedioTable
from Geral.ieg import IEGTable
from Geral.iaa import IAATable
from Psicologico.ipp import IPPTable
from Psicologico.ips import IPSTable
from Psicologico.ipv import IPVTable
from Materias.ida import IDATable
from Materias.ida_f import IDA_fTable
from Materias.ida_f2 import IDA_f2Table
from Materias.ida_em import IDA_emTable
import pandas as pd

def main():
    db_connection = DatabaseConnection('passos_magicos')
    engine = db_connection.get_engine()

    """
    Função principal que cria a tabela 'CadastroAlunos' no banco de dados.
    """
    cadastro_alunos_table = CadastroAlunosTable(engine)
    cadastro_alunos_table.create_table()
    """
    Função principal que cria a tabela 'Docentes' no banco de dados.
    """
    docentes_table = DocentesTable(engine)
    docentes_table.create_table()
    """
    Função principal que cria a tabela 'Escolas' no banco de dados.
    """
    escolas_table = EscolasTable(engine)
    escolas_table.create_table()
    """
    Função principal que cria a tabela 'Matriculas' no banco de dados.
    """
    matriculas_table = MatriculasTable(engine)
    matriculas_table.create_table()
    """
    Função principal que cria a tabela 'Alfabetizacao' no banco de dados.
    """
    # Alfabetizacao_Table = AlfabetizacaoTable(engine)
    # Alfabetizacao_Table.initTableAlf()
    """
    Função principal que cria a tabela 'Fundamental' no banco de dados.
    """
    # Fundamental_Table = FundamentalTable(engine)
    # Fundamental_Table.initTableAlf()
    """
    Função principal que cria a tabela 'Fundamental2' no banco de dados.
    """
    # Fundamental2_Table = Fundamental2Table(engine)
    # Fundamental2_Table.initTableAlf()
    """
    Função principal que cria a tabela 'EnsinoMedio' no banco de dados.
    """
    # EnsinoMedio_Table = EnsinoMedioTable(engine)
    # EnsinoMedio_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IEG' no banco de dados.
    """
    # IEG_Table = IEGTable(engine)
    # IEG_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IAA' no banco de dados.
    """
    # IAA_Table = IAATable(engine)
    # IAA_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IPP' no banco de dados.
    """
    # IPP_Table = IPPTable(engine)
    # IPP_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IPS' no banco de dados.
    """
    # IPS_Table = IPSTable(engine)
    # IPS_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IPV' no banco de dados.
    """
    # IPV_Table = IPVTable(engine)
    # IPV_Table.initTableAlf()
    """
    Função principal que cria a tabela 'CadastroAlunos' no banco de dados.
    """
    cadastro_alunos_table = CadastroAlunosTable(engine)
    cadastro_alunos_table.initTableAlf()
    """
    Função principal que cria a tabela 'IDA' no banco de dados.
    """
    # IDA_Table = IDATable(engine)
    # IDA_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IDA_f' no banco de dados.
    """
    # IDAf_Table = IDA_fTable(engine)
    # IDAf_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IDA_f2' no banco de dados.
    """
    # IDAf2_Table = IDA_f2Table(engine)
    # IDAf2_Table.initTableAlf()
    """
    Função principal que cria a tabela 'IDA_em' no banco de dados.
    """
    # IDAem_Table = IDA_emTable(engine)
    # IDAem_Table.initTableAlf()

if __name__ == "__main__":
    main()
