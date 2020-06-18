
#  high-pi

Simple script that tweets the local IPv4 Address of your Raspberry Pi on startup. This method requires you to set up an account with Twilio where you can find <a href="https://www.twilio.com/">here.</a>

> Note: Although the following is cost free, it is limited with the free trial tier from Twilio. You will get roughly 260 free texts based on my usage and testing.

  

#  Usage

### 1. Cloning repo
Firtly, clone the repo into a location of your choice. In the example below, it has been cloned into /home/pi/git/high-pi

<code> pi@raspberrypi ~ cd ~/git && git clone https://github.com/floeck/high-pi.git </code>
Also, whilst in the repo directory, run <code>chmod a+x script.py</code> to ensure the file can be executed in startup.
### 2. Setting up config
Now, copy the config.ini.example file and remove the example extension. Using your Twilio credentials, you can now populate the config file with your preferences. There is an option in there for a pi to have a name. To do this, simply set use to true and set a pi name. It is enabled by default.


```ini
[Twilio]
account_sid  = somerandombits
auth_token  = somemorerandombits
to_number  = +46564563465
from_number  = +37655865685
message  = Hey! My IP is:

[Optional]
use  = true
pi_name  = Fred
```

### 3. Setting up cron job
Create a cron job on your pi. This can be done by running the following command.

<code> pi@raspberrypi ~ crontab -e </code>

Now add the following line in the file opened.

<code> @reboot sleep 30 && cd /home/pi/git/high-pi && python3 script.py >> out.txt 2>&1 </code>

> You may need to tweak the delay depending on your pi as it is essential the pi is connected to a network prior to the script executing. You may opt for a systemctl service if you wish.

### 4. Reboot

It's all set now. Simply reboot by running <code> sudo reboot</code> and you should receive a text shortly after the pi boots of its local ip address. If you run into any problems, check the log file created in the script location.
