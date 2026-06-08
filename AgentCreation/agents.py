# =========================================================
# Issue Detection Logic (Adapted For Your Ledger Dataset)
# =========================================================

def check_missing_invoices(gl_data: List[Dict[str, Any]]) -> List[str]:
    """
    Issue 1:
    Detects missing Entry Numbers.
    """

    issue_findings = []

    for row in gl_data:

        entry_no = str(
            row.get("EntryNo", "")
        ).strip()

        if (
            entry_no == ""
            or entry_no.lower() in [
                "missing",
                "none",
                "nan"
            ]
        ):

            issue_findings.append(
                f"Missing Entry Number detected on transaction dated {row.get('Date', 'Unknown Date')}."
            )

    return issue_findings


def check_gst_mismatch(gl_data: List[Dict[str, Any]]) -> List[str]:
    """
    Issue 2:
    Detects duplicate transactions.

    (Repurposed because your dataset has no GST column.)
    """

    issue_findings = []

    seen = set()

    for row in gl_data:

        transaction_key = (

            str(
                row.get("Date", "")
            ).strip(),

            str(
                row.get("Details", "")
            ).strip(),

            str(
                row.get("Amount", "")
            ).strip()
        )

        if transaction_key in seen:

            issue_findings.append(
                f"Possible Duplicate Transaction: "
                f"{row.get('Details')} "
                f"for amount {row.get('Amount')} "
                f"on {row.get('Date')}."
            )

        else:

            seen.add(
                transaction_key
            )

    return issue_findings


def check_uncoded_transactions(gl_data: List[Dict[str, Any]]) -> List[str]:
    """
    Issue 3:
    Detects unusually high-value transactions.

    (Repurposed because your dataset has no Account column.)
    """

    issue_findings = []

    for row in gl_data:

        try:

            amount = abs(
                float(
                    row.get(
                        "Amount",
                        0
                    )
                )
            )

            if amount > 100000:

                issue_findings.append(
                    f"High Value Transaction: "
                    f"{row.get('Details')} "
                    f"with amount {amount}."
                )

        except:

            continue

    return issue_findings


def check_negative_assets(gl_data: List[Dict[str, Any]]) -> List[str]:
    """
    Issue 4:
    Detects negative transaction values.
    """

    issue_findings = []

    for row in gl_data:

        try:

            amount = float(
                row.get(
                    "Amount",
                    0
                )
            )

            if amount < 0:

                issue_findings.append(
                    f"Negative Amount Detected: "
                    f"{row.get('Details')} "
                    f"has amount {amount}."
                )

        except:

            continue

    return issue_findings