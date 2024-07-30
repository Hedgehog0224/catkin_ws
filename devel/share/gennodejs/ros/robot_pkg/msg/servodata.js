// Auto-generated. Do not edit!

// (in-package robot_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class servodata {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.servo0 = null;
      this.servo1 = null;
      this.servo2 = null;
      this.servo3 = null;
      this.servo4 = null;
      this.servo5 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('servo0')) {
        this.servo0 = initObj.servo0
      }
      else {
        this.servo0 = 0;
      }
      if (initObj.hasOwnProperty('servo1')) {
        this.servo1 = initObj.servo1
      }
      else {
        this.servo1 = 0;
      }
      if (initObj.hasOwnProperty('servo2')) {
        this.servo2 = initObj.servo2
      }
      else {
        this.servo2 = 0;
      }
      if (initObj.hasOwnProperty('servo3')) {
        this.servo3 = initObj.servo3
      }
      else {
        this.servo3 = 0;
      }
      if (initObj.hasOwnProperty('servo4')) {
        this.servo4 = initObj.servo4
      }
      else {
        this.servo4 = 0;
      }
      if (initObj.hasOwnProperty('servo5')) {
        this.servo5 = initObj.servo5
      }
      else {
        this.servo5 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type servodata
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [servo0]
    bufferOffset = _serializer.int32(obj.servo0, buffer, bufferOffset);
    // Serialize message field [servo1]
    bufferOffset = _serializer.int32(obj.servo1, buffer, bufferOffset);
    // Serialize message field [servo2]
    bufferOffset = _serializer.int32(obj.servo2, buffer, bufferOffset);
    // Serialize message field [servo3]
    bufferOffset = _serializer.int32(obj.servo3, buffer, bufferOffset);
    // Serialize message field [servo4]
    bufferOffset = _serializer.int32(obj.servo4, buffer, bufferOffset);
    // Serialize message field [servo5]
    bufferOffset = _serializer.int32(obj.servo5, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type servodata
    let len;
    let data = new servodata(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [servo0]
    data.servo0 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [servo1]
    data.servo1 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [servo2]
    data.servo2 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [servo3]
    data.servo3 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [servo4]
    data.servo4 = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [servo5]
    data.servo5 = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_pkg/servodata';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '976b722a95bbf1a80c00724ccfc64d4e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    int32 servo0
    int32 servo1
    int32 servo2
    int32 servo3
    int32 servo4
    int32 servo5
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new servodata(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.servo0 !== undefined) {
      resolved.servo0 = msg.servo0;
    }
    else {
      resolved.servo0 = 0
    }

    if (msg.servo1 !== undefined) {
      resolved.servo1 = msg.servo1;
    }
    else {
      resolved.servo1 = 0
    }

    if (msg.servo2 !== undefined) {
      resolved.servo2 = msg.servo2;
    }
    else {
      resolved.servo2 = 0
    }

    if (msg.servo3 !== undefined) {
      resolved.servo3 = msg.servo3;
    }
    else {
      resolved.servo3 = 0
    }

    if (msg.servo4 !== undefined) {
      resolved.servo4 = msg.servo4;
    }
    else {
      resolved.servo4 = 0
    }

    if (msg.servo5 !== undefined) {
      resolved.servo5 = msg.servo5;
    }
    else {
      resolved.servo5 = 0
    }

    return resolved;
    }
};

module.exports = servodata;
