import itertools

def sorted_last_seen_middle(current_stats):
    cnt = itertools.cycle(range(1,21))
    sorted_last_seen = sorted([(next(cnt),last_seen) for last_seen in current_stats['last_seen']],key=lambda (i,c):c,reverse=True)

    sorted_percent = sorted([(next(cnt),last_seen) for last_seen in current_stats['percents'][5]],key=lambda (i,c):c,reverse=True)

    #exit(0)
    #print current_stats['last_seen']
    #print sorted_last_seen
    return sorted_last_seen[10][0]
    #return sorted_percent[10][0]

global_cnt = itertools.cycle(range(1,21))

def decider_counter(start):
    [next(global_cnt) for i in range(0,start-1)]
    cnt = itertools.cycle(range(1,21)) 
    
    def func(current_stats):
        sorted_last_seen = sorted([(next(cnt),last_seen) for last_seen in current_stats['last_seen']],key=lambda (i,c):c,reverse=True)
        sorted_percent_5 = sorted([(next(cnt),last_seen) for last_seen in current_stats['percents'][5]],key=lambda (i,c):c,reverse=True)
        return next(global_cnt)

    return func
    
def decider_constant(n):
    def func(current_stats):
        return n
    return func

