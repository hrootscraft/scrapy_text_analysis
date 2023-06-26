from get_metrics import (
    create_stopwords,
    remove_punct,
    remove_nltk_stopwords,
    remove_custom_stopwords,
)
import re


# Positive | Negative score
def posv_or_negv_score(cleaned_words_list, posv_or_negv_words):
    return sum(1 for word in cleaned_words_list if word in posv_or_negv_words)


# Polarity score : Range is from -1 to +1
def polarity_score(posv_score, negv_score):
    return (posv_score - negv_score) / (posv_score + negv_score + 0.000001)


# Subjectivity score : Range is from 0 to +1
def subjective_score(posv_score, negv_score, cleaned_words_list):
    return (posv_score + negv_score) / (len(cleaned_words_list) + 0.000001)


# Avg sentence length
def avg_sent_len(words_list, sent_list):
    try:
        x = len(words_list) / len(sent_list)
    except:
        x = 0
    return x


# Avg words per sentence
def avg_words_per_sentence(sentence_list):
    word_count = 0
    for sentence in sentence_list:
        for i in sentence:
            word_count += 1
    try:
        x = word_count / len(sentence_list)
    except:
        x = 0
    return (word_count, x)


# Count of complex words
def count_complex_words(word_list):
    # complex_words_count = 0
    # for word in word_list:
    #     syllables = count_syllables(word)
    #     if syllables > 2:
    #         complex_words_count += 1
    # return complex_words_count
    return sum(count_syllables(word) > 2 for word in word_list)


# utility function
def count_syllables(word):
    # This function estimates the number of syllables in a word
    # using a simple heuristic based on the number of vowel clusters
    # Count the number of vowel clusters (sequences of consecutive vowels)
    # in the word. There are other more sophisticated methods available for
    # accurately counting syllables in natural language processing tasks
    # like Lexicon-based approach, Machine learning models,
    # Hyphenation algorithms, Phonetic algorithms

    # Remove trailing "es" or "ed" from the word
    word = re.sub(r"(es|ed)$", "", word, flags=re.IGNORECASE)
    syllable_clusters = re.findall(r"[aeiouy]+", word, re.IGNORECASE)
    return len(syllable_clusters)


# utility function
def syllable_count_per_word(word_list):
    syllable_counts = [count_syllables(word) for word in word_list]
    return syllable_counts


# Average syllables in a word for a given article
def average_syllable_count_per_word(word_list):
    counts = syllable_count_per_word(word_list)
    average_count = sum(counts) / len(counts) if len(counts) > 0 else 0
    return average_count


# Percentage of comples words
def percent_complex_words(word_list):
    return count_complex_words(word_list) / len(word_list)


# Fog index
def fog_index(sentence_list, word_list):
    return 0.4 * (avg_sent_len(sentence_list) + percent_complex_words(word_list))


# Count of personal pronouns
def count_personal_pronouns(text):
    # Define the regex pattern to match personal pronouns, excluding "US"
    pattern = r"\b(I|we|my|ours|us)(?!\sUS)\b"
    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    # Count the number of matches
    return len(matches)


# Average length of a word in characters for a given article
def avg_word_len(word_list):
    total_characters = sum(len(word) for word in word_list)
    return total_characters / len(word_list)


# Clean word count
custom_stopwords = create_stopwords()


def word_count(word_list):
    # Remove punctuation
    cleaned_word_list = remove_punct(word_list)
    # Remove NLTK stopwords
    cleaned_word_list = remove_nltk_stopwords(cleaned_word_list)
    # Remove custom stopwords
    cleaned_word_list = remove_custom_stopwords(cleaned_word_list, custom_stopwords)
    return len(cleaned_word_list)
