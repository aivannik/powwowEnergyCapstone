from app import db

class Weather(db.Model):
    __tablename__ = 'weatherdata'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    station = db.Column(db.String)
    date = db.Column(db.Date)
    prcp = db.Column(db.Float)
    tmax = db.Column(db.Float)
    tmin = db.Column(db.Float)

    def __init__(self, name, station, date, prcp, tmax, tmin):
        self.name = name
        self.station = station
        self.date = date
        self.prcp = prcp
        self.tmax = tmax
        self.tmin = tmin

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name, 
            'station': self.station,
            'date': self.date,
            'prcp':self.prcp,
            'tmax': self.tmax,
            'tmin': self.tmin
        }

class Field(db.Model):
    __tablename__ = 'sbvectors2'
    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String)
    acres = db.Column(db.Float)
    coordinates = db.Column(db.String)

    def __init__(self, crop, acres, coordinates):
        self.crop = crop
        self.acres = acres
        self.coordinates = coordinates

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id' : self.id,
            'crop' : self.crop,
            'acres' : self.acres,
            'coordinates' : self.coordinates
        }                         