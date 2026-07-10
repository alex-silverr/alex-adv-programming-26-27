from tortoise.models import Model
from tortoise import fields

class Thing(Model):
    id = fields.IntField(primary_key=True)
    thing = fields.CharField(max_length=200)