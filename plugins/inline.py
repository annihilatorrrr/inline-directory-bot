#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import asyncio
from pyrogram import Client
from presets import Presets
from library.sql import query_msg
from pyrogram.enums import ParseMode
from library.buttons import replay_markup_close
from library.support import chat_member, user_name
from library.support import get_thumbnail, get_reply_markup, query_chat_participant
from pyrogram.types import InputTextMessageContent, InlineQuery, InlineQueryResultPhoto

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

# -------------------------- Answering Inline query --------------------------------- #
@Client.on_inline_query()
async def answer(bot, query: InlineQuery):
    id = query.from_user.id
    results = []
    await query_chat_participant(id, bot)
    if id not in chat_member:
        return
    string = query.query.strip()
    search = await query_msg(string)
    for file in search:
        try:
            results.append(
                InlineQueryResultPhoto(
                    photo_url=await get_thumbnail(file),
                    thumb_url=await get_thumbnail(file),
                    photo_width=300,
                    photo_height=300,
                    input_message_content=InputTextMessageContent(
                        Presets.RESULTS.format(file.name,
                                               file.dept.upper(),
                                               file.mobile,
                                               file.extension,
                                               file.mail,
                                               file.emp,
                                               )
                    ),
                    description=Presets.DESCRIPTION_TXT.format(file.name, file.dept.upper(), file.mobile),
                    reply_markup=get_reply_markup(user_name[id])
                )
            )
        except Exception:
            pass
    #
    if results:
        try:
            switch_pm_text = Presets.RESULT_TXT
            await query.answer(
                results=results,
                is_personal=True,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
        if (len(query.query) >= 3) and Config.DEV_ID is not None:
            user = await bot.get_users(id)
            try:
                await bot.send_message(
                    chat_id=Config.DEV_ID,
                    text=Presets.SEARCH_RESULT_LOG.format(user.mention(), query.query),
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                    reply_markup=replay_markup_close,
                    disable_notification=True
                )
            except Exception:
                pass
            await asyncio.sleep(5)
        else:
            return
    else:
        switch_pm_text = Presets.NO_RESULT_TXT
        if string:
            switch_pm_text = Presets.NO_RESULT_TXT_STR.format(string)
        try:
            await query.answer(
                results=[],
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="okay"
            )
        except Exception:
            pass
    #
    await asyncio.sleep(5)
    results.clear()
