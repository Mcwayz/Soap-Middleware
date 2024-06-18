# myapp/soap_client.py

from zeep import Client, Settings
from zeep.transports import Transport
from requests import Session

WSDL_TEST_URL = 'http://172.18.2.135:7661/payment/services/APIRequestMgrService?wsdl'
WSDL_PROD_URL = 'http://172.18.0.133:7661/payment/services/APIRequestMgrService?wsdl'

def call_b2c_service(data):
    session = Session()
    session.headers.update({
        'Content-Type': 'text/xml',
        'SOAPAction': '#POST'
    })

    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(wsdl=WSDL_TEST_URL, transport=Transport(session=session), settings=settings)


    # The SOAP request body
    
    request_data = {
        'api:Request': {
            'req:Header': {
                'req:Version': '1.0',
                'req:CommandID': data['CommandID'],
                'req:OriginatorConversationID': data['OriginatorConversationID'],
                'req:Caller': {
                    'req:CallerType': '2',
                    'req:ThirdPartyID': data['ThirdPartyID'],
                    'req:Password': data['Password'],
                    'req:ResultURL': data['ResultURL']
                },
                'req:KeyOwner': '1',
                'req:Timestamp': data['Timestamp']
            },
            'req:Body': {
                'req:Identity': {
                    'req:Initiator': {
                        'req:IdentifierType': '11',
                        'req:Identifier': data['Identifier'],
                        'req:SecurityCredential': data['SecurityCredential'],
                        'req:ShortCode': data['ShortCode']
                    },
                    'req:ReceiverParty': {
                        'req:IdentifierType': '1',
                        'req:Identifier': data['ReceiverIdentifier']
                    }
                },
                'req:TransactionRequest': {
                    'req:Parameters': {
                        'req:Amount': data['Amount'],
                        'req:Currency': data['Currency'],
                        'req:ReasonType': data['ReasonType']
                    }
                },
                'req:ReferenceData': {
                    'req:ReferenceItem': {
                        'com:Key': 'Comment2Customer',
                        'com:Value': data['Comment']
                    }
                }
            }
        }
    }

    response = client.service.Request(**request_data)
    return response
