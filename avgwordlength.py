#Here is a program that gives you the average word length of a sentence

def main():
    sentence=("Enter a sentence: ")
    words=sentence.split()
    totalwordlength=0
    for word in words:
        totalwordlength+=len(word)
    print("Average word length is " + str(totalwordlength*1./len(words)))

main() 
