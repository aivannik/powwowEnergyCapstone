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