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

class SlamState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lap_counter = null;
      this.cones_count_actual = null;
      this.cones_count_all = null;
    }
    else {
      if (initObj.hasOwnProperty('lap_counter')) {
        this.lap_counter = initObj.lap_counter
      }
      else {
        this.lap_counter = 0;
      }
      if (initObj.hasOwnProperty('cones_count_actual')) {
        this.cones_count_actual = initObj.cones_count_actual
      }
      else {
        this.cones_count_actual = 0;
      }
      if (initObj.hasOwnProperty('cones_count_all')) {
        this.cones_count_all = initObj.cones_count_all
      }
      else {
        this.cones_count_all = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SlamState
    // Serialize message field [lap_counter]
    bufferOffset = _serializer.uint8(obj.lap_counter, buffer, bufferOffset);
    // Serialize message field [cones_count_actual]
    bufferOffset = _serializer.int32(obj.cones_count_actual, buffer, bufferOffset);
    // Serialize message field [cones_count_all]
    bufferOffset = _serializer.int32(obj.cones_count_all, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SlamState
    let len;
    let data = new SlamState(null);
    // Deserialize message field [lap_counter]
    data.lap_counter = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [cones_count_actual]
    data.cones_count_actual = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [cones_count_all]
    data.cones_count_all = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fs_msgs/SlamState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a77c00628d1b607092740dc262c21142';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #
    # Give the lap count and number of cones
    #
    
    uint8 lap_counter
    int32 cones_count_actual
    int32 cones_count_all
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SlamState(null);
    if (msg.lap_counter !== undefined) {
      resolved.lap_counter = msg.lap_counter;
    }
    else {
      resolved.lap_counter = 0
    }

    if (msg.cones_count_actual !== undefined) {
      resolved.cones_count_actual = msg.cones_count_actual;
    }
    else {
      resolved.cones_count_actual = 0
    }

    if (msg.cones_count_all !== undefined) {
      resolved.cones_count_all = msg.cones_count_all;
    }
    else {
      resolved.cones_count_all = 0
    }

    return resolved;
    }
};

module.exports = SlamState;
