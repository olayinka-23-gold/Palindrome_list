def is_palindrome():
    words = []  # List to store user-inputted words
    palindrome = []  # List to store words that are palindromes
    npalindrome = []  # List to store words that are not palindromes
    
    # Ask the user how many words they want to check
    choice = int(input("How many words would you like to check for palindrome? input a number: "))
    
    # Collect words from the user
    while choice > 0:
        check_palindrome = input(f"Enter word {choice}: ")
        words.append(check_palindrome)
        choice -= 1
    
    # Check each word for being a palindrome
    for i in words:
        reversed_string = i[::-1]  # Reverse the word
        if i == reversed_string:  # If the word matches its reverse, it's a palindrome
            palindrome.append(i)
        else:  # Otherwise, it's not a palindrome
            npalindrome.append(i)
    
    # Display the results
    print("These are the palindromes:")
    print(palindrome)
    print("These are not palindromes:")
    print(npalindrome)

# Call the function
is_palindrome()
