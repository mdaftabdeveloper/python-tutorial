alphabet = input("Enter the Alphabet: ")
match alphabet:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Alphabet is vowel.")
    case _:
        print("Alphabet is consonant.")    



