import pytz

from .models import (
    MCustomer,
    MCast,
    MRank,
    MTax,
    MProduct,
    MSeat,
    MSetting,
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


def update_customer_rank(customer, sales):
    NORMAL_BOTTOM_LINE = 0
    NORMAL_TOP_LINE = 2999999
    GOLD_BOTTOM_LINE = 3000000
    GOLD_TOP_LINE = 6999999
    PLATINUM_BOTTOM_LINE = 7000000
    PLATINUM_TOP_LINE = 9999999
    BLACK_BOTTOM_LINE = 10000000

    if NORMAL_BOTTOM_LINE <= sales <= NORMAL_BOTTOM_LINE:
        pass
    elif GOLD_BOTTOM_LINE <= sales <= GOLD_TOP_LINE:
        if customer.rank.id != 2:
            try:
                rank = MRank.objects.get(pk=2)
            except MRank.DoesNotExist:
                logger.error('顧客のランク更新時、ランクの取得に失敗しました。')
            customer.rank = rank
            customer.save()
    elif PLATINUM_BOTTOM_LINE <= sales <= PLATINUM_TOP_LINE:
        if customer.rank.id != 3:
            try:
                rank = MRank.objects.get(pk=3)
            except MRank.DoesNotExist:
                logger.error('顧客のランク更新時、ランクの取得に失敗しました。')
            customer.rank = rank
            customer.save()
    elif BLACK_BOTTOM_LINE <= sales:
        if customer.rank.id != 4:
            try:
                rank = MRank.objects.get(pk=4)
            except MRank.DoesNotExist:
                logger.error('顧客のランク更新時、ランクの取得に失敗しました。')
            customer.rank = rank
            customer.save()

def get_setting():
    return MSetting.objects.first()

def get_sales_separate_time():
    return MSetting.objects.first().sales_separate_time
