def compress_tokens(tokens):
    return [t for t in tokens if len(t.strip()) > 1]
