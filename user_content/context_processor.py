from user_content.models import SiteUser


def profile_pic_address(request):
    user_id = request.user.id
    avatar_address = {}
    if user_id == None:
        return avatar_address
    get_profile_pic = SiteUser.objects.get(user_id=user_id)
    print("this is")

    if get_profile_pic.profile_pic != '':
        avatar_address['address'] = get_profile_pic.profile_pic
    else:
        avatar_address['address'] = '/profile_pics/default_avatar.png'
    print(avatar_address['address'])
    return avatar_address
