import gin

@gin.configurable
def run(run_fn, run_fn2=None):
    run_fn()
    #run_fn2()

