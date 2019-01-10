# InventorySystem Backend

## Config
Currenty in `config.py`. Copy from template file `config.py.template`



## Run
````
# Deps
pip3 install -r requirements.txt

# Update Database
python3 migrate.py db upgrade

# Run Server
python3 run.py
````


## DB Migrate
````
# Run after changes to db models
python3 migrate.py db migrate

# And then update Database
python3 migrate.py db upgrade
````
