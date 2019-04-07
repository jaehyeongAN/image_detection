'''
Created on 2017. 8. 7.

@author: jaehyeong
'''
from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Conv2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import os

# 카테고리 지정하기
categories = ["Car front crash","Car side crash","Rear and crash","Car broken windshield","Car scratch","Flat tire","Overturned vehicle"]
nb_classes = len(categories)
# 이미지 크기 지정하기
image_w = 64
image_h = 64
# 데이터 열기 
X_train, X_test, y_train, y_test = np.load("./image/7obj.npy")
# 데이터 정규화하기(0~1사이로)
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

# 모델 구조 정의 
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=X_train.shape[1:], padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 전결합층
model.add(Flatten())    # 벡터형태로 reshape
model.add(Dense(512))   # 출력
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))
# 모델 구축하기
model.compile(loss='binary_crossentropy',   # 최적화 함수 지정
    optimizer='rmsprop',
    metrics=['accuracy'])
# 모델 확인
#print(model.summary())

# 모델 훈련하기
#model.fit(X_train, y_train, batch_size=32, nb_epoch=20)
# 학습 완료된 모델 저장
hdf5_file = "./image/7obj-model.hdf5"
if os.path.exists(hdf5_file):
    # 기존에 학습된 모델 불러들이기
    model.load_weights(hdf5_file)
else:
    # 학습한 모델이 없으면 파일로 저장
    model.fit(X_train, y_train, batch_size=32, nb_epoch=10)
    model.save_weights(hdf5_file)
# 모델 평가하기 
score = model.evaluate(X_test, y_test)
print('loss=', score[0])        # loss
print('accuracy=', score[1])    # acc

# 예측 값 보기
y_pred = model.predict(X_test)
print(y_pred)
# 예측 클래스
a =[np.argmax(value) for value in  y_pred]
print(a)



print('-------------------------------------')
print('-------------------------------------')
#######################################
# 새로운 값 적용해보기
from PIL import Image

# 적용해볼 이미지 
test_image = './image/brokenwindow.jpg'
# 이미지 resize
img = Image.open(test_image)
img = img.convert("RGB")
img = img.resize((64,64))
data = np.asarray(img)
X = np.array(data)
X = X.astype("float") / 256
X = X.reshape(-1, 64, 64,3)
# 예측
pred = model.predict(X)  
result = [np.argmax(value) for value in pred]   # 예측 값중 가장 높은 클래스 반환
print('New data category : ',categories[result[0]])
#######################################
