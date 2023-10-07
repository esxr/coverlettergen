import os
from flask import Flask
 

def create_app(config_overrides=None): 
   app = Flask(__name__, static_folder='app', static_url_path="/") 
 
   app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite")
   if config_overrides: 
       app.config.update(config_overrides)
 
   # Register the blueprints 
   from server.routes import api 
   app.register_blueprint(api) 
 
   return app
