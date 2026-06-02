from ingestion.asset_loader import load_asset_inventory
from ingestion.vulnerability_loader import load_vulnerabilities
from correlation.exposure_analysis import calculate_exposure


def build_asset_context():

    assets = load_asset_inventory()

    vulnerabilities = load_vulnerabilities()

    exposure_data = calculate_exposure()

    vulnerability_lookup = {}

    for vuln in vulnerabilities:

        vulnerability_lookup[
            vuln["ip_address"]
        ] = vuln

    asset_context = []

    for asset in assets:

        ip = asset["ip_address"]

        vuln = vulnerability_lookup.get(ip)

        exposure = exposure_data.get(
            ip,
            {
                "connection_count": 0,
                "internet_facing": False,
                "exposure_score": 0
            }
        )

        asset_context.append(
            {
                "asset_name": asset["asset_name"],
                "ip_address": ip,
                "application": asset["application"],
                "operating_system": asset["operating_system"],
                "vlan": asset["vlan"],

                "server_category":
                    asset["server_category"],

                "server_type":
                    asset["server_type"],

                "cia_severity":
                    asset["cia_severity"],

                "cve":
                    vuln["cve"] if vuln else None,

                "vulnerability_priority":
                    vuln["priority"] if vuln else None,

                "connection_count":
                    exposure["connection_count"],

                "internet_facing":
                    exposure["internet_facing"],

                "exposure_score":
                    exposure["exposure_score"]
            }
        )

    return asset_context


if __name__ == "__main__":

    assets = build_asset_context()

    for asset in assets:

        print(asset)

        print("-" * 80)