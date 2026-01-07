from server import *
import requests
import platform

device = platform.system()

def two_factor_authentication(user, status):
    try:
        db.collection("users").document(user).collection("options").document("config").set({
            '2fa_status' : status
        }, merge=True)
        print(f"Hit : 2FA-STATUS = [{status}] for user=[{user}]")
    except Exception as error:
        print(f'Error : {error}')


def verified_badge_status(user, status):
    try:
        db.collection("users").document(user).update({
            'verified_badge' : status
        })
        print(f'HIt : verification_badge_status = [{status}] for user = [{user}]')
    except Exception as error  : 
        print(f"Error : {error}")

def get_verified_badge_status(user):
    try:
        doc = db.collection("users").document(user).get()
        if doc.exists:
            return doc.to_dict().get('verified_badge', False)
        return False
    except Exception as error:
        print(f'Error : {error}')
        return False

def get_2fa_status(user):
    try:
        doc = db.collection("users").document(user).collection("options").document("config").get()
        if doc.exists:
            return doc.to_dict().get('2fa_status', False)
        return False
    except Exception as error:
        print(f'Error : {error}')
        return False

def block(user, friend):
    try:
        db.collection("users").document(user).collection("block_list").document(friend).set({
            'username' : friend
        })
        print(f'Hit : {user} blocked {friend}')
    except Exception as error:
        print(f'Error : {error}')

def fetch_block_list(user):
    try:
        user_ref = db.collection("users").document(user).collection("block_list").stream()
        block_list = []
        for block in user_ref:
            block_list.append(block.to_dict()['username'])
        return block_list
    except Exception as error:
        print(f'Error : {error}')
        return False

def unblock(user, friend):
    try:
        db.collection("users").document(user).collection("block_list").document(friend).delete()
        print(f'Hit : {user} unblocked {friend}')
    except Exception as error:
        print(f'Error : {error}')

def push_new_session_notification(user, user_agent=None):
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        ip = data['ip']
        
        device_type = device
        if user_agent:
            ua = user_agent.lower()
            if 'mobile' in ua: device_type = "Mobile"
            elif 'tablet' in ua or 'ipad' in ua: device_type = "Tablet"
            else: device_type = "Desktop"
            
            if 'android' in ua: device_type += " (Android)"
            elif 'iphone' in ua: device_type += " (iPhone)"
            elif 'ipad' in ua: device_type += " (iPad)"
            elif 'windows' in ua: device_type += " (Windows)"
            elif 'macintosh' in ua or 'mac os' in ua: device_type += " (Mac)"
            elif 'linux' in ua: device_type += " (Linux)"

        user_ref = db.collection("users").document(user).collection("sessions").add({
            'device' : device_type,
            'location' : data['city'] + ', ' + data['region'] + ', ' + data['country'],
            'coordinates' : data['loc'],
            'ip' : data['ip'],
            'time' : firestore.SERVER_TIMESTAMP
        })
        print(f"new seesion add to session_list ofr {user}")
        security_message = f"New session found on {device_type} at {data['city']}, {data['region']}, {data['country']}"
        push_security_notification(user, security_message)
        print(f'security_notification added succesfully to {user}')
    except Exception as error:
        print(f'Error : {error}')

def fetch_sessions(user):
    try:
        user_ref = db.collection("users").document(user).collection("sessions").stream()
        session_list = []
        for session in user_ref:
            data = session.to_dict()
            if data.get('time'):
                data['time'] = data['time'].strftime("%d-%B-%Y %H:%M")
            session_list.append(data)
        print(f"session list fetched for {user}")
        return session_list
    except Exception as error:
        print(f'Error : {error}')
        return False

def change_password(user, old_password, new_password):
    try:
        user_ref = db.collection("users").document(user)
        user_doc = user_ref.get()
        if user_doc.exists:
            user_data = user_doc.to_dict()
            if user_data.get('password') == old_password:
                user_ref.update({
                    'password' : new_password
                })
                print(f"password updated for {user}")
                push_security_notification(user, f"Hit : Password Updated")
                return True
            else:
                return False
        else:
            return False
    except Exception as error:
        print(f'Error : {error}')
        return False

def account_delete(user):
    try:
        user_ref = db.collection("users").document(user)
        user_ref.delete()
        print(f"Success : account deleted for {user}")
    except Exception as error:
        print(f'Error : {error}')

def update_username(user, new_username):
    try:
        user_ref = db.collection("users").document(user)
        if is_new_username(new_username):
            user_ref.update({
                'username' : new_username
            })
            return {'Success' : 'Username updated successfully.'}
        else:
            print(f'Error : Username already exists')
            return {'Error' : 'Username already exists.'}
    except Exception as error:
        print(f'Error : {error}')
        return {'Error': str(error)}
    
def update_email(user, new_email):
    try:
        user_ref = db.collection("users").document(user)
        if is_new_email(new_email):
            user_ref.update({
                'email' : new_email
            })
            return {'Success' : 'Email updated successfully.'}
        else:
            print(f'Error : Email already exists')
            return {'Error' : 'Email already exists.'}
    except Exception as error:
        print(f'Error : {error}')
        return {'Error': str(error)}
    

def update_name(user, new_name):
    try:
        user_ref = db.collection("users").document(user)
        user_ref.update({
            'name' : new_name
        })
        print(f"Success : name updated for {user}")
        return {'Success' : 'Name updated successfully.'}
    except Exception as error:
        print(f'Error : {error}')
        return {'Error': str(error)}
    
def update_bio(user, new_bio):
    try:
        user_ref = db.collection("users").document(user)
        user_ref.update({
            'bio' : new_bio
        })
        print(f"Success : bio updated for {user}")
        return {'Success' : 'Bio updated successfully.'}
    except Exception as error:
        print(f'Error : {error}')
        return {'Error': str(error)}
    
def update_login_key(user, new_login_key):
    try:
        user_ref = db.collection("users").document(user)
        user_ref.update({
            'login_key' : new_login_key
        })
        print(f"Success : login_key updated for {user}")
        return {'Success' : 'login_key updated successfully.'}
    except Exception as error:
        print(f'Error : {error}')
        return {'Error': str(error)}
    




        