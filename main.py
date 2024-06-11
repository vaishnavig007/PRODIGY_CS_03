import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r'\d', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate strength
    criteria = [length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_criteria]
    score = sum(criteria)
    
    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Output criteria status and strength
    print(f"Password: {password}")
    print(f"Length (8+ characters): {'1' if length_criteria else '0'}")
    print(f"Contains digit: {'1' if digit_criteria else '0'}")
    print(f"Contains uppercase letter: {'1' if uppercase_criteria else '0'}")
    print(f"Contains lowercase letter: {'1' if lowercase_criteria else '0'}")
    print(f"Contains special character: {'1' if special_criteria else '0'}")
    print(f"Password Strength: {strength}")

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        check_password_strength(password)

if __name__ == "__main__":
    main()
