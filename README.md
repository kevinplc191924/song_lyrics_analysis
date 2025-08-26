# 🎵 Song Lyrics Analysis

---

## Overview

This project analyzes the lyrics of 20 songs by the artists Sin Bandera and Loveless. The analysis uncovers emotional themes and linguistic patterns within their music, providing insights into the emotional landscape of their songs.

---

## Project Highlights

- Extract lyrics automatically from the Genius API.
- Clean and preprocess raw lyrics data.
- Perform emotional analysis using lexicons.
- Generate visualizations to summarize findings.

---

## Libraries Used
This project leverages several Python libraries for text processing, sentiment analysis, visualization, and data extraction:

- `pandas` → Data manipulation and tabular organization
- `numpy`	→ Numerical operations and array handling
- `matplotlib` →	Plotting and visualizations
- `seaborn` →	Statistical data visualization
- `wordcloud` →	Generating word cloud visualizations
- `nltk` →	Natural language processing (tokenization, stopwords, emotion lexicons)
- `vaderSentiment` →	Sentiment analysis using VADER
- `lyricsgenius` →	Accessing Genius API to retrieve song lyrics and metadata
- `re` →	Regular expressions for text cleaning
- `collections` →	Frequency counting and data structuring

---

## Project Structure
```text
- song_lyrics_analysis/
  - data/ # Not included in the repository
    - loveless.csv
    - songs.csv
    - sin_bandera.csv
  - my_functions/ # Code used in the notebooks
    - data_analysis.py
    - data_cleaning.py
    - data_extraction.py
  - analysis.ipynb
  - data_cleaning.ipynb
  - data_extraction.ipynb
  - emotion_lexicons.json
  - notes.md # Notes on dictionaries and related methods
  - .gitignore
  - README.md
  - requirements.txt
```

---

## 📊 Project Insights: Song Lyrics Analysis
This notebook explores the emotional and linguistic patterns embedded in song lyrics using natural language processing techniques. The goal is to uncover how sentiment, word choice, and thematic elements vary across different songs and artists.

## 🔍 Key Analytical Steps
- Data Cleaning and Preprocessing: Lyrics are tokenized, lowercased, and stripped of stopwords to prepare for analysis.
- Sentiment Analysis: Each song is scored using VADER to assess emotional tone (positive, negative, neutral, compound).
- Word Frequency and Visualization: Common words are visualized using bar plots and word clouds to highlight dominant themes.
- Emotion Mapping: Lyrics are mapped to emotions like joy, sadness, anger, and surprise using the NRC lexicon.
- Artist Comparison: Sentiment distributions are compared across artists to reveal style and emotional differences.

## 💡 Notable Findings
The process and results are in the `analysis.ipynb` file.
- Songs with higher compound sentiment scores tend to use more emotionally charged vocabulary.
- Certain artists consistently lean toward specific emotional tones (melancholic vs. happiness).
- Word clouds reveal recurring words that characterize the themes—love, time, pain, possibility, and dreams—across genres.

## 📁 Structure and Reproducibility
- Modular code cells allow for easy adaptation to new datasets.
- Markdown commentary guides the reader through each analytical step.
- Visualizations are embedded for intuitive interpretation.

---
