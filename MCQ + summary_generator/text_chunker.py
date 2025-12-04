import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_text(text, max_words=350):
    sentences = sent_tokenize(text)
    chunks, current = [], []
    word_count = 0

    for s in sentences:
        w = len(s.split())
        if word_count + w > max_words:
            chunks.append(" ".join(current))
            current, word_count = [s], w
        else:
            current.append(s)
            word_count += w

    if current:
        chunks.append(" ".join(current))
    return chunks
