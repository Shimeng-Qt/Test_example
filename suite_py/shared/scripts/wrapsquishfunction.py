import sys # Add this line

def wrapSquishFunction(functionName, wrappedFunctionGetter): # Add this function
    module = sys.modules["squish"]
    if functionName in dir(module):
        wrappedFunction = wrappedFunctionGetter(getattr(module, functionName))
        setattr(module, functionName, wrappedFunction)
    else:
        raise RuntimeError("function %s not part of squish module" % functionName)

    if functionName in globals():
        globals()[functionName] = wrappedFunction
