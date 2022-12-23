
def lang(arg=None, **kvargs):
    print(f"Lang: {arg} {kvargs}")
    return "AHHHHH"

def on_env(env, config, files, **kwargs): 
    env.filters['lang'] = lang
    #print(list(env.filters))
    return env

def on_pre_page(page, config, files):
    #print(output_content)
    #print(template_name)
    print([(key, config[key]) for key in config if 'url' in key])