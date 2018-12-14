# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _MMgt.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MMgt', [dirname(__file__)])
        except ImportError:
            import _MMgt
            return _MMgt
        if fp is not None:
            try:
                _mod = imp.load_module('_MMgt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _MMgt = swig_import_helper()
    del swig_import_helper
else:
    import _MMgt
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _MMgt.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_MMgt.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_MMgt.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_MMgt.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_MMgt.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_MMgt.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_MMgt.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_MMgt.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_MMgt.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_MMgt.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_MMgt.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_MMgt.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_MMgt.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_MMgt.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_MMgt.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_MMgt.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_MMgt.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _MMgt.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass

class MMgt_TShared(OCC.Standard.Standard_Transient):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_MMgt_TShared(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _MMgt.delete_MMgt_TShared
MMgt_TShared_swigregister = _MMgt.MMgt_TShared_swigregister
MMgt_TShared_swigregister(MMgt_TShared)

class Handle_MMgt_TShared(OCC.Standard.Handle_Standard_Transient):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _MMgt.Handle_MMgt_TShared_swiginit(self,_MMgt.new_Handle_MMgt_TShared(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_MMgt.Handle_MMgt_TShared_DownCast)
    __swig_destroy__ = _MMgt.delete_Handle_MMgt_TShared
Handle_MMgt_TShared.Nullify = new_instancemethod(_MMgt.Handle_MMgt_TShared_Nullify,None,Handle_MMgt_TShared)
Handle_MMgt_TShared.IsNull = new_instancemethod(_MMgt.Handle_MMgt_TShared_IsNull,None,Handle_MMgt_TShared)
Handle_MMgt_TShared.GetObject = new_instancemethod(_MMgt.Handle_MMgt_TShared_GetObject,None,Handle_MMgt_TShared)
Handle_MMgt_TShared_swigregister = _MMgt.Handle_MMgt_TShared_swigregister
Handle_MMgt_TShared_swigregister(Handle_MMgt_TShared)

def Handle_MMgt_TShared_DownCast(*args):
  return _MMgt.Handle_MMgt_TShared_DownCast(*args)
Handle_MMgt_TShared_DownCast = _MMgt.Handle_MMgt_TShared_DownCast


