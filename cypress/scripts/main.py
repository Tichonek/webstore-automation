from data_generators import *
import json

def main():
    firstName = generateFirstName()
    lastName = generateLastName()
    email = generateEmail(firstName, lastName)
    password = generatePassword()
    birthDate = generateBirthDate()

    person = generatePerson(firstName, lastName, email, password, birthDate)

    saveToJSON(person)

if __name__ == "__main__":
    main()