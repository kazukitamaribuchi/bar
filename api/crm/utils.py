import pytz

from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MSeat,
)

from .sub_models import (
    CardManagement,
    BottleManagement,
    SalesHeader,
    SalesDetail,
    # AttendanceManagement,
    BookingManagement,
)

import logging


logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')


logger = logging.getLogger(__name__)



def utc_to_jst(timestamp_utc):
    datetime_jst = timestamp_utc.astimezone(pytz.timezone('Asia/Tokyo'))
    return datetime_jst


def get_card_user(customer_no):
    """
    指定の会員Noのユーザーを返す。
    紐づいていなければNoneを返す。
    """
    try:
        res = MCustomer.objects.get(card__customer_no=customer_no)
    except MCustomer.DoesNotExist:
        logger.debug("ユーザーと紐づいていないカードです。")
        return None

    return res


def users_card(customer_no):
    """
    既にユーザーと紐づいているカードか
    """
    try:
        MCustomer.objects.get(card__customer_no=customer_no)
        logger.debug('既に他のユーザーと紐づいているカードです。')
        return True
    except MCustomer.DoesNotExist:
        return False


def other_users_card(custoner_no, my_no):
    """
    既に他のユーザーと紐づいているカードか
    """
    try:
        me = MCustomer.objects.get(pk=my_no)
    except MCustomer.DoesNotExist:
        logger.error('ユーザー情報が取得出来ません。')
        return False

    try:
        card_user = MCustomer.objects.get(card__customer_no=customer_no)
        if me != card_user:
            return True
    except MCustomer.DoesNotExist:
        pass
    finally:
        return False


def get_val_in_validated_data(key, data):
    if key in data:
        if data[key] == '':
            return None
        return data[key]
    return None
