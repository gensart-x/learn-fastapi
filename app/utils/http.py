def is_whitelisted(path: str, whitelisted_paths: list[str]) -> bool:
    for pattern in whitelisted_paths:
        # Exact match for "/"
        if pattern == "/" and path == "/":
            return True

        # Simple wildcard match: /api/v1/* matches anything under /api/v1/
        if pattern.endswith("/*"):
            base = pattern[:-1]  # keep the trailing slash
            if path.startswith(base):
                return True

        # Exact match
        if path == pattern:
            return True

    return False
