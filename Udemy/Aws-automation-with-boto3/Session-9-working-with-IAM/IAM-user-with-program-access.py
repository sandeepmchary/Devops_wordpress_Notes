import boto3
from random import choice
import sys

def passwd():
	passwd_length=8
	char_for_passwd="abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>~`"
	password=[]
	return "".join(choice(char_for_passwd) for each_char in range(passwd_length))


def get_iam_client_object():
	session=boto3.session.Session(profile_name="root")
	iam_client=session.client("iam")
	return iam_client
def main():
	iam_client=get_iam_client_object()
	Iam_user_name="intel345"
	passwd=get_random_passwd()
	PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
	try:
		iam_client.create.user(UserName=Iam_user_name)
	except Exception as e:
		if e.response['Error']['Code']=="EntityAlreadyExists":
			print("Already with Iam user with {} is exists".format(Iam_user_name))
			sys.exit(0)
		else:
			print("Please verify the following error and retry")
			print(e)
			sys.exit(0)
response = iam_client.create_access_key(UserName=Iam_user_name)	 
print("AccessKeyId={}\nSecretAccesskey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey'])
iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
return None	

if __name__ == "__main__":
	main()