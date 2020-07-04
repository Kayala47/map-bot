# Notes #

This is where I'll put everything I'm learning in regards to Machine Learning, starting with some of the acronyms Prof. Osborn used. 

## BERT ##

Explained thanks to: [Towards Data Science BERT page](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)

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

#### Next Sentence Prediction (NPS) ####

Here, the model receives a pair of sentences as input and has to learn to tell whether the second sentence is the subsequent sentence to the first. About half of the pairs given actually are sequential, while in the other 50%, a randomly chosen sentence is given as the second half of the pair (under the assumption that the random sentence is not sequential). 

The input is processed in the following way before entering the model: 

1. a [CLS] token is inserted at the beginning of the first sentence and a [SEP] token is inserted at the end of each sentence
2. A sentence embedding indicating Sentence A or Sentence B is added to each token. Sentence embeddings are similar in concept to token embeddings with a vocabulary of 2. 
3. A positional embedding is added to each token to indicate its position in the sequence. 

![](notes-imgs\BERT-nsp.PNG)

Once it's prepared in the above way, the model can then try to predict whether the second sentence is connected to the first, with the following steps:

1. The entire input sequence goes through the Transformer model
2. The output of the [CLS] token is transformed into a 2x1 shaped vector, using a simple classification layer (learned matrices of weights and biases)
3. Calculating the probability with softmax

## LSTM ##
= Long-Term, Short-Term Memory

Explanation from: [Towards Data Science LSTM/GRU page](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)

### Problem: Short-Term Memory

Recurrent Neural Networks have short term memory; they may lose information if a sequence is long enough. Esp. for things like processing a paragraph of text, they may not be the best bc they can lose stuff from the beginning. 

