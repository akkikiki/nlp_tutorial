
# how many time does it appear

def update_weights(weight_dic, phi, y):
  for name in phi:
    weight_dic[name] += phi[name]*y
    #print name, weight_dic[name]
    # if y = -1, smaller
    # if y = 1, bigger

def learn(input_file):
  weight_dic = {}
  #assume that the first element is the y
  for line in open(input_file, "r"):
    #print line
    temp = line[:-1].split('\t')
    #print line
    y = int(temp.pop(0))
    #print y
    for x in temp[0].split():
      if x not in weight_dic:
        weight_dic[x] = 0 # initializing weights
    #print weight_dic
    phi = create_features(temp[0])
    #print phi
    y_pre = predict_one(weight_dic, phi)
    #print y, y_pre
    if y != y_pre:
      update_weights(weight_dic, phi, y)
      #if 'The' in weight_dic: weight_dic['The'] = -1
  return weight_dic

def create_features(sentence):
  phi = {}
  words = sentence.split()
  
  for word in words:
    #phi["UNI: " + word] += 1
    if word in phi: phi[word] += 1
    else: phi[word] = 1
      
  return phi

def predict_one(weight_dic, phi):
  score = 0
  for name in phi:
    if name in weight_dic:
      score += weight_dic[name] * phi[name]
      #print score
  if score >= 0: return 1
  else: return -1

def predict_all(model_file, input_file):
  #train_file = open(model_file, "r")
  weight_dic = learn(model_file) 
  #for line in file_input:
  #  word, weight = line[:-1].split() 
  #  weight_dic[word] = int(weight)

  
  for line in open(input_file, "r"):
    phi = create_features(line[:-1])
    y = predict_one(weight_dic, phi)
    print str(y) + "\t" + line[:-1]
    

if __name__ == "__main__":
  train_file = open("../test/03-train-input.txt", "r")
  weight_dic = learn(train_file)
  #print weight_dic
  
  #for key, value in sorted(weight_dic.items(), key=lambda x:x[0], reverse=False):
  #  print key, value
