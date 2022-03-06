import random
import Words

class Dict:
    def __init__(self):
        self.prompt = ""
        self.words = []
        self.impressive_words = []
        self.simple_words = []
        self.wordDict = {}
        self.impWordDict = {}
        self.simpWordDict = {}

    # def save(self, str):
    #     with open("Prompts.txt", "a") as file:
    #         word = file.write(str)
    #     file.close()

    def makeLists(self, lang):
        if lang == 1:
            with open("englishwords.txt", "r") as file:
                word = file.readline()
                while word:
                    word = word.strip()
                    self.words.append(word.lower())
                    if len(word) >= 10:
                        self.impressive_words.append(word.lower())
                    if len(word) <= 5:
                        self.simple_words.append(word.lower())
                    word = file.readline()
            print(self.words)
            file.close()
        if lang == 2:
            self.words = Words.words

    def findAnswer(self, sub):
        # self.save(sub+"\n")
        if sub in self.wordDict:
            return self.wordDict[sub].pop()
        else:
            subList = []
            for word in self.words:
                if sub in word:
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
