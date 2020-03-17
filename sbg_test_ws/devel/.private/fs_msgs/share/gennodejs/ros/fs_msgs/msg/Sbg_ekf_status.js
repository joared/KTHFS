// Auto-generated. Do not edit!

// (in-package fs_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Sbg_ekf_status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.COMPUTATION_MODE = null;
      this.ATTITUDE_VALID = null;
      this.HEADING_VALID = null;
      this.VELOCITY_VALID = null;
      this.POSITION_VALID = null;
      this.VERT_REF_USED = null;
      this.MAG_REF_USED = null;
      this.GPS1_VEL_USED = null;
      this.GPS1_POS_USED = null;
      this.GPS1_HDT_USED = null;
      this.GPS2_VEL_USED = null;
      this.GPS2_POS_USED = null;
      this.GPS2_HDT_USED = null;
      this.ODO_USED = null;
      this.DVL_BT_USED = null;
      this.DVL_WT_USED = null;
      this.USBL_USED = null;
      this.AIR_DATA_USED = null;
      this.ZUPT_USED = null;
      this.ALIGN_VALID = null;
      this.DEPTH_USED = null;
    }
    else {
      if (initObj.hasOwnProperty('COMPUTATION_MODE')) {
        this.COMPUTATION_MODE = initObj.COMPUTATION_MODE
      }
      else {
        this.COMPUTATION_MODE = 0;
      }
      if (initObj.hasOwnProperty('ATTITUDE_VALID')) {
        this.ATTITUDE_VALID = initObj.ATTITUDE_VALID
      }
      else {
        this.ATTITUDE_VALID = false;
      }
      if (initObj.hasOwnProperty('HEADING_VALID')) {
        this.HEADING_VALID = initObj.HEADING_VALID
      }
      else {
        this.HEADING_VALID = false;
      }
      if (initObj.hasOwnProperty('VELOCITY_VALID')) {
        this.VELOCITY_VALID = initObj.VELOCITY_VALID
      }
      else {
        this.VELOCITY_VALID = false;
      }
      if (initObj.hasOwnProperty('POSITION_VALID')) {
        this.POSITION_VALID = initObj.POSITION_VALID
      }
      else {
        this.POSITION_VALID = false;
      }
      if (initObj.hasOwnProperty('VERT_REF_USED')) {
        this.VERT_REF_USED = initObj.VERT_REF_USED
      }
      else {
        this.VERT_REF_USED = false;
      }
      if (initObj.hasOwnProperty('MAG_REF_USED')) {
        this.MAG_REF_USED = initObj.MAG_REF_USED
      }
      else {
        this.MAG_REF_USED = false;
      }
      if (initObj.hasOwnProperty('GPS1_VEL_USED')) {
        this.GPS1_VEL_USED = initObj.GPS1_VEL_USED
      }
      else {
        this.GPS1_VEL_USED = false;
      }
      if (initObj.hasOwnProperty('GPS1_POS_USED')) {
        this.GPS1_POS_USED = initObj.GPS1_POS_USED
      }
      else {
        this.GPS1_POS_USED = false;
      }
      if (initObj.hasOwnProperty('GPS1_HDT_USED')) {
        this.GPS1_HDT_USED = initObj.GPS1_HDT_USED
      }
      else {
        this.GPS1_HDT_USED = false;
      }
      if (initObj.hasOwnProperty('GPS2_VEL_USED')) {
        this.GPS2_VEL_USED = initObj.GPS2_VEL_USED
      }
      else {
        this.GPS2_VEL_USED = false;
      }
      if (initObj.hasOwnProperty('GPS2_POS_USED')) {
        this.GPS2_POS_USED = initObj.GPS2_POS_USED
      }
      else {
        this.GPS2_POS_USED = false;
      }
      if (initObj.hasOwnProperty('GPS2_HDT_USED')) {
        this.GPS2_HDT_USED = initObj.GPS2_HDT_USED
      }
      else {
        this.GPS2_HDT_USED = false;
      }
      if (initObj.hasOwnProperty('ODO_USED')) {
        this.ODO_USED = initObj.ODO_USED
      }
      else {
        this.ODO_USED = false;
      }
      if (initObj.hasOwnProperty('DVL_BT_USED')) {
        this.DVL_BT_USED = initObj.DVL_BT_USED
      }
      else {
        this.DVL_BT_USED = false;
      }
      if (initObj.hasOwnProperty('DVL_WT_USED')) {
        this.DVL_WT_USED = initObj.DVL_WT_USED
      }
      else {
        this.DVL_WT_USED = false;
      }
      if (initObj.hasOwnProperty('USBL_USED')) {
        this.USBL_USED = initObj.USBL_USED
      }
      else {
        this.USBL_USED = false;
      }
      if (initObj.hasOwnProperty('AIR_DATA_USED')) {
        this.AIR_DATA_USED = initObj.AIR_DATA_USED
      }
      else {
        this.AIR_DATA_USED = false;
      }
      if (initObj.hasOwnProperty('ZUPT_USED')) {
        this.ZUPT_USED = initObj.ZUPT_USED
      }
      else {
        this.ZUPT_USED = false;
      }
      if (initObj.hasOwnProperty('ALIGN_VALID')) {
        this.ALIGN_VALID = initObj.ALIGN_VALID
      }
      else {
        this.ALIGN_VALID = false;
      }
      if (initObj.hasOwnProperty('DEPTH_USED')) {
        this.DEPTH_USED = initObj.DEPTH_USED
      }
      else {
        this.DEPTH_USED = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Sbg_ekf_status
    // Serialize message field [COMPUTATION_MODE]
    bufferOffset = _serializer.uint8(obj.COMPUTATION_MODE, buffer, bufferOffset);
    // Serialize message field [ATTITUDE_VALID]
    bufferOffset = _serializer.bool(obj.ATTITUDE_VALID, buffer, bufferOffset);
    // Serialize message field [HEADING_VALID]
    bufferOffset = _serializer.bool(obj.HEADING_VALID, buffer, bufferOffset);
    // Serialize message field [VELOCITY_VALID]
    bufferOffset = _serializer.bool(obj.VELOCITY_VALID, buffer, bufferOffset);
    // Serialize message field [POSITION_VALID]
    bufferOffset = _serializer.bool(obj.POSITION_VALID, buffer, bufferOffset);
    // Serialize message field [VERT_REF_USED]
    bufferOffset = _serializer.bool(obj.VERT_REF_USED, buffer, bufferOffset);
    // Serialize message field [MAG_REF_USED]
    bufferOffset = _serializer.bool(obj.MAG_REF_USED, buffer, bufferOffset);
    // Serialize message field [GPS1_VEL_USED]
    bufferOffset = _serializer.bool(obj.GPS1_VEL_USED, buffer, bufferOffset);
    // Serialize message field [GPS1_POS_USED]
    bufferOffset = _serializer.bool(obj.GPS1_POS_USED, buffer, bufferOffset);
    // Serialize message field [GPS1_HDT_USED]
    bufferOffset = _serializer.bool(obj.GPS1_HDT_USED, buffer, bufferOffset);
    // Serialize message field [GPS2_VEL_USED]
    bufferOffset = _serializer.bool(obj.GPS2_VEL_USED, buffer, bufferOffset);
    // Serialize message field [GPS2_POS_USED]
    bufferOffset = _serializer.bool(obj.GPS2_POS_USED, buffer, bufferOffset);
    // Serialize message field [GPS2_HDT_USED]
    bufferOffset = _serializer.bool(obj.GPS2_HDT_USED, buffer, bufferOffset);
    // Serialize message field [ODO_USED]
    bufferOffset = _serializer.bool(obj.ODO_USED, buffer, bufferOffset);
    // Serialize message field [DVL_BT_USED]
    bufferOffset = _serializer.bool(obj.DVL_BT_USED, buffer, bufferOffset);
    // Serialize message field [DVL_WT_USED]
    bufferOffset = _serializer.bool(obj.DVL_WT_USED, buffer, bufferOffset);
    // Serialize message field [USBL_USED]
    bufferOffset = _serializer.bool(obj.USBL_USED, buffer, bufferOffset);
    // Serialize message field [AIR_DATA_USED]
    bufferOffset = _serializer.bool(obj.AIR_DATA_USED, buffer, bufferOffset);
    // Serialize message field [ZUPT_USED]
    bufferOffset = _serializer.bool(obj.ZUPT_USED, buffer, bufferOffset);
    // Serialize message field [ALIGN_VALID]
    bufferOffset = _serializer.bool(obj.ALIGN_VALID, buffer, bufferOffset);
    // Serialize message field [DEPTH_USED]
    bufferOffset = _serializer.bool(obj.DEPTH_USED, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Sbg_ekf_status
    let len;
    let data = new Sbg_ekf_status(null);
    // Deserialize message field [COMPUTATION_MODE]
    data.COMPUTATION_MODE = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ATTITUDE_VALID]
    data.ATTITUDE_VALID = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [HEADING_VALID]
    data.HEADING_VALID = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [VELOCITY_VALID]
    data.VELOCITY_VALID = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [POSITION_VALID]
    data.POSITION_VALID = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [VERT_REF_USED]
    data.VERT_REF_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [MAG_REF_USED]
    data.MAG_REF_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS1_VEL_USED]
    data.GPS1_VEL_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS1_POS_USED]
    data.GPS1_POS_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS1_HDT_USED]
    data.GPS1_HDT_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS2_VEL_USED]
    data.GPS2_VEL_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS2_POS_USED]
    data.GPS2_POS_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GPS2_HDT_USED]
    data.GPS2_HDT_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ODO_USED]
    data.ODO_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [DVL_BT_USED]
    data.DVL_BT_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [DVL_WT_USED]
    data.DVL_WT_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [USBL_USED]
    data.USBL_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [AIR_DATA_USED]
    data.AIR_DATA_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ZUPT_USED]
    data.ZUPT_USED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ALIGN_VALID]
    data.ALIGN_VALID = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [DEPTH_USED]
    data.DEPTH_USED = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 21;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fs_msgs/Sbg_ekf_status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '464794a3821aebe67baf95cbfb19fb69';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 COMPUTATION_MODE
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
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Sbg_ekf_status(null);
    if (msg.COMPUTATION_MODE !== undefined) {
      resolved.COMPUTATION_MODE = msg.COMPUTATION_MODE;
    }
    else {
      resolved.COMPUTATION_MODE = 0
    }

    if (msg.ATTITUDE_VALID !== undefined) {
      resolved.ATTITUDE_VALID = msg.ATTITUDE_VALID;
    }
    else {
      resolved.ATTITUDE_VALID = false
    }

    if (msg.HEADING_VALID !== undefined) {
      resolved.HEADING_VALID = msg.HEADING_VALID;
    }
    else {
      resolved.HEADING_VALID = false
    }

    if (msg.VELOCITY_VALID !== undefined) {
      resolved.VELOCITY_VALID = msg.VELOCITY_VALID;
    }
    else {
      resolved.VELOCITY_VALID = false
    }

    if (msg.POSITION_VALID !== undefined) {
      resolved.POSITION_VALID = msg.POSITION_VALID;
    }
    else {
      resolved.POSITION_VALID = false
    }

    if (msg.VERT_REF_USED !== undefined) {
      resolved.VERT_REF_USED = msg.VERT_REF_USED;
    }
    else {
      resolved.VERT_REF_USED = false
    }

    if (msg.MAG_REF_USED !== undefined) {
      resolved.MAG_REF_USED = msg.MAG_REF_USED;
    }
    else {
      resolved.MAG_REF_USED = false
    }

    if (msg.GPS1_VEL_USED !== undefined) {
      resolved.GPS1_VEL_USED = msg.GPS1_VEL_USED;
    }
    else {
      resolved.GPS1_VEL_USED = false
    }

    if (msg.GPS1_POS_USED !== undefined) {
      resolved.GPS1_POS_USED = msg.GPS1_POS_USED;
    }
    else {
      resolved.GPS1_POS_USED = false
    }

    if (msg.GPS1_HDT_USED !== undefined) {
      resolved.GPS1_HDT_USED = msg.GPS1_HDT_USED;
    }
    else {
      resolved.GPS1_HDT_USED = false
    }

    if (msg.GPS2_VEL_USED !== undefined) {
      resolved.GPS2_VEL_USED = msg.GPS2_VEL_USED;
    }
    else {
      resolved.GPS2_VEL_USED = false
    }

    if (msg.GPS2_POS_USED !== undefined) {
      resolved.GPS2_POS_USED = msg.GPS2_POS_USED;
    }
    else {
      resolved.GPS2_POS_USED = false
    }

    if (msg.GPS2_HDT_USED !== undefined) {
      resolved.GPS2_HDT_USED = msg.GPS2_HDT_USED;
    }
    else {
      resolved.GPS2_HDT_USED = false
    }

    if (msg.ODO_USED !== undefined) {
      resolved.ODO_USED = msg.ODO_USED;
    }
    else {
      resolved.ODO_USED = false
    }

    if (msg.DVL_BT_USED !== undefined) {
      resolved.DVL_BT_USED = msg.DVL_BT_USED;
    }
    else {
      resolved.DVL_BT_USED = false
    }

    if (msg.DVL_WT_USED !== undefined) {
      resolved.DVL_WT_USED = msg.DVL_WT_USED;
    }
    else {
      resolved.DVL_WT_USED = false
    }

    if (msg.USBL_USED !== undefined) {
      resolved.USBL_USED = msg.USBL_USED;
    }
    else {
      resolved.USBL_USED = false
    }

    if (msg.AIR_DATA_USED !== undefined) {
      resolved.AIR_DATA_USED = msg.AIR_DATA_USED;
    }
    else {
      resolved.AIR_DATA_USED = false
    }

    if (msg.ZUPT_USED !== undefined) {
      resolved.ZUPT_USED = msg.ZUPT_USED;
    }
    else {
      resolved.ZUPT_USED = false
    }

    if (msg.ALIGN_VALID !== undefined) {
      resolved.ALIGN_VALID = msg.ALIGN_VALID;
    }
    else {
      resolved.ALIGN_VALID = false
    }

    if (msg.DEPTH_USED !== undefined) {
      resolved.DEPTH_USED = msg.DEPTH_USED;
    }
    else {
      resolved.DEPTH_USED = false
    }

    return resolved;
    }
};

module.exports = Sbg_ekf_status;
