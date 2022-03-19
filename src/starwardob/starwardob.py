from datetime import date


class StarwarDOB:
    ''' The battle of Yavin took place in was epoch event 
    in Starwar hence event are recorded with reference to it occurence
    The year of the battle is identified as either 0BBY (Before Year of Yavin) 
    or 0ABY (After Battle of Yavin)

    See https://starwars.fandom.com/wiki/Prince/Legends

    Inspiration  was derived from parse birth_date  from data 
    retrieve from API avaiablabe at 

    WHY 0BBY or 0ABY is epoch
    in the openning paragraph available here 
    0 BBY (Before Battle of Yavin) was a period of time that, 
    together with 0 ABY,[9] made up a single year.[10] 
    That year was also known as 3277 LY according to the Lothal Calendar[7] 
    and year 7977 in the C.R.C. calendar
    See https://starwars.fandom.com/wiki/0_BBY

    0BBY or 0ABY is transalated into Unix dob of 1970 
    '''
    __current_year = date.today().year
    __epoch_year = 1970   # ('Unix Epoch Time')
    

    def __init__(self,starwardob):
        '''Actor date_birth of format eithher 78BY or 87ABY 
        is an argument to the class

        The object will return date of birth in human readable format 
        and the Age of the Actor
        '''
        self.unix_year, self.age = self.main(starwardob)
      

    def yavin_date_check(self, dt):
        #TO DO:
        # check third character from end, if the chr is number, return not support
        dt_end = dt[-3:]
        if dt_end not in ['BBY', 'ABY']:
            return False
        else:
            return True


    def get_delimeter(self, year_format):
        return year_format[:-2]


    def getAge(self, unixdob):
        if unixdob > StarwarDOB.__current_year:
            return 'Actor not yet Exist'
        elif int(unixdob) == StarwarDOB.__epoch_year:
            return StarwarDOB.__current_year - StarwarDOB.__epoch_year
        elif int(unixdob) > StarwarDOB.__epoch_year:
            return StarwarDOB.__current_year - int(unixdob)
        else:
            return abs(unixdob - StarwarDOB.__epoch_year) \
            + StarwarDOB.__current_year - StarwarDOB.__epoch_year


    def calculateUnixYear(self, *args):
        if not args[0] in ['0B', '0A']:
            if args[0].endswith('A'):
                yr = int(args[0][:-1])
                unix_dob = StarwarDOB.__epoch_year + yr
            else:
                yr = int(args[0][:-1])
                unix_dob = StarwarDOB.__epoch_year - yr
        else:
            unix_dob = StarwarDOB.__epoch_year
        return unix_dob 

    def main(self, starwardob):
        starwardob = starwardob.upper()
        if self.yavin_date_check(starwardob):
            year_pre = self.get_delimeter(starwardob)
            self.unix_year = self.calculateUnixYear(year_pre)
            self.age = self.getAge(self.unix_year)
            return self.unix_year, self.age
        else:
            return 'date not convertible'


# Usage **********************
# import the module
# instantiate the class See Below
# author = StarwarDOB('0aby')
# retrieve unix based dated of birth and age by 
# author.unix_year
# author.age