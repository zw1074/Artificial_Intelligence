# Solution for text mining
This README file will introduce the problem and give the method to solve it.

## Problem Introduction
The problem wants to find a way to cluster those eminent guys by their biography. The detail for it is presented [here](http://cs.nyu.edu/courses/fall15/CSCI-GA.2560-001/prog4.pdf).

Input for this problem is like
```
Bella Abzug 
An American lawyer, U.S. Representative, social activist and a
leader of the Women's Movement. Abzug joined other leading feminists
such as Gloria Steinem and Betty Friedan to found the National Women's
Political Caucus. 

Benjamin Britten
A composer, conductor and pianist. He was a central figure of
twentieth-century British classical music, with a range of works 
including opera,
other vocal music, orchestral and chamber pieces. 
```

And the ouput is like
```
Politician Social: Bella Abzug, Charles de Gaulle, Benjamin Disraeli, Segolene Royal, 
Composer Music: Benjamin Britten, John Cage, Lady Gaga, Erik Satie
Writer Author : Willa Cather, Simone de Beauvoir, George Eliot, Naguid Mahfouz, Hilary Mantel, Toni Morrison
Scientist Physicist: Marie Curie, Rosalind Franklin, Aung San Suu Kyi, John Lewis, Barbara McClintock, Jean Perrin, Sin Itiro Tomonaga
```

## How to compile it
There are four `.py` files.
### utility.py
This file stores the **kmeans** method. In the `kmeans` function, you can select three matric. They are `L2, pearson, cosine`.

### DataClean.py
This file makes the data cleaning process. I mainly use regular expression to extract their name and biography. Then I use **Porter Stemming Algorithm** (referred from [here](http://tartarus.org/~martin/PorterStemmer/)) to stem words. Also I set up some limitation:

1. Discard all stop words and all words of fewer than three characters
2. Discard any word that appears in more than half of the texts or appear only once.

Then the function `matrix_construct(Biography, method = "frequency")` construct the matrix for the input of kmeans. The method here is how to set the weights of each word. I set up two method, one is *frequence* which is only how many times the particular word appears in one biography. And the other is TFIDF (referred from the book [Data Science for Bussiness written by Foster Provost & Tom Fawcett](http://www.amazon.com/Data-Science-Business-data-analytic-thinking/dp/1449361323)).

### P_S_algo.py
**Porter Stemming Algorithm**

### main.py
This file is the main program for this assignment. To compile it, type the following script in any bash command line system:
```
python main.py
```
You can change the input file by changing `'Sample.txt'` in 
```python
Name, Biography = dataclean("Sample.txt","stopwords2.txt")
```
Also you can change the output file by changing `'output.txt'` in
```python
Group(bestmatches, matrix, whole, Name, 'output.txt')
```
To change the matric, you can change the third parameter in
```python
bestmatches = kmeans(matrix, 100, cosine, 4)
```
You have three option: `cosine`-cosine matric, `pearson`-pearson correlation, `L2`-L2 matric
And you can change the weight algorithm of each word by changing `"frequency"` in
```python
matrix, whole = matrix_construct(Biography, "frequency")
```
You have two option: `"frequency"` for word freqency and `"TFIDF"` for TFIDF method.