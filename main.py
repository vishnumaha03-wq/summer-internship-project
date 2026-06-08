import csv
from pathlib import Path

from issue_detection_agent import detect_issues
from query_drafting_agent import draft_queries
from human_review_agent import review_query
from communication_hub_agent import send_query


def run_pipeline():

    csv_file = Path(
        "cleaned_data/cleaned_GL.csv"
    )

    if not csv_file.exists():

        print(
            "Run preprocess.py first."
        )

        return

    gl_rows = []

    with open(
        csv_file,
        mode="r",
        encoding="utf-8-sig"
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            gl_rows.append(
                dict(row)
            )

    print(
        f"\nLoaded {len(gl_rows)} rows"
    )

    findings = detect_issues(
        gl_rows
    )

    for issue_type in findings:

        findings[issue_type] = findings[issue_type][:10]

    final_report = draft_queries(
        findings
    )

    approved = review_query(
        final_report
    )

    if approved:

        send_query(
            final_report
        )

    else:

        print(
            "\nWorkflow stopped."
        )


if __name__ == "__main__":

    run_pipeline()