# Hi
Hi! This Code was gets data from MQTT or Firebase and sends between each other\
May The Force Be With Us

## Installation
Dont forget setup the mosqiutto broker.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
sudo pip3 install paho-mqtt
sudo pip3 install firebase-admin
```

## Setting IP adress
Open "ip.json" and change "ip" with your mosquitto address or write another broker address
```json
{
    "ip": "172.22.222.27"
}
```
## Setting Firebase credentials
Download Service account key from Firebase and change "Login.json" with yours. (you can just change name of the new file with "Login.json")
```json
{
  "type": "service_account",
  "project_id": "dene-sdsd1066c",
  "private_key_id": "fb12fsdsadd4a9c02e5523c1427cf55397543745f8143c",
  "private_key": "This ones are just example",
  "client_email": "firebase-adminsdk-tgf8j@dene-1066c.iam.gserviceaccount.com",
  "client_id": "111946142960asdasd348508209",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-tgf8j%40dene-1066c.iam.gserviceaccount.com"
}
```
## Video (just TR language)
https://youtu.be/xCU33UL0WIs
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
