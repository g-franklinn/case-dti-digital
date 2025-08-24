from typing import List, Union

def median(int_list: List[Union[int, float]]):
    if not int_list:
        raise ValueError("A lista não pode estar vazia.")
    
    for item in int_list:
        if not isinstance(item, (int, float)):
            raise TypeError(f"A lista deve conter apenas números.")
    
    ordered_list = sorted(int_list)
    n = len(ordered_list)
    half_index = n // 2

    if n % 2 == 1:
        median = ordered_list[half_index]
    else:
        first_half_index = ordered_list[half_index-1]
        second_half_index = ordered_list[half_index]
        median = (first_half_index + second_half_index) / 2

    return median


if __name__ == "__main__":    
    odd_list = [1, 5, 2, 8, 3]
    print(f"A mediana de {odd_list} é: {median(odd_list)}")

    even_list = [1, 6, 2, 8, 3, 10]
    print(f"A mediana de {even_list} é: {median(even_list)}")
