class CDDBRouter:
    db_app_route_map = {'pricing' : 'oms', 'awi': 'awi'}

    def db_for_read(self, model, **hints):
        app_name = model._meta.app_label
        db_name = CDDBRouter.db_app_route_map.get(app_name, 'default')
        return db_name

    def db_for_write(self, model, **hints):
        app_name = model._meta.app_label
        db_name = CDDBRouter.db_app_route_map.get(app_name, 'default')
        return db_name

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        #db_set = {'primary', 'replica1', 'replica2'}
        #if obj1._state.db in db_set and obj2._state.db in db_set:
        #    return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return None
