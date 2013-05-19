import train_perceptron as tp

if __name__ == "__main__":
  train_file = "../data/titles-en-train.labeled"
  predict_file = "../data/titles-en-test.word"
  weight_dic = tp.learn(train_file)
  for key in weight_dic:
    print key, weight_dic[key]
  tp.predict_all(train_file, predict_file)
  

