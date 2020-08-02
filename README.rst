Flask
=====

Simple Library to use Flask on Google Cloud Platform - mainly AppEngine.


Documentation
-------------

Please read README on Github.

Requirements
------------

This Library don't specify google libraries.
If you need, install it yourself.


A Simple Example
----------------

.. code-block:: python

    from flask_gcp_wand.gae import create_gae_flask_app

    """
    Instead of "app = Flask(__name__)"
    Flask(__name__) is executed in create_gae_flask_app
    Automatically setup to use Cloud Logging.
    """
    app = create_gae_flask_app(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"



Links
-----

* Code: https://github.com/skxeve/flask_gcp_wand
* Issue tracker: https://github.com/skxeve/flask_gcp_wand/issues
