from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_mcqs(text, num=5):
    prompt = f"""
    Generate {num} MCQs from the given text.
    Format output EXACTLY like this:

    Q1: Question text?
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4
    Answer: A

    Q2: ...
    ...
    
    Text: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return parse_mcqs(raw)


def parse_mcqs(text):
    """Formats MCQs into structured readable blocks"""

    mcqs = text.strip().split("\n\n")  # split block-wise

    formatted_mcqs = []
    for mcq in mcqs:
        lines = mcq.split("\n")
        if len(lines) >= 6:
            formatted_mcqs.append({
                "question": lines[0],
                "A": lines[1],
                "B": lines[2],
                "C": lines[3],
                "D": lines[4],
                "answer": lines[5]
            })
    return formatted_mcqs
