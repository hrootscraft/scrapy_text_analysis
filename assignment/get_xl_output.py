import pandas as pd

df = pd.read_json("output.json")

df_copy = df.copy()

df_copy = df_copy.rename(
    columns={
        "positive_score": "POSITIVE SCORE",
        "negative_score": "NEGATIVE SCORE",
        "polarity_score": "POLARITY SCORE",
        "subjectivity_score": "SUBJECTIVITY SCORE",
        "average_sentence_length": "AVG SENTENCE LENGTH",
        "average_words_per_sentence": "AVG NUMBER OF WORDS PER SENTENCE",
        "complex_words_count": "COMPLEX WORD COUNT",
        "percentage_of_complex_words": "PERCENTAGE OF COMPLEX WORDS",
        "fog_index": "FOG INDEX",
        "avg_syllable_per_word": "SYLLABLE PER WORD",
        "personal_pronouns_count": "PERSONAL PRONOUNS",
        "average_word_length": "AVG WORD LENGTH",
        "word_count": "WORD COUNT",
    }
)

df_copy = df_copy.drop(columns=["title", "body"])

# Save DataFrame to Excel file
output_file = "output.xlsx"
df_copy.to_excel(output_file, index=False)

print("DataFrame successfully saved to Excel file:", output_file)
