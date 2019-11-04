Build VPC
- switch to a new region
- search for vpc
- AWS gives default one vpc
- dont use the default vpc for customized deployments
$ your vpc
$ create vpc
$ give name
$ CIDR block: <some ip address>
<10.0.0.0/26>
- if we choose dedicated we can use only dedicated instances only in this vpc
$ choose default
- 10.0.0.0/26
starting ip - 10.0.0.0

2(power)(32-26) = 2(power)(6) =64
end: 10.0.0.63

-divide 64 into 4 subnets 16 ip address each 
$ create
-- define this vpc in subnets 
$ create subnet
name tag: private-a
vpc: <choose our vpc>
$ leave avalibilty zone as it is
$ CIDR block: 10.0.0.0/28
starting ip : 10.0.0.0

2 (power)(32-28) = 2(power)(4) =16

$ create
$ create one more
name tag: private-c
vpc: <choose our vpc>
avalibilty-zone: <choose another>
CIDR block: 10.0.0.16/28
$ create
$ create vpc in public
name tag: public-a
vpc: <choose our vpc>
avalibilty zone: in 1a
CIDR block: 10.0.0.32/28
$ create

$ create vpc
name tag: public-c
vpc: <choose our vpc>
avalibilty zone: 1c
cidr block: 10.0.0.48/28
$ create
- here we have only 11 ip address 
- 5 are taken by aws for internet usage
- first 4 and last 1 ip address
-------------------
Route tables
- when ever we create VPC one Route table is created along with it
- search with created VPC name
- rename it public-RT
$ create one Route table
$ name: private-rt
vpc: <choose our vpc>
$ create
$ choose private rt
$ subnet associations
$ edit
$ choose both private ones
$ save
$ choose public Route table
$ subnet associations
$ choose both are public ones
$ save
-- one subnet has only one Route table
-- one RT can associates to multiple subnets
-- 1 RT -- 1 subnets
--but n subnets - 1 RT
-------------------
Internet Gateway
$ choose internet gateway
$ create internet gateway
$ myIGW
$ create
$ select the created internet gateway 
$ right click 
$ attach to vpc
$ vpc: <choose our vpc>
-- one IGW is attached to vpc
-------------------
comeback to RT
$ choose public-RT
$ Routes
$ edit
$ Add another route
$ 0.0.0.0/0
$ igw<the one which we created>
-------------------
NAT Gateways
$ create NAT Gateway
$ subnet: choose one of the public subnet
$ create new EIP
$ create a NAT Gateway
------------------
Route table
$ choose private-RT
$ Routes
$ edit
$ Add another
$ 0.0.0.0/0 
$ nat<the one which we created>
$ save
-------------------
-- what is the use of NAT Gateway
- outbounds/internet bound traffic from the private instances 
- goes to nat
- nat got to internet
- internet to nat
- nat to private instances
















































































