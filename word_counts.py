from typing import *
sample_text = """As I was waiting, a man came out of a side room,
                and at a glance I was sure he must be Long John.
                His left leg was cut off close by the hip, and 
                under the left shoulder he carried a crutch,
                which he managed with wonderful dexterity, 
                hopping about upon it like a bird. He was very 
                tall and strong, with a face as big as a ham—plain 
                and pale, but intelligent and smiling. Indeed, he
                seemed in the most cheerful spirits, whistling as 
                he moved about among the tables, with a merry word 
                or a slap on the shoulder for the more favoured of his guests."""


def count_words(text: str) -> Dict[str, int]:
    """This is a function 
    to count word frequencies or 
    to count how many times each unique word occurs in the text.

    Args:
        text (str): A long string

    Returns:
        Dict[str, int]: A dictionary with sorted word frequencies
    """
    freq = {}
    for word in text.split(' '):
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return {word: freq[word] for word in sorted(freq, key=freq.get)}


if __name__ == "__main__":
    counts = count_words(sample_text)
    least_common = dict(list(counts.items())[:10])
    most_common = dict(list(counts.items())[-10:])
    print(f"10 least common unique words. \n{least_common}\n")
    print(f"10 most common unique words. \n{most_common}\n")
