# Automated-Study-Table-
We generally forget to switch of the table lamp after getting up from the study table, this project automates the switching off and on process.

This project uses a raspberryPi 3 connected to a relay and ultrasonic sensor. The working is simple, when the ultrasonic sensor detects someoone sitting on the chair, it switches the table lamp on using the relay models and keeps checking if the person gets off the chair, the Pi puts the relay to off.

This can be further expanded to IOT by sending the time stamps to THingSpeak API
