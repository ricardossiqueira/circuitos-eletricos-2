from src.components.rss_Transformer import SinusoidalTransformer
from src.components.rss_CurrentSource import DCCurrentSource, CurrentSourceControlledByVoltage, SinusoidalCurrentSource
from src.components.rss_Resistor import Resistor
from src.components.rss_Inductor import SinusoidalInductor
from src.components.rss_Capacitor import SinusoidalCapacitor


# parse each component to it's own class
def new_component(arr, omega):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        if 'DC' in arr[3]:
            return DCCurrentSource(arr)
        if 'SIN' in arr[3]:
            return SinusoidalCurrentSource(arr)
    elif 'G' in arr[0]:
        return CurrentSourceControlledByVoltage(arr)
    elif 'L' in arr[0]:
        arr.append(omega)
        return SinusoidalInductor(arr)
    elif 'C' in arr[0]:
        arr.append(omega)
        return SinusoidalCapacitor(arr)
    elif 'K' in arr[0]:
        arr.append(omega)
        return SinusoidalTransformer(arr)
