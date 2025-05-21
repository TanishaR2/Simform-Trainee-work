def init_context(user_input):
    return {"user_input": user_input}


def update_context(context, key, value):
    context[key] = value


def get_context(context, key, default=None):
    return context.get(key, default)


def get_all_context(context):
    return context
