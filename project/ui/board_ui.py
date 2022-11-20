def parse_cmd(cmd):
    parts = cmd.split(" ")
    if len(parts) > 1:
        return parts[0], parts[1:]
    return parts[0], ()
