#!/usr/bin/env python
import random
from math import sqrt

def get_ingredients(name):
    if name == "Elixir To Induce Euphoria":
        return [
            'Shrivelfig',
            'Porcupine quills',
            'Peppermint sprigs',
		    'Sopophorous beans',
            'Wormwood'
        ]
    elif name == "Felix Felicis":
        return [
            'Ashwinder egg',
            'Horseradish',
            'Squill bulb',
            'Murtlap tentacle',
		    'Tincture of thyme',
            'Occamy eggshell',
            'Powdered common rue'
        ]
            
def add(cauldron, ingredient):
    print "Adding " + ingredient + " to the cauldron"
    return cauldron + ingredient

def stir(cauldron, num_times):
    random.seed(0)
    for i in range(num_times):
        print "Stirring..."
        cauldron = ''.join(random.sample(cauldron, len(cauldron)))
    return cauldron

def say_incantation(cauldron):
    print 'Felixempra!!!!!'
    return cauldron + ' Felixempra!!!!!'

def get_cauldron():
    return ''

def __gen_colors(n):
    possible_foreground = range(30, 38) + range(90, 98)
    possible_background = range(40, 48) + range(100, 108)
    fx = n % len(possible_foreground)
    bx = (n * 2 - 17 * 3029) % len(possible_background)
    f_hsh = possible_foreground[fx]
    b_hsh = possible_background[bx]

    fmt = '\033[{0};{1}m'
    # \e[103m with \e[96m is elixir
    if n == 68: return fmt.format(103, 96)
    #\e[43m  with \e[37m is felix 
    if n == 118: return fmt.format(43, 37)
    return fmt.format(f_hsh, b_hsh)

def __reset_colors(n):
    # default \e[49m \e[39m
    return '\033[49;39m'

def render_potion(cauldron):
    length = len(cauldron)
    if not length:
        return 'Your cauldron is empty:\n\n\   /\n | |\n ---\n'
    n = int(min(sqrt(length), 60)) * 2

    # colors
    enable = __gen_colors(length)
    disable = __reset_colors(length)
    # build 
    result = str()
    result += "Your Potion:\n\n"
    result += ('\\' + ' ' * (n + 2) + ' ' + '/' + '\n')
    for x in [cauldron[i:i+n] for i in range(0, len(cauldron), n)]:
        if len(x) < n:
            x += ' ' * (n - len(x))
        result += (" | " + enable + x + disable + " | " + '\n')
    result += ('  ' + '-' * (n + 2) + '\n')
    return result
