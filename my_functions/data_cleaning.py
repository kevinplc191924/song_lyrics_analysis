import re
from nltk.corpus import stopwords

## Data cleaning


# Process the lyrics with regular expressions and stopwords from nltk
def clean_lyrics(text, language="Spanish"):
    """
    Clean and preprocess song lyrics by removing unwanted expressions,
    non-alphabetic characters, and stopwords.

    Parameters
    ----------
    text : str
        The raw lyrics text to be cleaned.
    language : str, optional
        The language of the lyrics, used to determine the stopwords
        (default is 'Spanish').

    Returns
    -------
    str
        The cleaned lyrics as a single string, with unwanted words and
        characters removed.

    Notes
    -----
    - Removes repetitive expressions like 'oh', 'la', 'na', etc.
    - Keeps only letters and spaces, including accented characters.
    - Removes stopwords based on the specified language ('Spanish' or 'English').
    - Filters out words with fewer than 3 characters.
    - Run nltk.download('stopwords') once before calling the function and when using nltk for the first time, not needed again.
    """

    # Remove expressions similar to 'oh'
    text = re.sub(r"\b([oaeui][h]?|la|na|mm|ja)\1+\b", "", text.lower())
    # Keep only letters and spaces (accents included)
    text = re.sub(r"[^\w\sáéíóúüñ]", " ", text)

    if language == "Spanish":
        stops = set(stopwords.words("spanish") + ["yeah", "yeh"])
    else:
        stops = set(stopwords.words("english") + ["yeah", "mmh", "bam", "ooh"])

    words = [w for w in text.split() if w not in stops and len(w) > 2]

    return " ".join(words)


# Remove information placed after the word 'lyrics'
def after_lyrics(text):
    """
    Remove undesired information that appears before the word 'lyrics' in a text.

    Parameters
    ----------
    text : str
        The text to be processed, typically song lyrics.

    Returns
    -------
    str
        The processed text with all content before and including the word 'lyrics' removed.

    Notes
    -----
    - The function identifies the word 'lyrics' or variations of it (e.g., 'otherwordlyrics') using regex.
    - If the word 'lyrics' is found, all content before and including it is removed.
    - If the word 'lyrics' is not found, the original text is returned unchanged.
    """
    split = text.split()

    for expression in split:
        # Search if pattern exists anywhere
        if re.search(r"lyrics", expression):
            # Get the index to ignore what is before
            get_index = split.index(expression)
            return " ".join(split[get_index + 1 :])

    return " ".join(split)


# Replace "tal vez" for "quizás"
def del_tal_vez(lyrics):
    """
    Replace the Spanish phrase "tal vez" with its synonym "quizás" to avoid issues
    with word frequency analysis caused by treating "tal" and "vez" as separate words.

    Parameters
    ----------
    lyrics : str
        The lyrics text to be processed.

    Returns
    -------
    str
        The modified lyrics with all occurrences of "tal vez" replaced by "quizás".

    Notes
    -----
    - The function identifies occurrences of "tal vez" and replaces them with "quizás".
    - This helps maintain consistency in word frequency analysis for Spanish text.
    """
    split = lyrics.split()
    # Modify the split list
    for word in split:
        if word == "tal":
            next_word_index = split.index(word) + 1  # Next word index
            try:  # Handle 'tal' as last word of the lyric
                if split[next_word_index] == "vez":
                    split[next_word_index - 1] = "quizás"  # Replace 'tal' for 'quizás'
                    del split[
                        next_word_index
                    ]  # Delete 'vez', that remains at the same position
            except IndexError:
                pass

    return " ".join(split)


# A different cleaning, keeping all the words and newlines
def clean_modified(text):
    """
    Perform a different cleaning process on song lyrics, keeping all words and newlines intact.

    Parameters
    ----------
    text : str
        The raw lyrics text to be cleaned.

    Returns
    -------
    str
        The cleaned lyrics with unwanted expressions removed, retaining newlines.

    Notes
    -----
    - Removes repetitive expressions like 'ah', 'oh', 'uh', etc.
    - Keeps only letters, spaces, and newlines (including accented characters).
    - Collapses multiple spaces into a single space.
    - Removes empty lines from the text.
    """
    # Remove expressions similar to 'oh'
    text = re.sub(r"\b(?:a+h+|o+h+||u+h+|e+h+|mm+|ja+|la+|na+)\b", "", text.lower())
    # Keep only letters, spaces and new lines
    text = re.sub(r"[^\wáéíóúüñ'\n]", " ", text)
    # Collapse multiple spaces into one
    text = re.sub(r" +", " ", text)

    return "\n".join([line.strip() for line in text.split("\n") if line.strip()])


# A function to delete unnecessary information from lyrics, similar to after_lyrics
def after_lyrics_modified(text):
    """
    Remove unnecessary information from song lyrics, focusing on the first line.

    Parameters
    ----------
    text : str
        The raw lyrics text to be processed.

    Returns
    -------
    str
        The modified lyrics with the first line removed, if applicable.

    Notes
    -----
    - Splits the lyrics into lines and removes the first line, which may contain unwanted data.
    - If the input text is empty or has no lines to remove, the original text is returned unchanged.
    """
    try:
        split = text.split("\n")  # Split line by line, not word by word
        del split[0]  # Delete the first element: where not needed data is
        return "\n".join(split)
    except:
        return text
