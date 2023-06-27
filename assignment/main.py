from preprocess_text import (
    create_stopwords,
    get_json_output,
    tokenize,
    sentence_tokenize,
    remove_punct,
    remove_custom_stopwords,
    remove_nltk_stopwords,
)
from get_metrics import (
    get_dict,
    polarity_score,
    subjectivity_score,
    avg_sent_len,
    avg_words_per_sentence,
    count_complex_words,
    average_syllable_count_per_word,
    percent_complex_words,
    fog_index,
    count_personal_pronouns,
    avg_word_length,
)
import json

# initiate constants
custom_stopwords = create_stopwords()
json_output = get_json_output()
pn = {"p": 0, "n": 0}

# create the table
for item in json_output:
    article = item["body"]

    article_word_tokens = tokenize(article)

    article_word_tokens_wo_punct = remove_punct(article_word_tokens)

    article_word_tokens_wo_punct_n_custom_stopwords = remove_custom_stopwords(
        article_word_tokens_wo_punct, custom_stopwords
    )
    article_word_tokens_wo_punct_n_all_stopwords = remove_nltk_stopwords(
        article_word_tokens_wo_punct_n_custom_stopwords
    )
    cleaned_word_count = len(article_word_tokens_wo_punct_n_all_stopwords)
    item["word_count"] = cleaned_word_count

    dict_obj = get_dict(article_word_tokens_wo_punct_n_all_stopwords)
    posv_score = len(dict_obj["p"])
    negv_score = len(dict_obj["n"])
    item["positive_score"] = posv_score
    item["negative_score"] = negv_score

    item["polarity_score"] = polarity_score(posv_score, negv_score)

    item["subjectivity_score"] = subjectivity_score(
        posv_score, negv_score, cleaned_word_count
    )

    article_sentence_tokens = sentence_tokenize(article)

    article_sentence_tokens_wo_punct = remove_punct(article_sentence_tokens)

    average_sent_len = avg_sent_len(
        article_word_tokens_wo_punct, article_sentence_tokens_wo_punct
    )
    item["average_sentence_length"] = average_sent_len
    item["average_words_per_sentence"] = avg_words_per_sentence(
        article_sentence_tokens_wo_punct
    )

    item["complex_words_count"] = count_complex_words(article_word_tokens_wo_punct)

    pcent_compl_words = percent_complex_words(article_word_tokens_wo_punct)
    item["percentage_of_complex_words"] = pcent_compl_words

    item["fog_index"] = fog_index(average_sent_len, pcent_compl_words)

    item["avg_syllable_per_word"] = average_syllable_count_per_word(
        article_word_tokens_wo_punct
    )

    item["personal_pronouns_count"] = count_personal_pronouns(article)

    item["average_word_length"] = avg_word_length(article_word_tokens_wo_punct)


# # Open the file in write mode and save the JSON object
# with open("output.json", "w") as json_file:
#     json.dump(json_output, json_file)