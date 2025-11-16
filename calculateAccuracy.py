import pandas as pd
from argparse import ArgumentParser


def calculate_ship_average(path: str) -> float:
    df = pd.read_csv(path)
    if len(df.columns) < 2:
        raise ValueError("CSV file must contain at least two columns.")
    penultimate_col = df.columns[-2]
    if penultimate_col.lower() != "ship":
        raise ValueError(f"Expected penultimate column to be 'ship', found '{penultimate_col}'.")
    ship_scores = pd.to_numeric(df[penultimate_col], errors="coerce").dropna()
    if ship_scores.empty:
        raise ValueError("Column 'ship' contains no numeric values.")
    return float(ship_scores.mean())


def main() -> None:
    parser = ArgumentParser(description="Calculate the average of the 'ship' column from a CSV file.")
    parser.add_argument("--path-file", required=True, help="Path to the CSV file containing CLIP scores.")
    args = parser.parse_args()
    average = calculate_ship_average(args.path_file)
    print(f"Average ship score: {average:.6f}")


if __name__ == "__main__":
    main()
