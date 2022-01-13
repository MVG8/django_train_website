import requests
from .models import TeleSettings


#token = '5083451369:AAEZ9O219A9EnivZJT5I8G9W7-LcEzE-bpI'
#chat_id = '-607011586'
#text = 'Test_2'

def sendTelegram(tg_name, tg_phone):
	if TeleSettings.objects.get(pk=1):
		settings = TeleSettings.objects.get(pk=1)
		token = str(settings.tg_token)
		chat_id = str(settings.tg_chat)
		text = str(settings.tg_message)
		api = 'https://api.telegram.org/bot'
		method = api + token + '/sendMessage'

		#a = text.find('{')
		#b = text.find('}')
		#c = text.rfind('{')
		#d = text.rfind('}')

		if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
			part_1 = text[0:text.find('{')]
			part_2 = text[text.find('}') + 1:text.rfind('{')]
			part_3 = text[text.rfind('}'):-1]

			text_slise = part_1 + tg_name + part_2 + tg_phone + part_3

		else:
			text_slise = text

			req = requests.post(method, data={
				'chat_id': chat_id,
				'text': text_slise
			})

		part_1 = text[0:a]
		part_2 = text[b + 1:c]
		part_3 = text[d:-1]

		text_slise = part_1 + tg_name + part_2 + tg_phone + part_3

		try:

			req = requests.post(method, data={
				'chat_id': chat_id,
				'text': text_slise
				})
		except:
			pass

		finally:
			if req.status_code != 200:
				print('Ошибка отправки!')
			elif req.status_code == 500:
				print('Ошибка 500')
			else:
				print('Все ОК сообщение отправлено!')


	else:
		pass
