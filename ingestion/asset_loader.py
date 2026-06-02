import csv


def load_asset_inventory():

    assets = []

    with open(
        "data/asset_inventory.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            assets.append(
                {
                    "asset_name": row["Asset Name"],
                    "ip_address": row["Manual_IP_Address"],
                    "application": row["Application/Tool Name"],
                    "operating_system": row["Operating System"],
                    "vlan": row["VLAN ID"],
                    "server_category": row["Server Category"],
                    "server_type": row["Server Type"],
                    "cia_severity": row["Severity(CIA)"]
                }
            )

    return assets


if __name__ == "__main__":

    assets = load_asset_inventory()

    for asset in assets:
        print(asset)