import logging

from yapsy.PluginManager import PluginManager

from categories import Painter,Formatter

logging.basicConfig(level=logging.DEBUG)

# Build the manager
simplePluginManager = PluginManager(plugin_info_ext='plugin',categories_filter={ "Formatter": Formatter,
                                                                           "Painter": Painter})
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(["plugindir"])
simplePluginManager.collectPlugins()

print simplePluginManager.getCategories()

simplePluginManager.activatePluginByName('TwoFormatter',category='Formatter')
p = simplePluginManager.getPluginByName('TwoFormatter',category='Formatter')
print p.plugin_object.formatText('hello1')

simplePluginManager.activatePluginByName('ThreeFormatter',category='Formatter')
p = simplePluginManager.getPluginByName('ThreeFormatter',category='Formatter')
print p.plugin_object.formatText('hello2')

simplePluginManager.activatePluginByName('TwoPainter',category='Painter')
p = simplePluginManager.getPluginByName('TwoPainter',category='Painter')
print p.plugin_object.paintText('hello3')

simplePluginManager.activatePluginByName('ThreePainter',category='Painter')
p = simplePluginManager.getPluginByName('ThreePainter',category='Painter')
print p.plugin_object.paintText('hello4')
