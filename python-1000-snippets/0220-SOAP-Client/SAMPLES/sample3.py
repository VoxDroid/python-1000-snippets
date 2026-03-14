# sample3.py
# Use zeep to print available operations from the WSDL
from zeep import Client
from requests.exceptions import RequestException

if __name__ == '__main__':
    try:
        client = Client('http://www.dneonline.com/calculator.asmx?WSDL')
        print('Available operations:')
        for service in client.wsdl.services.values():
            for port in service.ports.values():
                for op in port.binding._operations.values():
                    print('-', op.name)
    except RequestException as e:
        print('Network error:', e)
    except Exception as e:
        print('Unexpected error:', e)

