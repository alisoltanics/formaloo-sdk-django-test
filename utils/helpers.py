from uuid import uuid4
import shortuuid

from django.conf import settings


def create_short_uuid():
    shortuuid.set_alphabet(settings.SUUID_ALPHABET)
    suid = shortuuid.ShortUUID().random(length=settings.SUUID_LENGTH)
    return suid
