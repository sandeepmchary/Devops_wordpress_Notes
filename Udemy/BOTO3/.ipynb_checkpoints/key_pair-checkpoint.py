{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Create Key Pair for EC2 Instance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ClientError",
     "evalue": "An error occurred (InvalidKeyPair.Duplicate) when calling the CreateKeyPair operation: The keypair 'ec2_key_pair' already exists.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mClientError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-681afd571820>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0moutfile\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'ec2_key_pair.pem'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'w'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m# Call the boto create_key_pair function to create key pair\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mkeypair\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mec2_re\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcreate_key_pair\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mKeyName\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'ec2_key_pair'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkeypair\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkey_material\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Python38\\lib\\site-packages\\boto3\\resources\\factory.py\u001b[0m in \u001b[0;36mdo_action\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    518\u001b[0m             \u001b[1;31m# instance via ``self``.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    519\u001b[0m             \u001b[1;32mdef\u001b[0m \u001b[0mdo_action\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 520\u001b[1;33m                 \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maction\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    521\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    522\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'load'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Python38\\lib\\site-packages\\boto3\\resources\\action.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, parent, *args, **kwargs)\u001b[0m\n\u001b[0;32m     81\u001b[0m                     operation_name, params)\n\u001b[0;32m     82\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 83\u001b[1;33m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmeta\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclient\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     84\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     85\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Response: %r'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Python38\\lib\\site-packages\\botocore\\client.py\u001b[0m in \u001b[0;36m_api_call\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    314\u001b[0m                     \"%s() only accepts keyword arguments.\" % py_operation_name)\n\u001b[0;32m    315\u001b[0m             \u001b[1;31m# The \"self\" in this scope is referring to the BaseClient.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 316\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_api_call\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0moperation_name\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    318\u001b[0m         \u001b[0m_api_call\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__name__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpy_operation_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Python38\\lib\\site-packages\\botocore\\client.py\u001b[0m in \u001b[0;36m_make_api_call\u001b[1;34m(self, operation_name, api_params)\u001b[0m\n\u001b[0;32m    624\u001b[0m             \u001b[0merror_code\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mparsed_response\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Error\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Code\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    625\u001b[0m             \u001b[0merror_class\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexceptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfrom_code\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merror_code\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 626\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0merror_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparsed_response\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    627\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    628\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mparsed_response\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mClientError\u001b[0m: An error occurred (InvalidKeyPair.Duplicate) when calling the CreateKeyPair operation: The keypair 'ec2_key_pair' already exists."
     ]
    }
   ],
   "source": [
    "import boto3\n",
    "#region=input(\"Enter the region:\")\n",
    "ec2_re=boto3.resource('ec2')\n",
    "# Create a file to store the key locally\n",
    "outfile=open('ec2_key_pair.pem','w')\n",
    "# Call the boto create_key_pair function to create key pair\n",
    "keypair=ec2_re.create_key_pair(KeyName='ec2_key_pair')\n",
    "print(keypair.key_material)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
