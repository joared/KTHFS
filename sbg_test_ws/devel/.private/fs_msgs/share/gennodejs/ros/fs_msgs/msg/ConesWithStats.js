// Auto-generated. Do not edit!

// (in-package fs_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ConeWithStats = require('./ConeWithStats.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ConesWithStats {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.cones = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('cones')) {
        this.cones = initObj.cones
      }
      else {
        this.cones = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConesWithStats
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [cones]
    // Serialize the length for message field [cones]
    bufferOffset = _serializer.uint32(obj.cones.length, buffer, bufferOffset);
    obj.cones.forEach((val) => {
      bufferOffset = ConeWithStats.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConesWithStats
    let len;
    let data = new ConesWithStats(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [cones]
    // Deserialize array length for message field [cones]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.cones = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.cones[i] = ConeWithStats.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 81 * object.cones.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fs_msgs/ConesWithStats';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6718c9a6b3d40b0468a363f35c8b1688';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #
    # Array of cones with statistics
    #
    
    # Extra information on the message
    # header.stamp: time of the message
    # header.frame_id: frame in which the cones are given
    Header header
    
    # Array of cones
    ConeWithStats[] cones
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    ================================================================================
    MSG: fs_msgs/ConeWithStats
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
    const resolved = new ConesWithStats(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.cones !== undefined) {
      resolved.cones = new Array(msg.cones.length);
      for (let i = 0; i < resolved.cones.length; ++i) {
        resolved.cones[i] = ConeWithStats.Resolve(msg.cones[i]);
      }
    }
    else {
      resolved.cones = []
    }

    return resolved;
    }
};

module.exports = ConesWithStats;