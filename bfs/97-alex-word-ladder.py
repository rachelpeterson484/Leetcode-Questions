class Solution:
    wordList = set()

    def validSteps(self, beginWord: str, visited: Set[str]) -> List[str]:
        steps = []

        # this might seem inefficient, but it's faster than checking for oneEditDistance
        # against every other word for very large lengths of wordList, since wordLength <= 10
        # this is at most 10*24 operations
        for i in range(len(beginWord)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                newWord = beginWord[:i] + ch + beginWord[i+1:]
                if newWord in self.wordList and newWord not in visited:
                    steps.append(newWord)
                    visited.add(newWord)

        return steps

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordList = set(wordList)
        queue = [{'word': beginWord, 'dist': 1}]
        visited = {beginWord}

        while len(queue) != 0:
            curr = queue.pop(0)

            options = self.validSteps(curr['word'], visited)
            for option in options:
                queue.append({'word': option, 'dist': curr['dist'] + 1})

            if curr['word'] == endWord:
                return curr['dist']

        return 0
