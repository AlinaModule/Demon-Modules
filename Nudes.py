#meta developer: @hikka_dmod

from .. import loader, utils
from asyncio import sleep
import random 

@loader.tds
class Nudes(loader.Module):
    """Рандомные нюдсы рандомных моделей 

‼️<b>СТРОГО 18+, СОЗДАТЕЛЬ МОДУЛЯ НЕ НЕСЁТ ОТВЕСТВЕННОСТИ ЕСЛИ С ВАМИ ЧТО-ТО СЛУЧИТСЯ ИЗ-ЗА ЭТОГО МОДУЛЯ</b> ‼️"""
    strings = {'name': 'Nudes 18+'}
    
    @loader.command(alias='ника')
    async def nika(self, message):
        """- показать модель Нику (не интимку)"""
        NikaPhoto = [
            "https://0x0.st/s/2rSFOPSP0fAByte8HZKATw/XYvH.jpg",
        ]
        
        Nika = " "
         
        await self.client.send_file(message.peer_id, random.choice(NikaPhoto))
        await message.delete()
    
    @loader.command(alias='иника')
    async def inika(self, message):
        """- фото нюдс Ники (всего 64)"""
        stories = []
        async for msg in message.client.iter_messages('@xxxNIKAxxxINTIMxxx', limit=64):
            if msg.document and msg.document.mime_type in ['image/jpeg', 'image/jpg']:
                stories.append(msg)

        if stories:
            random_story = random.choice(stories)
            await self.client.send_file(message.peer_id, random_story.document)
        else:
            await utils.answer(message, "🚫<b>Ошибка\nПо вашему запросу ничего не найденo</b>")
            await message.delete()
            
    @loader.command(alias='виника')
    async def vinika(self, message):
        """- видео нюдс Ники (всего 27)"""
        media = []
        async for msg in message.client.iter_messages('@videonudesnika', limit=27):
            if msg.video:
                media.append(msg.video)
            elif msg.photo:
                media.append(msg.photo)

        if media:
            random_media = random.choice(media)
            await self.client.send_file(message.peer_id, random_media)
        else:
            await utils.answer(message, "🚫<b>Ошибка\nПо вашему запросу ничего не найдено</b>")
            await message.delete()
