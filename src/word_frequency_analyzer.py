from src.logger import logging
from src.exception import CustomException
import os, sys
class WordFrequencyAnalyzer:
    unique_words_list = list()
    word_counts = dict()
    highest_freq = dict()
    __words_list = list()
    result = str()
    

    def __init__(self,analysing_string):
        try:
            self.__analysing_string = analysing_string
            logging.info(f"string :{self.__analysing_string}")
            self.__analyze()
        except Exception as e:
            raise CustomException(e, sys)
    
    def __analyze(self):
        try:
            logging.info(f"analyzing started")
            self.__seprating_words()
            self.__identifying_unique_words()
            self.__words_frequency()
            self.__highest_freq()
            self.__highest_length()
            self.__render_result()
        except Exception as e:
            raise CustomException(e, sys)
    
    def __seprating_words(self):
        try:
            WordFrequencyAnalyzer.__words_list = []
            temp = str()
            for character in self.__analysing_string:
                #print(character, end="")
                if character.isalpha():
                    temp = temp + character
                else:
                    if temp != "" and len(temp)>1:
                        logging.info(f"Detected Word : '{temp}'")
                        WordFrequencyAnalyzer.__words_list.append(temp)
                    temp = ""   
        except Exception as e:
            raise CustomException(e, sys)  
    
    def __identifying_unique_words(self):
        try:
            WordFrequencyAnalyzer.unique_words_list = list(set(WordFrequencyAnalyzer.__words_list))
            logging.info(f"unique words list : {WordFrequencyAnalyzer.unique_words_list}")
        except Exception as e:
            raise CustomException(e, sys) 
    
    def __words_frequency(self):
        try:
            for unique_word in WordFrequencyAnalyzer.unique_words_list:
                count = 0
                for word in WordFrequencyAnalyzer.__words_list:
                    if unique_word == word :
                        count = count + 1
                WordFrequencyAnalyzer.word_counts[unique_word] = count
        except Exception as e:
            raise CustomException(e, sys)
            
    def __highest_freq(self):
        try:
            highest = list()
            highest_len = 1
            for word in WordFrequencyAnalyzer.word_counts:
                if WordFrequencyAnalyzer.word_counts[word] == highest_len:
                    highest.append(word)
                    highest_len = WordFrequencyAnalyzer.word_counts[word]
                if WordFrequencyAnalyzer.word_counts[word] > highest_len:
                    highest.clear()
                    highest.append(word)
                    highest_len = WordFrequencyAnalyzer.word_counts[word]
            WordFrequencyAnalyzer.highest_freq["Word"] = highest
            WordFrequencyAnalyzer.highest_freq["frequency"] = highest_len
        except Exception as e:
            raise CustomException(e, sys)
    

    
    def __highest_length(self):
        try:
            highest_length_word = list()
            length = 1
            if len(WordFrequencyAnalyzer.highest_freq["Word"]) >1:
                for word in WordFrequencyAnalyzer.highest_freq["Word"]:
                    if len(word)==length:
                        highest_length_word.append(word)
                        length = len(word)  
                    if len(word)>length:
                        highest_length_word.clear()
                        highest_length_word.append(word)
                        length = len(word)
            else:
                if len(WordFrequencyAnalyzer.highest_freq["Word"]) ==1:
                    highest_length_word.append(WordFrequencyAnalyzer.highest_freq["Word"][0])
                    length = len(WordFrequencyAnalyzer.highest_freq["Word"][0])
            WordFrequencyAnalyzer.highest_freq["highest_len_Words"] = highest_length_word
            WordFrequencyAnalyzer.highest_freq["highest_length"] = length
        except Exception as e:
            raise CustomException(e, sys)   
    def __render_result(self):
        try:
            words_freq = str()
            words_len = str()
            for index in ['Word','highest_len_Words']:
                print(index)
                if len(WordFrequencyAnalyzer.highest_freq[index])>1:
                    string = ""
                    for word in WordFrequencyAnalyzer.highest_freq[index]:
                        string = string + "'"+word+"', "
                else:
                    string = "'"+WordFrequencyAnalyzer.highest_freq[index][0]+"'"
                string =string.removesuffix(",")
                if index == 'Word':
                    words_freq = string
                else:
                    words_len = string
            logging.info(WordFrequencyAnalyzer.highest_freq)        
            WordFrequencyAnalyzer.result = f"""There are total {len(WordFrequencyAnalyzer.__words_list)} words out of which {len(WordFrequencyAnalyzer.unique_words_list)} are unique words \n\n From the given string we can note that the most frequent words are {words_freq} and they appeard {WordFrequencyAnalyzer.highest_freq['frequency']} times, and words having maxium length from most frequent words are {words_len} and its/there corresponding length is {WordFrequencyAnalyzer.highest_freq['highest_length']}"""
        except Exception as e:
            raise CustomException(e,sys)