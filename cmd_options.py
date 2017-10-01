import argparse

# Default arguments
DEFAULT_WIDTH = 80
DEFAULT_HEIGHT = 60

# In case percentage arguments out of bounds are given
def percentage_clamp(percent, default_val):
    if (int(percent) < 0) or (int(percent) > 100):
        return default_val
    else:
        return percent

# Used to parse arguments
def protect_arguments(args):

    args.width_perc = \
        percentage_clamp(args.width_perc, DEFAULT_WIDTH)

    args.height_perc = \
        percentage_clamp(args.height_perc, DEFAULT_HEIGHT)

    return args

# Returns the command line arguments
def command_options():

    cmd_options = argparse.ArgumentParser(description='PyPost')

    cmd_options.add_argument('-wp', '--width', dest='width_perc',
                                action='store', default=DEFAULT_WIDTH,
                                help='Width screen percentage')
    cmd_options.add_argument('-hp', '--height', dest='height_perc',
                                action='store', default=DEFAULT_HEIGHT,
                                help='Height screen percentage')
    arguments = cmd_options.parse_args()

    return protect_arguments(arguments)
