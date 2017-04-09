from pyplanet.core.events import Callback
from pyplanet.core.instance import Controller


async def handle_map_begin(source, signal, **kwargs):
	# Retrieve and update map, return it to our callback listeners.
	map = await Controller.instance.map_manager.handle_map_change(source)
	return dict(map=map)


async def handle_map_end(source, signal, **kwargs):
	# Retrieve and update map, return it to our callback listeners.
	map = await Controller.instance.map_manager.handle_map_change(source)
	return dict(map=map)


# We don't use scripted map events due to the information we get and the stability of the information structure.
map_begin = Callback(
	call='ManiaPlanet.BeginMap',
	namespace='maniaplanet',
	code='map_begin',
	target=handle_map_begin,
)

map_end = Callback(
	call='ManiaPlanet.EndMap',
	namespace='maniaplanet',
	code='map_end',
	target=handle_map_end,
)
