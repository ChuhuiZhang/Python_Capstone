
# File created: Feb 16, 2016
# File commited:
# This program is in support of content analysis.

# Activity 1
def read():
# read text from end user
    fileContent = input("Please input your text with triple quotation marks: ")
    # remove all leading and trailing spaces of the texts
    fileContent = fileContent.strip()

    # remove all symbols and numbers
    fileContent = fileContent.replace(',', ' ')
    fileContent = fileContent.replace('.', ' ')
    fileContent = fileContent.replace(':', ' ')
    fileContent = fileContent.replace(';', ' ')
    fileContent = fileContent.replace('?', ' ')
    fileContent = fileContent.replace('!', ' ')
    fileContent = fileContent.replace('\'', ' ')
    fileContent = fileContent.replace('\"', ' ')
    fileContent = fileContent.replace('<', ' ')
    fileContent = fileContent.replace('>', ' ')
    fileContent = fileContent.replace('-', ' ')
    fileContent = fileContent.replace('$', ' ')
    fileContent = fileContent.replace('1', ' ')
    fileContent = fileContent.replace('2', ' ')
    fileContent = fileContent.replace('3', ' ')
    fileContent = fileContent.replace('4', ' ')
    fileContent = fileContent.replace('5', ' ')
    fileContent = fileContent.replace('6', ' ')
    fileContent = fileContent.replace('7', ' ')
    fileContent = fileContent.replace('8', ' ')
    fileContent = fileContent.replace('9', ' ')
    fileContent = fileContent.replace('0', ' ')


    # split text into individual words
    individualWords = ' '.join(fileContent.split())

    # create a list of tokens
    tokenList = individualWords.split()

    # print list of tokens to end user
    print(tokenList)

    #return tokenList to the main function
    return tokenList


