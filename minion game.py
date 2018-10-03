
def minion_game(string):
    string = string.lower()
    subStrings = get_all_substrings(string)
   
    Stuart = set()
    Kevin = set()
    kevinCount = 0
    stuartCount = 0
    for subString in subStrings:
        if subString[0] in "aeiou":
            Kevin.add(subString)
        else:
            Stuart.add(subString)
            
    
    for subString in Stuart:
        stuartCount += occurrences(string, subString)
        
    for subString in Kevin:
        kevinCount += occurrences(string, subString)
        
    return stuartCount, kevinCount

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

    
if __name__ == '__main__':
    while True:
        string  = input("Please enter a string: ")
        try:
            value = float(string)
            print("please enter a word or letters and not numbers")
            
        except ValueError:
            print("Setting up game \n...............Calculating\n")
            kevin, stuart = minion_game(string)
            if kevin > stuart:
                print("Kevin wins with " + str(kevin) + " points")
            else:
                print("Stuart wins with " + str(stuart) + " points")
            break
        
    
