# Role-based Access Control

Role-based Access Control (RBAC) restricts the actions that an authenticated
user can perform on the RI Platform. These restrictions are mediated by user
[roles](userroles.md).

## Assigning user privileges

1.  Sign in to a user account that has administrative privileges for an RI
    Platform instance or a workspace in that instance.  
    >    The Workspaces page appears.
2.  Click the *Settings* icon in the lower left.  
    >    The Organization Settings page appears.
3.  Click *Members*.
    >   The Members pane appears.
4.  Click the three-dot icon at the right of a user and select *Edit*.
    >   The *Edit Member* dialog box appears.
5.  From the *Role* drop-down, select a new role for the user account.
6.  Click *Save*.

The user account privilege level is now changed.

## Granting a user membership in a workspace

User accounts must have the Organization administrator or Workspace administrator
role to grant an existing user membership in a workspace.

User accounts configured to use [Single Sign-on (SSO)](sso.md) cannot be assigned membership
in a workspace before logging in with SSO once.

1.  Sign in to a user account that has administrative privileges for a
    workspace.  
    >    The Workspaces page appears.
2.  Click a workspace.
    >   The summary page for the workspace appears.
3.  Click the *Settings* icon in the lower left.  
    >    The Workspace Settings page appears.
4.  Click *Members*.
    >   The Members pane appears.
5.  Click *Add New Member*.
    >   The Add New Member dialog box appears.
6.  In *Name*, type the username of an existing user account.
    >   The list of user accounts is filtered by the typed string.
7.  Select a user from the filtered list and click *Add*.
    >   Repeat the previous two steps to add more users.
8.  Click *Done*.

The selected users now have the Workspace user role in addition to any
previous roles.

## Removing a user from a workspace

1.  Sign in to a user account that has administrative privileges for a
    workspace.  
    >    The Workspaces page appears.
2.  Click a workspace.
    >   The summary page for the workspace appears.
3.  Click the *Settings* icon in the lower left.  
    >    The Workspace Settings page appears.
4.  Click *Members*.
    >   The Members pane appears.
5.  Select *Remove* from the three-dot menu at the right of a listed user.
    >   A confirmation dialog box appears.
6.  Click *Remove Member*.

The user is no longer a member of the workspace.