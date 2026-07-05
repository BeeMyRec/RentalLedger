# === Stage 34: Add support for multiple local user profiles ===
# Project: RentalLedger
class UserProfilesManager:
    def __init__(self, storage_path="profiles"):
        self.storage_path = storage_path
        self.profiles = {}
    
    def load_profiles(self):
        import os
        if not os.path.exists(self.storage_path):
            return
        for filename in os.listdir(self.storage_path):
            if filename.endswith(".json"):
                filepath = os.path.join(self.storage_path, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        self.profiles[data["name"]] = {
                            "username": data.get("username"),
                            "password_hash": data.get("password_hash"),
                            "permissions": data.get("permissions", ["read"])
                        }
                except (json.JSONDecodeError, IOError):
                    continue
    
    def save_profile(self, name, username, password_hash, permissions=None):
        import os
        if not permissions:
            permissions = ["read"]
        profile_data = {
            "name": name,
            "username": username,
            "password_hash": password_hash,
            "permissions": permissions
        }
        filepath = os.path.join(self.storage_path, f"{name}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(profile_data, f, indent=2)
    
    def authenticate(self, username, password):
        import hashlib
        for profile in self.profiles.values():
            if profile["username"] == username and profile["password_hash"] == hashlib.sha256(password.encode()).hexdigest():
                return True
        return False
    
    def get_profile_permissions(self, username):
        for profile in self.profiles.values():
            if profile["username"] == username:
                return profile.get("permissions", [])
        return []
