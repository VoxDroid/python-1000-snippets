# sample2.py
# Call another method on the SOAP calculator service
from zeep import Client
from zeep.exceptions import Fault
from requests.exceptions import RequestException


def call_multiply(a: int, b: int) -> int:
    client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Multiply(a, b)


if __name__ == '__main__':
    try:
        result = call_multiply(6, 7)
        print('Result:', result)
    except Fault as e:
        print('SOAP fault:', e)
    except RequestException as e:
        print('Network error:', e)
    except Exception as e:
        print('Unexpected error:', e)

