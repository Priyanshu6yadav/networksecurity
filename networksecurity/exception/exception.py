import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error_messsage,error_details:sys):
        self.error_message = error_messsage
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in pytjon script name [{0}] line number [{1}] error message[{2}]".format(
        self.file_name, self.lineno,str(self.error_message))

if __name__=="__main__":
    try:
        logger.logging.INFO("Enter the try block")
        # Intentionally raising an exception to test the custom exception
        a=1/0
        print("this will no be printed",a)
        raise Exception("Test error to trigger exception")
    except Exception as e:
        raise NetworkSecurityException(e,sys)