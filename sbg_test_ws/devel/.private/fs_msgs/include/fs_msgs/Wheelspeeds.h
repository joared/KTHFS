// Generated by gencpp from file fs_msgs/Wheelspeeds.msg
// DO NOT EDIT!


#ifndef FS_MSGS_MESSAGE_WHEELSPEEDS_H
#define FS_MSGS_MESSAGE_WHEELSPEEDS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace fs_msgs
{
template <class ContainerAllocator>
struct Wheelspeeds_
{
  typedef Wheelspeeds_<ContainerAllocator> Type;

  Wheelspeeds_()
    : header()
    , front_left(0.0)
    , front_right(0.0)
    , rear_left(0.0)
    , rear_right(0.0)
    , variance(0.0)  {
    }
  Wheelspeeds_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , front_left(0.0)
    , front_right(0.0)
    , rear_left(0.0)
    , rear_right(0.0)
    , variance(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef double _front_left_type;
  _front_left_type front_left;

   typedef double _front_right_type;
  _front_right_type front_right;

   typedef double _rear_left_type;
  _rear_left_type rear_left;

   typedef double _rear_right_type;
  _rear_right_type rear_right;

   typedef double _variance_type;
  _variance_type variance;





  typedef boost::shared_ptr< ::fs_msgs::Wheelspeeds_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fs_msgs::Wheelspeeds_<ContainerAllocator> const> ConstPtr;

}; // struct Wheelspeeds_

typedef ::fs_msgs::Wheelspeeds_<std::allocator<void> > Wheelspeeds;

typedef boost::shared_ptr< ::fs_msgs::Wheelspeeds > WheelspeedsPtr;
typedef boost::shared_ptr< ::fs_msgs::Wheelspeeds const> WheelspeedsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fs_msgs::Wheelspeeds_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fs_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'fs_msgs': ['/home/joar/KTHFS/sbg_test_ws/src/fs_msgs/msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::Wheelspeeds_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::Wheelspeeds_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::Wheelspeeds_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "981b415c45e4921582fc5e4dda54a1c9";
  }

  static const char* value(const ::fs_msgs::Wheelspeeds_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x981b415c45e49215ULL;
  static const uint64_t static_value2 = 0x82fc5e4dda54a1c9ULL;
};

template<class ContainerAllocator>
struct DataType< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fs_msgs/Wheelspeeds";
  }

  static const char* value(const ::fs_msgs::Wheelspeeds_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"float64 front_left\n"
"float64 front_right\n"
"float64 rear_left\n"
"float64 rear_right\n"
"float64 variance\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::fs_msgs::Wheelspeeds_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.front_left);
      stream.next(m.front_right);
      stream.next(m.rear_left);
      stream.next(m.rear_right);
      stream.next(m.variance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Wheelspeeds_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fs_msgs::Wheelspeeds_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fs_msgs::Wheelspeeds_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "front_left: ";
    Printer<double>::stream(s, indent + "  ", v.front_left);
    s << indent << "front_right: ";
    Printer<double>::stream(s, indent + "  ", v.front_right);
    s << indent << "rear_left: ";
    Printer<double>::stream(s, indent + "  ", v.rear_left);
    s << indent << "rear_right: ";
    Printer<double>::stream(s, indent + "  ", v.rear_right);
    s << indent << "variance: ";
    Printer<double>::stream(s, indent + "  ", v.variance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FS_MSGS_MESSAGE_WHEELSPEEDS_H