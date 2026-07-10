def add_setting(settings:dict, data:tuple):
    key, value = data
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings.update([(key,value)])
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings:dict, data:tuple):
    key, value = data
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings.update([(key,value)])
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings:dict):
    if not settings.items():
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        result += "\n".join(f"{key.capitalize()}: {value}" for key, value in settings.items())
        result += "\n"
        return result

if __name__ == "__main__":
    test_settings  = {'Theme':'dark', 'Notifications':'enabled', 'Volume':'high'}
    print(add_setting(settings={'name':'notName', 'age':34, 'username':'johndoe'}, data=('username', 'johndoe')))
    print(update_setting(settings=test_settings, data=('Theme', 'light')))
    print(delete_setting(settings=test_settings, key='age'))
    print(view_settings(settings=test_settings))