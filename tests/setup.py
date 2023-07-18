from src.utils.inverted_index import inverted_index_to_text


def inverted_index() -> dict:
    return {'This': [0], 'paper': [1], 'clarifies': [2], 'the': [3, 9, 12, 15, 29, 32, 45], 'characteristics': [4], 'of': [5], 'parallel': [6, 20], 'conductors': [7, 21], 'and': [8, 50], 'mechanism': [10], 'for': [11], 'phenomenon': [13], 'at': [14, 31], 'light': [16, 33, 46], 'line.': [17], 'By': [18], 'analyzing': [19], 'with': [22, 54], 'an': [23], 'equivalent': [24], 'circuit': [25], 'model': [26], 'including': [27], 'retardation,': [28], 'singularity': [30], 'line': [34, 47], 'is': [35, 41], 'clarified.': [36], 'Using': [37], 'this': [38], 'singularity,': [39], 'it': [40], 'possible': [42], 'to': [43], 'excite': [44], 'mode': [48], 'specifically': [49], 'form': [51], 'a': [52, 55], 'beam': [53], 'sharp': [56], 'directivity.': [57]}


def expected_text() -> str:
    return " This paper clarifies the characteristics of parallel conductors and the mechanism for the phenomenon at the light line. By analyzing the the with an equivalent circuit model including retardation, the singularity parallel conductors and line is clarified. Using this singularity, it at possible to excite light light with mode specifically line form a beam is a sharp directivity."


def test_inverted_index() -> bool:
    arrange_inverted_index = inverted_index()
    arrange_expected_text = expected_text()

    assert inverted_index_to_text(
        arrange_inverted_index) == arrange_expected_text
