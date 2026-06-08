def review_query(
    drafted_report
):

    print("\n")
    print("=" * 80)
    print("HUMAN REVIEW LAYER")
    print("=" * 80)

    print(
        drafted_report
    )

    decision = input(
        "\nApprove? (yes/no): "
    )

    if (
        decision.lower()
        == "yes"
    ):

        print(
            "\nAPPROVED"
        )

        return True

    print(
        "\nREJECTED"
    )

    return False