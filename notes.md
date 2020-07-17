# Notes #

This is where I'll put everything I'm learning in regards to Machine Learning, starting with some of the acronyms Prof. Osborn used. 


## Noise Generation ##

For things like map generation, we often want some degree of randomness. Most of the time, we use uniform generators, ie random.randint(1,100) is equally likely to produce numbers in the 1-100 range. Sometimes we can skew it, such as by squaring, square rooting, etc the values so we're more likely to get certain values. 

The problem is, we're still generating each value in isolation. Sometimes you want values appearing together, such as mountains naturally forming with other high terrain near each other. Noise generates values in a set. One example is with a 1D array: say it was generating a bunch of random numbers in a row. To create noise, you could take the min (or max) of the numbers in pairs, moving along the line. You'd end up with noise that was more likely to include clusters, so you'd have a larger area of valleys, mountains close together, etc.

There are several ways to generate noise for 2D/3D: you can use random numbers directly for output, or feed them in as parameters for either sin/cosine, or gradients. Simplex and Perlin Noise is based off using random numbers as parameters for gradients. 

You can also modify the noise you get! You can apply filters to add/remove certain features, add multiple noises together (usually you'd do this with weights so some layers affect more than others), or smooth out the existing noise. 

### Frequency ###

We can adjust frequency to achieve the desired effects. A lower fequency means you're more likely to see similar data bundled together, and higher means you're going to get more variation from space to space. To increase the frequency, you're going to multiply the *input* by some factor: sin(2x) has twice as much frequency as sin(x). 

### Amplitude ###

Increasing the amplitute is a vertical change, it affects how high your values get. To do this, you're going to multiply the *output*. 2 sin(x) has twice as high amplitude as sin(x).


Here is the github for examples: [Caseman Noise](https://github.com/caseman/noise/blob/master/examples/2dtexture.py)

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

To create generative models, we essentially try to create random variables along a probability that we've established. To do this, we turn the data into a dimensional vector by stacking columns on top of each others. For example, we can represent an image of a dog as a vector. to generate a new image of a dog, we'd have to look at which variables are present where in other pictures of dogs, and where they would be probabilistically. Then, we can generaactuallyte variables according to those probabilites. 

> look more closely into transform method




## Sequence to Sequence Translation ##

= a sequence to sequence model aims to map a fixed-length input with a fixed-length output where the length of the input and output may differ. Ex: Google Translare. 

Explanation by: [Towards Data Science StS page](https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346)

![Encoder Decoder Model of Sequence to Sequence Translation](notes-imgs\sts-encoder-decoder.PNG)

There are three parts to this model: 

### Encoder ###

This is a stack of LSTM or GRU elements. Each takes a single element of the input, collects information for it, and then propagates it forward. 
- in question answering problems, you pass in each word one by one, marked with a number for its position in the sequence. 
- you compute hidden states using the formula:
![](notes-imgs\sts-encoder-formula.PNG)
- it uses a recurrent neural network to apply appropriate weight to each previous s hidden state and the input vector

### Intermediate (encoder) vector ###

This is the final hidden state produced from the encoder. It aims to encapsulate all the ifnormation for all input elements and will act as the initial hidden state of the decoder part of the model. 

### Decoder ###
- another stack of recurrent units, each predicting an output y_t at time t. 
- each recurrent unit accepts not only its own hidden unit, but also the hidden state from the previous unit and produces an answer for that. 
-  for question answering, each unit would be producing one word of the answer. 
- we use the previous hidden state to compute the next one. Using softmax, we calculate the outputs using the hidden state at the current step together with the respective weight. We're basically making a probability vector with softmax. 


## Transposed Convolutions ##
= the Convolution operation reduces the spatial dimensions as we go deeper down the network and creates an abstract representation of the input image. It's good for things like image classification because you just have to predict an object's presence, but much more problematic for tasks like Object Localization, or Segmentation, where the spatial dimensions of the object ar necessary to predict the output bounding the box or segment the object. 

> Does this mean it wouldn't be good for generating the image? Since it's not going to be very good at keeping track of where to put items? 
>
> Answer: no, there are techniques to fix this, such as using 'same' padding to preserve the input dimensions. This is done in a fully convolutional neural network.

Explained by: [Towards Data Science TC page](https://towardsdatascience.com/transposed-convolution-demystified-84ca81b4baba#:~:text=Transposed%20convolution%20is%20also%20known,upsample%20the%20input%20feature%20map.)

Another technique used for image segmentation is dividing 
![](notes-imgs\trans-conv-same-padding.PNG)
The problem with the above method is that it increases the computation cost because the convolution operation has to be applied to original input dimensinos throughout the network. 

There is another method, referred to as Downsampling & Upsampling. In this method, you'd use a downsampling network to turn a high res image into a low res representation using CNN architectures. Then, you'd use the Upsampling network to take the abstract images and make their spatial dimensions equal to the input image. 

> They didn't go into downsampling

### Upsampling ###

There are a couple of different techniques for this:

1. Nearest neighbors - take a pixel from one location in the lower res file and make that the value for pixels near that location in the higher res file. You copy the value into the K-nearest neighbors, and the value of K depends on the expected output.

![](notes-imgs\tc-nn.PNG)

2. Bi-Linear Interpolation - you assign pixels to the output image based on a weighted average of the pixels closest to it in the input image.

![](notes-imgs\tc-bilin.PNG)

3. Bed of nails - the pixels of the input image (downsampled version) get copied to the ouput image in the position they'd be, and everything else turns into a 0. 

![](notes-imgs\tc-bedNails.PNG)

4. Max-Unpooling - this depends on the Max-Pooling layer in the CNN taking the max value and the index of that value and saving those. The image gets downsampled regularly, but then upsampling, the max's index value is used to put max values back in the output image. All others are 0. 

![](notes-imgs\tc-maxPool.PNG)

Using some of the methods above, transposed convolutions upsample the input feature map. There are some learnable parameters that affect the process. 

The basic idea is as follows: (Consider a 2x2 input and expecting a 3x3 output)
- You start with the top left corner of the input image and take that as your first element. Then, the entire kernel is multiplied one by one by the element and put into the appropriate place on the output image. 

![](notes-imgs\tc-kernelxelem.PNG)

- Continue doing this for the rest of the elements in the input image. 
- you'll get some overlap. What you want to do is add up any elements that overlap. So for example, if a square would contain both a 2 and a 6, that square becomes an 8. 

![](notes-imgs\tc-kernelxelem-total.PNG)

The process of Transposed Convolution is also known as Deconvolution, but that's not a really good description since it implies removing the effects of convolution, and we're really not doing that here. 

It can also be called upsampled convolution, fractionally strided convolution. This is because stride over the output is equivalent to fractional stride over the input. Ex: a stride of 2 over output is 1/2 stride over the input. 

It is also referred to as backward strided convolution bc forward pass of Transposed Convolution is equivalent to backward pass of a normal convolution. 

### The Problem ###
Uneven overlap in some parts of the image causes artifacts, which lead to a "checkerboard" effect. To fix this, you can make sure that your kernel size is divisible by your stride. Ex: when your stride equals 2, you want your kernel size to be something like 2x2, 4x4, etc. 

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

### Stride ###

Stride is the amount by which a kernel is moved when it passes over an image. Here, a kernel refers to a set block of pixels. So if your stride is set to one, the kernel moves along by one pixel every time it chooses to represent new pixels. 

[Here is a good explanation on Quora](https://qr.ae/pNKznW)


## Others ##

GELU

Norm