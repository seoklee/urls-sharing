from app import db


class LinkEntry(db.Document):
    token = db.StringField(primary_key=True, max_length=255, required=True)
    links = db.ListField(db.StringField(max_length=255, required=True))
    description = db.StringField(max_length=1000)

    def __unicode__(self):
        return self.token
