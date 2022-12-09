# User Management


* RI Platform now has a concept of users.
* Admins can create users, view users, and edit user roles from the members page. 
* Users configured via OIDC only appear on the members page after the user logs in for the first time.
* Users created manually can also be logged into via SSO, providing their emails match. 

RIME has 3 kinds of users - 
#### Admin User
   * Each RIME Cloud organization can have multiple admin user. 
   * Admins can invite other users within their organization to their RIME workspace from
   the "Members" page under "Workspace Settings". See the below image.
   * The admin will need to manually create the account details for these standard users.
   The admin can manage the user's account access.
   * The admin has the ability to create and delete API Access tokens for RIME APIs. 
   

#### Standard User
   * Standard users need to get their account details from their organization admin. 
   * Standard users have the same permissions as admins, except for 3 scenarios -
       * Standard users do not have access to the members page and account management. 
       * Standard users can create API tokens but not delete API tokens.
       * Standard users cannot configure SSO or SMTP settings. 

#### Support User
   * Admin users can create support accounts for the Robust Intelligence team 
to help with troubleshoot and guidance on how to use RIME. 
   * Admin users need to provide support account details to the Robust Intelligence team.
   * After the support user is created, they have the same permissions as admins. 
   * Admin users can delete the support user to revoke access.  


<img src="../../_static/user-management.png">