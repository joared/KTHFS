// Auto-generated. Do not edit!

// (in-package fs_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Cone = require('./Cone.js');
let ConeStats = require('./ConeStats.js');

//-----------------------------------------------------------

class ConeWithStats {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cone = null;
      this.stats = null;
    }
    else {
      if (initObj.hasOwnProperty('cone')) {
        this.cone = initObj.cone
      }
      else {
        this.cone = new Cone();
      }
      if (initObj.hasOwnProperty('stats')) {
        this.stats = initObj.stats
      }
      else {
        this.stats = new ConeStats();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConeWithStats
    // Serialize message field [cone]
    bufferOffset = Cone.serialize(obj.cone, buffer, bufferOffset);
    // Serialize message field [stats]
    bufferOffset = ConeStats.serialize(obj.stats, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConeWithStats
    let len;
    let data = new ConeWithStats(null);
    // Deserialize message field [cone]
    data.cone = Cone.deserialize(buffer, bufferOffset);
    // Deserialize message field [stats]
    data.stats = ConeStats.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 81;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fs_msgs/ConeWithStats';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bc6abd39812a69dee6e5d6c6dbebf194';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #
    # Description of a cone with statistics
    #
    
    Cone cone
    ConeStats stats
    
    ================================================================================
    MSG: fs_msgs/Cone
    #
    # Description of a cone
    #
    
    # 2D-position of the cone
    float64 x
    float64 y
    
    # Color of the cone
    uint8 UNDEFINED = 0
    uint8 YELLOW = 1
    uint8 BLUE = 2
    uint8 SMALL_ORANGE = 3
    uint8 BIG_ORANGE = 4
    
    uint8 color
    
    # Covariance on the position [m^2] (2x2 matrix in row-major order)
    float64[4] covariance
    
    # Confidence in the detection
    float64 probability
    
    ================================================================================
    MSG: fs_msgs/ConeStats
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
    const resolved = new ConeWithStats(null);
    if (msg.cone !== undefined) {
      resolved.cone = Cone.Resolve(msg.cone)
    }
    else {
      resolved.cone = new Cone()
    }

    if (msg.stats !== undefined) {
      resolved.stats = ConeStats.Resolve(msg.stats)
    }
    else {
      resolved.stats = new ConeStats()
    }

    return resolved;
    }
};

module.exports = ConeWithStats;
