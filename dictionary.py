import random
import frenchWords
import englishWords
# TODO Add SPANISH
# import spanishWords

class Dict:
    def __init__(self, lang):
        self.lang = lang
        self.prompt = ""
        self.words = []
        self.impressive_words = []
        self.simple_words = []
        self.wordDict = {}
        self.impWordDict = {}
        self.simpWordDict = {}

    def makeLists(self):
        if self.lang == 1:
            self.words = englishWords.words
        if self.lang == 2:
            self.words = frenchWords.words
        # if self.lang == 3:
        #     self.words = spanishWords.words

    def findAnswer(self, sub):
        if sub in self.wordDict:
            return self.wordDict[sub].pop()
        else:
            subList = []
            for word in self.words:
                if sub in word.lower():
                    subList.append(word)
            random.shuffle(subList)
            self.wordDict[sub] = subList
            return self.wordDict[sub].pop()

    def findAnswerImp(self, sub):
        if sub in self.impWordDict:
            return self.impWordDict[sub].pop()
        else:
            subList = []
            for word in self.impressive_words:
                if sub in word:
                    subList.append(word)
            random.shuffle(subList)
            self.impWordDict[sub] = subList
            return self.impWordDict[sub].pop()

    def findAnswerSimple(self, sub):
        if sub in self.simpWordDict:
            return self.simpWordDict[sub].pop()
        else:
            subList = []
            for word in self.simple_words:
                if sub in word:
                    subList.append(word)
            random.shuffle(subList)
            self.simpWordDict[sub] = subList
            return self.simpWordDict[sub].pop()
