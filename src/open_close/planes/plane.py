from abc import ABC, abstractmethod, abstractproperty 

class Plane(ABC):
    """Abstract base clase to create plane subclases such as WideBody, NarrowBody or Freighter"""    

    @abstractproperty
    def type(self):
        """Required method"""
    
    @abstractmethod
    def __str__(self):
        pass    

        