Recurrent neural networks suffer from the vanishing gradient problem. (Gradients are values used to update a neural network's weights). The problem is that the gradient shrinks as it propogates back through time. If it becomes extremely small, it doesn't help with learning at all.

### The Solution: LSTM's (and GRU's) ###

LSTMs and GRUs have internal mechanisms called gates that regulate information. Those gates can learn which info to keep and which to throw way, which means they can pass relevant info down the long chain of sequences to make predictions. 

### Core Concept ###

The core concept is the cell state and various gates. The cell state act as a transport highway that transfers relative information all the way down the sequence chain. It's the "memory" of the network. 

As it travels throughout the sequence, the cell state has information added or removed to it by the gates. The gates are different neural networks that decide which information is allowed on the cell state. The gates can learn what information is relevant to keep or forget during training. 

Gates contain sigmoid activations (similar to tahn activation). Instead of squishing values between -1 and 1, it squishes between 0 and 1. To forget values, it can multiply them by 0. 

#### Gate Types ####
**Forget gate** - decides what information should be thrown away. It spits out values from 0 to 1, and values close to 0 means forget, closer to 1 means keep.

**Input Gate** - These update the cell state. Again, spits out values from 0 to 1, with 0 being not important and 1 being important. First, we pass the previous hidden state and current input into a sigmoid function, which transforms them between 0 and 1. Then, we pass the hidden state and current input into the tahn function, which spits out between -1 and 1. Multiplyting the tahn output with the sigmoid output so that the sigmoid output decides which info to keep from the tanh output. 

**Cell state** - To get our new cell state, we first multiply by the forget vector, which has a chance of deleting info if it was close to 0. Then take the output form the input gate and do a pointwise addition which updates the cell state to new values that the neural network finds relevant. 

**Output Gate** - the output gate decides what the next hidden state should be. The hidden state contains info on previous inputs and is used for predictions. First, we pass the previous hidden state and the current input into a sigmoid function. Then we pass the newly modified cell state to the tanh function. We multiply tahn output times sigmoid output to decide what info the hidden state shuold carry. The output is the hidden state. The new cell state and the new hidden state is then carried over to the next step. 

To review, the Forget gate decides what is relevant to keep from prior steps. The input gate decides what information is relevant to add from the current step. The output gate determines what the next hidden state should be.


## VAE ##
= Variational auto-encoders

Explanation by: [Towards Data Science VAE Page](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73)

A deep generative model, like GAN. VAE is an autoencoder whose encodings distribution is regularised during the training in order to ensure that its latent space has good properties allowing us to generate some new data. 

Autoencoders cannot be used to generate new data; Variational Autoencoders are regularised versions of autoencoders making the generative process possible. 

### Dimensionality Reduction ###
= the process of reducing the number of features that describe some data. This is done either by selection (only some features are conserved) or by extraction (a reduced number of new features are created based on the old features). This is useful in situations that require low dimensional data, such as data visualization, data storage, heavy computation, etc. 

The main idea is this:

![](notes-imgs\dimensionality-reduction.PNG)


For a set of info, there is an encoder that produces new features from the old and a decoder that can reverse the process. Sometimes, that process is "lossy" - it produces loss. The purpose of dimensionality reduction is to find the best encoder/decoder pair among a given family, so that we keep as much of the information as we can. Again, we're looking for **maximum information kept when encoding** and **minimum reconstruction error when decoding**. 

#### Principal Components Analysis (PCA) ####

A method of dimensionality reduction

= the idea of PCA is to build $n_e$ new independent features that are linear combinations of the $n_d$ old features in a way that the projections of the data on the subspace defined by these new features are as close to the initial data (in terms of euclidean distance) as possible. 

The idea of PCA is to build n_e new independent features that are linear combinations of the n_d old features and so that the projections of the data on the subspace defined by these new features are as close as possible to the initial data (in term of euclidean distance). In other words, PCA is **looking for the best linear subspace of the initial space** (described by an orthogonal basis of new features) such that the error of approximating the data by their projections on this subspace is as small as possible.
> Ask question abuot this above secion - what does it mean to create a linear combination, and what is a linear subspace of a space?



## GAN ##
= Generative Adversarial Networks

Explanation from: [Towards Data Science GAN Page](https://towardsdatascience.com/understanding-generative-adversarial-networks-gans-cd6e4651a29)

- generative means they can produce new content

We start by just being able to generate random variables (or as close to random as we can get).There are many different methods of generating these variables, including rejection sampling, Metropolis-Hasting algorithm, inverse transform method, etc.

To create generative models, we essentially try to create random variables along a probability that we've established. To do this, we turn the data into a dimensional vector by stacking columns on top of each others. For example, we can represent an image of a dog as a vector. to generate a new image of a dog, we'd have to look at which variables are present where in other pictures of dogs, and where they would be probabilistically. Then, we can generate variables according to those probabilites. 


## Sequence to Sequence Translation ##

## Transposed Convolutions ##

## Recurrent Neural Networks (optional) ##

## Other relevant Definitions ##

### Softmax ###
= a normalized exponential function. It takes an input of a vector, z, of K real numbers, and normalizes it into a probability distribution consisting of K probabilities proportional to the exponentials of the input numbers. 
- ie, it maps inputs such that each component will be in the interval (0,1) and all of them together will add to one. Thus they can be interpreted as probabilities. It's a way of normalizing data common to neural networks. 

### Embedding Matrix ###
= a way to represent inputs that come from discrete domains (ex: words in a sentence, nodes in a network). 

In the context of language, we'd assign a number to each word, except then we'd be in the unfortunate situation where word1 < word2. So we don't want something like (word1 = 1, word2 = 2). Rather, we can make it a matrix so that there's no strict order between the two. 

Thus, our dictionary becomes word1 = [0, 0, 0, 1] and word2 = [0, 0, 1, 0]. And yet, this still doesn't code as much info as we want in there. We want there to be some meaning to these matrices, so that our computer understands that words like "dog" and "cat" are more related to each other than "dog" and "like" (both mammals versus a verb and a noun"). 

An embedded matrix is a linear mapping from the original space (one of k) to a real-valued space where entities can have meaningful relationships, so that distance(dog x $W_e$, cat x $W_e$) < distance(dog x $W_e$, like x $W_e$). The embedding matrix, $W_e$, is an element of $R^{K*D}$

### Token Embedding ###
The purpose of Token Embeddings is to transform words into vector representation of fixed dimensions. for BERT, each word is represented as a 768-dimensional vector. Token Embedding is a layer which turns each word, or token, into a 768-dimensional vector representation. 

## Others ##

GELU

Norm