class LcmException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'lcmException, {0}'.format(self.message)
        else:
            return 'lcmException has been raised'
