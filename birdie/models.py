from mongoengine import Document, fields
from enum import Enum

import re

def sanitize(string):
    if string is None:
        return ''
    return re.sub("[\$\.]", "_", string)

class TgUser(Document):
    tg_user_id = fields.IntField(primary=True)
    name = fields.StringField()
    address = fields.StringField()
    meta = {
        'indexes': ['tg_user_id']
    }

    @classmethod
    def find_or_create(cls, tg_user_id, first_name, last_name):
        user = TgUser.objects(tg_user_id=tg_user_id).first()
        if user is None:
            user = TgUser(
            tg_user_id = tg_user_id,
            name=f'{sanitize(first_name)} {sanitize(last_name)}',
            )
            user.save()
        return user

class TgChannel(Document):
    tg_id = fields.IntField(primary=True)
    trial = fields.BooleanField(default = True)

    meta = {
        'indexes': ['tg_id']
    }

    @classmethod
    def find_or_create(cls, tg_channel_id):
        channel = cls.objects(tg_id=tg_channel_id).first()
        if channel is None:
            channel = TgChannel(
                tg_id = tg_channel_id
            )
            channel.save()
        return channel

class Venue(Document):
    channel = fields.ReferenceField(TgChannel)
    name = fields.StringField()
    address = fields.StringField()
    suburb = fields.StringField()
    phone = fields.StringField()
    map_url = fields.StringField()
    courts = fields.IntField()
    meta = {
        'indexes': ['name']
    }

    @classmethod
    def find_or_create(cls, venue_name):
        venue = cls.objects(name=venue_name).first()
        if venue is None:
            venue = Venue()
            venue.name = venue_name
            venue.save()
        return venue

    @classmethod
    def list(cls, channel):
        return cls.objects(channel=channel)

class SocialEventSchedule(Document):
    class RepeatType(Enum):
        DAY = 0
        WEEK = 1
        MONTH = 2
        YEAR = 3

    channel = fields.ReferenceField(TgChannel)
    name = fields.StringField()
    venue = fields.ReferenceField(Venue)
    start_time = fields.DateTimeField()
    end_time = fields.DateTimeField()
    day = fields.IntField()
    repeat_type = fields.EnumField(RepeatType)

class SocialEvent(Document):
    channel = fields.ReferenceField(TgChannel)
    name = fields.StringField()
    schedule = fields.ReferenceField(SocialEventSchedule)
    date = fields.DateField()

class SocialEventBooking(Document):
    event = fields.ReferenceField(SocialEvent)
    user = fields.ReferenceField(TgUser)
    has_paid = fields.BooleanField()
