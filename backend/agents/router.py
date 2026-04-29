def route(persona,context):
    if persona.lower()=='compliance':
        return context[:2]
    return context
