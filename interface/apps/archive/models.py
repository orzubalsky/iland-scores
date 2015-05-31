from django.db.models import *
from django.utils import timezone


class BaseModel(Model):
    """
    Base model for all of the models in the application.
    """
    class Meta:
        abstract = True

    created = DateTimeField(editable=False)
    updated = DateTimeField(editable=False)
    is_active = BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Save timezone-aware values for created and updated fields.
        """

        self.created = timezone.now()
        self.updated = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

    def __unicode__(self):
        if hasattr(self, 'name') and self.name:
            return self.name
        else:
            return "%s" % (type(self))


class Project(BaseModel):
    class Meta:
        ordering = ['name', ]

    name = CharField(max_length=200)

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains',)


class Event(BaseModel):
    class Meta:
        ordering = ['name', ]

    name = CharField(max_length=200)

    @staticmethod
    def autocomplete_search_fields():
        return ('name__icontains',)


class Score(BaseModel):
    class Meta:
        ordering = ['project', 'event', 'name']

    name = CharField(max_length=200, blank=True, null=True)
    description = TextField()
    place = CharField(max_length=100, blank=True, null=True)
    city = CharField(max_length=100, blank=True, null=True)
    state = CharField(max_length=2, blank=True, null=True)
    country = CharField(max_length=100, blank=True, null=True)
    project = ForeignKey(Project, blank=True, null=True)
    event = ForeignKey(Event, blank=True, null=True)
    year = PositiveIntegerField(blank=True, null=True)
    collaborators = TextField(blank=True, null=True)
