from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        indices = []
        s_slice = s[:len(p)]
        counter = Counter(s_slice)
        x = range(len(s) - len(p) + 1)
        for letter in range(len(s) - len(p) + 1):
            if self.test_for_anagrams(counter, p):
                indices.append(letter)
            if letter + len(p) < len(s):

                previous_letter = s[letter]
                next_letter = s[letter + len(p)]

                counter[previous_letter] -= 1
                if counter[previous_letter] == 0:
                    del counter[previous_letter]

                counter[next_letter] += 1

        return indices

    def test_for_anagrams(self, counter, str_2):
        return counter == Counter(str_2.lower())
if __name__ == "__main__":
    x = "cbaebabacd"
    y = "abc"
#s → anagram_source
#p → string_for_searching
    Solution().findAnagrams(x, y)