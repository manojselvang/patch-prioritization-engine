from ingestion.firewall_loader import load_firewall_rules


def calculate_exposure():

    firewall_rules = load_firewall_rules()

    exposure_results = {}

    for rule in firewall_rules:

        destination = rule["destination"]

        if destination not in exposure_results:

            exposure_results[destination] = {
                "connection_count": 0,
                "internet_facing": False
            }

        exposure_results[destination]["connection_count"] += 1

        if rule["source"].lower() == "internet":

            exposure_results[destination]["internet_facing"] = True

    for ip, data in exposure_results.items():

        count = data["connection_count"]

        if count <= 2:
            exposure_score = 5

        elif count <= 5:
            exposure_score = 15

        else:
            exposure_score = 25

        if data["internet_facing"]:
            exposure_score += 20

        data["exposure_score"] = exposure_score

    return exposure_results


if __name__ == "__main__":

    results = calculate_exposure()

    for ip, details in results.items():

        print(ip)
        print(details)
        print("-" * 50)