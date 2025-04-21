def find_removed_numbers_xor(full_sequence, sample_data):
    xor_full = 0
    xor_sample = 0

    # XOR wszystkich liczb w pełnej sekwencji
    for num in full_sequence:
        xor_full ^= num

    # XOR wszystkich liczb w sekwencji po usunięciu dwóch
    for num in sample_data:
        xor_sample ^= num

    # XOR brakujących liczb
    xor_missing = xor_full ^ xor_sample

    # Znajdowanie jednej z brakujących liczb
    bit_position = 0
    while xor_missing & 1 == 0:
        xor_missing >>= 1
        bit_position += 1

    # Ponowne XOR ze wszystkimi liczbami w pełnej sekwencji, pomijając te dwie usunięte
    xor_missing ^= xor_full

    # Znajdowanie drugiej brakującej liczby
    for num in full_sequence:
        if (num >> bit_position) & 1:
            xor_missing ^= num

    # Znalezione brakujące liczby
    missing_number1 = xor_missing
    missing_number2 = xor_missing ^ xor_sample

    return missing_number1, missing_number2

# Zadana sekwencja
full_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]

# Brakujące liczby
removed_numbers = [23, 14]

# Użycie programu do znalezienia usuniętych liczb
found_removed_numbers = find_removed_numbers_xor(full_sequence, removed_numbers)

# Wyświetlanie wyników
print("Zadana sekwencja:", full_sequence)
print("Brakuje liczb:", removed_numbers)
print("Znalezione brakujące liczby (XOR):", found_removed_numbers)
dziekuje 