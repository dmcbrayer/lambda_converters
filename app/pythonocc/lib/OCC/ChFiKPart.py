# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _ChFiKPart.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ChFiKPart', [dirname(__file__)])
        except ImportError:
            import _ChFiKPart
            return _ChFiKPart
        if fp is not None:
            try:
                _mod = imp.load_module('_ChFiKPart', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ChFiKPart = swig_import_helper()
    del swig_import_helper
else:
    import _ChFiKPart
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
    __swig_destroy__ = _ChFiKPart.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_ChFiKPart.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_ChFiKPart.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_ChFiKPart.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_ChFiKPart.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_ChFiKPart.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_ChFiKPart.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_ChFiKPart.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_ChFiKPart.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_ChFiKPart.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_ChFiKPart.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_ChFiKPart.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_ChFiKPart.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_ChFiKPart.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_ChFiKPart.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_ChFiKPart.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_ChFiKPart.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _ChFiKPart.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.TopOpeBRepDS
import OCC.TopAbs
import OCC.Standard
import OCC.TCollection
import OCC.MMgt
import OCC.TopOpeBRepTool
import OCC.TopoDS
import OCC.TopLoc
import OCC.gp
import OCC.TopTools
import OCC.TColStd
import OCC.Message
import OCC.Bnd
import OCC.Geom2d
import OCC.GeomAbs
import OCC.TColgp
import OCC.GeomAdaptor
import OCC.Adaptor3d
import OCC.Geom
import OCC.Adaptor2d
import OCC.math
import OCC.BRepClass3d
import OCC.IntCurveSurface
import OCC.Intf
import OCC.IntSurf
import OCC.BRepAdaptor
import OCC.Geom2dAdaptor
import OCC.IntCurvesFace
import OCC.Extrema
import OCC.ChFiDS
import OCC.Law
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

class ChFiKPart_ComputeData(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def Compute(*args):
        """
        * Computes a simple fillet in several particular cases.

        :param DStr:
        :type DStr: TopOpeBRepDS_DataStructure &
        :param Data:
        :type Data: Handle_ChFiDS_SurfData &
        :param S1:
        :type S1: Handle_Adaptor3d_HSurface &
        :param S2:
        :type S2: Handle_Adaptor3d_HSurface &
        :param Or1:
        :type Or1: TopAbs_Orientation
        :param Or2:
        :type Or2: TopAbs_Orientation
        :param Sp:
        :type Sp: Handle_ChFiDS_Spine &
        :param Iedge:
        :type Iedge: int
        :rtype: bool

        """
        return _ChFiKPart.ChFiKPart_ComputeData_Compute(*args)

    Compute = staticmethod(Compute)
    def ComputeCorner(*args):
        """
        * Computes a toric or spheric corner fillet.

        :param DStr:
        :type DStr: TopOpeBRepDS_DataStructure &
        :param Data:
        :type Data: Handle_ChFiDS_SurfData &
        :param S1:
        :type S1: Handle_Adaptor3d_HSurface &
        :param S2:
        :type S2: Handle_Adaptor3d_HSurface &
        :param OrFace1:
        :type OrFace1: TopAbs_Orientation
        :param OrFace2:
        :type OrFace2: TopAbs_Orientation
        :param Or1:
        :type Or1: TopAbs_Orientation
        :param Or2:
        :type Or2: TopAbs_Orientation
        :param minRad:
        :type minRad: float
        :param majRad:
        :type majRad: float
        :param P1S1:
        :type P1S1: gp_Pnt2d
        :param P2S1:
        :type P2S1: gp_Pnt2d
        :param P1S2:
        :type P1S2: gp_Pnt2d
        :param P2S2:
        :type P2S2: gp_Pnt2d
        :rtype: bool

        * Computes spheric corner fillet with non iso pcurve on S2.

        :param DStr:
        :type DStr: TopOpeBRepDS_DataStructure &
        :param Data:
        :type Data: Handle_ChFiDS_SurfData &
        :param S1:
        :type S1: Handle_Adaptor3d_HSurface &
        :param S2:
        :type S2: Handle_Adaptor3d_HSurface &
        :param OrFace1:
        :type OrFace1: TopAbs_Orientation
        :param OrFace2:
        :type OrFace2: TopAbs_Orientation
        :param Or1:
        :type Or1: TopAbs_Orientation
        :param Or2:
        :type Or2: TopAbs_Orientation
        :param Rad:
        :type Rad: float
        :param PS1:
        :type PS1: gp_Pnt2d
        :param P1S2:
        :type P1S2: gp_Pnt2d
        :param P2S2:
        :type P2S2: gp_Pnt2d
        :rtype: bool

        * Computes a toric corner rotule.

        :param DStr:
        :type DStr: TopOpeBRepDS_DataStructure &
        :param Data:
        :type Data: Handle_ChFiDS_SurfData &
        :param S:
        :type S: Handle_Adaptor3d_HSurface &
        :param S1:
        :type S1: Handle_Adaptor3d_HSurface &
        :param S2:
        :type S2: Handle_Adaptor3d_HSurface &
        :param OfS:
        :type OfS: TopAbs_Orientation
        :param OS:
        :type OS: TopAbs_Orientation
        :param OS1:
        :type OS1: TopAbs_Orientation
        :param OS2:
        :type OS2: TopAbs_Orientation
        :param Radius:
        :type Radius: float
        :rtype: bool

        """
        return _ChFiKPart.ChFiKPart_ComputeData_ComputeCorner(*args)

    ComputeCorner = staticmethod(ComputeCorner)
    def __init__(self): 
        _ChFiKPart.ChFiKPart_ComputeData_swiginit(self,_ChFiKPart.new_ChFiKPart_ComputeData())
    __swig_destroy__ = _ChFiKPart.delete_ChFiKPart_ComputeData
ChFiKPart_ComputeData_swigregister = _ChFiKPart.ChFiKPart_ComputeData_swigregister
ChFiKPart_ComputeData_swigregister(ChFiKPart_ComputeData)

def ChFiKPart_ComputeData_Compute(*args):
  """
    * Computes a simple fillet in several particular cases.

    :param DStr:
    :type DStr: TopOpeBRepDS_DataStructure &
    :param Data:
    :type Data: Handle_ChFiDS_SurfData &
    :param S1:
    :type S1: Handle_Adaptor3d_HSurface &
    :param S2:
    :type S2: Handle_Adaptor3d_HSurface &
    :param Or1:
    :type Or1: TopAbs_Orientation
    :param Or2:
    :type Or2: TopAbs_Orientation
    :param Sp:
    :type Sp: Handle_ChFiDS_Spine &
    :param Iedge:
    :type Iedge: int
    :rtype: bool

    """
  return _ChFiKPart.ChFiKPart_ComputeData_Compute(*args)

def ChFiKPart_ComputeData_ComputeCorner(*args):
  """
    * Computes a toric or spheric corner fillet.

    :param DStr:
    :type DStr: TopOpeBRepDS_DataStructure &
    :param Data:
    :type Data: Handle_ChFiDS_SurfData &
    :param S1:
    :type S1: Handle_Adaptor3d_HSurface &
    :param S2:
    :type S2: Handle_Adaptor3d_HSurface &
    :param OrFace1:
    :type OrFace1: TopAbs_Orientation
    :param OrFace2:
    :type OrFace2: TopAbs_Orientation
    :param Or1:
    :type Or1: TopAbs_Orientation
    :param Or2:
    :type Or2: TopAbs_Orientation
    :param minRad:
    :type minRad: float
    :param majRad:
    :type majRad: float
    :param P1S1:
    :type P1S1: gp_Pnt2d
    :param P2S1:
    :type P2S1: gp_Pnt2d
    :param P1S2:
    :type P1S2: gp_Pnt2d
    :param P2S2:
    :type P2S2: gp_Pnt2d
    :rtype: bool

    * Computes spheric corner fillet with non iso pcurve on S2.

    :param DStr:
    :type DStr: TopOpeBRepDS_DataStructure &
    :param Data:
    :type Data: Handle_ChFiDS_SurfData &
    :param S1:
    :type S1: Handle_Adaptor3d_HSurface &
    :param S2:
    :type S2: Handle_Adaptor3d_HSurface &
    :param OrFace1:
    :type OrFace1: TopAbs_Orientation
    :param OrFace2:
    :type OrFace2: TopAbs_Orientation
    :param Or1:
    :type Or1: TopAbs_Orientation
    :param Or2:
    :type Or2: TopAbs_Orientation
    :param Rad:
    :type Rad: float
    :param PS1:
    :type PS1: gp_Pnt2d
    :param P1S2:
    :type P1S2: gp_Pnt2d
    :param P2S2:
    :type P2S2: gp_Pnt2d
    :rtype: bool

    * Computes a toric corner rotule.

    :param DStr:
    :type DStr: TopOpeBRepDS_DataStructure &
    :param Data:
    :type Data: Handle_ChFiDS_SurfData &
    :param S:
    :type S: Handle_Adaptor3d_HSurface &
    :param S1:
    :type S1: Handle_Adaptor3d_HSurface &
    :param S2:
    :type S2: Handle_Adaptor3d_HSurface &
    :param OfS:
    :type OfS: TopAbs_Orientation
    :param OS:
    :type OS: TopAbs_Orientation
    :param OS1:
    :type OS1: TopAbs_Orientation
    :param OS2:
    :type OS2: TopAbs_Orientation
    :param Radius:
    :type Radius: float
    :rtype: bool

    """
  return _ChFiKPart.ChFiKPart_ComputeData_ComputeCorner(*args)

class ChFiKPart_DataMapIteratorOfRstMap(OCC.TCollection.TCollection_BasicMapIterator):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :rtype: None

        :param aMap:
        :type aMap: ChFiKPart_RstMap &
        :rtype: None

        """
        _ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_swiginit(self,_ChFiKPart.new_ChFiKPart_DataMapIteratorOfRstMap(*args))
    def Initialize(self, *args):
        """
        :param aMap:
        :type aMap: ChFiKPart_RstMap &
        :rtype: None

        """
        return _ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Initialize(self, *args)

    def Key(self, *args):
        """
        :rtype: int

        """
        return _ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Key(self, *args)

    def Value(self, *args):
        """
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Value(self, *args)

    __swig_destroy__ = _ChFiKPart.delete_ChFiKPart_DataMapIteratorOfRstMap
ChFiKPart_DataMapIteratorOfRstMap.Initialize = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Initialize,None,ChFiKPart_DataMapIteratorOfRstMap)
ChFiKPart_DataMapIteratorOfRstMap.Key = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Key,None,ChFiKPart_DataMapIteratorOfRstMap)
ChFiKPart_DataMapIteratorOfRstMap.Value = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_Value,None,ChFiKPart_DataMapIteratorOfRstMap)
ChFiKPart_DataMapIteratorOfRstMap_swigregister = _ChFiKPart.ChFiKPart_DataMapIteratorOfRstMap_swigregister
ChFiKPart_DataMapIteratorOfRstMap_swigregister(ChFiKPart_DataMapIteratorOfRstMap)

