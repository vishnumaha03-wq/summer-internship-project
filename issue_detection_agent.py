from AgentCreation.agents import (
    check_missing_invoices,
    check_gst_mismatch,
    check_uncoded_transactions,
    check_negative_assets
)


def detect_issues(gl_rows):

    print(
        "\n[ISSUE DETECTION AGENT STARTED]"
    )

    findings = {}

    findings[
        "Missing Invoices"
    ] = check_missing_invoices(
        gl_rows
    )

    findings[
        "GST Mismatches"
    ] = check_gst_mismatch(
        gl_rows
    )

    findings[
        "Uncoded Transactions"
    ] = check_uncoded_transactions(
        gl_rows
    )

    findings[
        "Negative Assets"
    ] = check_negative_assets(
        gl_rows
    )

    total = sum(
        len(v)
        for v in findings.values()
    )

    print(
        f"\nTotal Issues Found: {total}"
    )

    return findings