from pyad import *

pyad.set_defaults(ldap_server="WIN-3QMNF1PAO8B.testlab.local",username="ajoseph", password="Test2020!" )

user=pyad.aduser.ADUser.from_cn("Susan Sally")
#users =pyad.aduser.ADUser()
#users = pyad.adgroup.ADGroup.from_cn("User")
#laborWebappGroup = pyad.adgroup.ADGroup.from_cn("Labor Webapp")

#from pyad import adquery
qobj = adquery.ADQuery()
qobj.execute_query(
attributes = ["distinguishedName", "description"],
where_clause = "objectClass = '*'",
base_dn = "OU=users, DC=domain, DC=com"
)

for row in q.get_results():
    print ["distinguishedName"]

print (user) 
print ('Attributes of AD User: Department, Company, Employee ID')
print (user.get_attribute("department"),user.get_attribute("Company"),user.get_attribute("mail"))

print('\n')


#print (laborWebappGroup)
print (users)
print ('Members of Labor Webapp Security Group:')
print (laborWebappGroup.get_attribute("member"))

f = open("whitelist.txt", "w")
print (laborWebappGroup.get_attribute("member"), file = f)
f.close()


print ('\n')

#testing all the regex functions

my_password := "secretpass" or my_password := secretpass

api_key: foo

api_key: "foo"

my_password = "secretpass"
my_password = @"secretpass"
my_password[] = "secretpass";

my_password="secretpass"
my_password=@"secretpass"
my_password[]="secretpass";

my_password = secretpass

my_password = "secretpass"

private_key "something";


