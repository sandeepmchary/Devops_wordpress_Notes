import boto3
iam_cli=boto3.client('iam')
user_name=input('Enter the User Name: ')
created_user=iam_cli.create_user(
              UserName=user_name,
              Tags=[
                  {
                      'Key':'Env',
                      'Value': 'Test'
                  }
              ]  
)
print(created_user)