import re


def generator_numbers(text: str):
    pattern_float = r"\d+[.]+\d*"
    
    for number in re.findall(pattern_float, text):
        yield float(number)


def sum_profit(text: str, func: callable):
    total_sum = 0

    for num in func(text):
        total_sum += num


    return total_sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")