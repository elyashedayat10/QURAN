import os
import uuid

from django.core.exceptions import ValidationError
from kavenegar import *

errore_message = {
    ''
}


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


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
