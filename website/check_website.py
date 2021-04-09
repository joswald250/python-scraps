from __future__ import print_function

from datetime import datetime
import urllib.request

url = 'insert url here'
keyword = 'Username?'
email = 'insert email here'


def validate(res):
    result = (keyword in res)
    return result


def lambda_handler(event, context):
    print('Checking Site...')

    try:
        if not validate(urllib.request.urlopen(url, None, 12).read().decode()):
            print('Site not reachable')
            raise Exception('Validation failed')
    except:
        print('Check failed!  Rebooting server.')
        mailclient=boto3.client('ses')
        ec2 = boto3.resource('ec2', region_name='us-east-1')
        client = ec2.meta.client
        rebootstatus = client.reboot_instances(InstanceIds=[instance])
        print ('Reboot status: ' + str(rebootstatus))
        
        message='EC2 Instance ' + instance + ' Rebooted'

        mailresponse = mailclient.send_email(
            Source=email,
            Destination={
                'ToAddresses': [
                email,
                ]
                },
            Message={
                'Subject': {
                'Data': message},
                'Body': {
                'Text': {
                'Data': str(rebootstatus),
                    }
                }
            },
        )   
        raise
    else:
        print('Check passed!')
        return 1;
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
