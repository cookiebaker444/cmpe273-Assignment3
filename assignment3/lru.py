def LRUCache(max_size):
    """A simple dict-based LRU cache
    The cached function must:
     - Have no kwargs
     - Have only hashable args
       - If the decorated function is passed an unhashable arg, a TypeError
         will be raised
     - Be idempotent (be without side effects)
       - Otherwise the cache could become invalid
    Usage:
        @LRUCache(max_size=50)
        def to_be_cached(foo, bar):
            ... some computation ...
            return retval
    """
    cache = {}
    cache_keys = []

    def lrucache_dec(fn):
        def cached_fn(*args):
            # args is a tuple, so it can be used as a dict key
            if args in cache:
                # Set args as most-recently-used
                del cache_keys[cache_keys.index(args)]
                cache_keys.append(args)
                return cache[args]

            # If fn(*args) raises an exception, the cache will not be affected,
            # so no special measures need be taken.
            retval = fn(*args)

            # Add to the cache and set as most-recently-used
            cache[args] = retval
            cache_keys.append(args)

            # Prune the cache if necessary
            if len(cache_keys) > max_size:
                del cache[cache_keys[0]]
                del cache_keys[0]

            return retval
        return cached_fn
    return lrucache_dec
