def password_validator_from_file(filename, selected_criteria):
    def has_uppercase(password):
        return any(c.isupper() for c in password)

    def has_lowercase(password):
        return any(c.islower() for c in password)

    def has_number(password):
        return any(c.isdigit() for c in password)

    def has_special(password):
        allowed_specials = "!@#"
        return any(c in allowed_specials for c in password)

    def has_invalid_special(password):
        allowed_specials = "!@#"
        return any(not c.isalnum() and c not in allowed_specials for c in password)

    valid_count = 0
    invalid_count = 0

    with open(filename, 'r') as file:
        password_list = file.readlines()

    password_list = [password.strip() for password in password_list]

    for password in password_list:
        if len(password) < 8:
            print(f"{password}: Invalid password. Less than 8 characters.")
            invalid_count += 1
            continue

        is_valid = True
        missing_criteria = []

        if 1 in selected_criteria and not has_uppercase(password):
            missing_criteria.append(1)
            is_valid = False
        if 2 in selected_criteria and not has_lowercase(password):
            missing_criteria.append(2)
            is_valid = False
        if 3 in selected_criteria and not has_number(password):
            missing_criteria.append(3)
            is_valid = False
        if 4 in selected_criteria:
            if not has_special(password):
                missing_criteria.append(4)
                is_valid = False
            if has_invalid_special(password):
                print(f"{password}: Invalid password. It contains invalid special characters.")
                is_valid = False

        if is_valid:
            print(f"{password}: Valid password.")
            valid_count += 1
        else:
            invalid_count += 1
            if len(missing_criteria) > 0:
                missing = ", ".join([str(c) for c in missing_criteria])
                print(f"{password}: Invalid password. Missing criteria: {missing}")

    print(f"\nTotal valid passwords: {valid_count}")
    print(f"Total invalid passwords: {invalid_count}")


print("Select the criteria you want to validate passwords against:")
print("1: Uppercase letters (A-Z)")
print("2: Lowercase letters (a-z)")
print("3: Numbers (0-9)")
print("4: Special characters (!, @, #)")

selected_criteria = list(map(int, input("Enter criteria numbers separated by commas (e.g., 1,3,4): ").split(',')))

filename = 'input.txt'
password_validator_from_file(filename, selected_criteria)