# Restart Triggers

Carrying out the actions below will cause the planner (engine) pods of all active clusters to restart. Any running queries will be terminated.

1. When caching is enabled or disabled.
2. When the query timeout is enabled or disabled.
3. When query timeout values are changed (when timeout is enabled).
4. When a user is assigned or removed from a cluster.
5. When a new access token is created.
6. When an access token is revoked/deleted.

