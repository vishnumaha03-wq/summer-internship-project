import streamlit as st
import pandas as pd

from issue_detection_agent import detect_issues
from query_drafting_agent import draft_queries

from database import (
    save_findings,
    save_report
)

st.set_page_config(
    page_title="Bank Issue Detection System",
    layout="wide"
)

st.title("🏦 Bank Issue Detection System")

uploaded_file = st.file_uploader(
    "Upload Ledger File",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:

    # Automatically detect file type
    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(
            uploaded_file
        )

    else:

        df = pd.read_excel(
            uploaded_file
        )

    st.success(
        "File uploaded successfully!"
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        df.head()
    )

    if st.button(
        "Run Issue Detection"
    ):

        with st.spinner(
            "Analyzing ledger..."
        ):

            gl_rows = (
                df.to_dict(
                    orient="records"
                )
            )

            findings = detect_issues(
                gl_rows
            )

            # Save findings to database
            save_findings(
                findings
            )

            # Limit findings sent to Gemini
            for issue_type in findings:

                findings[
                    issue_type
                ] = findings[
                    issue_type
                ][:10]

            report = draft_queries(
                findings
            )

            # Save report to database
            save_report(
                report
            )

        st.success(
            "Analysis Complete"
        )

        st.subheader(
            "Issue Summary"
        )

        for category, issues in findings.items():

            st.write(
                f"✅ {category}: {len(issues)} issue(s)"
            )

        st.subheader(
            "Detected Issues"
        )

        st.json(
            findings
        )

        st.subheader(
            "Generated Client Query Report"
        )

        st.write(
            report
        )

        st.success(
            "Findings and report saved to database successfully."
        )