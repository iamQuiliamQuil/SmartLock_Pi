#! /bin/bash
find ~/Desktop/SmartLock_pi/Storage/Captures -mtime +7 -exec rm {} \;
#to make this work, you neeed to run "crontab -e", choose nano, 
#and add the line 
# 0 * * * * /bin/sh ~/Desktop/SmartLock_pi/Storage/remove_old_photos_cronjob.sh
# this deletes old photos at the start of every hour, which is excessive, 
# but reasonable given that the pi generaly only runs for a couple of hours a week. 

