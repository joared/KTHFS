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

class ConeStats {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.nbr_detections = null;
      this.yellow_counter = null;
      this.blue_counter = null;
      this.avg_innovation_x = null;
      this.avg_innovation_y = null;
      this.std_innovation = null;
    }
    else {
      if (initObj.hasOwnProperty('nbr_detections')) {
        this.nbr_detections = initObj.nbr_detections
      }
      else {
        this.nbr_detections = 0;
      }
      if (initObj.hasOwnProperty('yellow_counter')) {
        this.yellow_counter = initObj.yellow_counter
      }
      else {
        this.yellow_counter = 0;
      }
      if (initObj.hasOwnProperty('blue_counter')) {
        this.blue_counter = initObj.blue_counter
      }
      else {
        this.blue_counter = 0;
      }
      if (initObj.hasOwnProperty('avg_innovation_x')) {
        this.avg_innovation_x = initObj.avg_innovation_x
      }
      else {
        this.avg_innovation_x = 0.0;
      }
      if (initObj.hasOwnProperty('avg_innovation_y')) {
        this.avg_innovation_y = initObj.avg_innovation_y
      }
      else {
        this.avg_innovation_y = 0.0;
      }
      if (initObj.hasOwnProperty('std_innovation')) {
        this.std_innovation = initObj.std_innovation
      }
      else {
        this.std_innovation = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConeStats
    // Serialize message field [nbr_detections]
    bufferOffset = _serializer.int32(obj.nbr_detections, buffer, bufferOffset);
    // Serialize message field [yellow_counter]
    bufferOffset = _serializer.int32(obj.yellow_counter, buffer, bufferOffset);
    // Serialize message field [blue_counter]
    bufferOffset = _serializer.int32(obj.blue_counter, buffer, bufferOffset);
    // Serialize message field [avg_innovation_x]
    bufferOffset = _serializer.float32(obj.avg_innovation_x, buffer, bufferOffset);
    // Serialize message field [avg_innovation_y]
    bufferOffset = _serializer.float32(obj.avg_innovation_y, buffer, bufferOffset);
    // Serialize message field [std_innovation]
    bufferOffset = _serializer.float32(obj.std_innovation, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConeStats
    let len;
    let data = new ConeStats(null);
    // Deserialize message field [nbr_detections]
    data.nbr_detections = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [yellow_counter]
    data.yellow_counter = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [blue_counter]
    data.blue_counter = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [avg_innovation_x]
    data.avg_innovation_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [avg_innovation_y]
    data.avg_innovation_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [std_innovation]
    data.std_innovation = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fs_msgs/ConeStats';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e29d797ff713ceaa2ace1ff34729c17e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #
    # Statistics of a cone
    #
    
    # Number of times the cone has been seen
    int32 nbr_detections
    
    # Color counters
    int32 yellow_counter
    int32 blue_counter
    
    # Average innovation (innovation = mapped position - detected position)
    float32 avg_innovation_x
    float32 avg_innovation_y
    
    # Standard deviation of innovation norms
    float32 std_innovation
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConeStats(null);
    if (msg.nbr_detections !== undefined) {
      resolved.nbr_detections = msg.nbr_detections;
    }
    else {
      resolved.nbr_detections = 0
    }

    if (msg.yellow_counter !== undefined) {
      resolved.yellow_counter = msg.yellow_counter;
    }
    else {
      resolved.yellow_counter = 0
    }

    if (msg.blue_counter !== undefined) {
      resolved.blue_counter = msg.blue_counter;
    }
    else {
      resolved.blue_counter = 0
    }

    if (msg.avg_innovation_x !== undefined) {
      resolved.avg_innovation_x = msg.avg_innovation_x;
    }
    else {
      resolved.avg_innovation_x = 0.0
    }

    if (msg.avg_innovation_y !== undefined) {
      resolved.avg_innovation_y = msg.avg_innovation_y;
    }
    else {
      resolved.avg_innovation_y = 0.0
    }

    if (msg.std_innovation !== undefined) {
      resolved.std_innovation = msg.std_innovation;
    }
    else {
      resolved.std_innovation = 0.0
    }

    return resolved;
    }
};

module.exports = ConeStats;
