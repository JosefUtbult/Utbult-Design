def categories(arg=None, **kvargs):
    print(f"Categories: {arg} {kvargs}")
    return "AHHHHH"

def on_env(env, config, files, **kwargs): 
    print("Here")
    env.filters['categories'] = categories
    return env