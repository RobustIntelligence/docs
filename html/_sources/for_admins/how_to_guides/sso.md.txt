# SSO Configuration

* An Admin User can configure SSO to integrate with an external identity provider.
  Currently, only OIDC is supported as an authentication mechanism.
* To set up SSO, an Admin simply needs to navigate to SSO Configuration under Workspace settings. You will need to provide the Client ID, Client Secret, and Issuer URL.
* You will also need to add `https://rime.<domain>/v1/auth/oidc/callback` as a callback url for your provider.
* Users can login via basic authN service or SSO. Admin operations need to be performed via basic authN login.

<img src="../../_static/sso_configuration.png">