import itertools

from settings import ITEMS

def extract_stats(data,index,ns=[5,10,100]):

    #print 'stats for %d' % index
    #print [data_dict['date'] for data_dict in data[index-5:index+1]]

    last_seen = [index - _find_item(data,item,index) + 1 for item in ITEMS]
    #print 'last_seen: %s'%last_seen

    percent_dict = {}
    #ns.append(len(data)-index)

    for interval in ns:
        interval_nums = [data_dict['nums'] for data_dict in data[index-interval+1:index+1]]
        all_nums = sorted(itertools.chain(*interval_nums))
        interval_percent = [float(len(list(gen)))/interval for (item,gen) in itertools.groupby(all_nums)]
        percent_dict[interval] = interval_percent
        #print 'interval_%d: %s' % (interval,interval_percent)

    return {'last_seen':last_seen,
            'percents':percent_dict}

def _find_item(data,item,startindex):
    current_index = startindex
    while item not in data[current_index]['nums']:
        current_index-=1
    #print 'found %d at %d' % (item,current_index)
    return current_index