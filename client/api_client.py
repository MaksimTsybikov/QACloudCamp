import requests


class APIHandler:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/posts/"

    def get_posts(self, params):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.get(self.base_url, headers=headers, params=params)
        return response

    def get_posts_with_id(self, post_id):
        url = self.base_url + f"/{post_id}"
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.get(url, headers=headers)
        return response

    def post_posts(self, params):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(self.base_url, headers=headers, params=params)
        return response

    def delete_posts_with_id(self, post_id):
        url = self.base_url + f"/{post_id}"
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.delete(url, headers=headers)
        return response

    def delete_posts_with_params(self, params):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.delete(self.base_url, headers=headers, params=params)
        return response
