"""Hello State integration minimal example."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "hello_state"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hello State integration.

    This will create a new state entity `hello_state.world`
    with the value 'Paulus' when Home Assistant starts.
    """
    hass.states.async_set(f"{DOMAIN}.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
