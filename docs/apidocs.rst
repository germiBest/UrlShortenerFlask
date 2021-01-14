#################
API Documentation
#################


Endpoints
----------------------

* /api/v1/get_domain
* /api/v1/<api_key>

/api/v1/get_domain (Get)
""""""""""""""""""""""""
Params
******************
Empty

Response
******************
* domain - url for the site

Example::

	{ "domain": "http://127.0.0.1:5000/" }


/api/v1/<api_key> (Get)
"""""""""""""""""""""""
Params
******************
* api_key - required parameter, passed in path

Response
******************
* short - url of shorted link
* long - url to original link
* expired - unix timestamp format date, when url will be expired

Example::

	[
		{
			"expired": 1612216800,
			"long": "https://github.com/",
			"short": "8eNb"
		},
		{
			"expired": 1612216800,
			"long": "https://google.com/",
			"short": "5bUi"
		}
	]

/api/v1/<api_key> (Post)
""""""""""""""""""""""""
Params
**********
* api_key - required parameter, passed in path
* link - required parametr, passed in body
* expired - pararmetr, passed in body, must be from 1 to 365, default is 90
* type - if passed "relative" response returns relative path to redirect url

Response
**********
* short - url of shorted link
* long - url to original link
* expired - unix timestamp format date, when url will be expired

Example::

	
	{
		"expired": 1612216800,
		"long": "https://github.com/",
		"short": "8eNb"
	}

