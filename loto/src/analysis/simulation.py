import itertools
from datetime import datetime

from statistics import extract_stats
from settings import ITEMS
from settings import K
from settings import MT
import deciders

def simulate(data,start,end,initial_amount,betting_strategy_func):

    data = data.values()
    current_amount = initial_amount

    current_bets = []
    bets_success = []
    bets_failed = []

    bet_stats = {}

    total_bet_num = 0
    total_bet_days = (end - start).days
    total_bet_amount = 0
    total_won_amount = 0

    min_amount = {'amount':initial_amount+1,'date':None}
    max_amount = {'amount':0,'date':None}

    def update_bet_stats(bet,success):
        amount = bet['amount']
        #num = bet['num']
        if amount not in bet_stats:
            bet_stats[amount] = {'success':0,'fail':0}
        bet_stats[amount]['success' if success else 'fail'] += 1

    for (i,current_data) in enumerate(data):

        current_date = current_data['date']
        if current_date < start:
            continue
        elif current_date>=end:
            break

        current_stats = extract_stats(data,i-1)
        current_nums = current_data['nums']

        if current_amount < min_amount['amount']:
            min_amount = {'amount':current_amount,'date':current_date}
        if current_amount > max_amount['amount']:
            max_amount = {'amount':current_amount,'date':current_date}

        print '\n%s' % current_date
        #print 'current nums %s' % current_data['nums']
        #print 'prior nums %s' % data[current-1]['nums']
        #print 'current stats(last seen) %s' % current_stats['last_seen']
        #print 'current stats(percent last 5) %s' % current_stats['percents'][5]
        #print 'current stats(percent last 10) %s' % current_stats['percents'][10]

        current_bets = betting_strategy_func(current_stats,bets_success,bets_failed)
        bet_amount = sum([bet['amount'] for bet in current_bets])
        current_amount -= bet_amount
        total_bet_amount += bet_amount
        total_bet_num += len(current_bets)
        print 'bet %s amount %.2f (remaining %.2f)' % (current_bets,bet_amount,current_amount)

        keyfunc = lambda d:d['num'] in current_nums
        bets_success = filter(keyfunc,current_bets)
        bets_failed = list(itertools.ifilterfalse(keyfunc,current_bets))
        won_amount = sum([K * (1-MT) * bet['amount'] for bet in bets_success])
        current_amount += won_amount
        total_won_amount += won_amount
        [update_bet_stats(bet,True) for bet in bets_success]
        [update_bet_stats(bet,False) for bet in bets_failed]
        print 'won amount %.2f (remaining %.2f)' % (won_amount,current_amount)

        #print 'bets_success %s' % (bets_success,)
        #print 'bets_failed %s' % (bets_failed,)

    return {'initial_amount' : initial_amount,
            'final_amount' : current_amount,
            'profit' : float(current_amount-initial_amount),
            'profit(per day)' : float(current_amount-initial_amount)/total_bet_days,
            'return' : float(current_amount-initial_amount)/initial_amount,
            'return(per day)' : float(current_amount-initial_amount)/(initial_amount*total_bet_days),
            'total_bet_num' : total_bet_num,
            'total_bet_days' : total_bet_days,
             'total_bet_amount' : total_bet_amount,
             'total_won_amount' : total_won_amount,
             'initial_date' : start,
             'final_date' : end,
             'min' : min_amount,
             'max' : max_amount,
             'bet_stats' : bet_stats,
             'betting_strategy' : betting_strategy_func.__name__}

def betting_strategy_dummy(current_stats,bets_success,bets_failed):
    return ({'num':1,'amount':100},)

def betting_strategy_double_with_limit(stake_values,stake_limit,num_choose_func):

    intial_stake = stake_values[0]

    def func(current_stats,bets_success,bets_failed):
        func.betting_strategy = 'betting_strategy_double_with_limit + %s' % num_choose_func.__name__

        bets = []

        for failed_bet in bets_failed:
            failed_num = failed_bet['num']
            failed_stake = failed_bet['amount']
            i = stake_values.index(failed_stake)
            next_stake = stake_values[i+1]
            if next_stake <= stake_limit:
                #num = random.randrange(1,21)
                #num = failed_num
                num = num_choose_func(current_stats)
                bets.append({'num':num,'amount':next_stake})

        if not bets:
            num = num_choose_func(current_stats)
            bets.append({'num':num,'amount':intial_stake})

        return bets
    return func

if __name__ == '__main__':
    from pprint import pprint
    from data import fetch

    local_data = fetch.fetch_local_item_data()

    simulation_params_current = {
        'initial_amount': 2500,
        'data':local_data,
        'start':datetime(2011,9,1,8,0),
        'end':datetime(2011,10,1,8,0),
        'betting_strategy_func':betting_strategy_double_with_limit(
            [5.00,15.00,35.00,80.00,180.00,400.00,900.00,2050.00,1000000.00],
            401,
            deciders.sorted_last_seen_middle)
    }

    simulation_params_counter = {
        'initial_amount': 2500,
        'data':local_data,
        'start':datetime(2011,9,1,8,0),
        'end':datetime(2011,10,31,16,0),
        'betting_strategy_func':betting_strategy_double_with_limit(
            [5.00,15.50,38.00,85.00,184.00,393.00,832.00,1000.00],
            900,
            deciders.decider_counter(8)
        )
    }
    
    simulation_params_constant = {
        'initial_amount': 2500,
        'data':local_data,
        'start':datetime(2011,10,15,8,0),
        'end':datetime(2011,10,31,16,0),
        'betting_strategy_func':betting_strategy_double_with_limit(
            [5.00,15.50,38.00,85.00,184.00,393.00,832.00,1000.00],
            900,
            deciders.decider_constant(18)
        )
    }

    #simulation_params = simulation_params_current
    simulation_params = simulation_params_constant
    #simulation_params = simulation_params_counter
    simulation_result = simulate(**simulation_params)
    print '\nSimulation result:'
    pprint(simulation_result)