"""
    208. Implement Trie (Prefix Tree)

    @date: 2017/01/20
"""
class TrieNode(object):
    
    def __init__(self):
        self.end = False
        self.next = {}
            
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) == 0:
            return
        node = self.root
        for i in xrange(len(word)):
            if word[i] not in node.next:
                node.next[word[i]] = TrieNode()
            node = node.next[word[i]]
        node.end = True
        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return
        node = self.root
        for i in xrange(len(word)):
            if word[i] not in node.next:
                return False
            node = node.next[word[i]]
        return node.end
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return
        node = self.root
        for i in xrange(len(prefix)):
            if prefix[i] not in node.next:
                return False
            node = node.next[prefix[i]]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)