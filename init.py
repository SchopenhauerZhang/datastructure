import sys 

class Init(object):
    def __init__(self):
        try:
            import sys
            sys.path.append('/Users/schopenhauerzhang/code/pythonCode/datastructure/')
        except Exception:
            exit("import fail error")

        return None
