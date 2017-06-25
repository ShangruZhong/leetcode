"""
    211. Add and Search Word - Data structure design

    @date: 2017/06/10
"""
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_list = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word_list[len(word)].append(word)
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word or not self.word_list:
            return False
        if '.' not in word:
            return (word in self.word_list[len(word)])
        candidate = self.word_list[len(word)]
        for cand in candidate:
            flag = 0
            for i in xrange(len(word)):
                if word[i] == cand[i] or word[i] == '.':
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                return True
        return False
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)