class ChFiKPart_DataMapNodeOfRstMap(OCC.TCollection.TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param K:
        :type K: int &
        :param I:
        :type I: Handle_Adaptor2d_HCurve2d &
        :param n:
        :type n: TCollection_MapNodePtr &
        :rtype: None

        """
        _ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_swiginit(self,_ChFiKPart.new_ChFiKPart_DataMapNodeOfRstMap(*args))
    def GetKey(self):
        """GetKey(ChFiKPart_DataMapNodeOfRstMap self) -> Standard_Integer"""
        return _ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_GetKey(self)

    def SetKey(self, *args):
        """SetKey(ChFiKPart_DataMapNodeOfRstMap self, Standard_Integer value)"""
        return _ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_SetKey(self, *args)

    def Value(self, *args):
        """
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_Value(self, *args)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_ChFiKPart_DataMapNodeOfRstMap(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _ChFiKPart.delete_ChFiKPart_DataMapNodeOfRstMap
ChFiKPart_DataMapNodeOfRstMap.GetKey = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_GetKey,None,ChFiKPart_DataMapNodeOfRstMap)
ChFiKPart_DataMapNodeOfRstMap.SetKey = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_SetKey,None,ChFiKPart_DataMapNodeOfRstMap)
ChFiKPart_DataMapNodeOfRstMap.Value = new_instancemethod(_ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_Value,None,ChFiKPart_DataMapNodeOfRstMap)
ChFiKPart_DataMapNodeOfRstMap_swigregister = _ChFiKPart.ChFiKPart_DataMapNodeOfRstMap_swigregister
ChFiKPart_DataMapNodeOfRstMap_swigregister(ChFiKPart_DataMapNodeOfRstMap)

