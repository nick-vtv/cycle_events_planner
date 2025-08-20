# Cycle Events Planner

My final exam django project for Python Web Django Advanced course.

Concept, design, back-end and front-end functionality developed by me.

#

Deployed and running @ Debian 12 + postgreSQL17 + Gunicorn + Nginx

Currently accessible at:

https://werewolf-open-aphid.ngrok-free.app/

#

DB credentials and Project secrets are loaded from separate .env file !

#

Quick description at: /about/

Authenticated users can Add, Edit, Delete own profiles. Accounts are not deleted, but set to NOT active.

Authenticated users can Add, Edit, Delete own bikes, and only Add and Edit own routes and events.

Comments are create and read-only.

Deletion of Routes, Events and Comments is possible only from Django Admin site with special Moderator group with delete permissions.

Anonymous users can view only Main page, Gallery and About sections.

Additional Gallery functionality is currently under development.
