# dhis2-api-testing

[![Build Status](https://travis-ci.org/dhis2/dhis2-api-testing.svg)](https://travis-ci.org/dhis2/dhis2-api-testing)

### Install dependencies
```sh
pip install -r requirements.txt
```

### Run the tests
```sh
python runtests.py config.file
#or
./runtests.py config.file
```
config.file will default to apitests.default. Otherwise, it should be configured to point to the server of your choice with the proper details.
