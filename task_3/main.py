from collections import defaultdict
import sys


def parse_log_line(line: str) -> dict:
    result = {}
    splitted_line = line.split()

    result["date"] = splitted_line[0]
    result["time"] = splitted_line[1]
    result["level"] = splitted_line[2]
    result["message"] = ' '.join(splitted_line[3:])

    return result 


def load_logs(file_path: str) -> list[dict]:
    result = []
    
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                result.append(parse_log_line(line))
    except (FileNotFoundError, OSError) as e:
        print(f"При виконанні програми виникла помилка: {e}")

    return result


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log_level: log_level["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    result = defaultdict(int)

    for log in logs:
        level_log = log["level"]
        result[level_log] += 1


    return result


def display_log_counts(counts: dict):
    print("\nРiвень логування | Кількість")
    print("----------------------------")
    print(f"INFO             | {counts['INFO']}")
    print(f"DEBUG            | {counts['DEBUG']}")
    print(f"ERROR            | {counts['ERROR']}")
    print(f"WARNING          | {counts['WARNING']}")


def display_choiced_level_log(logs: list, level_log: str):
    print(f"\nДеталі логів для рівня '{level_log}':")
    for log in logs:
        print(f'{log["date"]} {log["time"]} {log["level"]} - {log["message"]}')


def main():
    if len(sys.argv) > 3:
        print("Занадто багато аргументів")
        sys.exit(-1)
    elif len(sys.argv) < 2:
        print(f"Пропущений обов'язковий аргумент (шлях до логфайла)")
        sys.exit(-1)
    else:
        level_log = sys.argv[2].upper() if len(sys.argv) == 3 else None
        logs = load_logs(sys.argv[1])
        count_logs = count_logs_by_level(logs)

        display_log_counts(count_logs)

        if level_log:
            display_choiced_level_log(filter_logs_by_level(logs, level_log), level_log)



if __name__ == "__main__":
    main()

