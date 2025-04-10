class Node:
    def __init__(self):
        self.children={}
        self.word_end=False
class WordDictionary:

    def __init__(self):
        self.root=Node()

        

    def addWord(self, word: str) -> None:
        current_node=self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch]=Node()
            current_node = current_node.children[ch]
        current_node.word_end = True

        

    def search(self, word: str) -> bool:
        def dfs(idx,root):
            current_node = root
            for i in range(idx,len(word)):
                ch=word[i]
                if ch == '.':
                    for child in current_node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if ch not in current_node.children:
                        return False
                    current_node = current_node.children[ch]
            return current_node.word_end
        return dfs(0,self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)