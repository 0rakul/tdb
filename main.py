
"""
Open public transport
"""
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import logging
from django.utils import simplejson


class MainHandler(webapp.RequestHandler):
    """
    Renders the main page
    """
    def get(self):
        "Renders the main page"
        transports = get_transport_headers()
        logging.info(transports)
        #        transports=[Transport(name='asd', city='Budapest')]
        self.response.out.write(template.render('main.html', 
                                                {'transports':
                                                 transports}))
        
        
        

class DetailedHandler(webapp.RequestHandler):
    "Handles the /detailed/city/busname url"
    def get(self):
        "Renders the details.html"
        path = self.request.path
        splittedpath = path.rsplit('/')
        stops = get_stops()
        stops_json = {}
        stops_list = []
        i = 0
        for stop in stops:
            stops_list.append((stop.latitude, stop.longitude))
            i = i + 1
        stops_json.append('asdf', stop_list)
#        timeheaders = ['10', '20', '30', '40', '50']
        self.response.out.write(template.render('detailed.html', {'path':path, 'stops':['sdf', '11'],
                                                                  't_name':splittedpath[3],
                                                                  'bus_coordinates':stops_json
                                                                  }))
        
        
        
        

class TransportHandler(webapp.RequestHandler):
    """Transport related class"""
    def get(self):
        "Get method of transport related class"
#        t_name = self.request.get('t_name')
#        stops = self.request.get('stations')
#        logging.info('stops' + stops)
#        if t_name:
#            save_transport_header(t_name, self.request.get('t_city'))
#        else:
#            self.request.get('name')
#            self.response.out.write('asd')


    def post(self):
        "Processes data updates from client"
        args = simplejson.loads(self.request.body)
        t_name = args['t_name']
        stops = args['stations']
        coordinates = args['coords']
        stopsdata = (stops, coordinates)
        save_transport_header(t_name, 'Budapest', stopsdata)
        self.response.out.write('ok')
              
class Transport(db.Model):
    "Transport data"
    name = db.StringProperty()
    city = db.StringProperty()

class StationCoordinate(db.Model):
    "Coordinates of stations"
    latitude = db.FloatProperty()
    longitude = db.FloatProperty()
    transport = db.ReferenceProperty(Transport)
    
class Stops(db.Model):
    "Transport's 'stops' list"
    stops = db.StringListProperty()
    coordinates = db.ListProperty(db.Key)
    transport_header = db.ReferenceProperty(Transport)
    
class Timetable(db.Model):
    "A bus's timetable snapshot"
    times = db.StringListProperty()
    
def get_transport_headers():
    "Get the transport headers ordered"
    return db.GqlQuery('SELECT * FROM Transport ORDER BY name')

def save_transport_header(name, city, stops_data):
    """
    name: of the bus
    city: the main location of the transport
    stops_list: list of stops (list of tuples (stop name, arrival time from the first stop)
    timetable: a list of minutes from midnight    
    """
    query_t = Transport.gql('WHERE name= :1', name)
    for a in query_t:
        logging.info('SD');
#    logging.info(dir(query_t))
    if (query_t):
        transport_to_save = query_t
    else:
        transport_to_save = Transport(name=name, city=city)
    transport_to_save.put()

#    for stop, coordinate in stops_data:
    for coordinate in stops_data[1]:
        #        stopsDb = Stops(stop=stop, transport_header=transport_to_save)
        #        stopsDb.put()
        coordinates = StationCoordinate(latitude=coordinate[0],
                                         longitude=coordinate[1],
                                         transport=transport_to_save
                                         )
        coordinates.put()

def get_stops():
    "Returns the stops on the map"
#    stops = db.GqlQuery('SELECT * FROM Stops')
    stops = db.GqlQuery('SELECT * FROM StationCoordinate')
    #    for stops in query:        
    return stops
#    return stops

def main():
    "The entry points"
    application = webapp.WSGIApplication([
        ('/', MainHandler), ('/query', TransportHandler),
        ('^/detail/.*/.*$', DetailedHandler)],
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
    

