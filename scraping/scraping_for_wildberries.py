import requests

from scraping import constants


def get_info_goods(article):
    data = requests.get(constants.WB_CARD_URL.format(article),
                        headers=constants.HEADERS)
    data = data.json()
    output_data = {}
    try:
        output_data.update({
            'name': data['data']['products'][0]['name'],
            'goods_id': data['data']['products'][0]['id'],
            'root_id': data['data']['products'][0]['root'],
            'price': '{:.2f} руб'.format(
                data['data']['products'][0]['extended']['clientPriceU'] / 100)
        })
    except IndexError:
        return None
    return output_data


def _get_reviews_goods(url):
    data = requests.get(url, headers=constants.HEADERS)
    data = data.json()
    feedbacks = data['feedbacks']
    output_data = []
    if feedbacks:
        for feedback in feedbacks:
            output_data.append({
                'name': feedback['wbUserDetails']['name'],
                'country': feedback['wbUserDetails']['country'],
                'text_reviews': feedback['text'],
                'rating': feedback['productValuation']
            })
        return output_data


def get_url(root=None):
    if not _get_reviews_goods(constants.WB_REVIEWS_URL_2.format(root)):
        return _get_reviews_goods(constants.WB_REVIEWS_URL_1.format(root))
    return _get_reviews_goods(constants.WB_REVIEWS_URL_2.format(root))
