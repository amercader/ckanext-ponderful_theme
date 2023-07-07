import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Ponderful_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public', 'ponderful')

    entry_points='''
        [ckan.plugins]
        ponderful_theme=ckanext.ponderful_theme.plugin:PonderfulThemePlugin''',
