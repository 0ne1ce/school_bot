from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

direction_1 = InlineKeyboardButton('Физмат', callback_data='direction1')
direction_2 = InlineKeyboardButton('Биохим', callback_data='direction2')
direction_3 = InlineKeyboardButton('Соцэк', callback_data='direction3')
direction_4 = InlineKeyboardButton('Гум', callback_data='direction4')
direction_5 = InlineKeyboardButton('Дизайн', callback_data='direction5')
directions = InlineKeyboardMarkup(row_width=1).add(direction_1, direction_2, direction_3, direction_4, direction_5)

#Физмат
geometry = InlineKeyboardButton("Геометрия", callback_data='geometry')
algebra = InlineKeyboardButton("Алгебра", callback_data='algebra')
matan = InlineKeyboardButton("Мат Анализ", callback_data='matan')
it_1 = InlineKeyboardButton("Информатика ч.1", callback_data="it_1")
it_2 = InlineKeyboardButton("Информатика ч.2", callback_data='it_2')
physics = InlineKeyboardButton("Физика", callback_data='physics')
russian_phys = InlineKeyboardButton("Русский язык", callback_data='rus_phys')
russian_history_1 = InlineKeyboardButton("История России ч.1", callback_data='rus_history_1')
russian_history_2 = InlineKeyboardButton("История России ч.2", callback_data='rus_history_2')
russian_history_3 = InlineKeyboardButton("История России ч.3", callback_data='rus_history_3')
english_sb = InlineKeyboardButton("Английский язык (учебник)", callback_data='english_sb')
english_wb = InlineKeyboardButton("Английский язык (тетрадь)", callback_data='english_wb')
english_mc = InlineKeyboardButton("Английский язык (Macmillan)", callback_data='english_mc')

subjects_phys = InlineKeyboardMarkup(row_width=1).add(algebra, english_sb, english_wb, english_mc, geometry, it_1, it_2, russian_history_1, russian_history_2, russian_history_3, russian_phys, physics, matan)


button_gdz_geometry = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/geometria/atanasyan-10-11/")
button_gdz_algebra = InlineKeyboardButton("Списать", url="https://gdz.ru/class-11/algebra/kolmogorov/")
button_gdz_matan = InlineKeyboardButton("Списать", url="https://youtube.com/shorts/1brRuAovbSo?feature=share")
button_gdz_it_1 = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/informatika/reshebnik-polyakov-k-yu-eremin/40-item/")
button_gdz_it_2 = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/informatika/reshebnik-polyakov-k-yu-eremin/40-item/")
button_gdz_russian_phys = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/russkii_yazik/grekov-10-11/")
button_gdz_russian_history = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/istoriya/gorinov/")
button_gdz_physics = InlineKeyboardButton("Списать", url="https://reshak.ru/reshebniki/fizika/10/myakishev/index.html")
button_gdz_english_sb = InlineKeyboardButton("Списать", callback_data='english_tb')
button_gdz_english_wb = InlineKeyboardButton("Списать", url="http://onlinegdz.3dn.ru/focus/fwb4/")


keyboard_gdz_geometry = InlineKeyboardMarkup().add(button_gdz_geometry)
keyboard_gdz_algebra = InlineKeyboardMarkup().add(button_gdz_algebra)
keyboard_gdz_matan = InlineKeyboardMarkup().add(button_gdz_matan)
keyboard_gdz_it_2 = InlineKeyboardMarkup().add(button_gdz_it_1)
keyboard_gdz_it_1 = InlineKeyboardMarkup().add(button_gdz_it_2)
keyboard_gdz_russian_phys = InlineKeyboardMarkup().add(button_gdz_russian_phys)
keyboard_gdz_russian_history = InlineKeyboardMarkup().add(button_gdz_russian_history)
keyboard_gdz_physics = InlineKeyboardMarkup().add(button_gdz_physics)
keyboard_gdz_english_sb = InlineKeyboardMarkup().add(button_gdz_english_sb)
keyboard_gdz_english_wb = InlineKeyboardMarkup().add(button_gdz_english_wb)


#Биохим
russian_bio = InlineKeyboardButton("Русский язык", callback_data='rus_bio')
biology = InlineKeyboardButton("Биология", callback_data='biology')
chemistry = InlineKeyboardButton("Химия", callback_data='chemistry')
history_bio = InlineKeyboardButton("История", callback_data='history_bio')
subjects_bio = InlineKeyboardMarkup(row_width=1).add(algebra, english_sb, english_wb, english_mc, biology, geometry, history_bio, russian_bio, chemistry)


button_gdz_russian_bio = InlineKeyboardButton("Списать", url="https://spishi.me/10-klass-onlajn/russkij-yazik-10/gdz-reshebnik-po-russkomu-yazyku-10-11-klass-rozental/")
button_gdz_biology = InlineKeyboardButton("Списать", url="https://resheba.me/gdz/biologija/10-klass/teremov-uglublennyj-uroven")
button_gdz_chemistry = InlineKeyboardButton("Списать", url="https://resheba.me/gdz/biologija/10-klass/teremov-uglublennyj-uroven")
button_history_bio = InlineKeyboardButton("Списать", url="https://gdz.ru/class-10/istoriya/rabochaya-tetrad-soroko-cupa/")

keyboard_gdz_russian_bio = InlineKeyboardMarkup().add(button_gdz_russian_bio)
keyboard_gdz_biology = InlineKeyboardMarkup().add(button_gdz_biology)
keyboard_gdz_chemistry = InlineKeyboardMarkup().add(button_gdz_chemistry)
keyboard_gdz_history_bio = InlineKeyboardMarkup().add(button_history_bio)


#Соцэк
social = InlineKeyboardButton("Обществознание", callback_data='social')

subjects_economy = InlineKeyboardMarkup(row_width=1).add(algebra, english_sb, english_wb, english_mc, geometry, it_1, it_2, social, russian_history_1, russian_history_2, russian_history_3, russian_phys, physics)


button_gdz_social = InlineKeyboardButton("Списать", url="https://гдз-класс.рф/load/10_klass/obshhestvoznanie/gdz_po_obshhestvoznaniju_10_klass_uchebnik_grinberg_koroleva/233-1-0-13379")

keyboard_gdz_social = InlineKeyboardMarkup().add(button_gdz_social)




geometry_id = "BQACAgIAAxkBAAPeYmWLwaPQEk6KAAFphlD0TQZ52LwXAAJKFwACR_YwS0cvNewH3uLEJAQ"
algebra_id = "BQACAgIAAxkBAAPoYmWS3boIuJnE3sLU90q9TjQ1NlsAAnkXAAJH9jBLNPV6_9rlzlAkBA"
