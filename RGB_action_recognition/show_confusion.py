from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

from data_gen_bkb import DataGeneratorBKB
from model_ML import create_model_pretrain
from data_helper import readfile_to_dict

dim = (224,224)
n_sequence = 8
n_channels = 3
n_output = 4

path_dataset = 'F:\\Master Project\\Dataset\\BasketBall-RGB\\'

params = {'dim': dim,
          'batch_size': 2,
          'n_sequence': n_sequence,
          'n_channels': n_channels,
          'path_dataset': path_dataset,
          'option': 'RGBdiff',
          'shuffle': False}

test_txt = "dataset_list/testlistBKB.txt"
test_d = readfile_to_dict(test_txt)
num_mul = 60
key_list = list(test_d.keys()) * num_mul  # IDs

# validation_generator = DataGeneratorBKB(partition['validation'] , labels, **params, type_gen='test') # for evalutate_generator
predict_generator = DataGeneratorBKB(key_list , test_d, **params, type_gen='predict')


weights_path = 'MobileNetV2-BKB-Add3StandSideView-04-0.97-0.94.hdf5' 
model = create_model_pretrain(dim, n_sequence, n_channels, n_output, 'MobileNetV2')
model.load_weights(weights_path)


# Example for evaluate generator
# If you want to use, just uncomment it
# loss, acc = model.evaluate_generator(validation_generator, verbose=0)
# print(loss,acc)


# #### Confusion Matr
y_pred_prob = model.predict_generator(predict_generator, workers=0)
test_y = np.array(list(test_d.values()) * num_mul)
print("-----------")
print(y_pred_prob.shape)
print(len(test_y))

y_pred = np.argmax(y_pred_prob, axis=1)
normalize = True

all_y = len(test_y)
sum = all_y
for i in range(len(y_pred)):
    if test_y[i] != y_pred[i]:
        sum -= 1
        print(key_list[i],' actual:',test_y[i],'predict:',y_pred[i])

cm = confusion_matrix(test_y, y_pred)
if normalize:
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    print("Normalized confusion matrix")
else:
    print('Confusion matrix, without normalization')


accuracy = sum / all_y
print("accuracy:",accuracy)

classes = [*range(1,19)] # [1,2,3,...,18]

df_cm = pd.DataFrame(cm, columns=classes, index=classes)
df_cm.index.name = 'Actual'
df_cm.columns.name = 'Predicted'
fig, ax = plt.subplots(figsize=(5,5))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, cmap="Blues", annot=True,fmt=".2f", annot_kws={"size": 16})# font size
ax.set_ylim(5, 0)
plt.show()