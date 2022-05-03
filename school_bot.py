from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile

import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Выберите своё направление:\n"
                        "(команда /help для дополнительной помощи)", reply_markup=kb.directions)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Команды можно использовать через меню команд.\n"
                        "\n"
                        "Список команд:\n"
                        "/start - запуск бота\n"
                        "/help - помощь\n"
                        "/change - смена направления и учебников")


@dp.message_handler(commands=['change'])
async def process_start_command(message: types.Message):
    await message.reply("Выберите своё направление:", reply_markup=kb.directions)

#Направления

@dp.callback_query_handler(lambda c: c.data == 'direction1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали направление: Физмат')
    await bot.send_message(callback_query.from_user.id, 'Выберите предмет:', reply_markup=kb.subjects_phys)


@dp.callback_query_handler(lambda c: c.data == 'direction2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали направление: Биохим')
    await bot.send_message(callback_query.from_user.id, 'Выберите предмет:', reply_markup=kb.subjects_bio)


@dp.callback_query_handler(lambda c: c.data == 'direction3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали направление: Соцэк')
    await bot.send_message(callback_query.from_user.id, 'Выберите предмет:', reply_markup=kb.subjects_economy)


@dp.callback_query_handler(lambda c: c.data == 'direction4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали направление: Гум')
    await bot.send_message(callback_query.from_user.id, 'Выберите предмет:', reply_markup=kb.subjects_phys)


@dp.callback_query_handler(lambda c: c.data == 'direction5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали направление: Дизайн')
    await bot.send_message(callback_query.from_user.id, 'Выберите предмет:', reply_markup=kb.subjects_phys)

#Физмат

@dp.callback_query_handler(lambda c: c.data == 'geometry')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAPeYmWLwaPQEk6KAAFphlD0TQZ52LwXAAJKFwACR_YwS0cvNewH3uLEJAQ", reply_markup=kb.keyboard_gdz_geometry) #присылаем файл с кнопкой гдз


@dp.callback_query_handler(lambda c: c.data == 'algebra')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAPoYmWS3boIuJnE3sLU90q9TjQ1NlsAAnkXAAJH9jBLNPV6_9rlzlAkBA", reply_markup=kb.keyboard_gdz_algebra)


