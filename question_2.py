# write a script that counts the frequency of words in a given text and stores the result in a dictionary.

def word_freq(text):
  frequencies={}
  for word in text:
    if word in frequencies:
      frequencies[word]+=1
    else:
      frequencies[word]=1 
  return frequencies    
def main() :     
  text=input("enter your text here: ")
  frequency=word_freq(text)
  for word,count in frequency.items():
    print(f"{word}:{count}")
if __name__=="__main__" :
  main()   

