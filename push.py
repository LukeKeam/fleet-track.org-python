import requests

"""
Please go to fleet-track.org to get your free token and auth_user id
"""
def post_to_server():
    try:
        token = "0000000000000000000000000000"  # fleet-track.org token 
        user_id = "Toyota"  # device name
        auth_user = "12423  # fleet-track.org auth_user
        utc = ""
        latitude = ""
        longitude = ""
        speed = ""
        vehicle_move_stop = ""
        vehicle_move_start = ""
        alert = ""
        # combined
        payload = '{{"user_id":"{0}", "auth_user":"{1}", "utc":"{2}" , "latitude":"{3}", "longitude":"{4}", ' \
                  '"speed":"{5}", "vehicle_move_stop":"{6}", "vehicle_move_start":"{7}", ' \
                  '"alert":"{8}"}}, '.format(user_id, auth_user, utc, latitude, longitude, speed, vehicle_move_stop,
                                             vehicle_move_start, alert)
        data_to_send = payload
        url = 'https://api.fleet-track.org/gps/'
        # send data
        ssn = requests.Session()

        # test
        headers = {'content-type': 'application/json', 'Authorization': 'Token {0}', 'user:Toyota'.format(token)}
        r = ssn.post(url, data=data_to_send, headers=headers)
        print("Status code", r.status_code)  # 200 is ok, 524 timeout, 400 bad request, 413 payload too large
        print('Posted and completed')
        print('')
        ssn.close()
    except Exception as e:
        print('post_to_server except', e)
