import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER

TOKEN = "8549333159:AAEoGLv-mMtQ8sHS-r_0m_X7MIJDz3uivdQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.chat_member(ChatMemberUpdatedFilter(
    member_status_changed=(IS_NOT_MEMBER >> IS_MEMBER)
))
async def welcome(event: ChatMemberUpdated):
    user = event.new_chat_member.user

    text = (
        f"👋 <b>Добро пожаловать в дурку</b>, {user.mention_html()} 😈\n\n"
        f"📜 Теперь вы можете ознакомиться с "
        f"<a href='https://telegra.ph/Pravila-KL-02-09'>правилами</a>."
    )

    await bot.send_message(
        chat_id=event.chat.id,
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
