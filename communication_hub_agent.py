from pathlib import Path
from datetime import datetime


def send_query(
    drafted_report
):

    hub_dir = Path(
        "Outputs/CommunicationHub"
    )

    hub_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = (
        datetime.now()
        .strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    output_file = (
        hub_dir /
        f"query_{timestamp}.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            drafted_report
        )

    print(
        "\nQuery sent to Communication Hub"
    )

    print(
        output_file
    )