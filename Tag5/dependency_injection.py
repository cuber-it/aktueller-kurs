class ServiceBasis:
    def request(self):
        raise RuntimeError("NOT YET IMPLMENTED or MISSING: request() for Service")

class ServiceA(ServiceBasis):
    def request(self):
        return "ServiceA"

class ServiceB(ServiceBasis):
    def request(self):
        return "ServiceB"

class ServiceC(ServiceBasis):
    def request(self):
        return "ServiceC"

class ServiceD(ServiceBasis):
    def request(self):
        return "ServiceD"

#---------------------------------
class ClientAlt:
    def __init__(self):
        self.services = dict( # Sprungtabelle
            A = ServiceA(),
            B = ServiceB(),
            C = ServiceC()
        )

    def machwas(self, service_id="A"):
        print(self.services[service_id].request())


class ClientNeu:
    def machwas(self, service_object): # Dependency Injection
        if not isinstance(service_object, ServiceBasis): # es dürfen nur Objekte vom Typ Child of ServiceBasis übergeben werden!
            raise TypeError("service_object must be an instance of ServiceBasis or its subclass")
        print(service_object.request())


#-------------------------------
c = ClientAlt()
c.machwas()
c.machwas("B")
c.machwas("A")
c.machwas("C")
#c.machwas("D") -> failt!, erst muss Client angepasst werden

c = ClientNeu()
c.machwas(ServiceA())
c.machwas(ServiceB())
c.machwas(ServiceA())
c.machwas(ServiceC())
c.machwas(ServiceD())
#c.machwas(ServiceE())
c.machwas(ClientNeu())
