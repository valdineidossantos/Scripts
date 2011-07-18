from django.core.mail import send_mail
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'




Subject = 'Subject here'
Message = "Message here" 
From    =  "valdinei@valdineidossantos.com"
To      = ["valdinei@mailinator.com",'valdineidossantos@mailinator.com']
result  =send_mail(Subject, Message, From, To, fail_silently=False)
print   "Result: %s" % result
