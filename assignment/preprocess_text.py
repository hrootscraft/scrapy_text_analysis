import json
import nltk
import os

# Read output.json and get the articles body
try:
    with open("output.json") as json_file:
        output_data = json.load(json_file)
except FileNotFoundError:
    print("output.json not found")
except IOError:
    print("An error occurred while reading output.json")


# Creating positive and negative words list so that we can compare each word from each cleaned article with it
def create_posv_words_list():
    try:
        with open("MasterDictionary/positive-words.txt", "r") as f:
            text = f.read()
            posv_words = text.lower().split("\n")
        return posv_words
    except FileNotFoundError:
        print("positive-words.txt not found")
    except IOError:
        print("An error occurred while reading positive-words.txt")


def create_negv_words_list():
    try:
        with open("MasterDictionary/negative-words.txt", "r") as f:
            text = f.read()
            negv_words = text.lower().split("\n")
        return negv_words
    except FileNotFoundError:
        print("negative-words.txt not found")
    except IOError:
        print("An error occurred while reading negative-words.txt")


# Creating our stopwords list
def create_stopwords():
    try:
        custom_stopwords_dir = r"stopwords"
        for i in os.listdir(custom_stopwords_dir):
            with open(custom_stopwords_dir + "/" + i, "r") as f:
                print(f)
                data = f.read()
                custom_stopwords_list = data.lower().split("\n")
        custom_stopwords = list(map(lambda i: i.lower(), custom_stopwords_list))
        return custom_stopwords
    except FileNotFoundError:
        print("File not found when creating list of stopwords")
    except IOError:
        print("An error occurred while reading the file of stopwords")


# Tokenizing
def tokenize(text):
    tokens = nltk.word_tokenize(text.lower())
    return tokens


# Sentence tokenizing
def sentence_tokenize(text):
    tokens = nltk.sent_tokenize(text.lower())
    return tokens


# Remove stopwords
def remove_stopwords(tokens, custom_stopwords):
    cleaned_words = [token for token in tokens if token not in custom_stopwords]
    return cleaned_words