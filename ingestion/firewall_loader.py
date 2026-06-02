import csv


def load_firewall_rules():

    rules = []

    with open(
        "data/firewall_rules.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            rules.append(
                {
                    "source": row["SOURCE"],
                    "destination": row["DESTINATION"],
                    "service": row["SERVICE"]
                }
            )

    return rules


if __name__ == "__main__":

    rules = load_firewall_rules()

    for rule in rules:
        print(rule)