from Solution import WordDictionary

def main():

    # Output: [null,null,null,null,false,true,true,true]
    testCommands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    testInput = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

    obj = None
    output = []

    for cmd, arg in zip(testCommands, testInput):
        if cmd == "WordDictionary":
            obj = WordDictionary()
            output.append(None)
        elif cmd == "addWord":
            obj.addWord(arg[0])
            output.append(None)
        elif cmd == "search":
            output.append(obj.search(arg[0]))

    print(output)

if __name__ == "__main__":
    main()