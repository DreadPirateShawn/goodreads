import requests
import xmltodict
import json


class GoodreadsRequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class GoodreadsRequest():
    def __init__(self, client, path, query_dict, req_format='xml', force_list=None):
        """Initialize request object."""
        self.params = query_dict
        self.params.update(client.query_dict)
        self.host = client.base_url
        self.path = path
        self.req_format = req_format
        self.force_list = force_list

    def request(self):
        resp = requests.get(self.host+self.path, params=self.params)
        if resp.status_code != 200:
            raise GoodreadsRequestException(resp.reason, self.path)
        if self.req_format == 'xml':
            # XML spec does not disambiguate "always single child" vs "list that happens to be a single item".
            # For cases where a list is expected, pass param like "force_list={'review'}" to GoodreadsRequst.
            # Reference: https://stackoverflow.com/questions/37207353/xmltodict-does-not-return-a-list-for-one-element
            data_dict = xmltodict.parse(resp.content, force_list=self.force_list)
            return data_dict['GoodreadsResponse']
        elif self.req_format == 'json':
            return json.loads(resp.content)
        else:
            raise Exception("Invalid format")
