import csv
import re
import tensorflow as tf
import matplotlib.pyplot as plt
'''
#read data
with open('train.csv',  encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)

    #parse input data
    for line in  csv_reader:
        #print(line[1], line[2], line[4])

        #print(re.match('<.*\/>', line[1]))

        #Obtained edited headline
        line[1] = re.sub('<.*\/>',
                  line[2],
                  line[1])

        print(line[1], line[4])
'''

set = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = set.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer= 'adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)
'''
plt.imshow(x_train[0])
plt.show()
print(x_train[0])
'''