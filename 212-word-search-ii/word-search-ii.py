class Node:
    def __init__(self):
        self.children={}
        self.word = None
        self.word_end=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nr = len(board)
        nc= len(board[0])
        res=[]
        root = Node()
        def insert(word):
            current_node= root
            for ch in word:
                current_node = current_node.children.setdefault(ch,Node())
            current_node.word=word
        for word in words:
            insert(word)
        def dfs(i,j,node):
            if i <0 or i >=nr or j<0 or j>=nc:
                return 
            if board[i][j] =='*':
                return 
            ch=board[i][j]
            if ch not in node.children:
                return 
            child = node.children[ch]
            if child.word:
                res.append(child.word)
                child.word=None
            board[i][j] = '*'
            dfs(i,j+1,child)
            dfs(i,j-1,child)
            dfs(i-1,j,child)
            dfs(i+1,j,child)
            board[i][j] = ch
        for row in range(nr):
            for col in range(nc):
                dfs(row,col,root)
        return res



        

        