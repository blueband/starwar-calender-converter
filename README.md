# starwar-calender-converter
This library was inspired by the needs to parse and convert date_birth in Star war datasets made available at https://swapi.dev/api/ into human readable format

**** In case of Alien Invasion from Star War, we need a quick way to parsed DOB of such alien, and this python module is doing that. 


See following Url:
1. https://swapi.dev/api/people/
2. https://starwars.fandom.com/wiki/Battle_of_Yavin
3. https://starwars.fandom.com/wiki/0_BBY


# INSTALLATION
Get it by running this python in your working environment
'pip install starwar-dob==3.14.post0'

# USAGE
'from starwardob import starwardob'

'actor = starwardob.StarwarDOB('3Aby')'
'print(actor.unix_year)'          # Actor DOB in UNIX format (1970) is display
'print(actor.age)'                # Actor age is dispay in human readable format


**** BUG TRACKING
Join us at https://github.com/blueband/starwar-calender-converter/issues