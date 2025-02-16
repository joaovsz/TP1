class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _autocomplete_helper(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._autocomplete_helper(child, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._autocomplete_helper(node, prefix, results)
        return results

def main():
    trie = Trie()
    words = ["casa", "carro", "cadeira", "cachorro", "caminhão"]
    for word in words:
        trie.insert(word)

    print("Palavras disponíveis:", words)
    while True:
        prefix = input("Digite um prefixo para autocompletar (ou 'sair' para encerrar): ")
        if prefix.lower() == 'sair':
            break
        suggestions = trie.autocomplete(prefix)
        if suggestions:
            print("Sugestões:", suggestions)
        else:
            print("Nenhuma sugestão encontrada.")

if __name__ == "__main__":
    main()
