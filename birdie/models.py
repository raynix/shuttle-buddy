from mongoengine import Document, fields

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
            name=f'{first_name or ""} {last_name or ""}',
         )
         user.save()
      return user

class Venue(Document):
    name = fields.StringField()
    address = fields.StringField()
    suburb = fields.StringField()
    phone = fields.StringField()
    map_url = fields.StringField()
    courts = fields.IntField()
    meta = {
        'indexes': ['name']
    }

class SocialEventSchedule(Document):
    name = fields.StringField()
    venue = fields.ReferenceField(Venue)
    start_time = fields.DateTimeField()
    end_time = fields.DateTimeField()

class SocialEvent(Document):
    name = fields.StringField()
    schedule = fields.ReferenceField(SocialEventSchedule)
    date = fields.DateField()

class SocialEventBooking(Document):
    event = fields.ReferenceField(SocialEvent)
    user = fields.ReferenceField(TgUser)
    has_paid = fields.BooleanField()
