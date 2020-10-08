
WEEK_IDX_RANGE = range(1, 14)

DATES_FROM_WEEK_IDX = {
     1: ('2020-04-23', '2020-05-05'),
     2: ('2020-05-07', '2020-05-12'),
     3: ('2020-05-14', '2020-05-19'),
     4: ('2020-05-21', '2020-05-26'),
     5: ('2020-05-28', '2020-06-02'),
     6: ('2020-06-04', '2020-06-09'),
     7: ('2020-06-11', '2020-06-16'),
     8: ('2020-06-18', '2020-06-23'),
     9: ('2020-06-25', '2020-06-30'),
    10: ('2020-07-02', '2020-07-07'),
    11: ('2020-07-09', '2020-07-14'),
    12: ('2020-07-16', '2020-07-21'),
    13: ('2020-08-19', '2020-08-31'),
}

DEMOGRAPHICS_VARS = [
    'TBIRTH_YEAR', 'EGENDER', 'MS', 'EST_ST',
    'RHISPANIC', 'RRACE',
    'EEDUC',
    'THHLD_NUMPER', 'THHLD_NUMKID', 'THHLD_NUMADLT',
    'INCOME',
]

HEALTH_VARS = [
    'HLTHSTATUS',
    'ANXIOUS', 'WORRY', 'INTEREST', 'DOWN'
]

WORK_VARS = [
    'WRKLOSS', 'EXPCTLOSS', 'ANYWORK', 'KINDWORK', 'RSNNOWRK', 'UNEMPPAY'
]

STATES =  ['Alabama',
          'Alaska',
          'Arizona',
          'Arkansas',
          'California',
          'Colorado',
          'Connecticut',
          'Delaware',
          'District of Columbia',
          'Florida',
          'Georgia',
          'Hawaii',
          'Idaho',
          'Illinois',
          'Indiana',
          'Iowa',
          'Kansas',
          'Kentucky',
          'Louisiana',
          'Maine',
          'Maryland',
          'Massachusetts',
          'Michigan',
          'Minnesota',
          'Mississippi',
          'Missouri',
          'Montana',
          'Nebraska',
          'Nevada',
          'New Hampshire',
          'New Jersey',
          'New Mexico',
          'New York',
          'North Carolina',
          'North Dakota',
          'Ohio',
          'Oklahoma',
          'Oregon',
          'Pennsylvania',
          'Rhode Island',
          'South Carolina',
          'South Dakota',
          'Tennessee',
          'Texas',
          'Utah',
          'Vermont',
          'Virginia',
          'Washington',
          'West Virginia',
          'Wisconsin',
          'Wyoming']
