from typing import Dict, List


def inverted_index_to_text(inverted_index: Dict[str, int]) -> str:
    words_list: List[str] = []
    text: str = ''
    for word, indices in inverted_index.items():
        for index in indices:
            words_list.insert(index, f' {word}')
    return text.join(words_list)
