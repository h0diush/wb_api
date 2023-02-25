import datetime as dt

import requests

from scraping import constants


class GetReviewsProduct:
    URLS = [constants.WB_REVIEWS_URL_1, constants.WB_REVIEWS_URL_2]

    def get_info_goods(self, article):
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
                    data['data']['products'][0]['extended'][
                        'clientPriceU'] / 100)
            })
        except KeyError:
            output_data.update({
                'name': data['data']['products'][0]['name'],
                'goods_id': data['data']['products'][0]['id'],
                'root_id': data['data']['products'][0]['root'],
                'price': '{:.2f} руб'.format(
                    data['data']['products'][0]['salePriceU'] / 100)
            })
        except IndexError:
            return None
        return output_data

    def _get_reviews_url(self, url):
        output_data = []
        data = requests.get(url, headers=constants.HEADERS)
        data = data.json()
        feedbacks = data['feedbacks']
        if feedbacks:
            for feedback in feedbacks:
                if feedback['createdDate'].split('-')[0] == str(
                        dt.datetime.now().year):
                    output_data.append({
                        'author': feedback['wbUserDetails']['name'],
                        'country': feedback['wbUserDetails']['country'],
                        'text': feedback['text'],
                        'rating': feedback['productValuation']
                    })
            return output_data

    def get_reviews_data(self, root_id):
        results = []
        for url in self.URLS:
            url_data = self._get_reviews_url(url.format(
                root_id
            ))
            if url_data is not None:
                results.extend(url_data)
        return results
