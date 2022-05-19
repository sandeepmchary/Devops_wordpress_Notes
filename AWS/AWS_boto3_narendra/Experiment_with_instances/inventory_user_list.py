import boto3
import csv
iam_re=boto3.resource('iam')
cnt=1
csv_ob=open("users.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S.No","IAM User Name","User Id","User ARN","User Creation Date","Attached Policies"])
for each_user in iam_re.users.all():
    #print(dir(each_user))
    print(each_user.user_name,each_user.user_id,each_user.arn,each_user.create_date,each_user.attached_policies)
    csv_w.writerow([cnt,each_user.user_name,each_user.user_id,each_user.arn,each_user.create_date,each_user.attached_policies])
    cnt+=1
csv_ob.close()