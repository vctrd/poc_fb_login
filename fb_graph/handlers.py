import os

import requests


BASE_URL = f"https://graph.facebook.com/{os.getenv('FACEBOOK_API_VERSION', 'v21.0')}"


class FacebookGraphAPIHandler:
    accounts = None
    instagram_account_id = None

    def __init__(self, access_token):
        self.access_token = access_token

    def _get(self, endpoint, params=None):
        response = requests.get(
            BASE_URL + endpoint,
            params={
                "access_token": self.access_token,
                **(params or {}),
            },
        )
        return response.json()

    def list_pages(self):
        self.accounts = self._get("/me/accounts")["data"]

        return self.accounts

    def get_first_instagram_account_id(self):
        if not self.accounts:
            self.list_pages()

        for account in self.accounts:
            if result := self._get(
                f"/{account['id']}", params={"fields": "instagram_business_account"}
            ).get("instagram_business_account"):
                self.page = account
                self.instagram_account_id = result["id"]
                return self.instagram_account_id

    def get_instagram_data(self):
        if not self.instagram_account_id:
            self.get_first_instagram_account_id()

        self.instagram_data = self._get(
            f"/{self.instagram_account_id}",
            params={
                "fields": "followers_count,media_count,name,profile_picture_url,username,website"
            },
        )
        return self.instagram_data

    def get_instagram_insights(self):
        if not self.instagram_account_id:
            self.get_first_instagram_account_id()

        self.instagram_insights = self._get(
            f"/{self.instagram_account_id}/insights",
            params={"metric": "impressions,reach", "period": "day"},
        )
        return self.instagram_insights

    def get_instagram_medias(self):
        if not self.instagram_account_id:
            self.get_first_instagram_account_id()

        self.instagram_medias = self._get(
            f"/{self.instagram_account_id}/media",
            params={
                "fields": "caption,id,comments_count,like_count,media_type,media_url,permalink,thumbnail_url,timestamp"
            },
        )
