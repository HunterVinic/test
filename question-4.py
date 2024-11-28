from androguard.core.bytecodes.apk import APK

class APKAnalyzer:
    def __init__(self, apk_path):
        self.apk = APK(apk_path)

    def get_metadata(self):
        return {
            "package_name": self.apk.package,
            "version_name": self.apk.version_name,
            "version_code": self.apk.version_code,
            "permissions": self.apk.get_permissions()
        }

if __name__ == "__main__":
    analyzer = APKAnalyzer("path/to/app.apk")
    metadata = analyzer.get_metadata()
    print("APK Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
