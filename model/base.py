from core import db

def commit(obj):
    db.session.add(obj)
    db.session.commit()
    db.session.refresh(obj)
    return obj

class Model(object):
    @classmethod
    def add(cls, **kwargs):
        obj = cls(**kwargs)
        # db.session.add(obj)
        # print(obj.__dict__)
        # db.session.commit()
        return commit(obj)

    @classmethod
    def update(cls, row_id, **kwargs):
        cls.query.filter_by(id=row_id).update(kwargs)
        obj = cls.query.filter_by(id=row_id).first()
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def delete(cls, row_id):

        """ if object was deleted return 1 else 0 """
        obj_for_del = cls.query.filter_by(id=row_id).first()
        obj = 1 if db.session.delete(obj_for_del) == None else 0
        db.session.commit()
        return obj