class Handle_ChFiKPart_DataMapNodeOfRstMap(OCC.TCollection.Handle_TCollection_MapNode):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_swiginit(self,_ChFiKPart.new_Handle_ChFiKPart_DataMapNodeOfRstMap(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_DownCast)
    __swig_destroy__ = _ChFiKPart.delete_Handle_ChFiKPart_DataMapNodeOfRstMap
Handle_ChFiKPart_DataMapNodeOfRstMap.Nullify = new_instancemethod(_ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_Nullify,None,Handle_ChFiKPart_DataMapNodeOfRstMap)
Handle_ChFiKPart_DataMapNodeOfRstMap.IsNull = new_instancemethod(_ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_IsNull,None,Handle_ChFiKPart_DataMapNodeOfRstMap)
Handle_ChFiKPart_DataMapNodeOfRstMap.GetObject = new_instancemethod(_ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_GetObject,None,Handle_ChFiKPart_DataMapNodeOfRstMap)
Handle_ChFiKPart_DataMapNodeOfRstMap_swigregister = _ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_swigregister
Handle_ChFiKPart_DataMapNodeOfRstMap_swigregister(Handle_ChFiKPart_DataMapNodeOfRstMap)

def Handle_ChFiKPart_DataMapNodeOfRstMap_DownCast(*args):
  return _ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_DownCast(*args)
Handle_ChFiKPart_DataMapNodeOfRstMap_DownCast = _ChFiKPart.Handle_ChFiKPart_DataMapNodeOfRstMap_DownCast

class ChFiKPart_RstMap(OCC.TCollection.TCollection_BasicMap):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        :param NbBuckets: default value is 1
        :type NbBuckets: int
        :rtype: None

        """
        _ChFiKPart.ChFiKPart_RstMap_swiginit(self,_ChFiKPart.new_ChFiKPart_RstMap(*args))
    def Assign(self, *args):
        """
        :param Other:
        :type Other: ChFiKPart_RstMap &
        :rtype: ChFiKPart_RstMap

        """
        return _ChFiKPart.ChFiKPart_RstMap_Assign(self, *args)

    def Set(self, *args):
        """
        :param Other:
        :type Other: ChFiKPart_RstMap &
        :rtype: ChFiKPart_RstMap

        """
        return _ChFiKPart.ChFiKPart_RstMap_Set(self, *args)

    def ReSize(self, *args):
        """
        :param NbBuckets:
        :type NbBuckets: int
        :rtype: None

        """
        return _ChFiKPart.ChFiKPart_RstMap_ReSize(self, *args)

    def Clear(self, *args):
        """
        :rtype: None

        """
        return _ChFiKPart.ChFiKPart_RstMap_Clear(self, *args)

    def Bind(self, *args):
        """
        :param K:
        :type K: int &
        :param I:
        :type I: Handle_Adaptor2d_HCurve2d &
        :rtype: bool

        """
        return _ChFiKPart.ChFiKPart_RstMap_Bind(self, *args)

    def IsBound(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: bool

        """
        return _ChFiKPart.ChFiKPart_RstMap_IsBound(self, *args)

    def UnBind(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: bool

        """
        return _ChFiKPart.ChFiKPart_RstMap_UnBind(self, *args)

    def Find(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _ChFiKPart.ChFiKPart_RstMap_Find(self, *args)

    def ChangeFind(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: Handle_Adaptor2d_HCurve2d

        """
        return _ChFiKPart.ChFiKPart_RstMap_ChangeFind(self, *args)

    def Find1(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: Standard_Address

        """
        return _ChFiKPart.ChFiKPart_RstMap_Find1(self, *args)

    def ChangeFind1(self, *args):
        """
        :param K:
        :type K: int &
        :rtype: Standard_Address

        """
        return _ChFiKPart.ChFiKPart_RstMap_ChangeFind1(self, *args)

    __swig_destroy__ = _ChFiKPart.delete_ChFiKPart_RstMap
ChFiKPart_RstMap.Assign = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Assign,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.Set = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Set,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.ReSize = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_ReSize,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.Clear = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Clear,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.Bind = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Bind,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.IsBound = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_IsBound,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.UnBind = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_UnBind,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.Find = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Find,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.ChangeFind = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_ChangeFind,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.Find1 = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_Find1,None,ChFiKPart_RstMap)
ChFiKPart_RstMap.ChangeFind1 = new_instancemethod(_ChFiKPart.ChFiKPart_RstMap_ChangeFind1,None,ChFiKPart_RstMap)
ChFiKPart_RstMap_swigregister = _ChFiKPart.ChFiKPart_RstMap_swigregister
ChFiKPart_RstMap_swigregister(ChFiKPart_RstMap)



