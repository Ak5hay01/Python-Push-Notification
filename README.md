# PythonPushNotification
Notification can be sent to any Android or iOS device using Firebase and pyfcm. You need to create an account on firebase console, enable GCM, and get the server key for authentication on the python server. On Android or iOS devices get the token(Unique identification key for that particular device). Send that key to the server-side in the background for initiating push notification to the device from python backend. 

On the server-side, you need to install pyfcm using pip.  

pip install pyfcm  

OR  

pip install git+https://github.com/olucurious/PyFCM.git  

Here is the documentation: https://pypi.org/project/pyfcm/  

You can send a notification to a single device as well as to multiple devices at the same time just you must have the token or registration id from Android or iOS device. You can manage title, body, color, icon, and many more things of the notification. 
