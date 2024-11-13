#### Existing API available

- [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) : deprecated on Dec 4, 2024
- [Instagram API with Instagram Login](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login) : only for businesses / creators, no insights access but doesnt require facebook account
- [Instagram API with Facebook Login](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login): only for businesses / creators, require a linked facebook page to the instagram account


#### Rate limit
200 calls per hour times the number of users

#### Permissions
`instagram_basic` and `pages_show_list` are enough to list instagram accounts (not yet insights)

[full permissions reference](https://developers.facebook.com/docs/permissions)


#### Current features

- listing user insights and medias for a business instagram account linked to a business page
- login via facebook


#### local setup

You need a .env file see .env_sample for the needed variables

##### with `uv`

```
uv sync
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```

#### with `pip`
- you need a virtual environment with python 3.12 (you can use pyenv)
then

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```