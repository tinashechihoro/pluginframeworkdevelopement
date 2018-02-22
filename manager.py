class PluginManager():
    def __init__(self.path=None,plugin_init_args={}):
        self.plugins = {}
        if path:
            self.plugin_dir = path
        else:
            self.plugin_dir = os.path.dirname(__file__) + '/plugins/'
        self.plugins = []
        self._load_plugins()
        self._register_plugins(**plugin_init_args)

    def _load_plugins(self):
        sys.path.append(plugin_dir)
        plug_files = [file  for file in os.listdir(self.plugin_dir) if file.startswith('plugin_') and file.endswith('.py') ]
        plugin_modules = [ module.split('.')[0] for module in plug_files ]
        for module in plugin_modules:
            module = __import__(module)
    
    def __register_plugins(self,**kwargs):
        for plugin in Plugins.__subclasses__():
            obj = plugin(**kwargs)
            self.plugins[obj] = obj.keywords if hasattr(obj,'keywords') else []
    def call_method(seld,method,args={},keywords=[]):
        for plugin in self.plugins:
            if not keywords or (set(keywords)) & set(self.plugins[plugin]):
                try:
                    getattr(plugin,method)(**args)
                except:
                    pass