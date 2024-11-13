from mongoengine import Document, StringField, DateTimeField, ListField, BooleanField

class User(Document):
    upn = StringField(required=True, unique=True)
    created_at = DateTimeField(default=datetime.utcnow)
    created_by = StringField()
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    department = StringField(required=True)
    role = StringField(required=True)
    supervisor = StringField(required=True)
    job_title = StringField(required=True)
    start_date = DateTimeField(required=True)
    notes = StringField()
    shared_mailboxes = ListField(StringField())
    distribution_groups = ListField(StringField())
    groups = ListField(StringField())
    calendar_editor = BooleanField(default=False)
    onboarded = BooleanField(default=False)
    onboarded_date = DateTimeField()