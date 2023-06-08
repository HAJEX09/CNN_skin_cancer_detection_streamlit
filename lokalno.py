import numpy as np
from PIL import Image
from keras.models import load_model

# Загрузка модели
model = load_model('mymodel-2.h5')

# Загрузка и предобработка изображения
image_path = 'screen2.jpg'
image = Image.open(image_path)
image = image.resize((128, 128))  # Подгоняем размер изображения под требования модели
image = np.expand_dims(image, axis=0)  # Добавляем размерность пакета (batch dimension)

# Выполняем предсказание
predictions = model.predict(image)
predictions
if predictions[[0]] < 0.5:
    print('Злокачественная! Обратитесь к доктору!')
else:
    print('Доброкачественная)')

# Выводим результат
#print(f"Классификация изображения: {class_label}")
