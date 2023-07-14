from validator_collection import validators

def main():
    email_address = input("What is your enil address? ")
    try:
        if valid_mail_id := validators.email(email_address):
            print("valid")
    except ValueError:
        print("Invalid")

if __name__ == "__main__":
    main()