from django.core.mail import send_mail
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'




Subject = 'Subject here'
Message = "Message here" 
From    =  "valdinei@valdineidossantos.com"
From    =  "valdineis@ctallen.com.br"
To      = ["valdinei.santos@allen.com.br",'valdineidossantos@gmail.com']
result  =send_mail(Subject, Message, From, To, fail_silently=False)
print   "Result: %s" % result
