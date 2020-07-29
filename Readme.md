# Aspect based co attention model for recommendation

Our research is based on expanded MovieLens 1M dataset. Our baseline is [MLAM]. [1]

Firstly, we use an aspect extraction tool which named [Sentires] to extract aspect words of the movie stories. Then we generate our aspect lexicon and use it to filter the dataset. We develop a recommendation model which is based on aspect information and cast member information of movies. In this model, we convert these information to embedding vectors and calculate two attention distribution on them: global attention distribution and co-attention distribution. Especially, we implement two kinds of co-attention mechanism. The model will finally calculate a recommendation score based on these two attention distribution, and we can use this score to recommend movies to users. 

We do some experiments of our model and make comparisons. The results show that our model is explicitly better than the baselines.

[1] Hu L, Jian S, Cao L, et al. Interpretable Recommendation via Attraction Modeling: Learning Multilevel Attractiveness over Multimodal Movie Contents[C]//IJCAI. 2018: 3400-3406.



   [MLAM]: <https://github.com/rainmilk/ijcai18mlma>
   [Sentires]: <http://yongfeng.me/code/>
