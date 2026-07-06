# -*- coding: utf-8 -*-

import names

def main():
    startApplication("appapp_sample_QML")
    
    obj_scroll = waitForObject(names.assemblies_ScrollView)
  
    button_Fvisible = waitForObject(names.coin_system_Button)
    button_Pvisible = waitForObject(names.another_Item_Button)
    button_Nvisible = waitForObject(names.extra_Item_Button)
    
    visible = isVisible(button_Pvisible, obj_scroll)
    
    test.verify(visible, "Item is inside scroll area")
    
    
    if visible:
        mouseClick(button_Pvisible)
    else:
        test.log("Item not visible → scrolling required")

    
def isVisible(element, container):  
        return (element.x >= container.x and
            element.y >= container.y and
            element.x + element.width <= container.x + container.width and
            element.y + element.height <= container.y + container.height)


#===============================================================================
# 510 + 900  510 + 900
# 510 + 70 876
# 822 + 54(876)   276+600(876)
#===============================================================================