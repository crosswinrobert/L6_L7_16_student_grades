
def average_marks(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        return 0.0

    try:
        marks = [int(m.strip()) for m in marks_csv.split(',')]

        if not marks:
            return 0.0

        return round(sum(marks) / len(marks), 2)

    except ValueError:
        return 0.0


def parse_srn(srn):
    if not isinstance(srn, str) or len(srn) < 10:
        return "", None, ""

    year = srn[6:8]
    dept = srn[8:10]

    if not year.isdigit() or not dept.isalpha():
        return "", None, ""

    return srn[:4], int(year), dept


def short_name(full_name):
    if not isinstance(full_name, str):
        return "Invalid name"

    parts = full_name.split()

    if len(parts) < 2:
        return "Invalid name"

    first = parts[0]
    last = parts[-1]

    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)


if __name__ == "__main__":
    main()
