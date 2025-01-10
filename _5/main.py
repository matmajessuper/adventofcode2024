from math import floor


def parse_rules(raw_rules: list) -> dict:
    rules = {str(key): [] for key in range(100)}
    for rule in raw_rules:
        split_rule = rule.split('|')
        rules[split_rule[0]].append(split_rule[1])
    return rules


def check_rules(line: list, rules: dict) -> bool:
    for index, update in enumerate(line):
        if index > 0 and set(rules[update]) & set(line[:index]):
            return False
    return True


def fix_line(line: list, rules: dict) -> list:
    while not check_rules(line, rules):
        for index, update in enumerate(line):
            if index > 0 and set(rules[update]) & set(line[:index]):
                line[index-1], line[index] = line[index], line[index-1]
                break
    return line


def main():
    rules = []
    updates = []
    source = rules
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if line == '\n':
                source = updates
                continue
            line = line.strip()
            if source is updates:
                line = line.split(',')
            source.append(line)

    rules = parse_rules(rules)
    result_1 = sum([int(line[floor(len(line)/2)]) for line in updates if check_rules(line, rules)])
    corrupted_lines = [line for line in updates if not check_rules(line, rules)]
    for index, line in enumerate(corrupted_lines):
        corrupted_lines[index] = fix_line(line, rules)

    result_2 = sum([int(line[floor(len(line)/2)]) for line in corrupted_lines])

    return f'{result_1} {result_2}'


if __name__ == '__main__':
    print(main())
