from chat_providers.basic import Chat
import pyautogui, asyncio

# The most cursed Twitch chat bot ever. do NOT run this on anything you care about

async def main(chat_provider_class: Chat):
    chat = chat_provider_class()
    while True:
        message = await chat.get_message()
        if message != None or '':
            if '^' in message:
                pyautogui.hotkey(*message.split('^'))
            else:
                pyautogui.write(message, interval = 0.2)
                pyautogui.press('enter')

asyncio.run(main(Chat))
