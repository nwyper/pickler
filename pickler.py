import cPickle
def pickler(fn):
    def wrapped(*args, **kwargs):
        filename = '{}.pickle'.format(fn.__name__)
        try:
            # try to read from the pickle file
            with open(filename, 'r') as f:
                retval = cPickle.load(f)

        except IOError:
            # pickle file doesn't exist: call the original function
            retval = fn(*args, **kwargs)

            # save the data to the pickle file
            with open(filename, 'w') as f:
                cPickle.dump(retval, f)
            
        return retval

    return wrapped
