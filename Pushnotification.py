from pyfcm import FCMNotification

push_service = FCMNotification(api_key="Server Api KEY under cloud messaging on Firebase console")

# OR initialize with proxies

# proxy_dict = {
#           "http"  : "http://127.0.0.1",
#           "https" : "http://127.0.0.1",
#         }
# push_service = FCMNotification(api_key="Server Api KEY under cloud messaging on Firebase console", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging


# -------------------------------------Single device--------------------------------------------------

 registration_id = "Device registration_id / token generated on Android and iOS device."
 message_title = "Test Notification"
 message_body = "Hi Akshay, your customized news for today is ready"
 result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

 print(result)
# --------------------------------------End Single device -----------------------------------------

# Send to multiple devices by passing a list of ids.

registration_id1 = "Device registration_id / token generated on Android and iOS device."
registration_id2 = "Device registration_id / token generated on Android and iOS device."

registration_ids = [registration_id1, registration_id2]
message_title = "Test Multiple Notification"
message_body = "Hi, Akshay has completed his given Assignment..."
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title,
                                              message_body=message_body, color="#008000")

print(result)

