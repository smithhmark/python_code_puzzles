
def leftmost(s, l, r, test):
    for ii in range(r, l-1, -1):
        if test(s[l:ii]):
            return ii-1
    return -1

def expand_options(s, l, r, crit):
    # expand options
    opts = []
    prev = None
    for ii in range(l+1, r+1):
        if crit(s[l:ii]):
            opts.append(ii)
    return opts

def brute(s, crit):
    ##print(s)
    if crit(s):
        return 1
    splits = 1
    options = expand_options(s, 0, len(s)-1, crit)
    #print(options)
    if len(options) == 0:
        return -1

    split_opts = {1: set(options)}
    #print(split_opts)
    while splits < len(s):
        #print("processing level:", splits)
        options = split_opts.get(splits)
        #print("options:", options)
        #print("options:", list(options).sort())
        if options is None:
            return -1
        opts = sorted(list(options), reverse=True)
        #print("opts", opts)
        for opt in opts:
            #print("opt", opt)
            if crit(s[opt:]):
                #print("not done")
                return splits + 1
            else:
                #print("expanding:",splits+1)
                options2 = expand_options(s, opt, len(s)-1, crit)
                need_to_check = split_opts.setdefault(splits + 1, set())
                #print("adding:",options2)
                need_to_check.update(options2)
                ##print("added:",need_to_check)
                #print("\t", split_opts)
        splits += 1
    #print("reached end")
    return -1

