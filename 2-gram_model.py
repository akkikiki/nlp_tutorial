


if __name__ == "__main__":
  file_test = "../test/02-train-input.txt"
  file_train = "../data/wiki-en-train.word"

  counts_ngram = {}
  context_counts = {} # for 3-gram, it consists of 2 words
  
  for line in open(file_train, "r"):
    sentence = line[:-1].split()
    sentence.append("_EOS_")
    sentence.insert(0, "_BOS_")
    for i in range(len(sentence) - 1):
      # calculating for bigram
      word = " ".join(sentence[i:i+2])
      if word in counts_ngram:
        counts_ngram[word] += 1
      else:
        counts_ngram[word] = 1
      
      context = sentence[i+1]
      if context in context_counts:
        context_counts[context] += 1
      else:
        context_counts[context] = 1
  #print context_counts
  for ngram in counts_ngram:
    words = ngram.split(" ")
    target = words.pop()
    context = "".join(words)
    #print context
    if ngram in counts_ngram:
      numerator = counts_ngram[ngram]
    else:
      numerator = 0
    if context in context_counts:
      dominator = context_counts[context]
    else:
      dominator = 0
    if dominator != 0:
      prob = (1.0 * numerator)/dominator
    else:
      prob = 0
    print ngram, prob
