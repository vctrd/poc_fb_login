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
                "fields": "caption,id,comments_count,like_count,media_type,media_product_type,media_url,permalink,thumbnail_url,timestamp"
            },
        )
        
        return self.instagram_medias
    
    
    def get_instagram_stories(self):
        """
        https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/stories
        
        
        Only one caption will be returned per Instagram story, even if more than one caption exists
        """
        
        
        if not self.instagram_account_id:
            self.get_first_instagram_account_id()

        self.instagram_stories = self._get(
            f"/{self.instagram_account_id}/stories",
            params={
                "fields": "id,media_type,media_url,permalink,thumbnail_url,timestamp"
            },
        )
        
        return self.instagram_stories
    
    
    def get_instagram_media_insights(self, media_id, metrics_list):

        return self._get(
            f"/{media_id}/insights",
            params={"metric": ",".join(metrics_list), "period": "lifetime"},
        )
        
    
