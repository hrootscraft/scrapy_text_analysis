## -------------------SENTIMENT ANALYSIS-------------------
# Positive | Negative score
def posv_or_negv_score(cleaned_words_list, posv_or_negv_words):
    return sum(1 for word in cleaned_words_list if word in posv_or_negv_words)


# Polarity score : Range is from -1 to +1
def polarity_score(posv_score, negv_score):
    return (posv_score - negv_score) / (posv_score + negv_score + 0.000001)


# Subjectivity score : Range is from 0 to +1
def subjective_score(posv_score, negv_score, cleaned_words_list):
    return (posv_score + negv_score) / (len(cleaned_words_list) + 0.000001)


## -------------------READABILITY ANALYSIS-------------------
# Avg sentence length
def avg_sent_len(len_raw_words_list, len_raw_sent_list):
    pass


def avg_words_per_sentence():
    pass


def avg_word_len():
    pass


def complex_words_count():
    pass


def percent_complex_words():
    pass