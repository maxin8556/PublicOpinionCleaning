



class CustomException(Exception):
   """Base class for other exceptions"""
   pass

class PackaegNotFoundError(CustomException):
   """Raised when the input value is too small"""
   pass

# class ValueTooLargeException(CustomException):
#    """Raised when the input value is too large"""
#    pass
