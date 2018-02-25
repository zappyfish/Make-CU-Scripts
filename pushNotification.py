from pyfcm import FCMNotification
import pyrebase
import ngrokURL
import pyrebase


def pushNote(alertType):

    config = {
      "apiKey": "AAAAqY_jUO4:APA91bEM9eW-WJ70a77GvPiQa1P-I_PI1VSFnJDe9aEJn84Cba0_WpsV0gEyLjwbra-wvCvJQthnttnDRBPbHiibaPhTDZGb6c6i5IIzMLlsFdA15fZ3QffSAjlb5kXERN88mKWkc56f",
      "authDomain": "hackharvard.firebaseapp.com",
      "databaseURL": "https://hackharvard-43aaa.firebaseio.com",
      "storageBucket": "gs://hackharvard-43aaa.appspot.com",
      "serviceAccount": "hackharvard-43aaa-firebase-adminsdk-wosvr-878ad8eafe.json"
    }
    firebase = pyrebase.initialize_app(config)
    import ngrokURL
    ngrokIP = ngrokURL.sendURL()
    firebase.database().child("url").push(ngrokIP)

    push_service = FCMNotification(api_key="AAAAqY_jUO4:APA91bEM9eW-WJ70a77GvPiQa1P-I_PI1VSFnJDe9aEJn84Cba0_WpsV0gEyLjwbra-wvCvJQthnttnDRBPbHiibaPhTDZGb6c6i5IIzMLlsFdA15fZ3QffSAjlb5kXERN88mKWkc56f")

    reg_id = firebase.database().child("reg_id").get().val()

    push_service = FCMNotification(api_key="AAAAqY_jUO4:APA91bEM9eW-WJ70a77GvPiQa1P-I_PI1VSFnJDe9aEJn84Cba0_WpsV0gEyLjwbra-wvCvJQthnttnDRBPbHiibaPhTDZGb6c6i5IIzMLlsFdA15fZ3QffSAjlb5kXERN88mKWkc56f")

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    registration_id = reg_id

    result = push_service.notify_single_device(registration_id=registration_id, message_title=alertType, message_body=alertType)

    # Send to multiple devices by passing a list of ids.

    print(result)

pushNote()
