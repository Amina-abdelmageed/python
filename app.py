
import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split text into words and remove stop words
    words = [word for word in text.split() if word not in stop_words]
    return words

def count_word_frequency(words):
    # Count the frequency of each word
    return Counter(words)

def main():
   
        # Read the contents of the file
        with open('random_paragraphs.txt', 'r') as file:
            text = file.read()
        
        # Remove stop words from the text
        words = remove_stop_words(text)
        
        # Count the frequency of each word
        word_freq = count_word_frequency(words)
        
        # Display the word frequency count
        for word, freq in word_freq.items():
            print(f'Word: {word}, Frequency: {freq}')
    
    

if __name__ == "__main__":
    main()