# Activity 2
def deleteNoise(tokenList):
    # create the noise list
    noiseList = ['a', 'an', 'the', 'off', 'out', 'in', 'with', 'it', 'to', 'is','are',
             'you', 'we', 'us', 'our', 'their', 'your', 'by', 'and', 'after', 'as',
             'across', 'from', 'on', 'so', 'if', 'just', 'even', 'her','him', 'did',
             'do', 'does', 'over','always', 'be', 'but', 'within', 'yes', 'no', 'i',
             'at','this', 'that', 'those', 'they', 'bad', 'very', 'may', 'its', 'when',
             'where', 'what', 'how', 'than', 'up', 'down',  'end', 'who', 'his', 'her'
             'finally', 'if', 'out', 'some', 'more', 's', 'since', 'being', 'mr', 'of',
             'for', 'new', 't', 'me', 'while', 'could', 'any', 'two', 'too', 'about', 'four',
             'well', 'must', 'really', 'around', 'also', 'less', 'ago', 'neither', 'either',
             'before', 'still', 've', 'i', 'm', 'able', 'abroad', 'access', 'above' ,'al',
             'another', 'will', 'all', 'almost', 'could', 'couldn', 'doesn', 'doesn', 'should',
             'shouldn', 's', 'will', 'can', 'not', 'has', 'have','every','he', 'like', 'into', 
             'ever', 'been', 'again', 'never', 'through', 'because', 'them', 'got', 'everything',
             'pre', 'she', 'today', 'd', 'was', 'already', 'ahead', 'other', 'most', 'else', 'or',
             'let', 're', 'why', 'now', 'my', 'without', 'anything', 'everything', 'whenever',
             'whatever', 'however', 'don', 'doesn', 'didn', 'f', 'am']

    # create a new token list to store the text without the noise
    newTokenList = []

    # delete noise 
    for each in tokenList:
        if each not in noiseList:
            newTokenList.append(each)
    
    # join the no noise list as a big string
    cleanContent = ' '.join(newTokenList)

    # stemming
    cleanContent = cleanContent.replace('decades', 'decade')
    cleanContent = cleanContent.replace('jobs', 'job')
    cleanContent = cleanContent.replace('cars', 'car')
    cleanContent = cleanContent.replace('businesses', 'business')
    cleanContent = cleanContent.replace('exports', 'export')
    cleanContent = cleanContent.replace('dreams', 'dream')
    cleanContent = cleanContent.replace('fathers', 'father')
    cleanContent = cleanContent.replace('mothers', 'mother')
    cleanContent = cleanContent.replace('kids', 'kid')
    cleanContent = cleanContent.replace('speaks', 'speak')
    cleanContent = cleanContent.replace('citizens', 'citizen')
    cleanContent = cleanContent.replace('results', 'result')
    cleanContent = cleanContent.replace('efforts', 'effort')
    cleanContent = cleanContent.replace('years', 'year')
    cleanContent = cleanContent.replace('deficits', 'deficit')
    cleanContent = cleanContent.replace('democrats', 'democrat')
    cleanContent = cleanContent.replace('republicans', 'republican')
    cleanContent = cleanContent.replace('priorities', 'priority')
    cleanContent = cleanContent.replace('lives', 'life')
    cleanContent = cleanContent.replace('hopes', 'hope')
    cleanContent = cleanContent.replace('aspirations', 'aspiration')
    cleanContent = cleanContent.replace('wages', 'wage')
    cleanContent = cleanContent.replace('trends', 'trend')
    cleanContent = cleanContent.replace('costs', 'cost')
    cleanContent = cleanContent.replace('americans', 'american')
    cleanContent = cleanContent.replace('opportunities', 'opportunity')
    cleanContent = cleanContent.replace('plants', 'plant')
    cleanContent = cleanContent.replace('needs', 'need')
    cleanContent = cleanContent.replace('benefits', 'benefit')
    cleanContent = cleanContent.replace('leaders', 'leader')
    cleanContent = cleanContent.replace('degrees', 'degree')
    cleanContent = cleanContent.replace('expectations', 'expectation')
    cleanContent = cleanContent.replace('teachers', 'teacher')
    cleanContent = cleanContent.replace('students', 'student')
    cleanContent = cleanContent.replace('investments', 'investment')
    cleanContent = cleanContent.replace('schools', 'school')
    cleanContent = cleanContent.replace('deserves', 'deserve')
    cleanContent = cleanContent.replace('communities', 'community')
    cleanContent = cleanContent.replace('threats', 'threat')
    cleanContent = cleanContent.replace('conflicts', 'conflict')
    cleanContent = cleanContent.replace('limits', 'limit')
    cleanContent = cleanContent.replace('sanctions', 'sanction')
    cleanContent = cleanContent.replace('risks', 'risk')
    cleanContent = cleanContent.replace('standards', 'standard')
    cleanContent = cleanContent.replace('months', 'month')
    cleanContent = cleanContent.replace('colleges', 'college')
    cleanContent = cleanContent.replace('employers', 'employer')
    cleanContent = cleanContent.replace('comes', 'come')
    cleanContent = cleanContent.replace('deserves', 'deserve')
    cleanContent = cleanContent.replace('missions', 'mission')
    cleanContent = cleanContent.replace('rejects', 'reject')
    cleanContent = cleanContent.replace('restrictions', 'restriction')
    cleanContent = cleanContent.replace('remains', 'remain')
    cleanContent = cleanContent.replace('exchanges', 'exchange')
    cleanContent = cleanContent.replace('knows', 'know')
    cleanContent = cleanContent.replace('skills', 'skill')  
    cleanContent = cleanContent.replace('demands', 'demand')  
    cleanContent = cleanContent.replace('rejects', 'reject')
    cleanContent = cleanContent.replace('lifts', 'lift')
    cleanContent = cleanContent.replace('lights', 'light')
    cleanContent = cleanContent.replace('systems', 'system')
    cleanContent = cleanContent.replace('ideas', 'idea')
    cleanContent = cleanContent.replace('companies', 'company')
    cleanContent = cleanContent.replace('hubs','hub')
    cleanContent = cleanContent.replace('ends', 'end')
    cleanContent = cleanContent.replace('tragedies', 'tragedy')
    cleanContent = cleanContent.replace('eyes', 'eye')
    cleanContent = cleanContent.replace('defenses', 'defense')
    cleanContent = cleanContent.replace('floods', 'flood')
    cleanContent = cleanContent.replace('marines', 'marine')
    cleanContent = cleanContent.replace('says', 'say')
    cleanContent = cleanContent.replace('daughters', 'daughter')
    cleanContent = cleanContent.replace('attacks', 'attack')
    cleanContent = cleanContent.replace('burdens', 'burden')
    cleanContent = cleanContent.replace('laws', 'law')
    cleanContent = cleanContent.replace('works', 'work')
    cleanContent = cleanContent.replace('functions', 'function')
    cleanContent = cleanContent.replace('weeks', 'week')
    cleanContent = cleanContent.replace('stops', 'stop')
    cleanContent = cleanContent.replace('americas', 'america')
    cleanContent = cleanContent.replace('families', 'family')
    cleanContent = cleanContent.replace('troops', 'troop')
    cleanContent = cleanContent.replace('employees', 'employee')
    cleanContent = cleanContent.replace('allies', 'ally')
    cleanContent = cleanContent.replace('rates', 'rate')
    cleanContent = cleanContent.replace('turns', 'turn')
    cleanContent = cleanContent.replace('operations', 'operation')
    cleanContent = cleanContent.replace('governments', 'government')
    cleanContent = cleanContent.replace('succeeds', 'succeed')
    cleanContent = cleanContent.replace('ways', 'way')
    cleanContent = cleanContent.replace('organizations', 'organization')
    cleanContent = cleanContent.replace('threatens', 'threaten')
    cleanContent = cleanContent.replace('mistakes', 'mistake')
    cleanContent = cleanContent.replace('keeps', 'keep')
    cleanContent = cleanContent.replace('proposals', 'proposal')
    cleanContent = cleanContent.replace('means', 'mean')
    cleanContent = cleanContent.replace('speaks', 'speak')
    cleanContent = cleanContent.replace('shows', 'show')
    cleanContent = cleanContent.replace('unites', 'unite')
    cleanContent = cleanContent.replace('deployments', 'deployment')
    cleanContent = cleanContent.replace('passes', 'pass')
    cleanContent = cleanContent.replace('convices', 'convice')
    cleanContent = cleanContent.replace('ports', 'port')
    cleanContent = cleanContent.replace('aversaries', 'aversary')
    cleanContent = cleanContent.replace('allows', 'allow')
    cleanContent = cleanContent.replace('applications', 'application')
    cleanContent = cleanContent.replace('breaks', 'break')
    cleanContent = cleanContent.replace('causes', 'cause')
    cleanContent = cleanContent.replace('arguments', 'argument')

    # compound word
    cleanContent = cleanContent.replace('united states of america', 'united_states_of_america')
    cleanContent = cleanContent.replace('employment rate', 'employment_rate')
    cleanContent = cleanContent.replace('graduation rate', 'graduation_rate')
    cleanContent = cleanContent.replace('fuel efficient', 'fuel_efficient')
    cleanContent = cleanContent.replace('federal government', 'federal_government')
    cleanContent = cleanContent.replace('great recession', 'great_recession')
    cleanContent = cleanContent.replace('economic growth', 'economic_growth')
    cleanContent = cleanContent.replace('average wage', 'average_wage')
    cleanContent = cleanContent.replace('middle class', 'middle_class')
    cleanContent = cleanContent.replace('health care', 'health_care')
    cleanContent = cleanContent.replace('higher education', 'higher_education')
    cleanContent = cleanContent.replace('energy indenpendence', 'energy_indenpendence')
    cleanContent = cleanContent.replace('natural gas', 'natural_gas')
    cleanContent = cleanContent.replace('carbon pollution', 'carbon_pollution')
    cleanContent = cleanContent.replace('climate change', 'climate_change')
    cleanContent = cleanContent.replace('unemployment insurance', 'unemployment_insurance')
    cleanContent = cleanContent.replace('high quality early education', 'high_quality_early_education')
    cleanContent = cleanContent.replace('stock market', 'stock_market')
    cleanContent = cleanContent.replace('health insurance', 'health_insurance')
    cleanContent = cleanContent.replace('united states armed forces', 'united_states_armed_forces')
    cleanContent = cleanContent.replace('student loan', 'student_loan')
    cleanContent = cleanContent.replace('new york', 'new_york')
    cleanContent = cleanContent.replace('of', ' ')

    # normalization
    cleanContent = cleanContent.replace('spent', 'spend')
    cleanContent = cleanContent.replace('needed' ,'need')
    cleanContent = cleanContent.replace('flipped', 'flip')
    cleanContent = cleanContent.replace('prepared', 'prepare')
    cleanContent = cleanContent.replace('gave', 'give')
    cleanContent = cleanContent.replace('giving', 'give')
    cleanContent = cleanContent.replace('including', 'include')
    cleanContent = cleanContent.replace('produced', 'produce')
    cleanContent = cleanContent.replace('declared', 'declare')
    cleanContent = cleanContent.replace('consumed', 'consume')
    cleanContent = cleanContent.replace('commited', 'commit')
    cleanContent = cleanContent.replace('creating', 'create')
    cleanContent = cleanContent.replace('created', 'create')
    cleanContent = cleanContent.replace('eliminated', 'eliminate')
    cleanContent = cleanContent.replace('weakened', 'weaken')
    cleanContent = cleanContent.replace('helped', 'help')
    cleanContent = cleanContent.replace('helping', 'help')
    cleanContent = cleanContent.replace('launched', 'launch')
    cleanContent = cleanContent.replace('encouraged', 'encourage')
    cleanContent = cleanContent.replace('organized', 'organize')
    cleanContent = cleanContent.replace('argued', 'argue')
    cleanContent = cleanContent.replace('riddled', 'riddle')
    cleanContent = cleanContent.replace('connected', 'connect')
    cleanContent = cleanContent.replace('strengthening', 'strengthen')
    cleanContent = cleanContent.replace('strengthened', 'strengthen')
    cleanContent = cleanContent.replace('becoming', 'become')
    cleanContent = cleanContent.replace('increased', 'increase')
    cleanContent = cleanContent.replace('partnered', 'partner')
    cleanContent = cleanContent.replace('worked', 'work')
    cleanContent = cleanContent.replace('settled', 'settle')
    cleanContent = cleanContent.replace('acted', 'act')
    cleanContent = cleanContent.replace('asked', 'ask')
    cleanContent = cleanContent.replace('filled', 'fill')
    cleanContent = cleanContent.replace('convinced', 'convince')
    cleanContent = cleanContent.replace('reforming', 'reform')
    cleanContent = cleanContent.replace('employed', 'employ')
    cleanContent = cleanContent.replace('collected', 'collect')
    cleanContent = cleanContent.replace('claimed', 'claim')
    cleanContent = cleanContent.replace('earning', 'earn')
    cleanContent = cleanContent.replace('earned', 'earn')
    cleanContent = cleanContent.replace('making', 'make')
    cleanContent = cleanContent.replace('made', 'make')
    cleanContent = cleanContent.replace('decides', 'decide')
    cleanContent = cleanContent.replace('pledged', 'pledged')
    cleanContent = cleanContent.replace('offering', 'offer')
    cleanContent = cleanContent.replace('reaching', 'reach')
    cleanContent = cleanContent.replace('stifled', 'stifle')
    cleanContent = cleanContent.replace('eased', 'ease')
    cleanContent = cleanContent.replace('guarantees', 'guarantee')
    cleanContent = cleanContent.replace('protects', 'protect')
    cleanContent = cleanContent.replace('gained', 'gain')
    cleanContent = cleanContent.replace('dropped', 'drop')
    cleanContent = cleanContent.replace('denied', 'deny')
    cleanContent = cleanContent.replace('charged', 'charge')
    cleanContent = cleanContent.replace('supporting', 'support')
    cleanContent = cleanContent.replace('building', 'build')
    cleanContent = cleanContent.replace('built', 'build')
    cleanContent = cleanContent.replace('preventing', 'prevent')
    cleanContent = cleanContent.replace('resovled', 'resolve')
    cleanContent = cleanContent.replace('asking', 'ask')
    cleanContent = cleanContent.replace('permitting', 'permit')
    cleanContent = cleanContent.replace('saying', 'say')
    cleanContent = cleanContent.replace('targeted', 'target')
    cleanContent = cleanContent.replace('dividing', 'divide')
    cleanContent = cleanContent.replace('felt', 'feel')
    cleanContent = cleanContent.replace('halted', 'halt')
    cleanContent = cleanContent.replace('rising', 'rise')
    cleanContent = cleanContent.replace('annoucing', 'annouce')
    cleanContent = cleanContent.replace('dreaming', 'dream')
    cleanContent = cleanContent.replace('shaking', 'shake')
    cleanContent = cleanContent.replace('affiliates', 'affiliate')
    cleanContent = cleanContent.replace('allowed', 'allow')
    cleanContent = cleanContent.replace('adding', 'add')
    cleanContent = cleanContent.replace('balanced', 'balance')
    cleanContent = cleanContent.replace('boosted', 'boost')

    return cleanContent


# Activity 3
def count(cleanContent):
    # make the text all lowercases
    cleanContent = cleanContent.lower()

    # split the text into a list of words
    biglist = cleanContent.split()
    
    # create a dictionary to store the word : frequency
    dictionary = {}
    count = 0
    for each in biglist:
        if (str(each) in dictionary):
            count += 1
            dictionary[each] = count
        else:
            count = 1
            dictionary[each] = count

    # sort the dictionary alphabetically in accending order
    dictionary = sorted(dictionary.items(), key = lambda dictionary : dictionary[0])

    # outprint the words with their frequency
    for each in dictionary:
        print(each) 


def main():
    # read text from end user
    tokenList = read()

    # perform cleaning
    cleanContent = deleteNoise(tokenList)

    # perform frequency count
    count(cleanContent)


main()

        



