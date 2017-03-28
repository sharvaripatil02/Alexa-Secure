# Alexa-Secure
Using Amazon Eco (Alexa) to secure your homes

1. Now a days every house has a secure password which allows the owner to enter inside. But what if someone tries to enter into your house without the password.
2. The project is designed to use Amazon Echo (Alexa) to call and send an sms to the owner of the house if someone enters the house without the password.
3. I have designed a Arduino circuit which will act as a sensor or a switch which gets activated when there is an entry inside the house without the authenticated password.
4. The Arduino circuit when gets acitvated sends a signal which gets stored in Amazon AWS S3.
5. Amazon S3 will then trigger AWS Lambda function which will then call our custom skills designed for Alexa and then Alexa will call the registered user mobile number.
