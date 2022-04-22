This is a smiple web server used for demo purposes

# Installation

- Create python virtual environment with `python3 -m venv .venv`
- Activate environment with `source .venv/bin/activate`
- Install required libraries `pip install -r requirements.txt`

# Usage

To start the application run `APP_PORT=9090 python main.py ` and follow to the address [http://0.0.0.0:9090](http://0.0.0.0:9090)

# TODOs

## Legend

- (V) means steps that should be done by Vitalii
- (I) means steps that should be done by Illarion

## Necessary steps

- [x] (I)Create basic we server application
- [x] (I)Add some fancy bootstrap CSS :)
- [ ] (V)Copy repository to Vitalii's own public repo
- [ ] (V)Wrap application with docker container in a separate branch
- [ ] (V)Create pull request with docker and assign @ikhlestov to it
- [ ] (I)Add some linters and tests
- [ ] (V)Run linters automatically on every commit(you need some CI here)
- [ ] (V)Run test on pull requests only
- [ ] (I)Add some kind of database
