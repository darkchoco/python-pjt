#!/usr/bin/env python

__date__ = '2015-09-23'

from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def dl_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def dl_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(dl_one, sorted(cc_list))

    return len(list(res))


if __name__ == '__main__':
    # call the main function from the flags module(flags.py), passing the enhanced ver of dl_many
    main(dl_many)
