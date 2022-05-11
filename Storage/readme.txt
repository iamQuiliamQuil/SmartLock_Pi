It stores stuff.
Also other picture related utilites

Picture server exists because, in order to send images with Twilio, 
they need to be hosted on a public server. 
This means that anyone anywhere can look at the images in Storage, 
the way we have it implemented here. There's definitely a better way of doing 
this, and that should probably be looked into. The main Server in Python launches 
this server on startup, so there is no need to launch it here. 

Instructions on configuring remove_old_photos_cronjob.sh to work as a cronjob 
can be found in the comments of said file. 

Twilio errors can be found online in the Twilio error log
