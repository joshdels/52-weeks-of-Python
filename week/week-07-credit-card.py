"""
IDEA
Credit card input, input the 16 digits and shows the last digit


PLANNING PHASE
- slicing
- inputs and validation
- print result the last for digit
- function
"""


# mine
def ask_credit_card():
    while True:
        card_details = input("Enter you credit-card: ")

        try:
            is_number = int(card_details)
            card_length = len(card_details)

            if card_length < 4:
                print("Invalid input, card must be at least 4 digits long.")
                continue

            num_str = str(card_details)
            last_str = num_str[-4:]
            total_hide_numbers = card_length - 4

            card_hidden = ""

            for i in range(total_hide_numbers):
                card_hidden += "*"

            card_hidden += last_str

            print("\n Hidden Credit Card")
            print(card_hidden)
            break

        except ValueError:
            print("Invalid input, only numbers are allowed")


# Senior Reviewer GPT

def mask_card_number(card_number: str) -> str:
    """Mask a card number while preserving its last four digits."""
    digits = card_number.replace(" ", "")

    if not digits.isascii() or not digits.isdigit():
        raise ValueError("Card number must contain only digits.")

    if not 13 <= len(digits) <= 19:
        raise ValueError("Card number must contain 13 to 19 digits.")

    hidden_count = len(digits) - 4
    masked_prefix = "*" * hidden_count

    # Group masked characters from the right.
    groups = []
    while masked_prefix:
        groups.insert(0, masked_prefix[-4:])
        masked_prefix = masked_prefix[:-4]

    groups.append(digits[-4:])

    return " ".join(groups)


def main() -> None:
    while True:
        card_number = input("Enter your credit card number: ").strip()

        try:
            masked_card = mask_card_number(card_number)
        except ValueError as error:
            print(f"Invalid input: {error}\n")
            continue

        print(f"Masked card: {masked_card}")
        break


if __name__ == "__main__":
    main()
