from Solution import Trie

def main():
    
    # Instantiate the Trie object
    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple"))  # Correct output: True
    print(trie.search("app"))  # Correct output: False
    print(trie.startsWith("app"))  # Correct output: True
    trie.insert("app")
    print(trie.search("app"))  # Correct output: True

if __name__ == "__main__":
    main()