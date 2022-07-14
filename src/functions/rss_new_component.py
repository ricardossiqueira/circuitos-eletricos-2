from components.rss_CurrentSource import CurrentSource, CurrentSourceControlledByCurrent
from components.rss_CurrentSource import CurrentSourceControlledByVoltage
from components.rss_VoltageSource import VoltageSource, VoltageSourceControlledByVoltage
from components.rss_VoltageSource import VoltageSourceControlledByCurrent
from components.rss_Resistor import Resistor


# parse each component to it's own class
def new_component(arr):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        return CurrentSource(arr)
    elif 'G' in arr[0]:
        return CurrentSourceControlledByVoltage(arr)
    elif 'F' in arr[0]:
        return CurrentSourceControlledByCurrent(arr)
    elif 'E' in arr[0]:
        return VoltageSourceControlledByVoltage(arr)
    elif 'H' in arr[0]:
        return VoltageSourceControlledByCurrent(arr)
    elif 'V' in arr[0]:
        return VoltageSource(arr)
