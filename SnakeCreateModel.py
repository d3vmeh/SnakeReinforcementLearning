import pandas as pd 
import keras
from keras.models import load_model
import sklearn.model_selection  
import numpy as np
df = pd.read_csv(r"C:\Users\Dev Mehra\Documents\Python Projects\Pythonl\reinforcementlearning\SnakeRL\snakedata.csv")

input_data_original = np.array(df.drop(["currentdirection"],1))
output_data_original = np.array(df['currentdirection'])
input_data = []
output_data = []

for i in range(len(input_data_original)):
    if input_data_original[i][4] == 1:
        input_data.append(input_data_original[i][:5])


        if(output_data_original[i] == "left"):
            output_data.append(0)
        
        elif(output_data_original[i] == "right"):
            output_data.append(1)


        elif (output_data_original[i] == "up"):
            output_data.append(2)
        
        elif (output_data_original[i] == "down"):
            output_data.append(3)
        
        else:
            print("hello",output_data_original[i])
            

input_data = np.array(input_data)
output_data = np.array(output_data)

print(len(input_data),len(output_data))
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(input_data,output_data,test_size=0.2)

y_train_list = []
y_test_list = []

# for i in y_train:
   
#     if i == 'left':
#         y_train_list.append(0)
#     elif i == 'right':
#         y_train_list.append(1)
#     elif i == 'up':
#         y_train_list.append(2)
#     elif i == 'down':
#         y_train_list.append(3)
   
# for i in y_test:
   
#     if i == 'left':
#         y_test_list.append(0)
#     elif i == 'right':
#         y_test_list.append(1)
#     elif i == 'up':
#         y_test_list.append(2)
#     elif i == 'down':
#         y_test_list.append(3)

print(y_test_list)


print(x_train.shape,x_test.shape)

model = keras.Sequential([
keras.layers.Dense(512,activation='relu'),
keras.layers.Dense(4,activation='softmax')])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# #200 epochs
model.fit(x_train,y_train,epochs=400)
# #Calculating the accuracy for test data
test_loss, test_acc = model.evaluate(x_test,y_test)
print("Accuracy:",str(test_acc*100)+"%")
print("Loss:",test_loss)

model.save("snakemodel.h5")
