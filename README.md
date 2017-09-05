# gov-api

RESTful mash-up of [unitedstates/congress-legislators](https://github.com/unitedstates/congress-legislators) and Twitter.

See: [gov.vonapp.co](https://gov.vonapp.co/api/spec/)

## Endpoints

### admin

GET **/api/health** API health check

### congress

GET **/api/congress** List of legislator entities

GET **/api/congress/ids** List of legislator IDs

### legislator

GET **/api/legislator/{id}** Legislator entity

GET **/api/legislator/{id}/bio** Biographical info

GET **/api/legislator/{id}/id** Legislator IDs

GET **/api/legislator/{id}/name** Legislator name

GET **/api/legislator/{id}/social** Social accounts

GET **/api/legislator/{id}/term** Current term info

GET **/api/legislator/{id}/terms** List of terms served

GET **/api/legislator/{id}/tweet** Recent tweet

GET **/api/legislator/{id}/tweets** List of recent tweets

## Definitions

**id**: The alphanumeric bioguide ID for each legislator in http://bioguide.congress.gov.

**bio**: Biographical information including birthday.

**terms**: List of terms of office served in chronological order. Includes party affiliation.

**social**: Social account IDs including Facebook, Youtube, Instagram and Twitter if available.

**tweets**: List of recent tweets.
