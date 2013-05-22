

if __name__ == "__main__":
  train_file = "../data/wiki-en-train.word"
  dic = {}
  counts = 0
  
  
  
  for line in train_file:
    H = 0
    sentence = line[:-1].split()
    sentence.append("</s>")
    for w in sentence:
      if w in dic:
        dic[w] += 1
      else:
        dic[w] = 1
      counts += 1
        
  

  
