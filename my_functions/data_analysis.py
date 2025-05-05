import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import json

## Data analysis


# Getting emotion labels with nltk and custom labels/thresholds
def get_emotion(text, language):
    """
    Analyze the emotional tone of song lyrics using sentiment analysis and custom word lists.

    Parameters
    ----------
    text : str
        The lyrics text to be analyzed.
    language : str
        The language of the lyrics ('English' or 'Spanish').

    Returns
    -------
    str
        The dominant emotion in the lyrics, which can be one of the following:
        - 'joy': Positive sentiment is dominant.
        - 'anger': Negative sentiment is dominant, and anger-related words are present.
        - 'sadness': Negative sentiment is dominant, but no anger-related words are present.
        - 'neutral': Neutral sentiment is dominant.

    Notes
    -----
    - Uses NLTK's SentimentIntensityAnalyzer to calculate sentiment scores.
    - Custom word lists are used to identify anger-related words for English and Spanish.
    - The function determines the dominant emotion based on sentiment scores and word matches.
    """
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    words = text.split()

    # Anger indicators
    anger_words = {
        "English": ["no", "never", "hate", "stop"],
        "Spanish": ["no", "nunca", "odio", "basta"],
    }

    emotions = {
        "joy": scores["pos"] > 0.5,
        "anger": (scores["neg"] > 0.5)
        and any(w in anger_words[language] for w in words),
        "sadness": (scores["neg"] > 0.5)
        and not any(w in anger_words[language] for w in words),
        "neutral": scores["neu"] > 0.7,
    }

    return max(emotions, key=emotions.get)  # Get the key of the highest emotion score


# Get top words
def get_top(x):
    """
    Retrieve the top 10 most common words from a given text.

    Parameters
    ----------
    x : str
        The input text from which to extract the most common words.

    Returns
    -------
    str
        A string containing the 10 most common words, separated by spaces.

    Notes
    -----
    - The function uses Python's Counter to count word frequencies.
    - Words are sorted by frequency in descending order, and ties are resolved by their order of appearance.
    """
    return " ".join([song for song, _ in Counter(x.split()).most_common(10)])


# Enhanced approach to get labels by using customized lexicons
def get_emotion_with_lexicons(lyrics, path):
    """
    Analyze the emotional tone of song lyrics using custom emotion lexicons.

    Parameters
    ----------
    lyrics : str
        The lyrics text to be analyzed.
    path : str
        The file path to a JSON file containing custom emotion lexicons.

    Returns
    -------
    str
        The dominant emotion in the lyrics, based on the highest match count from the lexicons.
        If no matches are found, 'neutral' is returned.

    Notes
    -----
    - The function loads emotion lexicons from a JSON file, where each emotion is associated
      with a list of trigger words.
    - Counts the occurrences of words in the lyrics that match the trigger words for each emotion.
    - Returns the emotion with the highest count. If all counts are zero, 'neutral' is returned.
    """
    # Retrieve the lexicons from a json file
    with open(path, "r") as f:
        emotion_lexicons = json.load(f)
    # Count matches against emotion lexicons
    emotion_counts = {emotion: 0 for emotion in emotion_lexicons}

    for word in lyrics.split():
        for emotion, triggers in emotion_lexicons.items():
            if word in triggers:
                emotion_counts[emotion] += 1
                break  # No need to check other emotions for this word

    # Get emotion with highest count (returns 'neutral' if all are 0)
    return (
        max(emotion_counts, key=emotion_counts.get)
        if max(emotion_counts.values()) > 0
        else "neutral"
    )


# Get bigrams
def get_bigrams(lyrics):
    """
    Generate a list of bigrams (pairs of consecutive words) from a subset of song lyrics.

    Parameters
    ----------
    lyrics : list of str
        A list of song lyrics, where each element is a string representing the lyrics of a song.

    Returns
    -------
    list of tuple
        A list of tuples, where each tuple contains two consecutive words (bigrams) from the lyrics.

    Notes
    -----
    - The function processes each lyric in the subset individually.
    - Words are split by spaces, and bigrams are created by pairing consecutive words.
    - The resulting list contains all bigrams from all lyrics in the subset.
    - Use the result with counter to get tops: [*Counter(bigrams).most_common(7)]
    """
    result = []
    for lyric in lyrics:
        words = lyric.split()
        result.extend(
            [*zip(words[:-1], words[1:])] # Extend method concatenates the new list
        )  
    return result


# Get the last words of the lines
def get_last_word(lyrics):
    """
    Extract the last word from each line of song lyrics.

    Parameters
    ----------
    lyrics : str
        The lyrics text to be processed.

    Returns
    -------
    list of str
        A list containing the last word of each line in the lyrics.

    Notes
    -----
    - The function uses a regular expression to identify the last word before a newline character.
    - Empty lines are ignored, and only non-empty lines contribute to the result.
    """
    last_words = re.findall(
        r"(\w+)\s*\n", lyrics
    )  # Returns a list, so split not needed
    return last_words


# Get the rhyme scores
def rhyme_simple(lyrics):
    """
    Calculate a simple rhyme score for song lyrics based on the last words of each line.

    Parameters
    ----------
    lyrics : str
        The lyrics text to be analyzed.

    Returns
    -------
    int
        The rhyme score, representing the number of consecutive lines that end with words
        sharing the same last two letters.

    Notes
    -----
    - The function extracts the last word from each line using `get_last_word`.
    - It compares the last two letters of consecutive words to determine rhymes.
    - The score is incremented for each pair of consecutive lines that rhyme.
    """
    words = get_last_word(lyrics)
    # Check last two letters, adding 1 if the condition is met
    return sum(1 for i in range(len(words) - 1) if words[i][-2:] == words[i + 1][-2:])
