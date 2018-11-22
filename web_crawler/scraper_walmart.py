import requests
import json
from html.parser import HTMLParser

h = HTMLParser()
API_BASE_URL='http://api.walmartlabs.com/v1/'
API_KEY = '73qpnr7h9jbzgv48bjnpgy6v' # I don't want to publish my API key on github, if you need it just request it from me.


class WalmartException(Exception):
    """Base Class for Walmart Api Exceptions.
    """


class NoLinkShareIDException(WalmartException):
    """Exception thrown if no LinkShare ID was specified when creating the Walmart API instance
    """
    pass


class InvalidParameterException(WalmartException):
    """Exception thrown if an invalid parameter is passed to a function
    """
    pass


class InvalidRequestException(WalmartException):
    """Exception thrown if an invalid request response is return by Walmart
    """

    def __init__(self, status_code, **kwargs):
        error_message = 'Error'
        if status_code == 400:
            error_message = 'Bad Request'
            if 'detail' in kwargs:
                error_message = error_message + ' - ' + kwargs['detail']
        elif status_code == 403:
            error_message = 'Forbidden'
        elif status_code == 404:
            error_message = 'Wrong endpoint'
        elif status_code == 414:
            error_message = 'Request URI too long'
        elif status_code == 500:
            error_message = 'Internal Server Error'
        elif status_code == 502:
            error_message = 'Bad Gateway'
        elif status_code == 503:
            error_message = 'Service Unavailable/ API maintenance'
        elif status_code == 504:
            error_message = 'Gateway Timeout'
        message = '[Request failed] Walmart server answered with the following error: {0:s}. Status code: {1:d}'.format(error_message, status_code)
        super(self.__class__, self).__init__(message)
    pass


def search(query, **kwargs):
    """Search allows text search on the Walmart.com catalogue and returns matching items available for sale online.

    This implementation doesn't take into account the start parameter from the actual Walmart specification.
    Instead, we've abstracted the same concept to a paginated approach.
    You can specify which 'page' of results you get, according to the numItems you expect from every page.

    :param query:
        Search text - whitespace separated sequence of keywords to search for

    - Named params passed in kwargs:
        :param numItems [Optional]
            Number of matching items to be returned, max value 25. Default is 10.

        :param categoryId [Optional]
            Category id of the category for search within a category. This should match the id field from Taxonomy API

    :return:
        A list of :class:`~.WalmartProduct`.
    """

    url = API_BASE_URL + 'search'
    kwargs['query'] = query

    kwargs['start'] = 10+ 1

    kwargs.pop('page', None)
    data = _send_request(url, **kwargs).json()
    products = []

    if 'items' in data:
        for item in data["items"]:
            products.append(item)

    return products


def _send_request(url, **kwargs):
    """Sends a request to the Walmart API and return the HTTP response.

    Important remarks:
        - If the response's status code is differente than 200 or 201, raise an InvalidRequestException with the appripiate code
        - Format is json by default and cannot be changed through kwargs
        - Send richAttributes='true' by default. Can be set to 'false' through kwargs

    :param url:
        The endpoint url to make the request

    - Named params passed in kwargs can be any of the optional GET arguments specified in the Walmart specification
    """
    #Avoid format to be changed, always go for json
    kwargs.pop('format', None)
    request_params = {'apiKey':API_KEY,'format':'json'}
    for key, value in kwargs.items():
        request_params[key] = value


    #Even if not specified in arguments, send request with richAttributes='true' by default
    request_params['richAttributes']='true'

    r = requests.get(url, params=request_params)
    if r.status_code == 200 or r.status_code == 201:
        return r
    else:
        if r.status_code == 400:
            #Send exception detail when it is a 400 error
            raise InvalidRequestException(r.status_code, detail=r.json()['errors'][0]['message'])
        else:
            raise InvalidRequestException(r.status_code)
