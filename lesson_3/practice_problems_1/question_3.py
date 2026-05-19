# Starting with the string famous_words = "seven years ago ..." Show two 
# different ways to create a new string with "Four score and" prepended
# to the front of the string refrenced by famous_words
add_on_words = "Four score and "
famous_words = "seven years ago ..."
updated_words_1 = add_on_words + famous_words
print(updated_words_1)

updated_words_2 = "".join([add_on_words, famous_words])
print(updated_words_2)

updated_words_3 = f"{add_on_words}{famous_words}"
print(updated_words_3)

updated_words_4 = "{}{}".format(add_on_words, famous_words)
print(updated_words_4)



