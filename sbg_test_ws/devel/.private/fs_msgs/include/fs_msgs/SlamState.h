// Generated by gencpp from file fs_msgs/SlamState.msg
// DO NOT EDIT!


#ifndef FS_MSGS_MESSAGE_SLAMSTATE_H
#define FS_MSGS_MESSAGE_SLAMSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fs_msgs
{
template <class ContainerAllocator>
struct SlamState_
{
  typedef SlamState_<ContainerAllocator> Type;

  SlamState_()
    : lap_counter(0)
    , cones_count_actual(0)
    , cones_count_all(0)  {
    }
  SlamState_(const ContainerAllocator& _alloc)
    : lap_counter(0)
    , cones_count_actual(0)
    , cones_count_all(0)  {
  (void)_alloc;
    }



   typedef uint8_t _lap_counter_type;
  _lap_counter_type lap_counter;

   typedef int32_t _cones_count_actual_type;
  _cones_count_actual_type cones_count_actual;

   typedef int32_t _cones_count_all_type;
  _cones_count_all_type cones_count_all;





  typedef boost::shared_ptr< ::fs_msgs::SlamState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fs_msgs::SlamState_<ContainerAllocator> const> ConstPtr;

}; // struct SlamState_

typedef ::fs_msgs::SlamState_<std::allocator<void> > SlamState;

typedef boost::shared_ptr< ::fs_msgs::SlamState > SlamStatePtr;
typedef boost::shared_ptr< ::fs_msgs::SlamState const> SlamStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fs_msgs::SlamState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fs_msgs::SlamState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace fs_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'fs_msgs': ['/home/joar/KTHFS/sbg_test_ws/src/fs_msgs/msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::SlamState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fs_msgs::SlamState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::SlamState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fs_msgs::SlamState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::SlamState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fs_msgs::SlamState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fs_msgs::SlamState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a77c00628d1b607092740dc262c21142";
  }

  static const char* value(const ::fs_msgs::SlamState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa77c00628d1b6070ULL;
  static const uint64_t static_value2 = 0x92740dc262c21142ULL;
};

template<class ContainerAllocator>
struct DataType< ::fs_msgs::SlamState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fs_msgs/SlamState";
  }

  static const char* value(const ::fs_msgs::SlamState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fs_msgs::SlamState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#\n"
"# Give the lap count and number of cones\n"
"#\n"
"\n"
"uint8 lap_counter\n"
"int32 cones_count_actual\n"
"int32 cones_count_all\n"
;
  }

  static const char* value(const ::fs_msgs::SlamState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fs_msgs::SlamState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.lap_counter);
      stream.next(m.cones_count_actual);
      stream.next(m.cones_count_all);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SlamState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fs_msgs::SlamState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fs_msgs::SlamState_<ContainerAllocator>& v)
  {
    s << indent << "lap_counter: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.lap_counter);
    s << indent << "cones_count_actual: ";
    Printer<int32_t>::stream(s, indent + "  ", v.cones_count_actual);
    s << indent << "cones_count_all: ";
    Printer<int32_t>::stream(s, indent + "  ", v.cones_count_all);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FS_MSGS_MESSAGE_SLAMSTATE_H
