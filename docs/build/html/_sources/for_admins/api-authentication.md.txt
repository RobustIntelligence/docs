# API access tokens 

Access tokens authorize a user account to issue calls to the RI Platform REST API or Python SDK. API Access Tokens are tied to a specific [workspace](workspaces.md) and [user](users.md). Users with the Organizaton administrator [role](userroles.md) manage API access tokens for all user accounts that are members of a workspace. By default, an API access token is assigned to "Workspace 1" and the default administrator account. An RI Platform instance can have a maximum of 200 API access tokens across all workspaces. API access tokens expire 270 days after creation. 

## Generating an API access token.

1.  Sign in to a user account.  
    >   The Workspaces page appears.
2.  Select a workspace.
    >   The workspace summary page appears.
3.  Click the *Settings* icon in the lower left corner.
    >   The Workspace Settings page appears.
4.  Click *API Access Tokens*.
    >   The API Access Tokens pane appears.
5.  In *Token Name*, type a name for the API access token then click *Create Token*.
    >   A confirmation dialog box appears.
6.  Click the Copy to Clipboard icon at the right of the text field that displays the token.
    >   The API access token is copied to the system clipboard.
7.  Paste the API access token into a document for future reference.
    >   As a best practice, keep this document secure.

<!--img src="../_static/api-access-tokens.png"-->
## Authenticating to the SDK with the API token

The API token must be passed with each request to the REST API. The method used varies depending on the API access method used.

### Using the SDK

Import the SDK with `import rime`, assign the value of the token to the `API_TOKEN` variable, and initialize the client with the `Client(`*cluster_url*`, API_TOKEN)` call. Replace `cluster_url` with the URI of the API call. Sample request:

```
API_TOKEN = '' # value of the API access token 
CLUSTER_URL = '' # dedicated domain of RI Platform instance, such as rime.stable.rime.dev)
rime_client = Client(CLUSTER_URL, API_TOKEN)

project = rime_client.create_project(name='Fraud Demo', description='This is an Onboarding Demo')
```

### Using the Python requests API

When the Robust Intelligence SDK is unavailable in a specific environment, construct requests using the standard Python requests library. Sample request:

```
headers = {"rime-api-key": PASTE_API_KEY here}

# CREATE A PROJECT
body = {
    "name": "new",
    "description": "for rest testing"
}
res = requests.post("https://rime.latest.rime.dev/projects", json=body, headers=headers)
```

### Using the `curl` utility

You can make REST API calls directly from the command line with the `curl` utility.