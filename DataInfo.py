#meta developer: @hikka_dmod
#подпишись на канал сучка 
from datetime import datetime, timedelta
from .. import loader

@loader.tds
class DateInfo(loader.Module):
    strings = {
        'name': 'DateInfo',
    }

    @loader.command()
    async def di(self, message):
        """- узнать подробную информацию о сегодня"""
        now = datetime.now()
        months = [
            "Январь", "Февраль", "Март", "Апрель",
            "Май", "Июнь", "Июль", "Август",
            "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ]
        seasons = [
            "Зима", "Зима", "Весна", "Весна",
            "Лето", "Лето", "Осень", "Осень",
            "Осень", "Зима", "Зима", "Зима"
        ]
        emojis = {
            "Зима": ("☃️", "❄️", "2⃣"),
            "Весна": ("🌹", "🌾", "3⃣"),
            "Лето": ("🍃", "🪴", "4⃣"),
            "Осень": ("🍂", "🍁", "1⃣")
        }
        holidays = {
            (1, 1): "❄️ Новый год",
            (2, 23): "🇷🇺 День защитника Отечества",
            (5, 9): "🫡 День Победы",
            (6, 1): "🥵 День защиты детей",
            (9, 1): "📚 День знаний",
            (2, 14): "🩷 День влюбленных"
        }

        current_year = now.year
        current_month_index = now.month 
        current_month = months[current_month_index - 1]
        current_season = seasons[now.month - 1]
        current_emojis = emojis[current_season]
        current_day = now.day
        current_weekday = now.strftime("%A")
        weekdays_ru = {
            "Monday": "Понедельник",
            "Tuesday": "Вторник",
            "Wednesday": "Среда",
            "Thursday": "Четверг",
            "Friday": "Пятница",
            "Saturday": "Суббота",
            "Sunday": "Воскресенье"
        }
        current_weekday_ru = weekdays_ru[current_weekday]
        weekend_days = ["Суббота", "Воскресенье"]
        day_emoji = "❕" if current_weekday_ru in weekend_days else "❗️"
        days_in_month = (datetime(current_year, current_month_index + 1, 1) - datetime(current_year, current_month_index, 1)).days if current_month_index < 12 else 31
        days_remaining = days_in_month - current_day
        next_month = months[current_month_index] if current_month_index < 12 else months[0]
        last_day_of_year = datetime(current_year, 12, 31)
        days_until_end_of_year = (last_day_of_year - now).days
        holiday = holidays.get((now.month, now.day), None)
        holiday_message = f"🎉<b>{holiday}!</b>" if holiday else "😭 <b>Сегодня праздник не отмечается</b>"

        response = (
            f"{current_emojis[0]} <b>Сейчас:</b> <code>{current_month} ({current_month_index})</code>\n"
            f"{current_emojis[1]} <b>Время года</b>: <code>{current_season}</code>\n\n"
            f"{day_emoji} <b>Число:</b> <code>{current_day}</code>\n"
            f"📅 <b>Год:</b> <code>{current_year}</code>\n"
            f"💬 <b>День недели:</b> <code>{current_weekday_ru}</code>\n"
            f"{holiday_message}\n\n"
            f"💤 <b>Всего дней в месяце:</b> <code>{days_in_month}</code>\n"
            f"✅ <b>До конца месяца осталось <code>{days_remaining}</code> дней</b>\n"
            f"📆 <b>До конца года осталось <code>{days_until_end_of_year}</code> дней</b>\n"
            f"➡️ <b>Следующий месяц</b>: <code>{next_month}</code>"
        )

        await message.respond(response)
        await message.delete()

    @loader.command()
    async def tsru(self, message):
        """- посмотреть сколько сейчас времени в различных городах России"""
        time_zones = {
            "✨ Москва": 3,
            "💪 Калининград": 2,
            "🥴 Самара": 4,
            "✈️ Екатеринбург": 5,
            "🌌 Омск": 6,
            "❤️ Красноярск": 7,
            "🌑 Иркутск": 8,
            "⚙️ Якутск": 9,
            "⚕️ Владивосток": 10,
            "〰️ Камчатка": 12,

        }

        utc_now = datetime.utcnow()
        response = "🕖 <b>Текущее время в различных городах России:</b>\n\n"
        
        for city, offset in time_zones.items():
            city_time = utc_now + timedelta(hours=offset)
            response += f"<b>{city}:</b> <code>{city_time.strftime('%H:%M:%S')}</code>\n"

        await message.respond(response)
        await message.delete()