@dp.callback_query_handler(lambda c: c.data == 'it_1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAPzYmW8VqcSvI-yIfNGJl8MV-mh7poAAlMYAAJH9jBLe2ojdEARc-YkBA", reply_markup=kb.keyboard_gdz_it_1)


@dp.callback_query_handler(lambda c: c.data == 'it_2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAPzYmW8VqcSvI-yIfNGJl8MV-mh7poAAlMYAAJH9jBLe2ojdEARc-YkBA", reply_markup=kb.keyboard_gdz_it_2)


@dp.callback_query_handler(lambda c: c.data == 'rus_phys')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBB2Jlv1TAOp_LqYMFzXeo0N7ogkkXAAJXGAACR_YwS728E-maC4ADJAQ", reply_markup=kb.keyboard_gdz_russian_phys)


@dp.callback_query_handler(lambda c: c.data == 'rus_history_1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBD2JlwdMMYJVRI83VlwfP3hTIi-10AAJZGAACR_YwS2uK6D_e4pXNJAQ", reply_markup=kb.keyboard_gdz_russian_history)


@dp.callback_query_handler(lambda c: c.data == 'rus_history_2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBEmJlwtaVv-M8JqKEjtpcyzAoiAFkAAJfGAACR_YwSwU96UBqyhBtJAQ", reply_markup=kb.keyboard_gdz_russian_history)


@dp.callback_query_handler(lambda c: c.data == 'rus_history_3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBFWJlwzsiXicUaFvghXwZPohbkVBsAAJiGAACR_YwSzgsyDMn6ie_JAQ", reply_markup=kb.keyboard_gdz_russian_history)


@dp.callback_query_handler(lambda c: c.data == 'physics')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBxmJs8cKpXatU7cpXN4jQLeQdcJnMAAIHHAACC_FpS1PQNsFFQyuYJAQ", reply_markup=kb.keyboard_gdz_physics)


@dp.callback_query_handler(lambda c: c.data == 'english_sb')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIBzmJs9Vf_KJrsw1dMp7inuKWNMwJKAAJOHAACC_FpSy65BhU50Ww3JAQ", reply_markup=kb.keyboard_gdz_english_sb)


@dp.callback_query_handler(lambda c: c.data == 'english_wb')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIB0WJs9mN8hXYQjlM27H6fg9F4HeVaAAJWHAACC_FpS4ShrbnSxOk_JAQ", reply_markup=kb.keyboard_gdz_english_wb)


@dp.callback_query_handler(lambda c: c.data == 'english_tb')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAIB1GJs9rhq19nA_pTxr5tg1_LHWbXxAAJZHAACC_FpSzBxfWkAAY0wAAEkBA")


@dp.callback_query_handler(lambda c: c.data == 'english_mc')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICAmJtNJxXgC74E1IMkhlEm3NpQL3wAAJSHQACC_FpS0DTBlP_LyX9JAQ")


#БХ

@dp.callback_query_handler(lambda c: c.data == 'rus_bio')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICEGJtNvBby7A1PqYYxkfbc3b1WeeDAAJYHQACC_FpS89DwIh5G29pJAQ", reply_markup=kb.keyboard_gdz_russian_bio)


@dp.callback_query_handler(lambda c: c.data == 'biology')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICImJtQLHl55dynmC8QTShVSKaNvK4AAKTHQACC_FpS0PkJ8uQh62kJAQ", reply_markup=kb.keyboard_gdz_biology)


@dp.callback_query_handler(lambda c: c.data == 'chemistry')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICJWJtTH8ER3cv60XsSHX-sc5N6bToAALJHQACC_FpSxVIdk60dFULJAQ", reply_markup=kb.keyboard_gdz_chemistry)


@dp.callback_query_handler(lambda c: c.data == 'history_bio')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICoWJu1jfRFZXV11DN3WmNDZPie5crAAIXGgACvNxxS8ldj9JtCMytJAQ", reply_markup=kb.keyboard_gdz_history_bio)


#Соцэк
@dp.callback_query_handler(lambda c: c.data == 'social')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_document(callback_query.from_user.id, document="BQACAgIAAxkBAAICwmJu9KYWjLxUqUEFWE8hvQ4fsZZjAAJtGwACvNx5S-Hu9qGgh9FSJAQ", reply_markup=kb.keyboard_gdz_social)




@dp.message_handler(content_types=["document"])
async def sticker_file_id(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваш id документа") #берем id документа
    await message.answer(message.document.file_id)


@dp.message_handler(content_types=["sticker"])
async def sticker_file_id(message: types.Message):
    #await bot.send_message(message.from_user.id, "Ваш id sticker") #берем id стикера
    #await message.answer(message.sticker.file_id)
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAIBAAFiZb27vmIFT3AnQrjAI2yI1EFfOwACoxgAArvwwEuKzMnbs96XFyQE")


@dp.message_handler(content_types=["photo"])
async def sticker_file_id(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAIBYWJnG2CeKmmkrtjARuC4t5Vn_rbrAALhCwAC8fmxSxEOJDwPAcuzJAQ")


#@dp.message_handler(content_types=["text"])
#async def sticker_file_id(message: types.Message):
    #await bot.send_message(message.from_user.id, "Выберите направление или используйте команду /help через меню")


@dp.message_handler()
async def echo_message(msg: types.Message):
    try:
        command_parts = msg.text.split()
        classnum = command_parts[0]
        subject = command_parts[1]
        page = command_parts[2]
        if subject == "Алгебра" or subject == "алгебра":
            page = str(int(page) + 2)
            filename = 'Books/'+classnum+"/"+subject+"/img"+page+".jpg"
            text = "Страница " + str(int(page)-2) + " " + subject + " " + classnum + " класс"
        else:
            filename = 'Books/' + classnum + "/" + subject + "/img" + page + ".jpg"
            text = "Страница " + page + " " + subject + " " + classnum + " класс"
        media = types.MediaGroup()
        media.attach_photo(types.InputFile(filename), text)
        await bot.send_media_group(msg.from_user.id, media=media)
    except:
        await msg.reply("Неверный запрос!")


if __name__ == '__main__':
    print("Работаем работаем!")
    executor.start_polling(dp, skip_updates=False)