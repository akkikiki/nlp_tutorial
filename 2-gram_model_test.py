import math


if __name__ == "__main__":
  file_model = "../model/2-gram_model.model"
  file_test = "../test/02-train-input.txt"
  
  ngram_probs = {} # this prob is already conditional
  
  for line in open(file_model, "r"):
    words_prob = line[:-1].split()
    prob = float(words_prob.pop())
    
    word = " ".join(words_prob)
    ngram_probs[word] = prob
  
  H = 0
  W = 0
  for line in open(file_test, "r"):
    sentence = line[:-1].split()
    sentence.append("_EOS_")
    sentence.insert(0, "_BOS_")
    for i in range(len(sentence) - 1):
      target = " ".join(sentence[i:i+2])
      if target in ngram_probs:
        H += math.log(ngram_probs[target], 2)
      else: H += 0
      W += 1
    print "entropy = " + str((1.0 * H)/W)
