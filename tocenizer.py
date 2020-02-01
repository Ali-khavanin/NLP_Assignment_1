from document_seperator import load_var
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('punkt')
documents = load_var('all_documents_seperated')

tokenized_data = [word_tokenize(doc)
                  for doc in documents]


dictionary = Dictionary(tokenized_data)

print(dictionary.token2id)

print(dictionary.dfs)

