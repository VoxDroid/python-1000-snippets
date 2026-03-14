# sample1.py
# Call a public SOAP calculator service and handle network issues.
from zeep import Client
from zeep.exceptions import Fault
from requests.exceptions import RequestException


def call_add(a: int, b: int) -> int:
    client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Add(a, b)


if __name__ == '__main__':
    try:
        result = call_add(5, 3)
        print('Result:', result)
    except Fault as e:
        print('SOAP fault:', e)
    except RequestException as e:
        print('Network error:', e)
    except Exception as e:
        print('Unexpected error:', e)

