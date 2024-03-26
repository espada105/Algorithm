def solution(phone_number):
    new_num = (len(phone_number)-4) * "*" + phone_number[-4:]
    return new_num