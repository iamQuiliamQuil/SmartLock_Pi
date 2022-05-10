This is the meat and potatoes.  

use command  
python Server.py  
or run the file with an IDE like Thonny  

--missing server explanation--  

There is a second script which we did not implement into the system and acts on its own  
doorbell.py  
this checks if buttons if they are pressed  
when the outside button is pressed a picture is taken and notification text is sent  
a doorbell noise is also played. the noise might not work.  
requires speaker (i used sound played through a monitor with HDMI)
i think you need to restart the pi once before testing doorbell.py  
it works for every button press afterwards and will not need to be restarted again  
something to do with the pi picking which audio device to output to (speculation)  
may or may not fix the sound not playing. (:  
when the inside button is pressed, the lock will change  
the inside button was originally intended to be a button for pairing bluetooth
