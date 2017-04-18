from trie import Trie
from damerau import DamerauAutomaton

def extract(Automaton, state, node):
    #recursion
    if not Automaton.can_match(state):
        return []
    ans = []
    if Automaton.is_match(state) and node.is_end:
        ans.append('')
    for c in node.children:
        word_list = extract(Automaton, Automaton.step(state, c), node.children[c])
        b = [c + w for w in word_list]
        ans = ans + b
    return ans

def extract_words(node, string, n):
    Automaton = DamerauAutomaton(string, n)
    state = Automaton.start()
    return extract(Automaton, state, node)


T = Trie()
n = int(input())
dictionary = input().split()
for word in dictionary:
    T.add_word(word)

n = int(input())
tests = input().split()
for test in tests:
    ans = extract_words(T, test, 1)
    for a in ans:
        print(a, end=' ')

    print('')



