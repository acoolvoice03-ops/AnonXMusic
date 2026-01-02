# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic

import asyncio
from pyrogram import enums, filters, types
from pyrogram.types import InlineKeyboardMarkup

from anony import app, config, db, lang
from anony.helpers import buttons, utils


# ---------------- SAFE MARKUP HELPER ----------------
def safe_markup(markup):
    """
    Ensures reply_markup is valid and contains no None buttons
    """
    if not markup or not isinstance(markup, InlineKeyboardMarkup):
        return None

    clean_keyboard = []

    for row in markup.inline_keyboard:
        if not row:
            continue
        clean_row = [btn for btn in row if btn is not None]
        if clean_row:
            clean_keyboard.append(clean_row)

    if not clean_keyboard:
        return None

    return InlineKeyboardMarkup(clean_keyboard)


# ---------------- HELP COMMAND ----------------
@app.on_message(filters.command(["help"]) & filters.private & ~app.bl_users)
@lang.language()
async def _help(_, message: types.Message):
    markup = safe_markup(buttons.help_markup(message.lang))

    await message.reply_text(
        text=message.lang["help_menu"],
        reply_markup=markup,
        quote=True,
    )


# ---------------- START COMMAND ----------------
@app.on_message(filters.command(["start"]))
@lang.language()
async def start(_, message: types.Message):
    if (
        message.from_user.id in app.bl_users
        and message.from_user.id not in db.notified
    ):
        return await message.reply_text(message.lang["bl_user_notify"])

    if len(message.command) > 1 and message.command[1] == "help":
        return await _help(_, message)

    private = message.chat.type == enums.ChatType.PRIVATE

    text = (
        message.lang["start_pm"].format(message.from_user.first_name, app.name)
        if private
        else message.lang["start_gp"].format(app.name)
    )

    markup = safe_markup(
        buttons.start_key(message.lang, private)
    )

    await message.reply_photo(
        photo=config.START_IMG,
        caption=text,
        reply_markup=markup,
        quote=not private,
    )

    if private:
        if not await db.is_user(message.from_user.id):
            await utils.send_log(message)
            await db.add_user(message.from_user.id)
    else:
        if not await db.is_chat(message.chat.id):
            await utils.send_log(message, True)
            await db.add_chat(message.chat.id)


# ---------------- SETTINGS ----------------
@app.on_message(filters.command(["playmode", "settings"]) & filters.group & ~app.bl_users)
@lang.language()
async def settings(_, message: types.Message):
    admin_only = await db.get_play_mode(message.chat.id)
    cmd_delete = await db.get_cmd_delete(message.chat.id)
    language = await db.get_lang(message.chat.id)

    markup = safe_markup(
        buttons.settings_markup(
            message.lang,
            admin_only,
            cmd_delete,
            language,
            message.chat.id,
        )
    )

    await message.reply_text(
        text=message.lang["start_settings"].format(message.chat.title),
        reply_markup=markup,
        quote=True,
    )


# ---------------- NEW CHAT MEMBER ----------------
@app.on_message(filters.new_chat_members, group=7)
@lang.language()
async def _new_member(_, message: types.Message):
    if message.chat.type != enums.ChatType.SUPERGROUP:
        return await message.chat.leave()

    await asyncio.sleep(3)

    for member in message.new_chat_members:
        if member.id == app.id:
            if await db.is_chat(message.chat.id):
                return
            await utils.send_log(message, True)
            await db.add_chat(message.chat.id)
