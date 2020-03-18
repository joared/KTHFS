# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from fs_msgs/Sbg_ekf_status.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Sbg_ekf_status(genpy.Message):
  _md5sum = "464794a3821aebe67baf95cbfb19fb69"
  _type = "fs_msgs/Sbg_ekf_status"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 COMPUTATION_MODE
bool ATTITUDE_VALID
bool HEADING_VALID
bool VELOCITY_VALID
bool POSITION_VALID
bool VERT_REF_USED
bool MAG_REF_USED
bool GPS1_VEL_USED
bool GPS1_POS_USED
bool GPS1_HDT_USED
bool GPS2_VEL_USED
bool GPS2_POS_USED
bool GPS2_HDT_USED
bool ODO_USED
bool DVL_BT_USED
bool DVL_WT_USED
bool USBL_USED
bool AIR_DATA_USED
bool ZUPT_USED
bool ALIGN_VALID
bool DEPTH_USED

"""
  __slots__ = ['COMPUTATION_MODE','ATTITUDE_VALID','HEADING_VALID','VELOCITY_VALID','POSITION_VALID','VERT_REF_USED','MAG_REF_USED','GPS1_VEL_USED','GPS1_POS_USED','GPS1_HDT_USED','GPS2_VEL_USED','GPS2_POS_USED','GPS2_HDT_USED','ODO_USED','DVL_BT_USED','DVL_WT_USED','USBL_USED','AIR_DATA_USED','ZUPT_USED','ALIGN_VALID','DEPTH_USED']
  _slot_types = ['uint8','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       COMPUTATION_MODE,ATTITUDE_VALID,HEADING_VALID,VELOCITY_VALID,POSITION_VALID,VERT_REF_USED,MAG_REF_USED,GPS1_VEL_USED,GPS1_POS_USED,GPS1_HDT_USED,GPS2_VEL_USED,GPS2_POS_USED,GPS2_HDT_USED,ODO_USED,DVL_BT_USED,DVL_WT_USED,USBL_USED,AIR_DATA_USED,ZUPT_USED,ALIGN_VALID,DEPTH_USED

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Sbg_ekf_status, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.COMPUTATION_MODE is None:
        self.COMPUTATION_MODE = 0
      if self.ATTITUDE_VALID is None:
        self.ATTITUDE_VALID = False
      if self.HEADING_VALID is None:
        self.HEADING_VALID = False
      if self.VELOCITY_VALID is None:
        self.VELOCITY_VALID = False
      if self.POSITION_VALID is None:
        self.POSITION_VALID = False
      if self.VERT_REF_USED is None:
        self.VERT_REF_USED = False
      if self.MAG_REF_USED is None:
        self.MAG_REF_USED = False
      if self.GPS1_VEL_USED is None:
        self.GPS1_VEL_USED = False
      if self.GPS1_POS_USED is None:
        self.GPS1_POS_USED = False
      if self.GPS1_HDT_USED is None:
        self.GPS1_HDT_USED = False
      if self.GPS2_VEL_USED is None:
        self.GPS2_VEL_USED = False
      if self.GPS2_POS_USED is None:
        self.GPS2_POS_USED = False
      if self.GPS2_HDT_USED is None:
        self.GPS2_HDT_USED = False
      if self.ODO_USED is None:
        self.ODO_USED = False
      if self.DVL_BT_USED is None:
        self.DVL_BT_USED = False
      if self.DVL_WT_USED is None:
        self.DVL_WT_USED = False
      if self.USBL_USED is None:
        self.USBL_USED = False
      if self.AIR_DATA_USED is None:
        self.AIR_DATA_USED = False
      if self.ZUPT_USED is None:
        self.ZUPT_USED = False
      if self.ALIGN_VALID is None:
        self.ALIGN_VALID = False
      if self.DEPTH_USED is None:
        self.DEPTH_USED = False
    else:
      self.COMPUTATION_MODE = 0
      self.ATTITUDE_VALID = False
      self.HEADING_VALID = False
      self.VELOCITY_VALID = False
      self.POSITION_VALID = False
      self.VERT_REF_USED = False
      self.MAG_REF_USED = False
      self.GPS1_VEL_USED = False
      self.GPS1_POS_USED = False
      self.GPS1_HDT_USED = False
      self.GPS2_VEL_USED = False
      self.GPS2_POS_USED = False
      self.GPS2_HDT_USED = False
      self.ODO_USED = False
      self.DVL_BT_USED = False
      self.DVL_WT_USED = False
      self.USBL_USED = False
      self.AIR_DATA_USED = False
      self.ZUPT_USED = False
      self.ALIGN_VALID = False
      self.DEPTH_USED = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_21B().pack(_x.COMPUTATION_MODE, _x.ATTITUDE_VALID, _x.HEADING_VALID, _x.VELOCITY_VALID, _x.POSITION_VALID, _x.VERT_REF_USED, _x.MAG_REF_USED, _x.GPS1_VEL_USED, _x.GPS1_POS_USED, _x.GPS1_HDT_USED, _x.GPS2_VEL_USED, _x.GPS2_POS_USED, _x.GPS2_HDT_USED, _x.ODO_USED, _x.DVL_BT_USED, _x.DVL_WT_USED, _x.USBL_USED, _x.AIR_DATA_USED, _x.ZUPT_USED, _x.ALIGN_VALID, _x.DEPTH_USED))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.COMPUTATION_MODE, _x.ATTITUDE_VALID, _x.HEADING_VALID, _x.VELOCITY_VALID, _x.POSITION_VALID, _x.VERT_REF_USED, _x.MAG_REF_USED, _x.GPS1_VEL_USED, _x.GPS1_POS_USED, _x.GPS1_HDT_USED, _x.GPS2_VEL_USED, _x.GPS2_POS_USED, _x.GPS2_HDT_USED, _x.ODO_USED, _x.DVL_BT_USED, _x.DVL_WT_USED, _x.USBL_USED, _x.AIR_DATA_USED, _x.ZUPT_USED, _x.ALIGN_VALID, _x.DEPTH_USED,) = _get_struct_21B().unpack(str[start:end])
      self.ATTITUDE_VALID = bool(self.ATTITUDE_VALID)
      self.HEADING_VALID = bool(self.HEADING_VALID)
      self.VELOCITY_VALID = bool(self.VELOCITY_VALID)
      self.POSITION_VALID = bool(self.POSITION_VALID)
      self.VERT_REF_USED = bool(self.VERT_REF_USED)
      self.MAG_REF_USED = bool(self.MAG_REF_USED)
      self.GPS1_VEL_USED = bool(self.GPS1_VEL_USED)
      self.GPS1_POS_USED = bool(self.GPS1_POS_USED)
      self.GPS1_HDT_USED = bool(self.GPS1_HDT_USED)
      self.GPS2_VEL_USED = bool(self.GPS2_VEL_USED)
      self.GPS2_POS_USED = bool(self.GPS2_POS_USED)
      self.GPS2_HDT_USED = bool(self.GPS2_HDT_USED)
      self.ODO_USED = bool(self.ODO_USED)
      self.DVL_BT_USED = bool(self.DVL_BT_USED)
      self.DVL_WT_USED = bool(self.DVL_WT_USED)
      self.USBL_USED = bool(self.USBL_USED)
      self.AIR_DATA_USED = bool(self.AIR_DATA_USED)
      self.ZUPT_USED = bool(self.ZUPT_USED)
      self.ALIGN_VALID = bool(self.ALIGN_VALID)
      self.DEPTH_USED = bool(self.DEPTH_USED)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_21B().pack(_x.COMPUTATION_MODE, _x.ATTITUDE_VALID, _x.HEADING_VALID, _x.VELOCITY_VALID, _x.POSITION_VALID, _x.VERT_REF_USED, _x.MAG_REF_USED, _x.GPS1_VEL_USED, _x.GPS1_POS_USED, _x.GPS1_HDT_USED, _x.GPS2_VEL_USED, _x.GPS2_POS_USED, _x.GPS2_HDT_USED, _x.ODO_USED, _x.DVL_BT_USED, _x.DVL_WT_USED, _x.USBL_USED, _x.AIR_DATA_USED, _x.ZUPT_USED, _x.ALIGN_VALID, _x.DEPTH_USED))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.COMPUTATION_MODE, _x.ATTITUDE_VALID, _x.HEADING_VALID, _x.VELOCITY_VALID, _x.POSITION_VALID, _x.VERT_REF_USED, _x.MAG_REF_USED, _x.GPS1_VEL_USED, _x.GPS1_POS_USED, _x.GPS1_HDT_USED, _x.GPS2_VEL_USED, _x.GPS2_POS_USED, _x.GPS2_HDT_USED, _x.ODO_USED, _x.DVL_BT_USED, _x.DVL_WT_USED, _x.USBL_USED, _x.AIR_DATA_USED, _x.ZUPT_USED, _x.ALIGN_VALID, _x.DEPTH_USED,) = _get_struct_21B().unpack(str[start:end])
      self.ATTITUDE_VALID = bool(self.ATTITUDE_VALID)
      self.HEADING_VALID = bool(self.HEADING_VALID)
      self.VELOCITY_VALID = bool(self.VELOCITY_VALID)
      self.POSITION_VALID = bool(self.POSITION_VALID)
      self.VERT_REF_USED = bool(self.VERT_REF_USED)
      self.MAG_REF_USED = bool(self.MAG_REF_USED)
      self.GPS1_VEL_USED = bool(self.GPS1_VEL_USED)
      self.GPS1_POS_USED = bool(self.GPS1_POS_USED)
      self.GPS1_HDT_USED = bool(self.GPS1_HDT_USED)
      self.GPS2_VEL_USED = bool(self.GPS2_VEL_USED)
      self.GPS2_POS_USED = bool(self.GPS2_POS_USED)
      self.GPS2_HDT_USED = bool(self.GPS2_HDT_USED)
      self.ODO_USED = bool(self.ODO_USED)
      self.DVL_BT_USED = bool(self.DVL_BT_USED)
      self.DVL_WT_USED = bool(self.DVL_WT_USED)
      self.USBL_USED = bool(self.USBL_USED)
      self.AIR_DATA_USED = bool(self.AIR_DATA_USED)
      self.ZUPT_USED = bool(self.ZUPT_USED)
      self.ALIGN_VALID = bool(self.ALIGN_VALID)
      self.DEPTH_USED = bool(self.DEPTH_USED)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_21B = None
def _get_struct_21B():
    global _struct_21B
    if _struct_21B is None:
        _struct_21B = struct.Struct("<21B")
    return _struct_21B