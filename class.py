class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.speed_limit=speed_limit
        self.company=company

    def start(self):
        print("started")

    def stop(self):
        print("stoped")

    def accelarate(self):
        print("accelarating")

    def change_gear(self):
        print("gear_changed") 
buggati=Car("chiron","blue","buggati",320)
print(buggati.stop)