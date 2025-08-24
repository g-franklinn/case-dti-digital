import pandas as pd

AGE_THRESHOLD = 18
INPUT_FILE = "data/dados.csv"
OUTPUT_FILE = "data/maiores_de_idade.csv"

def filter_adults(input_file: str, output_file: str):
    try:
        df = pd.read_csv(input_file)
        df_adults = df[df['idade'] >= AGE_THRESHOLD].copy()
        df_adults.to_csv(output_file, index=False)
        print(f"Arquivo '{output_file}' criado com sucesso com {len(df_adults)} registros.")

    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{input_file}' não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    print(f"Lendo de '{INPUT_FILE}' e salvando em '{OUTPUT_FILE}'...")
    filter_adults(INPUT_FILE, OUTPUT_FILE)