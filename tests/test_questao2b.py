import pandas as pd
from pathlib import Path

from python.questao2b import filter_adults

def test_filter_adults():

    path_input = Path("data/dados.csv")
    path_output = Path("data/maiores_de_idade.csv")

    filter_adults(str(path_input), str(path_output))
    assert path_output.exists(), "O arquivo 'maiores_de_idade.csv' não foi criado."

    df_result = pd.read_csv(path_output)
    assert df_result['idade'].min() >= 18, "O arquivo de saída contém pessoas menores de 18 anos."

