def extract_media_info(apk_file):
    try:
        apk = APK(apk_file)
        print("App Information:")
        print("---------------")
        print("Package Name:", apk.get_package())
        print("App Name:", apk.get_app_name())
        print("Version Code:", apk.get_androidversion_code())
        print("Version Name:", apk.get_androidversion_name())
        print("\nMedia and Entertainment Features:")
        print("---------------------------------")
        media_features = []
        for activity in apk.get_activities():
            if "media" in activity or "entertainment" in activity:
                media_features.append(activity)
        for service in apk.get_services():
            if "media" in service or "entertainment" in service:
                media_features.append(service)
        if media_features:
            for feature in media_features:
                print("-", feature)
        else:
            print("No media and entertainment features found.")
    except Exception as e:
        print("Error:", str(e))

def main():
    apk_file = input("Enter APK file path: ")
    extract_media_info(apk_file)

if _name_ == "_main_":
    main()
```
