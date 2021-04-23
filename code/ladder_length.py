from typing import List


class Solution:
    # 单词接龙
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        len_word = len(beginWord)

        forward = {beginWord}
        backward = {endWord}
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        result = 2
        visited = set()

        while forward:
            word_set = word_set - visited
            visited = set()

            if len(forward) > len(backward):
                forward, backward = backward, forward

            for word in forward:
                for i in range(len_word):
                    prefix, suffix = word[:i], word[i + 1:]
                    for alphabet in alphabets:
                        new_word = prefix + alphabet + suffix
                        if new_word in backward:
                            return result
                        if new_word in word_set:
                            visited.add(new_word)
            forward = visited
            result += 1
        return 0
