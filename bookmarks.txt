import chrome_bookmarks
from sentence_transformers import SentenceTransformer
import numpy as np
import webbrowser


def open_bookmark(keyword):
    print(f'Keyword  - {keyword}')
    bookmarks_dict = {x.name: x.url for x in chrome_bookmarks.urls}
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path)

    def cosine(u, v):
        return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

    def sentence_similarity(source_sentence, compared_sentence):
        source_vec = model.encode([source_sentence])[0]
        comp_vec = model.encode([compared_sentence])[0]
        sim = cosine(source_vec, comp_vec)
        return sim

    sim_list = {sentence_similarity(keyword, key): value for key, value in bookmarks_dict.items()}
    print(f'Similar percentage - {max(sim_list.keys())}')
    url_res = sim_list[max(sim_list.keys())]
    webbrowser.get(chrome_path).open_new(url_res)
