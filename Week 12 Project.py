#Create your empty list of AWS services
myaws_services= []

#Populate your list of AWS Services
myaws_services.append('AWS Lambda')
myaws_services.append('AWS Code Pipeline')
myaws_services.append('Amazon Inspector')
myaws_services.append('AWS CloudHSM')
myaws_services.append('AWS Shield')
myaws_services.append('Amazon Cognito')
myaws_services.append('Amazon ElastiCache')
myaws_services.append('AWS Security Hub')
myaws_services.append('AWS Fargate')
myaws_services.append('Amazon EventBridge')

#Print the list of AWS Services and its length
print("10 Must include AWS and Amazon Services")
print(len(myaws_services))

#Remove two specific AWS Services from the list by name or by index
del myaws_services[0]
del myaws_services[-1]

#Print the new list and its new length
print(myaws_services)
print("8 Must include AWS and Amazon Services")
print(len(myaws_services))



