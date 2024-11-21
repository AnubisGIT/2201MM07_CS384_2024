def add_word(anagram_dict, word):
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        add_word(anagram_dict, word)

    result = {}
    for key, group in anagram_dict.items():
        smallest_word = min(group)
        result[smallest_word] = group
    return result

def frequency_analysis(anagram_dict):
    freq_dict = {}
    for key, words in anagram_dict.items():
        frequency = {}
        for word in words:
            for char in word:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
        freq_dict[key] = frequency
    return freq_dict

def group_with_highest_frequency(freq_dict):
    highest_freq_group = None
    highest_freq_sum = 0
    for key, frequency in freq_dict.items():
        total_freq = sum(frequency.values())
        if total_freq > highest_freq_sum:
            highest_freq_sum = total_freq
            highest_freq_group = key
    return highest_freq_group

words = input("Enter words separated by spaces: ").split()

anagram_dict = group_anagrams(words)
print("\nAnagram Groups:")
for key, group in anagram_dict.items():
    print(f"{key}: {group}")

freq_dict = frequency_analysis(anagram_dict)
print("\nFrequency Analysis:")
for key, frequency in freq_dict.items():
    print(f"{key}: {frequency}")

highest_freq_group = group_with_highest_frequency(freq_dict)
print(f"\nGroup with the highest frequency: {highest_freq_group} - {anagram_dict[highest_freq_group]}")