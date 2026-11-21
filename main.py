from src.data_quality import (check_datatypes, check_duplicated, check_empty_col, check_missing, check_temperature_ranges, remove_empty_columns)
from src.data_loader import(load_monthly_file, load_all_monthly_files)
from src.analysis import convert_to_long_format


def main():
    print("Lade Daten...")

    df = load_all_monthly_files(
        "data/raw"
    )

    print("Daten geladen")
    print(df.shape)

    print("\nPrüfe Datenqualität...")

    print(
        "Fehlende Werte:"
    )
    print(
        check_missing(df)
    )

    print(
        "\nDuplikate:"
    )
    print(
        check_duplicated(df)
    )

    print(
        "\nLeere Spalten:"
    )
    print(
        check_empty_col(df)
    )

    print(
        "\nBereinige Daten..."
    )

    df = remove_empty_columns(df)

    print(
        "Spalten nach Bereinigung:"
    )
    print(df.shape)

    print(
        "\nKonvertiere ins Long Format..."
    )

    long_df = convert_to_long_format(df)

    print(
        "Long Format erstellt"
    )

    print(long_df.shape)

    long_df.to_csv(
        "data/processed/weather_long.csv",
        index=False
    )

    print(
        "\nDatei gespeichert."
    )


if __name__ == "__main__":
    main()