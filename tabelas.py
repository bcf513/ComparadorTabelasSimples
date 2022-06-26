'''
    Consultar se as notas da planilha 'FOCO' estão no 'Relatório SIEG'
    Se encontrar, incluir coluna no final da planila 'FOCO' com 'sim' ou 'não'
    Classificar planilha pela coluna de conferência

    ATENÇÃO! A função 'display' SÓ funciona no programa Jupyter, para mostrar dados em outros programas
    utilize a função 'print'
'''
import pandas as pd  # Importa biblioteca 'pandas', para interação com arquivos de tabelas, com apelido 'pd'


def conversao(nome_tabela_notas, nome_tabela_relatorio):

    # Nota dos arquivos em Excel para importar e exportar
    # Importa tabela de notas para variável tabelaNotas
    tabelaNotasFocco = pd.read_csv(
        r'%s' % nome_tabela_notas, sep=',', encoding='latin-1')
    # Importa tabela do relatório para variável tabelaRelatorio
    tabelaRelatorioSieg = pd.read_excel(
        r'%s' % nome_tabela_relatorio)
    nomeTabelaFinal = "Final.xlsx"  # Nome do arquivo final

    # Cria coluna 'Verificado', e se a nota em questão estiver
    # em algum lugar dos valores da coluna 'Num NFe' de tabelaRelatorio
    # insere 'Sim', se não houver insere 'Não'
    tabelaRelatorioSieg['Verificado'] = tabelaRelatorioSieg['Num NFe'].map(
        lambda x: 'Sim' if x in tabelaNotasFocco['Nota'].values else 'Não')

    # Para mudar a cor das células e centralizar
    tabelaFinal = tabelaRelatorioSieg.style.applymap(lambda x: (
        "background-color: red;" if x == 'Não' else "background-color: #525BE0;") + 'text-align: center;', subset='Verificado')

    # Exporta arquivo final
    # Exporta a tabela final para o arquivo com o nome indicado, na mesma pasta do projeto
    tabelaFinal.to_excel(nomeTabelaFinal, index=False)
