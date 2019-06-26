class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabetmorze = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.",
                         'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
                         'p': ".--.",
                         'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
                         'x': "-..-", 'y': "-.--", 'z': "--.."}
        transf, result = '', []
        for word in words:
            for i in word:
                transf += alphabetmorze.get(i)

            result.append(transf)
            transf = ''
        return (len(set(result)))