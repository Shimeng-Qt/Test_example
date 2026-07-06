# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appQML_QENUM_00865379")
    
    model_name = "test"
    parameter_name = "washerType"
    
    
    window = waitForObjectExists("{type='QQuickWindowQmlImpl' visible='true'}")
    engine = qmlEngine(window)
    test.verify(engine is not None, "Engine fetched from object is valid")


    rootContext = engine.rootContext()

    model_object = object.convertTo(rootContext.contextProperty(model_name), "QObject")
    value = getattr(model_object,parameter_name)

    #textObj = waitForObject(names.washerType_Text)
    #model_value = getattr(obj, parameter_name)

    test.breakpoint()

