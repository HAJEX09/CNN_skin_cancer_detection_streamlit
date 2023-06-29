# import io
# import streamlit as st
# from PIL import Image
# from keras.models import load_model
# from tensorflow.keras.applications.efficientnet import preprocess_input
# from tensorflow.keras.applications.efficientnet import decode_predictions
# from tensorflow.keras.preprocessing import image
# import numpy as np

# # Загрузка модели
# model = load_model('mymodel.h5')

# def preprocess_image(img):
#     img = img.resize((128, 128))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     return x


# def load_image():
#     uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
#     if uploaded_file is not None:
#         image_data = uploaded_file.getvalue()
#         st.image(image_data)
#         return Image.open(io.BytesIO(image_data))
#     else:
#         return None


# def print_predictions(preds):
#     classes = decode_predictions(preds, top=2)[0]
#     for cl in classes:
#         st.write(cl[1], cl[2])



# def print_predictions(preds):
#     if preds[[0]] > 0.5:
#         st.write('Злокачественная! Пожалуйста, обратитесь к доктору!')
      
#     else:
#         st.write('Доброкачественная)')



# st.title('Нейросеть для обнаружения рака кожи ')

# disclaimer = st.checkbox('Нажми на меня')
# if disclaimer:
#     st.markdown('<span style="font-size: 20px;">    </span>', unsafe_allow_html=True)

#     st.header("Уважаемые пользователи, внимание!")
#     st.markdown('<span style="font-size: 20px;">Хотелось бы обратить ваше внимание на несколько важных аспектов, связанных с данным проектом. Пожалуйста, ознакомьтесь с этим дисклеймером, прежде чем использовать программу.</span>', unsafe_allow_html=True)
#     #st.markdown('<span style="font-size: 20px; margin-bottom: 10px;">Рак кожи - распространенное заболевание, которым страдает большое количество людей.</span>', unsafe_allow_html=True)
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Рак кожи - распространенное заболевание, которым страдает большое количество людей.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Выживаемость пациентов, у которых меланома выявлена на ранней стадии, составляет около 98 процентов.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Выживаемость пациентов, у которых болезнь достигает лимфатических узлов, снижается до 62 процентов.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Выживаемость пациентов, у которых болезнь достигает лимфатических узлов, снижается до 62 процентов.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Выживаемость пациентов, у которых болезнь метастазирует в отдаленные органы, падает до 18 процентов.</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.markdown(
#     """
#     <div style="padding-top: 1px; padding-bottom: 1px;">
#         <span style="font-size: 20px;">Раннее выявление имеет решающее значение!!!</span>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#     st.write("")
#     #st.markdown('<span style="font-size: 20px;">Выживаемость пациентов, у которых меланома выявлена на ранней стадии, составляет около 98 процентов.</span>', unsafe_allow_html=True)
#     #st.markdown('<span style="font-size: 20px;">Выживаемость пациентов, у которых болезнь достигает лимфатических узлов, снижается до 62 процентов.</span>', unsafe_allow_html=True)
#     #st.markdown('<span style="font-size: 20px;">Выживаемость пациентов, у которых болезнь метастазирует в отдаленные органы, падает до 18 процентов.</span>', unsafe_allow_html=True)
#     #    #st.markdown('<span style="font-size: 20px;">Раннее выявление имеет решающее значение!!!")

#     st.markdown('<span style="font-size: 20px;">Это веб-приложение предназначено исключительно в помощь людям. Оно создано с целью помочь пользователям получить предварительную оценку состояния кожи на основе изображения. Программа является инструментом, который может помочь вам в раннем обнаружении потенциальных проблем.</span>', unsafe_allow_html=True)

#     st.markdown('<span style="font-size: 20px;">Важно понимать, что результаты, полученные с помощью программы, не могут заменить профессиональную медицинскую консультацию. Рекомендуется обратиться к квалифицированному врачу для окончательной оценки и диагностики.</span>', unsafe_allow_html=True)

#     st.markdown('<span style="font-size: 20px;">Точность определения заболеваний кожи в большой степени зависит от качества предоставленного изображения. Изображения должны быть четкими, высокого разрешения, хорошо освещенными и предоставлять детальный вид места на коже, которое вас беспокоит. Помните, что низкое качество изображения может существенно ухудшить точность анализа.</span>', unsafe_allow_html=True)

#     st.markdown('<span style="font-size: 20px;">Предоставляемая информация и услуги основываются на технологии машинного обучения и не могут гарантировать 100% точности. Я не несу ответственности за любые возможные ошибки и неточности.</span>', unsafe_allow_html=True)

#     st.markdown('<span style="font-size: 20px;">Пользователи этого приложения несут полную ответственность за свои действия и решения, связанные с их здоровьем. При обнаружении любых изменений на коже или сомнениях, всегда обращайтесь к квалифицированному медицинскому специалисту.</span>', unsafe_allow_html=True)

#     st.markdown('<span style="font-size: 20px;">Пожалуйста, используйте эту систему ответственно, оценивайте ее возможности и ограничения адекватно. Заботьтесь о своем здоровье и не забывайте про регулярные медицинские осмотры.</span>', unsafe_allow_html=True)



#     # Показываем форму согласия
#     agreed = st.checkbox("Я согласен с условиями использования")

#     # Проверяем, согласился ли пользователь
#     if agreed:
#         img = load_image()
#         result = st.button('Распознать изображение')
#         if result:
#             x = preprocess_image(img)
#             preds = model.predict(x)
#             res = float(preds)
#             st.write('**Результаты распознавания:**')
#             print_predictions(preds)
#     else:
#         st.warning("Для продолжения работы необходимо согласиться с условиями использования.")






