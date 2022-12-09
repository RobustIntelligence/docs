# User Management


* RI Platform has a concept of users.
* Admins can create users, view users, and edit user roles from the members page under Organization Settings. 
* Users configured via OIDC only appear on the members page after the user logs in for the first time.
* Users created manually can also be logged into via SSO, providing their emails match. 

RIME has 3 kinds of users - 

### Admin User
* Each organization can have multiple admin user. 
* Admins can invite other users within their organization to their RIME workspace from
the "Members" page under "Organization Settings". 
* The admin will need to manually create the account details for these standard users.
The admin can manage the user's account access.
* The admin has ability to create, edit, and delete workspaces, see [Workspaces](/for_admins/how_to_guides/workspaces.md). 
* The admin has ability edit organization settings like (user management, managed agent setup, 
sso configuration, smtp configuration, data sources configuration) 
* Admins can manage all API tokens in a given workspace, see [API Access Tokens](/for_admins/how_to_guides/api-authentication.md).

### Standard User
* Standard users need to get their account details from their organization admin. 
* Standard users cannot view or edit organization level settings. 
* Standard users can access and use workspaces, see [Workspaces](/for_admins/how_to_guides/workspaces.md). 
* Standard users cannot edit any workspace level settings. 
* Standard users can create personal API tokens, see [API Access Tokens](/for_admins/how_to_guides/api-authentication.md). 


### Support User
* Admin users can create support accounts for the Robust Intelligence team 
to help with troubleshoot and guidance on how to use RIME. 
* Admin users need to provide support account details to the Robust Intelligence team.
* After the support user is created, they have the same permissions as admins. 
* Admin users can delete the support user to revoke access.  


