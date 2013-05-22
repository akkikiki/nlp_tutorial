
import math

def reverse(word):
  return word[::-1]

def load_unigram_dic(model_file):
  dic = {}
  for line in open(model_file, "r"):
    word, prob = line[:-1].split("\t")
    dic[word] = float(prob)
  print dic
  return dic

## forward algorithm
# recognize each subseq as a node
# calculate for each word_end in the edge


unigram_dic = load_unigram_dic("../test/04-model.txt")
for line in open('../test/04-input.txt', 'r'):
  line = line[:-1]

# initialization
  best_edge = []
  best_score = []
  best_edge.append(None)
  best_score.append(0)

  N = len(line)
  n = 1000000 #len(unigram_dic)
  
  for word_end in xrange(1, N+1):
    #best_score[word_end] = 10 ** 10
    best_score.append(10 ** 10)
    best_edge.append(None)
    for word_begin in xrange(0, word_end):
      # all possible seperation words
      word = line[word_begin : word_end]
      if word in unigram_dic:
        prob = unigram_dic[word]
      elif len(word) == 1:
        prob = 1.0/n # length of an unigram dic
  # calculate the score
      else: continue
      temp_score = best_score[word_begin] - math.log(prob)
      #print "temp_score" ,str(temp_score)
  # update the optimal score and the optimal edge
      if temp_score < best_score[word_end]:
        best_score[word_end] = temp_score
        best_edge[word_end] = (word_begin, word_end)


## backward algorithm
# follow the optimal path by following the optimal path
  #print best_score
  #print best_edge

  words = []
  next_edge = best_edge[len(best_edge) - 1]
  while next_edge != None:
    word = line[next_edge[0] : next_edge[1]]
    words.append(word)
    next_edge = best_edge[next_edge[0]] # next word
  words = reverse(words)
  print " ".join(words)

