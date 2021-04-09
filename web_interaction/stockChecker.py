import json
import urllib.request
import boto3.ec2

def lambda_handler(self, context):
    apikey = 'pk_22bd6caeeb774750bc7b10d998655615'
    emailaddress = 'joswald@nd.edu'
    prefix = 'https://cloud.iexapis.com/stable/stock/'
    ticker = 'AMZN'
    options = '/quote/latestPrice?token='

    
    url = prefix + ticker + options + apikey
    print(url)

    response = urllib.request.urlopen(url)
    stockinfo = json.loads(response.read().decode())

    price=str(stockinfo)
    print(price)


    mailclient=boto3.client('ses')
    
    subject= ticker + " is at " + price
    message = "At the time of the most recent trade, " + ticker + ' traded at ' + price +'.'
   
    mailresponse = mailclient.send_email(
        Source=emailaddress,
        Destination={
            'ToAddresses': [
            emailaddress,
            ]
            },
        Message={
            'Subject': {
            'Data': subject},
            'Body': {
            'Text': {
            'Data': message,
                }
            }
        },
    )