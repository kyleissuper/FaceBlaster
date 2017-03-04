# Automatically send Facebook messages

```python
from FaceBlaster import FaceBlaster

F = FaceBlaster()
print F.send_message(
    "user1234",     # exact Facebook username
    "Hello!"        # message to send
    )               # returns success/failure message
F.close()
```

Requires selenium (`pip install selenium`), and driver may need some configuration. Tested and works on MacOS with Google Chrome.

## Mass-messaging

I know that some people send messages to all the people who react to their FB posts, so there's a built-in method for that. Otherwise, you can just iterate through any list of usernames that you have.

```python
from FaceBlaster import FaceBlaster

F = FaceBlaster()
contacts = F.get_userids_from_post()
for contact in contacts:
    print F.send_message(
        contact,        # exact Facebook username
        "Hello!"        # message to send
        )               # returns success/failure message
F.close()
```

## Can I run this in the background?

No, this is just meant to make life a little bit easier :)
