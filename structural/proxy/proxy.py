import time
from producer import Producer


class Proxy:
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        '''check if a producer is available'''
        print('check if producer is free .....')
        if self.occupied == 'No':
            self.producer = Producer()
           #  simulate that creating producer is expensive
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print('producer is busy')
