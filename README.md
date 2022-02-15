# Sending-mail-through-python

Methods of sending mail:-

   METHOD-1:   Setting up a Gmail Account for Development

   In this method you have to allow less secure apps to access your G-mail account by going into the settings. But
   I highly recommend not to use this method because it may expose your login details to others making your 
   account less secure. But if you really want to use this method then I recommend you to create a throwaway 
   account for the development of your code.

   METHOD-2:   Setting up a local SMTP server

   For this method to work you can use local_hostname  of SMTP. In this smtpd module is used that comes pre-
   installed with Python. Rather than sending emails to the specified address, it discards them and prints their
   content to the console. To set up the local SMTP debugging server you can type the following in command 
   prompt.
             
             python -m smtpd -c DebuggingServer -n localhost:1025
             
             
   METHOD-3:   Setting up the app password

   For this method to your mail id should have 2-Step Verification. You can do this by going into settings and then
   security of your mail id. Without this app password for the mail id can not be created. After turning on the 2-Step
   Verification you can create app password from the option 'app password' below it. 
