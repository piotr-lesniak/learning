def vowels_count(s: str) -> int:
    vowels_count = 0
    vowels = ['a', 'o', 'u', 'i', 'y', 'e']

    for char in s:
        if char.lower() in vowels:
            vowels_count +=1
    return vowels_count
