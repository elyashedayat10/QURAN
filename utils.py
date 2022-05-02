import uuid

from kavenegar import *
import os


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI("kooft")
        params = {
            "sender": "",
            "receptor": phone_number,
            "message": f"{code} کد تایید شما ",
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)



def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("uploads/" + instance.__class__.__name__, filename)