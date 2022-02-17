from kavenegar import *


def send_otp_code(phone_number, code):
	try:
		api = KavenegarAPI('kooft')
		params = {
			'sender': '',
			'receptor': phone_number,
			'message': f'{code} کد تایید شما '
		}
		response = api.sms_send(params)
		print(response)
	except APIException as e:
		print(e)
	except HTTPException as e:
		print(e)
