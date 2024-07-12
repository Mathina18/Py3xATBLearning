letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u


def vowel_giver(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


# result  = filter_vowel('p')
# print(result)

filtered_words1 = filter(vowel_giver,letters_tuple)
print(tuple(filtered_words1))

filtered_words2 = filter(vowel_giver,letters_list)
print(list(filtered_words2))

filtered_words3 = filter(vowel_giver,letters_set)
print(set(filtered_words3))