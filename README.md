# flask_gcp_wand
Python flask library on GCP - mainly on GAE.

## Version

Now version `0.1.*` is alpha version.

In the future, release `0.2.*` beta version

## Install

```
$ pip install flask_gcp_wand
```

## Introduction

### Flask app initialize
```
from flask_gcp_wand.appengine import create_gae_flask_app

app = create_gae_flask_app(__name__)
```

#### Add simple error handler
```
from flask_gcp_wand.appengine import register_simple_error_handler

~~

register_simple_error_handler(app)
```

### AppEngine Env Variables

```
from flask_gcp_wand.appengine.env import GaeEnv
from flask import current_app

if GaeEnv.is_gae():
    current_app.logger.debug(f'instance:{GaeEnv.gae_instance}')
else:
    current_app.logger.debug('is not GAE')
```

### PubSub

#### Publisher

```
from flask_gcp_wand.pubsub import Publisher
from flask_gcp_wand.model.message import Message


message = Message(payload, attributes)

with Publisher() as p:
    p.publish(topic, message)
```

#### Subscriber

```
from flask_gcp_wand.pubsub import Subscriber
from flask_gcp_wand.model.message import PushMessage

@app.route('/receive/push')
def push():
    message = PushMessage()
    current_app.logger.debug({'message_id': message.message_id, 'payload': message.payload, 'attributes': message.attributes})

def pull():
    sub = Subscriber(subscription_path)
    for message in sub.pull_gen():
        current_app.logger.debug({'message_id': message.message_id, 'payload': message.payload, 'attributes': message.attributes})
        sub.ack_pool(message.ack_id)
```

### Decorator

```
from flask_gcp_wand.decorator import only_cloud_scheduler_for_gae_http

@app.route('/batch/sample')
@only_cloud_scheduler_for_gae_http
def batch():
    ~~
```


