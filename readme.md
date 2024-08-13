# El Fisherman

A script or service to fetch a Twitch stream using your credentials and, if you have a subscription or Twitch Turbo, save the current stream without ads or interruptions. The service could wait until the stream is live and then record it, continuing to wait for new streams from the selected user.

requeriments
https://streamlink.github.io/install.html#windows


## .env
a dotEnv file is needed to use this program.

the following data and .env file vars is nedded.

CLIENT_ID='your-client-id'
AUTH='Bearer your-auth-data'
CLIENT_SECRET='client-secret'
OAUTH = 'oauth-secret-from-twtich-page'
USER_LOGIN = 'user-name-from-twitch'

to get the Oath from twitch page you could get it from this javascript line in the developer console.:

```javascript
document.cookie.split("; ").find(item=>item.startsWith("auth-token="))?.split("=")[1]
```

## Docker Containers! 

if you have Docker installed you could run a docker container

### requirements
- Docker Desktop
- Vscode
- vscode Remote Connection plugin



