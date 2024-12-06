import re


def main():
    with open('input.txt', 'r') as f:
        content = f.read()
    mul_matches = re.findall('mul\(\d+\,\d+\)', content)
    result_1 = result_2 = 0
    for mul in mul_matches:
        mul_numbers = 1
        for number in re.findall('\d+', mul):
            mul_numbers *= int(number)
        result_1 += mul_numbers

    more_matches = re.findall("(mul\(\d+\,\d+\))|(do\(\))|(don't\(\))", content)
    do = True
    for m_m in more_matches:
        m_match = [m for m in m_m if m][0]
        mul_numbers = 1
        if m_match.startswith("don't"):
            do = False
        elif m_match.startswith('do'):
            do = True
        elif m_match.startswith('mul'):
            if do:
                for number in re.findall('\d+', m_match):
                    mul_numbers *= int(number)
                result_2 += mul_numbers

    return f'{result_1} {result_2}'


if __name__ == '__main__':
    print(main())
