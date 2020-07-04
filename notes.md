# Notes #

This is where I'll put everything I'm learning in regards to Machine Learning, starting with some of the acronyms Prof. Osborn used. 

## BERT ##

Explained thanks to: [Towards Data Science Article](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)

= Bidirectional Encoder Representations from Transformers
- It uses bidirectional training of Transformer. Trnasformer is already a popular attention model. Previous architectures only did left to right or vice versa; but in a paper by researchers at Google AI Language, they showed that a bidirectionally trained model can have a deeper sense of language context and flow
- Some approaches used in the past are transfer learning - where you first train the model on a known task and then do some fine-tuning, using the trained model as the basis of a purpose specific model. Another approach is feature-based training, wherein a pre-trained neural network produces word embeddings which are then used as features in NLP models. 
- bidirectional = this Transformer reads the entire sequence of words at once, so it is able to look at contextual relationships to the left and the right of each word. This is opposed to traditional models, where it either reads left to right or right to left. It's really not so much bidirectional as non-directional, since it doesn't look at them in any sequence. But this helps it learn context a lot better, since it's looking at many more options. 

### Training Strategies ###
- most prediction using other architectures is predicting the net word in a sequence, such as "bob likes ___". This is super directional. BERT uses two training strategies:

#### Masked LM (MLM) ####

Random words (about 15% of the original text) are replaced in the corpora. The model attempts to figure out what the value of those masked words was, using the context of the non-masked words around it to help. 

The prediction of outputs requires:

1. Adding a classification layer on top of encoder output
2. Multiplying the output vectors by the embeding matrix, transforming them into the vocabulary dimension 
3. Calculating the probability of each word in the vocabulary with softmax

![Image of MLM steps](notes-imgs\BERT-mlm.PNG)



## LSTM ##

## VAE ##

## GAN ##

## Sequence to Sequence Translation ##

## Transposed Convolutions ##

## Other relevant Definitions ##

### Softmax ###
= a normalized exponential function. It takes an input of a vector, z, of K real numbers, and normalizes it into a probability distribution consisting of K probabilities proportional to the exponentials of the input numbers. 
- ie, it maps inputs such that each component will be in the interval (0,1) and all of them together will add to one. Thus they can be interpreted as probabilities. It's a way of normalizing data common to neural networks. 

### Embedding Matrix ###
= a way to represent inputs that come from discrete domains (ex: words in a sentence, nodes in a network). 

In the context of language, we'd assign a number to each word, except then we'd be in the unfortunate situation where word1 < word2. So we don't want something like (word1 = 1, word2 = 2). Rather, we can make it a matrix so that there's no strict order between the two. 

Thus, our dictionary becomes word1 = [0, 0, 0, 1] and word2 = [0, 0, 1, 0]. And yet, this still doesn't code as much info as we want in there. We want there to be some meaning to these matrices, so that our computer understands that words like "dog" and "cat" are more related to each other than "dog" and "like" (both mammals versus a verb and a noun"). 

An embedded matrix is a linear mapping from the original space (one of k) to a real-valued space where entities can have meaningful relationships, so that distance(dog x $W_e$, cat x $W_e$) < distance(dog x $W_e$, like x $W_e$). The embedding matrix, $W_e$, is an element of $R^{K*D}$

