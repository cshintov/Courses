"""
Cookie Clicker Simulator
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
import poc_clicker_provided as provided

#from poc_testsuite import *
#from poc_clicker_provided import *
#from copy import deepcopy
from math import ceil
# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
       self._total_cookies = 0.0
       self._current_cookies = 0.0
       self._current_time = 0.0
       self._current_cps = 1.0
       self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        state = ""
        total = "{:20}".format(self._total_cookies)
        state += "Total Cookies Produced: " + total + "\n"
        cookies = "{:20f}".format(self._current_cookies)
        state += "Cookies in bank: " + str(cookies) + "\n"
        state += "Time Elapsed: " + str(self._current_time) + "\n"
        state += "Current CPS: " + str(self._current_cps) + "\n"
        return state
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        reqd_time = 0.0
        current_cookies = self.get_cookies()
        if current_cookies < cookies:
            cookies_needed = cookies - self.get_cookies()
            reqd_time = ceil((cookies_needed) / self.get_cps())
        return reqd_time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._current_time += time
            cookies_produced = time * self._current_cps
            self._current_cookies += cookies_produced
            self._total_cookies += cookies_produced

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_cookies))



def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    build = build_info.clone()
    state = ClickerState()
    while state.get_time() <= duration:
        cookies = state.get_cookies()
        cps = state.get_cps()
        history = state.get_history()
        
        time_left = duration - state.get_time()
        item = strategy(cookies, cps, history, time_left, build)
        if item is None:
            state.wait(time_left)
            break
        cost, additional_cps = build.get_cost(item), build.get_cps(item)
        required_time = state.time_until(cost)
        if required_time > time_left:
            state.wait(time_left)
            break
        state.wait(required_time)
        state.buy_item(item, cost, additional_cps)
        build.update_item(item)
    return state

#run_suite(ClickerState)
def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def item_costs(build_info):
    """ gets the costs of the upgrades"""
    items = build_info.build_items()
    cost = build_info.get_cost
    items = [(cost(item), item) for item in items]
    items = sorted(items)
    return items

def item_cps(build_info):
    """ gets the costs of the upgrades"""
    items = build_info.build_items()
    getcps = build_info.get_cps
    cost = build_info.get_cost
    items = [(getcps(item), cost(item), item) for item in items]
    items = sorted(items)
    return items

def get_cheapest_item(build_info):
    """ returns the cheapest item"""
    items = item_costs(build_info)
    return items[0]

def get_lowcps_item(build_info):
    """return teh lowest cps item"""
    items = item_cps(build_info)
    return items[0]

def get_costly_item(build_info):
    """ returns the cheapest item"""
    items = item_costs(build_info)
    return items[-1]

def get_bigcps_item(build_info):
    """return the highest cps item"""
    items = item_costs(build_info)
    return items[-1]

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cheapest_item_cost, cheapest_item = get_cheapest_item(build_info)
    max_possible = cookies + time_left * cps
    if max_possible < cheapest_item_cost:
        item = None
    else:
        item = cheapest_item
    return item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    items = item_costs(build_info)
    max_possible = cookies + time_left * cps
    items = [item for item in items if item[0] <= max_possible]
    if len(items) is 0:
        item = None
    else:
        item = items[-1][1]
    return item

def strategy_best_a(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    last_purch_item = history[-1][1]
    max_possible = cookies + time_left * cps
    items = item_costs(build_info)
    items = [itema[1] for itema in items if itema[0] <= max_possible]
    if last_purch_item == None or last_purch_item not in items:
        item = strategy_cheap(cookies, cps, history, time_left, build_info)
        return item
    
    if last_purch_item in items :
        index = items.index(last_purch_item)
        if index == len(items) - 1:
            item = last_purch_item
            return item
        
        cost_next_item = build_info.get_cost(items[index+1])
        cost_item = build_info.get_cost(last_purch_item)
        if cost_item < (0.86 * cost_next_item):
            item = last_purch_item
        else:
            item = items[index+1]
    
    return item


from random import choice
def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    total_possile = cookies + cps * time_left
    def cost_per_cps_ratio(item):
        item_cps = build_info.get_cps(item)
        item_cost = build_info.get_cost(item)
        ratio = item_cost / item_cps 
        return ratio
    def test_option(item):
        cost = build_info.get_cost(item)
        max_cookies = cookies + cps * time_left
        return cost <= max_cookies 
    options = [(cost_per_cps_ratio(item), item) for item in build_info.build_items() if test_option(item)]
    if len(options) == 0:
        return None
    return min(options)[1]

#run_suite(simulate_clicker, strategy_expensive)
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state
    #his = state._history
    #for item in his:
    #    print 'time     , item ,    cost,   totalcook'
    #    print item
    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    #run_strategy("Best", SIM_TIME, strategy_best_a)
    
run()
    

