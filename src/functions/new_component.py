from src.components.CurrentSource import CurrentSource, CurrentSourceControlledByVoltage
from src.components.Resistor import Resistor


# parse each component to it's own class
def new_component(arr):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        return CurrentSource(arr)
    elif 'G' in arr[0]:
        return CurrentSourceControlledByVoltage(arr)
