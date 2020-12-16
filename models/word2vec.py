from gensim.models.word2vec import Word2Vec

class Word2VecModel:

    def __init__(
            self, sentences=None, vector_size=100, window=5, 
            min_count=5, workers=3, epochs=5):
        
        self._model = Word2Vec(
                sentences=sentences, size=vector_size, window=window, 
                min_count=min_count, workers=workers, iter=epochs)

    @property
    def model(self):
        return self._model

    @property
    def wv(self):
        return self._model.wv

    def most_similar_to(self, positive_tokens, topn=10):
        """Returns words most similar to positive_tokens.

        Returns the top topn most similar tokens to positive_token.
        This functions is a wrapper to KeyedVector.most_similar.

        Args:
            positive_tokens (list of str): List of tokens to be searched.
            topn (int, optional): Number of most similar words to be 
                returned. Defaults to 10.

        Returns:
            list of (str, float): Most similar tokens with 
                similiraty measure.
        """

        return self.wv.most_similar(positive=positive_tokens, topn=10)
        