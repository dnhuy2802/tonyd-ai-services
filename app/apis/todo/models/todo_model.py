from tortoise.models import Model
from tortoise.fields import CharField, BooleanField, IntField

class Todo(Model):
    id = IntField(pk=True)
    task = CharField(max_length=100)
    done = BooleanField()