def get_itunes(word):
    """ (string) -> (list of strings)
    
    API that takes a string argument (Name of an artist) and returns a list of song names.
    
    -> get_itunes('Foo Fighters')
    -> ['The Pretender', 'Best of You', 'Everlong', 'My Hero', 'Learn to Fly', 'Times Like These', 'Best of You', 'My Hero', 'All My Life', 'Everlong', 'Monkey Wrench', 'Everlong', 'Wheels', 'Something from Nothing', 'Word Forward', 'This Is a Call', 'Big Me', 'These Days', 'Big Me', 'Skin and Bones', 'Long Road to Ruin', 'DOA', 'Breakout', "I'll Stick Around", 'Congregation', 'The Feast and the Famine', 'Run', 'What Did I Do?/God As My Witness', 'Monkey Wrench', 'Outside', 'I Am a River', 'This Is a Call', 'Subterranean', 'In the Clear', 'Rope', 'No Way Back', 'The Sky Is a Neighborhood', 'Dear Rosemary', 'Miracle', 'Arlandria', 'White Limo', 'Miss the Misery', 'Bridge Burning', 'I Should Have Known', 'Sunday Rain', 'The Line', 'Cold Day In the Sun', 'Next Year', 'T-Shirt', 'Learn to Fly']
    """
    
    baseurl = "https://itunes.apple.com/search"
    para_dict = {}
    para_dict['term'] = word
    para_dict["max"] = '3'#Get a max of 3 results
    resp = requests.get(baseurl, params=para_dict)
    py_data1 = json.loads(resp.text)
    track_list = []
    for r in py_data1['results']:
        track_list.insert(-1, r['trackName'])
    return track_list
