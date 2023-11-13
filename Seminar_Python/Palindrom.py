"""определить с помощью рекурсии , является ли слово полиндромом"""
def is_palindrome(word):
    word = word.lower() 
    if len(word) <= 1:  
        return True
    elif word[0] != word[-1]:  
        return False
    else:
        return is_palindrome(word[1:-1])  # рекурсия

word = "cat"
print(is_palindrome(word))