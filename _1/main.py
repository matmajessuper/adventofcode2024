from collections import Counter

import pandas as pd


def main():
    with open('input.txt', 'r') as f:
        df = pd.read_fwf(f, header=None)
        left, right = df[0], df[1]
        left = left.sort_values().reset_index()[0]
        right = right.sort_values().reset_index()[1]
        df = pd.DataFrame([left, right]).T
        df['delta'] = abs(df[0] - df[1])
        right_counter = Counter(df[1])
        df['similarity'] = df[0] * df[0].map(right_counter)
        return f"{df['delta'].sum()} {df['similarity'].sum()}"


if __name__ == '__main__':
    print(main())
